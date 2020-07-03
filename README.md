# CloudFlare DDNS
If you need a DDNS service you can use CloudFlare for free.

## Usage
You have to change some informations which are highlighted. You can find them in your CloudFlare Dashboard.

It can works as CronJob. Add a command like;

`*/1 * * * * /usr/bin/python '/home/test/ddns.py'`

## Finding DNS Record

[Cloudflare Get Domain's DNS Record]('https://gist.github.com/buraksakalli/410ccb26cdb1ad168ede3bd6377128eb')

```
curl -X GET "https://api.cloudflare.com/client/v4/zones/ZONE_ID/dns_records?type=A&name=<Domain>" \
     -H "X-Auth-Email: <email>" \
     -H "X-Auth-Key: <Global API Key>" \
     -H "Content-Type: application/json"
```