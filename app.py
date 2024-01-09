import json
from flask import Flask, render_template, request
import requests
import http.client
import urllib.parse
import sys
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def display_news():
    if request.method == 'POST':
        # Handle the form submission if needed
        search_entry = request.form.get('search_entry')
        # Add logic for handling search_entry if needed
    else:
        if len(sys.argv) != 2:
            print("Usage: python news.py <access_key>")
            sys.exit(1)

        access_key = sys.argv[1]

        conn = http.client.HTTPConnection('api.mediastack.com')

        params = urllib.parse.urlencode({
            'access_key': access_key,
            'categories': '-general,-sports,-business,-technology',
            'sort': 'published_desc',
            'limit': 10,
            'languages': 'en'
        })

        conn.request('GET', '/v1/news?{}'.format(params))

        res = conn.getresponse()
        articles = res.read()

        print(articles.decode('utf-8'))

    return render_template('news.html', articles=json.loads(articles.decode('utf-8')))

if __name__ == '__main__':
    app.run()
