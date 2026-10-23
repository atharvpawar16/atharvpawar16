#!/usr/bin/env python3
"""Render a truthful HackerRank card for atharvpawar16 from HackerRank's own public API.
Only real fields are shown: username and earned-badge count. No country/level."""
import json, urllib.request

USER = "atharvpawar16"
req = urllib.request.Request(
    f"https://www.hackerrank.com/rest/hackers/{USER}/badges",
    headers={"User-Agent": "Mozilla/5.0"},
)
data = json.load(urllib.request.urlopen(req, timeout=30))
badges = len(data.get("models", []))

svg = f'''<svg width="858" height="150" viewBox="0 0 858 150" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="HackerRank stats for {USER}">
  <rect x="0.5" y="0.5" width="857" height="149" rx="6" fill="#FFFEFE" stroke="#E4E2E2"/>
  <text x="32" y="52" font-family="Segoe UI, Ubuntu, Sans-Serif" font-size="24" font-weight="600" fill="#B87333">Atharv Pawar</text>
  <text x="32" y="78" font-family="Segoe UI, Ubuntu, Sans-Serif" font-size="15" fill="#434D58">HackerRank &#183; @{USER}</text>
  <text x="32" y="126" font-family="Segoe UI, Ubuntu, Sans-Serif" font-size="34" font-weight="700" fill="#B87333">{badges}</text>
  <text x="86" y="126" font-family="Segoe UI, Ubuntu, Sans-Serif" font-size="15" fill="#434D58">badges earned</text>
</svg>
'''
with open("hackerrank.svg", "w") as f:
    f.write(svg)
print(f"badges={badges}")
