import requests
import json

API_URL = 'https://api.buraksakalli.org/ip'
API_RES = json.loads(requests.get(API_URL).content)['ip']

URL = 'https://api.cloudflare.com/client/v4/zones/<YOUR_DNS_ZONE>/dns_records/<YOUR_DNS_RECORD>'

headers = {
  'X-Auth-Email': '<YOUR_EMAIL>',
  'X-Auth-Key': '<YOUR_AUTH_KEY>',
  'Content-Type': 'application/json'
}

data = {
  "type":"A",
  "name":"<DOMAIN_OR_SUBDOMAIN>", #to use DDNS
  "content": API_RES,
  "ttl": 120,
  "proxied": "false"
}

CF_RES = requests.put(URL, headers=headers, data=json.dumps(data))

print CF_RES.text