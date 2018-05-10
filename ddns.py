import json
import urllib
import os

ip = urllib.urlopen('http://api.buraksakalli.org/ip/?f=json')
data = json.loads(ip.read())
j = data['ip']

comm = komut = 'curl -X PUT "https://api.cloudflare.com/client/v4/zones/YOUR_DDNS_ZONE_ID/dns_records/YOUR_DNS_RECORD" \\n     -H "X-Auth-Email: yourmailaddress@address.com" \\n     -H "X-Auth-Key: YOUR_AUTH_KEY" \\n     -H "Content-Type: application/json" \\n     --data \'{"type":"A","name":"YOUR_DDNS_NAME","content":"'
cIp = j + "\"" + ',"ttl":120,"proxied":false}\''

lastComm = comm+cIp
os.system(lastComm)
print lastComm