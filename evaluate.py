import requests
from bs4 import BeautifulSoup

# Replace with your repo and pages URLs
repo_url = "https://github.com/23f2003274/test-round2-updated"
pages_url = "https://23f2003274.github.io/test-round2-updated/"

# 1. LICENSE Check
try:
    license_url = repo_url + "/blob/main/LICENSE"
    r = requests.get(license_url)
    if r.status_code == 200 and "MIT License" in r.text:
        print("✅ LICENSE check passed")
    else:
        print("❌ LICENSE missing or incorrect")
except:
    print("❌ LICENSE check failed")

# 2. README Check
try:
    readme_url = repo_url + "/blob/main/README.md"
    r = requests.get(readme_url)
    if r.status_code == 200 and len(r.text) > 50:
        print("✅ README check passed")
    else:
        print("❌ README missing or too short")
except:
    print("❌ README check failed")

# 3. Pages Check
try:
    r = requests.get(pages_url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.title.string if soup.title else ""
        if "Round" in title or "Welcome" in title:
            print("✅ Pages check passed")
        else:
            print("❌ Pages loaded but content not correct")
    else:
        print("❌ Pages URL not reachable")
except:
    print("❌ Pages check failed")
