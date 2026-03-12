import re
from datetime import datetime

class ExperienceParser:
    def __init__(self):
        # Upgraded Date Regex to catch YYYY, MM/YYYY, and Mon YYYY
        self.date_pattern = re.compile(
            r"((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}|\d{2}/\d{4}|\d{4})\s*(?:-|–|to)\s*((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}|\d{2}/\d{4}|\d{4}|Present|Current)",
            re.IGNORECASE
        )
        # Added FinTech / Quant specific titles
        self.common_titles = [
            "Data Scientist", "Data Analyst", "Machine Learning Engineer", 
            "Equity Research Analyst", "Quantitative Analyst", "Financial Analyst", 
            "Investment Banker", "Portfolio Manager", "Software Engineer",
            "Business Analyst", "Quantitative Equity Analyst"
        ]

    def parse_date(self, date_str):
        """Converts strings into exact datetime objects."""
        date_str = date_str.strip().lower()
        if date_str in ["present", "current"]:
            return datetime.today()
        
        if re.fullmatch(r"\d{4}", date_str):
            return datetime(int(date_str), 1, 1)
            
        mm_match = re.fullmatch(r"(\d{2})/(\d{4})", date_str)
        if mm_match:
            return datetime(int(mm_match.group(2)), int(mm_match.group(1)), 1)
            
        for fmt in ("%b %Y", "%B %Y"):
            try:
                return datetime.strptime(date_str.title(), fmt)
            except ValueError:
                continue
                
        return datetime.today() # Fallback safety

    def parse_experience(self, experience_text):
        jobs = []
        lines = experience_text.split('\n')
        previous_line = ""
        
        for line in lines:
            line = line.strip()
            if not line: continue
                
            date_match = self.date_pattern.search(line)
            if date_match:
                start_raw = date_match.group(1)
                end_raw = date_match.group(2)
                
                start_date = self.parse_date(start_raw)
                end_date = self.parse_date(end_raw)
                
                # Calculate duration in months
                duration_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                duration_months = max(duration_months, 1)
                
                found_title = "Unknown Title"
                for title in self.common_titles:
                    if title.lower() in previous_line.lower() or title.lower() in line.lower():
                        found_title = title
                        break
                
                company = "Unknown Company"
                if " at " in previous_line.lower():
                    company = previous_line.split(" at ")[-1].strip()
                elif "|" in previous_line:
                    company = previous_line.split("|")[0].strip()
                elif "," in previous_line:
                    company = previous_line.split(",")[0].strip()

                jobs.append({
                    "job_title": found_title,
                    "company": company,
                    "duration": f"{start_raw} - {end_raw}",
                    "start_date": start_date,  # Kept temporarily for timeline math
                    "end_date": end_date,      # Kept temporarily for timeline math
                    "duration_months": duration_months
                })
            previous_line = line 

        # Upgrade: Prevent Double Counting & Detect Gaps
        total_months = self._calculate_merged_months(jobs)
        gaps = self._detect_gaps(jobs)

        # Clean up datetime objects before saving to JSON
        for job in jobs:
            del job["start_date"]
            del job["end_date"]

        return {
            "experience_entries": jobs,
            "employment_gaps": gaps,
            "total_experience_years": round(total_months / 12.0, 1)
        }

    def _calculate_merged_months(self, jobs):
        """Prevents double-counting overlapping jobs."""
        if not jobs: return 0
        periods = [(job["start_date"], job["end_date"]) for job in jobs]
        periods.sort(key=lambda x: x[0])
        
        merged = [periods[0]]
        for current in periods[1:]:
            last = merged[-1]
            if current[0] <= last[1]: # Overlap detected!
                merged[-1] = (last[0], max(last[1], current[1]))
            else:
                merged.append(current)
                
        total_months = sum((end.year - start.year) * 12 + (end.month - start.month) for start, end in merged)
        return max(total_months, 1)

    def _detect_gaps(self, jobs):
        """Finds gaps > 6 months between jobs."""
        gaps = []
        if len(jobs) < 2: return gaps
        
        sorted_jobs = sorted(jobs, key=lambda x: x["start_date"])
        for i in range(1, len(sorted_jobs)):
            prev_end = sorted_jobs[i-1]["end_date"]
            curr_start = sorted_jobs[i]["start_date"]
            
            gap_months = (curr_start.year - prev_end.year) * 12 + (curr_start.month - prev_end.month)
            if gap_months >= 6:
                gaps.append({
                    "gap_duration_months": gap_months,
                    "between_roles": f"{sorted_jobs[i-1]['job_title']} and {sorted_jobs[i]['job_title']}"
                })
        return gaps