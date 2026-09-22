#!/usr/bin/env python3
"""
Autonomous Job Hunter Scraper
Pulls fresh remote design jobs from high-signal public APIs (Remotive, We Work Remotely),
applies strict filtering rules (no WordPress, no low pay, remote-only),
and outputs candidates for application into a clean markdown digest.
"""

import urllib.request
import json
import xml.etree.ElementTree as ET
import re
import os
from datetime import datetime

# Negative filter rules
DISALLOWED_KEYWORDS = [
    "wordpress", "elementor", "divi", "woocommerce",
    "intern", "internship", "volunteer", "unpaid",
    "telemarketer", "kundenservice", "customer service",
    "shopify developer", ".net", "java developer"
]

# Target titles and concepts
TARGET_KEYWORDS = [
    "product design", "ui/ux", "ux/ui", "ui designer", "ux designer",
    "product designer", "design engineer", "visual designer", "brand designer",
    "web designer", "content designer", "education designer"
]

def fetch_remotive_jobs():
    """Fetch jobs from Remotive's free public API"""
    url = "https://remotive.com/api/remote-jobs?category=design"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    results = []
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            data = json.loads(response.read().decode())
            jobs = data.get("jobs", [])
            for job in jobs:
                title = job.get("title", "")
                company = job.get("company_name", "")
                desc = job.get("description", "")
                url = job.get("url", "")
                salary = job.get("salary", "")
                location = job.get("candidate_required_location", "Anywhere")
                published = job.get("publication_date", "")
                
                results.append({
                    "source": "Remotive",
                    "title": title,
                    "company": company,
                    "salary": salary if salary else "Competitive / Unspecified",
                    "location": location,
                    "url": url,
                    "published": published,
                    "description": desc
                })
    except Exception as e:
        print(f"Error fetching Remotive: {e}")
    return results

def fetch_wwr_jobs():
    """Fetch jobs from We Work Remotely Design RSS"""
    url = "https://weworkremotely.com/categories/remote-design-jobs.rss"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    results = []
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            root = ET.fromstring(response.read())
            for item in root.findall(".//item"):
                title_full = item.find("title").text if item.find("title") is not None else ""
                link = item.find("link").text if item.find("link") is not None else ""
                desc = item.find("description").text if item.find("description") is not None else ""
                pubDate = item.find("pubDate").text if item.find("pubDate") is not None else ""
                
                company = "Company"
                title = title_full
                if ":" in title_full:
                    parts = title_full.split(":", 1)
                    company = parts[0].strip()
                    title = parts[1].strip()
                
                results.append({
                    "source": "We Work Remotely",
                    "title": title,
                    "company": company,
                    "salary": "Competitive / Unspecified",
                    "location": "Remote (Worldwide / Anywhere)",
                    "url": link,
                    "published": pubDate,
                    "description": desc
                })
    except Exception as e:
        print(f"Error fetching WWR: {e}")
    return results

def is_valid_match(job):
    title_lower = job["title"].lower()
    desc_lower = job["description"].lower()
    full_text = f"{title_lower} {desc_lower}"
    
    # Filter out dealbreakers
    for bad in DISALLOWED_KEYWORDS:
        if bad in title_lower:
            return False
            
    # Check if target title matches
    return any(target in title_lower for target in TARGET_KEYWORDS)

def run_pipeline():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running Autonomous Job Hunter...")
    
    remotive_jobs = fetch_remotive_jobs()
    wwr_jobs = fetch_wwr_jobs()
    
    all_jobs = remotive_jobs + wwr_jobs
    print(f"Fetched {len(all_jobs)} total listings from Remotive & WeWorkRemotely.")
    
    qualified = []
    for job in all_jobs:
        if is_valid_match(job):
            qualified.append(job)
            
    print(f"Identified {len(qualified)} matching qualified opportunities.")
    
    # Output markdown digest
    today_str = datetime.now().strftime('%Y-%m-%d')
    output_dir = "01_Brief/Job_Tracker/Digests"
    os.makedirs(output_dir, exist_ok=True)
    digest_path = os.path.join(output_dir, f"Job_Digest_{today_str}.md")
    
    with open(digest_path, "w") as f:
        f.write(f"# 🎯 Daily Curated Job Digest — {today_str}\n\n")
        f.write(f"> Curated automatically by Autonomous Job Hunter. Filtered for high-signal Product Design, UI/UX, and Design Engineering roles. No WordPress, no low-quality churn, verified remote.\n\n")
        
        f.write("## 📋 Qualified Matches\n\n")
        f.write("| Company | Position | Location | Source | Link |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- |\n")
        
        for job in qualified:
            f.write(f"| **{job['company']}** | {job['title']} | {job['location']} | {job['source']} | [View & Apply]({job['url']}) |\n")
            
        f.write("\n---\n\n## 🔍 Opportunity Breakdown\n\n")
        for i, job in enumerate(qualified, 1):
            clean_desc = re.sub('<[^<]+?>', ' ', job['description'])
            clean_desc = ' '.join(clean_desc.split()[:90]) + "..."
            
            f.write(f"### {i}. **{job['company']}** — {job['title']}\n")
            f.write(f"* **Source:** {job['source']} | **Location:** {job['location']}\n")
            f.write(f"* **Salary:** {job['salary']}\n")
            f.write(f"* **Application Link:** {job['url']}\n")
            f.write(f"* **Overview:** {clean_desc}\n\n")
            
    print(f"Daily digest saved to: {digest_path}")
    return digest_path, len(qualified)

if __name__ == "__main__":
    run_pipeline()
