import json
import urllib.request


def read_json():
    response = urllib.request.urlopen("https://httpbin.org/json")
    data = response.read().decode("utf-8")
    print(data)

    obj = json.loads(data)
    print(obj["slideshow"]["author"])

    for slide in obj["slideshow"]["slides"]:
        print(slide["title"])


def create_json_file():
    data = {
        "name": "Joe Marini",
        "author": True,
        "titles": [
            "Learning Python", "Advanced Python", "Python Standard Library Essential Training"
        ]
    }

    with open("json_output.json", "w") as fp:
        json.dump(data, fp, indent=4)


read_json()
create_json_file()
