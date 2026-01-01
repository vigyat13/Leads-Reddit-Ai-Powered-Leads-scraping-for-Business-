import json
import time
from groq import Groq
import config  # <--- IMPORTS YOUR API KEY

# Setup Groq Client
client = Groq(
    api_key=config.GROQ_API_KEY,
)

def call_ai_model(messages, model_name):
    """Wrapper to call AI with specific model."""
    return client.chat.completions.create(
        messages=messages,
        model=model_name,
        temperature=0.0,
        response_format={"type": "json_object"},
    )

def analyze_leads(posts):
    if not posts:
        return []

    # 1. Prepare Data (Keep it light: 250 chars max)
    posts_text = ""
    for index, post in enumerate(posts):
        posts_text += f"""
        --- POST #{index} ---
        ID: {index}
        Title: {post['title']}
        Snippet: {post['content'][:250]}...
        ---------------------
        """

    system_prompt = """
    You are a Lead Gen Filter.
    1. FILTER OUT: Students, tutorials, spam, generic discussions.
    2. KEEP ONLY: People BUYING (hiring, budget, looking for) or COMPLAINING (pain points).
    
    OUTPUT JSON ONLY in this EXACT format:
    {
        "leads": [
            {"id": 0, "lead_status": "High Priority", "reason": "Explicit hiring intent"},
            {"id": 1, "lead_status": "Not a Lead", "reason": "Just a tutorial"}
        ]
    }
    """

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Analyze these posts:\n{posts_text}"}
    ]

    response_content = None

    # 2. Try SMART Model First (Llama 3.3 70B)
    try:
        completion = call_ai_model(messages, "llama-3.3-70b-versatile")
        response_content = completion.choices[0].message.content
    except Exception as e:
        print(f"⚠️ 70B Model failed (Rate Limit?). Switching to Fast Model... Error: {e}")
        
        # 3. Fallback to FAST Model (Llama 3.1 8B)
        try:
            time.sleep(1) 
            completion = call_ai_model(messages, "llama-3.1-8b-instant")
            response_content = completion.choices[0].message.content
        except Exception as e2:
            print(f"❌ Critical AI Error: {e2}")
            return []

    # 4. Safe JSON Parsing
    try:
        data = json.loads(response_content)
        
        # Normalization: ensure we have a list of items
        items = []
        if isinstance(data, dict):
            if "leads" in data and isinstance(data["leads"], list):
                items = data["leads"]
            elif "results" in data and isinstance(data["results"], list):
                items = data["results"]
            else:
                items = [data] # Wrap single dict
        elif isinstance(data, list):
            items = data
            
        # 5. Map results back to original posts
        analyzed_posts = []
        for item in items:
            if not isinstance(item, dict):
                continue
                
            post_id = item.get('id')
            
            # Verify ID validity
            if post_id is not None and isinstance(post_id, int) and 0 <= post_id < len(posts):
                original_post = posts[post_id].copy()
                original_post['lead_status'] = item.get('lead_status', 'Potential Lead')
                original_post['reason'] = item.get('reason', 'Matches criteria')
                analyzed_posts.append(original_post)
                
        return analyzed_posts

    except Exception as e:
        print(f"Processing Error: {e}")
        return []