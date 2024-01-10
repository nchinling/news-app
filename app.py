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
       
        search_entry = request.form.get('search_entry')
        access_key = sys.argv[1]

        conn = http.client.HTTPConnection('api.mediastack.com')

        params = urllib.parse.urlencode({
            'access_key': access_key,
            'keywords': search_entry,
            'sort': 'published_desc',
            'limit': 10,
            'languages': 'en'
        })
        
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

    articles_data = json.loads(articles.decode('utf-8'))

    for article in articles_data['data']:
        article['published_at'] = format_date(article['published_at'])

    return render_template('news.html', articles=articles_data)


def format_date(date_str):
    date_object = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S+00:00")
    formatted_date = date_object.strftime("%d-%m-%Y %H:%M:%S")
    return formatted_date

if __name__ == '__main__':
    app.run()
