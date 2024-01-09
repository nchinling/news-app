import http.client, urllib.parse
import sys

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
    })

conn.request('GET', '/v1/news?{}'.format(params))

res = conn.getresponse()
data = res.read()

print(data.decode('utf-8'))