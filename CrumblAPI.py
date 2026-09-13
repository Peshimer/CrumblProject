import re
import requests
from flask import Flask, jsonify
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/Crumbl")
def get_crumbl_data():
    page = requests.get("https://crumblcookies.com/")
    html = page.content
    soup = BeautifulSoup(html, "html.parser")

    elements = soup.find_all('p', class_=re.compile(r'font-extrabold text-\[28px\] .* on-background !text-\[35px\]'))
    cookies = []
    for p in elements:
        cookies.append(p.get_text(strip=True))
    return jsonify({"crumbl_data": cookies})

if __name__ == "__main__":
    app.run(debug=True)