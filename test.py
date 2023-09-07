import http.client

conn = http.client.HTTPConnection("google.com", 80)
conn.request("GET", "/index.html")
response = conn.getresponse()
print(response.status, response.reason)
print(response.read())