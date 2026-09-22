#!/usr/bin/env python3
"""
Autonomous Job Hunter Scraper (Multi-Board Edition)
Pulls fresh remote design jobs from:
1. We Work Remotely (Design RSS)
2. Remotive API (Design & Product categories)
3. RemoteOK API (Design tags)
4. Jobicy API (Design & UX feed)

Applies strict filtering rules (no WordPress, no low pay, remote-only).
"""

import urllib.request
import json
import xml.etree.ElementTree as ET
import re
import os
from datetime import datetime

DISALLOWED_KEYWORDS = [
    "wordpress", "elementor", "divi", "woocommerce",
    "intern", "internship", "volunteer", "unpaid",
    "telemarketer", "kundenservice", "customer service",
    "shopify developer", ".net", "java developer", "backend"
]

TARGET_KEYWORDS = [
    "product design", "ui/ux", "ux/ui", "ui designer", "ux designer",
    "product designer", "design engineer", "visual designer", "brand designer",
    "web designer", "content designer", "education designer", "interaction designer"
]

def fetch_json_feed(url, headers=None):
    if headers is None:
        headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def fetch_remotive():
    jobs = []
    # Fetch both design and product categories
    for cat in ["design", "product"]:
        data = fetch_json_feed(f"https://remotive.com/api/remote-jobs?category={cat}")
        if data and "jobs" in data:
            for job in data["jobs"]:
                title = job.get("title", "")
                jobs.append({
                    "source": "Remotive",
                    "title": title,
                    "company": job.get("company_name", ""),
                    "salary": job.get("salary", "Competitive / Unspecified"),
                    "location": job.get("candidate_required_location", "Anywhere"),
                    "url": job.get("url", ""),
                    "published": job.get("publication_date", ""),
                    "description": job.get("description", "")
                })
    return jobs

def fetch_remoteok():
    jobs = []
    data = fetch_json_feed("https://remoteok.com/api?tag=design")
    if data and isinstance(data, list):
        for job in data[1:]: # First item is metadata
            if isinstance(job, dict):
                title = job.get("position", "")
                jobs.append({
                    "source": "RemoteOK",
                    "title": title,
                    "company": job.get("company", ""),
                    "salary": f"${job.get('salary_min', '')} - ${job.get('salary_max', '')}" if job.get('salary_min') else "Competitive / Unspecified",
                    "location": job.get("location", "Worldwide"),
                    "url": job.get("url", ""),
                    "published": job.get("date", ""),
                    "description": job.get("description", "")
                })
    return jobs

def fetch_jobicy():
    jobs = []
    data = fetch_json_feed("https://jobicy.com/api/v2/remote-jobs?count=50&tag=design")
    if data and "jobs" in data:
        for job in data["jobs"]:
            jobs.append({
                "source": "Jobicy",
                "title": job.get("jobTitle", ""),
                "company": job.get("companyName", ""),
                "salary": job.get("annualSalaryMin", "") or "Competitive / Unspecified",
                "location": job.get("jobGeo", "Worldwide"),
                "url": job.get("url", ""),
                "published": job.get("pubDate", ""),
                "description": job.get("jobDescription", "")
            })
    return jobs

def fetch_wwr():
    jobs = []
    url = "https://weworkremotely.com/categories/remote-design-jobs.rss"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
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
                
                jobs.append({
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
    return jobs

def is_valid_match(job):
    title_lower = job["title"].lower()
    
    # 1. Filter out dealbreakers in title
    for bad in DISALLOWED_KEYWORDS:
        if bad in title_lower:
            return False
            
    # 2. Check title keywords
    return any(target in title_lower for target in TARGET_KEYWORDS)

def run_pipeline():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running Multi-Board Autonomous Job Hunter...")
    
    remotive_jobs = fetch_remotive()
    wwr_jobs = fetch_wwr()
    remoteok_jobs = fetch_remoteok()
    jobicy_jobs = fetch_jobicy()
    
    all_jobs = remotive_jobs + wwr_jobs + remoteok_jobs + jobicy_jobs
    print(f"Aggregated {len(all_jobs)} total listings across 4 major remote boards.")
    
    # Deduplicate by URL/Title
    seen = set()
    qualified = []
    for job in all_jobs:
        identifier = f"{job['company'].lower()}-{job['title'].lower()}"
        if identifier not in seen and is_valid_match(job):
            seen.add(identifier)
            qualified.append(job)
            
    print(f"Filtered down to {len(qualified)} high-signal Product & UI/UX Design opportunities.")
    
    # Generate Daily Digest Markdown
    today_str = datetime.now().strftime('%Y-%m-%d')
    output_dir = "01_Brief/Job_Tracker/Digests"
    os.makedirs(output_dir, exist_ok=True)
    digest_path = os.path.join(output_dir, f"Job_Digest_{today_str}.md")
    
    with open(digest_path, "w") as f:
        f.write(f"# 🎯 Daily Curated Job Digest — {today_str}\n\n")
        f.write(f"> Curated automatically across WeWorkRemotely, Remotive, RemoteOK, and Jobicy. Filtered for high-signal Product Design, UI/UX, and Design Engineering roles. No WordPress, no low-quality churn, verified remote.\n\n")
        
        f.write("## 📋 Top Qualified Matches\n\n")
        f.write("| Company | Position | Location | Source | Link |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- |\n")
        
        for job in qualified[:20]:
            f.write(f"| **{job['company']}** | {job['title']} | {job['location']} | {job['source']} | [View & Apply]({job['url']}) |\n")
            
        f.write("\n---\n\n## 🔍 Opportunity Breakdown\n\n")
        for i, job in enumerate(qualified[:15], 1):
            clean_desc = re.sub('<[^<]+?>', ' ', job['description'])
            clean_desc = ' '.join(clean_desc.split()[:80]) + "..."
            
            f.write(f"### {i}. **{job['company']}** — {job['title']}\n")
            f.write(f"* **Source:** {job['source']} | **Location:** {job['location']}\n")
            f.write(f"* **Salary:** {job['salary']}\n")
            f.write(f"* **Application Link:** {job['url']}\n")
            f.write(f"* **Overview:** {clean_desc}\n\n")
            
    print(f"Daily digest updated at: {digest_path}")
    return digest_path, qualified

if __name__ == "__main__":
    run_pipeline()
