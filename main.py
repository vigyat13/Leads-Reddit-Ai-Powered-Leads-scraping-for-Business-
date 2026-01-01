import streamlit as st
import scraper
import ai_filter
import sheets
import time

st.set_page_config(page_title="Local AI Lead Gen", page_icon="🚀", layout="centered")
st.title("🚀 Local AI Lead Generator")

# --- INPUTS ---
col1, col2 = st.columns([3, 1])
with col1:
    keywords_input = st.text_input(
        "Target Keywords (comma separated)", 
        value="hiring video editor, looking for marketing help",
        help="Try: 'hiring python dev, budget for seo, saas alternative'"
    )
with col2:
    search_limit = st.slider("Limit", 5, 50, 10)

# --- RUN BUTTON ---
if st.button("🚀 Find Qualified Leads", type="primary", use_container_width=True):
    
    keywords = [k.strip() for k in keywords_input.split(',') if k.strip()]
    all_qualified_leads = [] 

    with st.status("🚀 Engine Starting...", expanded=True) as status:
        
        for keyword in keywords:
            status.update(label=f"🚀 Searching: '{keyword}'...")
            
            # 1. RUN SCRAPER
            posts = scraper.search_reddit(keyword, limit=search_limit)
            
            if posts:
                st.write(f"🕷️ Scraper found **{len(posts)} potential posts**. Asking AI...")
                
                # 2. RUN AI
                analyzed_batch = ai_filter.analyze_leads(posts)
                
                # 3. FILTER RESULTS
                valid_batch = [l for l in analyzed_batch if "Not" not in l.get('lead_status', '')]
                
                if valid_batch:
                    st.write(f"✅ **AI Approved {len(valid_batch)} leads!**")
                    all_qualified_leads.extend(valid_batch)
                else:
                    st.write("❌ AI rejected all posts in this batch (Low Quality).")
            else:
                st.write(f"⚠️ Scraper found 0 posts for \"{keyword}\".")
            
            time.sleep(1) 
            
        status.update(label=f"✅ Done! Found {len(all_qualified_leads)} leads.", state="complete", expanded=False)

    # --- RESULTS ---
    if all_qualified_leads:
        try:
            sheets.save_to_google_sheets(all_qualified_leads)
            st.success(f"Success! {len(all_qualified_leads)} leads added to Google Sheet.")
            
            st.subheader("🔍 Review AI Decisions")
            st.dataframe(
                all_qualified_leads,
                column_config={
                    "lead_status": "Priority",
                    "reason": st.column_config.TextColumn("Why?", width="medium"), 
                    "content": st.column_config.TextColumn("Snippet", width="medium"),
                    "url": st.column_config.LinkColumn("Link"),
                    "username": "Author"
                },
                use_container_width=True
            )
        except Exception as e:
            st.error(f"Google Sheet Error: {e}")
    else:
        st.warning("No leads found. Try broader keywords like 'hiring', 'budget', or 'help'.")