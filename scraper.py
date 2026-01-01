import requests
import xml.etree.ElementTree as ET
import time
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def clean_html(raw_html):
    if not raw_html:
        return ""
    clean_text = re.sub('<[^<]+?>', '', raw_html)
    return clean_text.strip()

def search_reddit(keyword, limit=10):
    clean_keyword = keyword.replace('"', '').replace("'", "")
    safe_keyword = clean_keyword.replace(" ", "+")
    required_words = clean_keyword.lower().split()

    url = f"https://www.reddit.com/search.rss?q={safe_keyword}&sort=new"
    print(f"DEBUG: Scraping -> {url}")

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            return []

        root = ET.fromstring(response.content)
        posts = []
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        
        entries = root.findall('atom:entry', ns)
        
        for entry in entries:
            if len(posts) >= limit:
                break
            
            try:
                title = entry.find('atom:title', ns).text
                link = entry.find('atom:link', ns).attrib['href']
                content_tag = entry.find('atom:content', ns)
                raw_content = content_tag.text if content_tag is not None else ""
                final_content = clean_html(raw_content)
                
                # --- NEW: GET REAL AUTHOR NAME ---
                author_tag = entry.find('atom:author', ns)
                if author_tag is not None:
                    name_tag = author_tag.find('atom:name', ns)
                    real_author = name_tag.text if name_tag is not None else "Unknown"
                else:
                    real_author = "Unknown"
                # ---------------------------------

                full_text = (title + " " + final_content).lower()

                # Relaxed Filter (Matches ANY word)
                if not any(word in full_text for word in required_words):
                    continue 

                if len(final_content) < 5: 
                    final_content = title

                posts.append({
                    'platform': 'Reddit',
                    'keyword': keyword,
                    'title': title,
                    'content': final_content,
                    'url': link,
                    'username': real_author,  # <--- Now uses real name
                    'created_utc': time.time()
                })
                
            except:
                continue
                
        print(f"DEBUG: Found {len(posts)} posts for '{keyword}'")
        return posts

    except Exception as e:
        print(f"RSS Error: {e}")
        return []