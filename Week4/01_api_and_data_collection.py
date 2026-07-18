"""
=========================================================
        API & DATA COLLECTION - PYTHON NOTES
=========================================================
"""

# =====================================================
# 1. WHAT IS AN API?
# =====================================================

"""
API = Application Programming Interface

An API allows two software applications to communicate.

Example:
Your Python program ---> API ---> Server ---> Data ---> Python program

Examples:
- Weather API
- GitHub API
- Google Maps API
- Twitter/X API
"""

# =====================================================
# 2. HTTP REQUEST METHODS
# =====================================================

"""
GET     -> Retrieve data
POST    -> Send new data
PUT     -> Update existing data
DELETE  -> Delete data
"""

# =====================================================
# 3. INSTALL REQUESTS LIBRARY
# =====================================================

# pip install requests

import requests

# =====================================================
# 4. SIMPLE GET REQUEST
# =====================================================

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print(response.status_code)      # 200 = Success

# =====================================================
# 5. RESPONSE CONTENT
# =====================================================

print(response.text)             # Raw text

# Convert JSON response into Python dictionary
data = response.json()

print(data)

"""
Output example:

{
 'userId':1,
 'id':1,
 'title':'...',
 'body':'...'
}
"""

# =====================================================
# 6. ACCESS JSON VALUES
# =====================================================

print(data["title"])
print(data["body"])

# =====================================================
# 7. JSON STRUCTURE
# =====================================================

"""
JSON looks like Python dictionaries.

JSON

{
    "name":"Aman",
    "age":20
}

Python

{
    "name":"Aman",
    "age":20
}
"""

# =====================================================
# 8. STATUS CODES
# =====================================================

"""
200 -> OK
201 -> Created
400 -> Bad Request
401 -> Unauthorized
403 -> Forbidden
404 -> Not Found
500 -> Server Error
"""

print(response.status_code)

# =====================================================
# 9. QUERY PARAMETERS
# =====================================================

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId":1
}

response = requests.get(url, params=params)

print(response.url)

# =====================================================
# 10. SEND DATA (POST)
# =====================================================

url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title":"Python",
    "body":"Learning APIs",
    "userId":1
}

response = requests.post(url, json=new_post)

print(response.status_code)
print(response.json())

# =====================================================
# 11. HEADERS
# =====================================================

headers = {
    "Accept":"application/json"
}

response = requests.get(url, headers=headers)

# =====================================================
# 12. API KEY (Example)
# =====================================================

"""
Some APIs require authentication.

headers = {
    "Authorization":"Bearer YOUR_API_KEY"
}

Never share your API key publicly.
"""

# =====================================================
# 13. ERROR HANDLING
# =====================================================

response = requests.get(url)

if response.status_code == 200:
    print("Success")
else:
    print("Request Failed")

# =====================================================
# 14. DATA COLLECTION METHODS
# =====================================================

"""
1. CSV files
2. Excel files
3. SQL Databases
4. APIs
5. Web Scraping
6. Sensors / IoT
"""

# =====================================================
# 15. READ CSV
# =====================================================

import pandas as pd

df = pd.read_csv("sample.csv")

print(df.head())

# =====================================================
# 16. READ EXCEL
# =====================================================

# pip install openpyxl

# df = pd.read_excel("sample.xlsx")

# =====================================================
# 17. WEB SCRAPING (BeautifulSoup)
# =====================================================

from bs4 import BeautifulSoup

html = """
<html>
<h1>Python</h1>
<p>Learning Web Scraping</p>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

print(soup.h1.text)
print(soup.p.text)

# =====================================================
# 18. SCRAPING FROM WEBSITE
# =====================================================

url = "https://example.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)

# =====================================================
# 19. SELENIUM (Dynamic Websites)
# =====================================================

"""
Used when JavaScript loads the page.

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://example.com")

print(driver.title)

driver.quit()
"""

# =====================================================
# 20. JSON TO DATAFRAME
# =====================================================

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

users = response.json()

df = pd.DataFrame(users)

print(df.head())

# =====================================================
# 21. SAVE DATA
# =====================================================

df.to_csv("users.csv", index=False)

# =====================================================
# 22. COMMON LIBRARIES
# =====================================================

"""
requests      -> API requests

json          -> JSON handling

pandas        -> Data analysis

BeautifulSoup -> HTML parsing

Scrapy        -> Large-scale web scraping

Selenium      -> Dynamic website automation
"""

# =====================================================
# 23. API WORKFLOW
# =====================================================

"""
Python Program
      │
      ▼
requests.get()
      │
      ▼
API Server
      │
      ▼
JSON Response
      │
      ▼
response.json()
      │
      ▼
Python Dictionary/List
      │
      ▼
Pandas DataFrame
      │
      ▼
Analysis
"""

# =====================================================
# 24. DATA COLLECTION WORKFLOW
# =====================================================

"""
Data Sources
      │
      ▼
CSV / Excel / API / Database / Website
      │
      ▼
Collect Data
      │
      ▼
Clean Data
      │
      ▼
Analyze
      │
      ▼
Visualize
      │
      ▼
Build Machine Learning Model
"""

# =====================================================
# 25. KEY POINTS TO REMEMBER
# =====================================================

"""
✔ requests.get()      -> Retrieve data
✔ requests.post()     -> Send data
✔ response.text       -> Raw response
✔ response.json()     -> Python dictionary/list
✔ response.status_code -> HTTP status
✔ BeautifulSoup()     -> Parse HTML
✔ pd.read_csv()       -> Read CSV
✔ pd.DataFrame()      -> Create DataFrame
✔ df.to_csv()         -> Save CSV
✔ Selenium            -> Dynamic websites
✔ Scrapy              -> Large web scraping projects
"""

print("Notes Completed!")