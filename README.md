# CloudFlare DDNS
If you need a DDNS service you can use CloudFlare for free.

# Using
You have to change some informations in "comm" variable. You can find them in your CloudFlare Dashboard.

It can work as CronJob. Add a command like;
*/1 * * * * /usr/bin/python '/home/test/ddns.py'
