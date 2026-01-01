Markdown

# 🚀 Local AI Lead Generator
### Turn Reddit Noise into High-Quality Business Leads automatically.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![AI](https://img.shields.io/badge/AI-Llama--3-purple)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![Google Sheets](https://img.shields.io/badge/Database-Google%20Sheets-green)

---

## 🧐 What is this? (In Plain English)
Imagine you are looking for gold in a river.
* **Traditional Scraping** is like using a bucket. You scoop up water, mud, rocks, and maybe a tiny speck of gold. You have to sort through it all manually.
* **This AI Tool** is like a **smart filter**. It scoops up the water, but before it shows you anything, an Artificial Intelligence (AI) looks at every single rock. If it’s just a rock, it throws it back. It **only** puts actual gold nuggets into your bucket.

**The Result:** You don't read 500 posts. You read the 5 that actually want to pay you money.

---

## 📸 See It In Action


### 1. The Dashboard (Search Interface)
> You type what you are looking for (e.g., "hiring video editor").
>
(https://github.com/vigyat13/Leads-Reddit-Ai-Powered-Leads-scraping-for-Business-/blob/main/Dashboard.png)

### 2. The Engine (Terminal Logs)
> The AI automatically switches brains (from 70B to 8B) if it gets "tired" (rate limited), ensuring it never crashes.


### 3. The Results (Google Sheets)
> Clean, organized leads appear in your spreadsheet instantly.
>
> **[📸 INSERT SCREENSHOT OF YOUR GOOGLE SHEET ROW HERE]**

---

## 🎯 How to Use This (3 Money-Making Scenarios)

### 🟢 Scenario 1: For Freelancers & Agencies (Finding Work)
You want to find people who are actively hiring right now.
* **Keywords to use:** `hiring video editor, looking for logo designer, budget for seo, need website help`
* **What the AI looks for:** Words like "hiring", "budget", "paid", "$".
* **Why it works:** It ignores students asking "how do I learn design?" and only keeps business owners saying "I need a designer."

### 🟠 Scenario 2: For SaaS Founders (Stealing Competitors)
You want to find people angry at your competitor so you can offer your better solution.
* **Keywords to use:** `clickup alternative, salesforce too expensive, hubspot bugs, migrate from asana`
* **What the AI looks for:** "Pain points," complaints, and "recommendation needed."
* **Why it works:** People complaining about software are 90% ready to switch. You just need to DM them.

### 🔴 Scenario 3: For Web Devs (The "Fix It" Method)
You want to find broken businesses that need urgent repairs.
* **Keywords to use:** `wordpress site hacked, shopify slow, stripe api error, database corrupted`
* **What the AI looks for:** Panic, urgency, technical errors.
* **Why it works:** These are high-ticket emergency leads. They need help *now*.

---

## 🧠 How It Works "Under the Hood"

1.  **The Net (Scraper):**
    The script scans live RSS feeds from Reddit for your keywords. It grabs everything that mentions "video editor" (for example).
2.  **The Brain (AI Filter):**
    Instead of saving everything, we send the text to **Groq (Llama-3 AI)**.
    * The AI reads the post like a human.
    * It asks: *"Is this person spending money?"*
    * If **NO** (it's a meme or tutorial) -> **DELETE**.
    * If **YES** (it's a job offer) -> **KEEP**.
3.  **The Bucket (Google Sheets):**
    The approved leads are formatted and sent instantly to your private Google Sheet, ready for you to contact.

---

## 🛠️ Quick Start Guide

### 1. Clone & Install
```bash
git clone [https://github.com/yourusername/lead-generator.git](https://github.com/yourusername/lead-generator.git)
cd lead-generator
pip install -r requirements.txt
2. Configure Keys
Create a config.py file:

Python

# config.py
GROQ_API_KEY = "gsk_your_key_here"
Note: Make sure you have service_account.json from Google Cloud for the Sheets integration.

3. Run the App
Bash

streamlit run main.py
🛡️ Features Checklist
[x] Real-Time Scraping: Fetches fresh data from the web.

[x] AI Intelligence: Distinguishes between "I want to be an editor" vs "I want to hire an editor."

[x] Auto-Fallback: Automatically switches from Llama-70B (Smart) to Llama-8B (Fast) if API limits are hit.

[x] Google Sheets Sync: Auto-saves leads to the cloud.

[x] Anti-Crash: Robust error handling so it can run 24/7.

💬 "Why Google Sheets?"
Because it is the universal database. You can connect Google Sheets to Zapier, Slack, or your CRM.

Lead comes in -> Google Sheet -> Zapier -> Email Notification to you.

You get a lead on your phone without lifting a finger.

Created for the "Lazy" Entrepreneur. Don't hunt for leads. Let the AI hunt for you.
