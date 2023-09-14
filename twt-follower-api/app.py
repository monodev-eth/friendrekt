import json
from flask import Flask, jsonify
from twitter.scraper import Scraper

with open("cookies.json") as f:
    cook = json.load(f)

cookies = {}
for cookie in cook:
    cookies[cookie["name"]] = cookie["value"]

email, username, password, session = "1", "1", "1", None
scraper = Scraper(password, cookies)

# Initialize Flask app
app = Flask(__name__)

# Define the endpoint to get followers
@app.route('/followers/<int:userid>')
def get_followers(userid):
    user = scraper.users_by_ids([userid])
    print(user)
    return str(user[0]['data']['users'][0]['result']['legacy']['followers_count'])

if __name__ == '__main__':
    app.run(debug=True)