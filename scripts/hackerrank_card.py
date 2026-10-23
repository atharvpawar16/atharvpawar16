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

svg = f'''<svg width="500" height="130" viewBox="0 0 500 130" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="HackerRank stats for {USER}">
  <rect x="0.5" y="0.5" width="499" height="129" rx="6" fill="#FFFEFE" stroke="#E4E2E2"/>
  <text x="25" y="42" font-family="Segoe UI, Ubuntu, Sans-Serif" font-size="20" font-weight="600" fill="#B87333">Atharv Pawar</text>
  <text x="25" y="64" font-family="Segoe UI, Ubuntu, Sans-Serif" font-size="13" fill="#434D58">HackerRank &#183; @{USER}</text>
  <text x="25" y="106" font-family="Segoe UI, Ubuntu, Sans-Serif" font-size="30" font-weight="700" fill="#B87333">{badges}</text>
  <text x="70" y="106" font-family="Segoe UI, Ubuntu, Sans-Serif" font-size="13" fill="#434D58">badges earned</text>
</svg>
'''
with open("hackerrank.svg", "w") as f:
    f.write(svg)
print(f"badges={badges}")
