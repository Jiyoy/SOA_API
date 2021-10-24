import urllib.request, urllib.parse, urllib.error
import json
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1392282.json"
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read() #string type
#print(data)
print('Retrieved', len(data), 'characters')

info = json.loads(data)
#print(info)
print('User count:', len(info))

count = 0
c_sum = 0
for item in info["comments"]:
    print('count', item["count"])
    count = count + 1
    c_sum = c_sum + int(item["count"])

print("Count :", count)
print("Sum :", c_sum)

