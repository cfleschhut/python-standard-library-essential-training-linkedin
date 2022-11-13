import urllib.request

sample_url = "http://httpbin.org/xml"

response = urllib.request.urlopen(sample_url)

status_code = response.status
if status_code >= 200 and status_code < 300:
    print(status_code)
    print(response.getheaders())
    print(response.getheader("Content-Type"))

    data = response.read().decode("utf-8")
    print(data)
