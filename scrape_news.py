import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the HTML content from Hacker News
url = "https://news.ycombinator.com/"
response = requests.get(url)

# Check if request was successful
if response.status_code != 200:
    print("Failed to fetch the webpage.")
    exit()

html_content = response.text

# Step 2: Parse HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Step 3: Extract headlines
headline_tags = soup.find_all("a", class_="titlelink")

# Collect unique headlines
headlines = []
for tag in headline_tags:
    text = tag.get_text(strip=True)
    if text not in headlines:
        headlines.append(text)

# Get at least 10 headlines
top_10 = headlines[:10]

# Step 4: Save to headlines.txt
with open("headlines.txt", "w", encoding="utf-8") as file:
    for headline in top_10:
        file.write(headline + "\n")

# Step 5: Output success message
print(f"Successfully saved {len(top_10)} headlines to headlines.txt")
