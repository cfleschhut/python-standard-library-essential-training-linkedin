import urllib.parse

sample_url = "http://server.example.com:8080/example.html?val1=1&val2=Hello+World"
sample_string = "Hello El Niño"
query_data = {
    'Name': "John Doe",
    "City": "Anytown USA",
    "Age": 37
}

result = urllib.parse.urlparse(sample_url)

print(result)
print(result.scheme, result.hostname, result.path)
print(result.geturl())

print(urllib.parse.quote(sample_string))
print(urllib.parse.quote_plus(sample_string))

print(urllib.parse.urlencode(query_data))
