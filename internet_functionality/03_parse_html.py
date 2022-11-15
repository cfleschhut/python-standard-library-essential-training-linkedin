from html.parser import HTMLParser

metacount = 0


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

        pos = self.getpos()
        print(f"At line {pos[0]} and char {pos[1]}")

        if len(attrs) > 0:
            print("\tAttributes")
            for attr in attrs:
                print(f"\t{attr[0]}='{attr[1]}'")

        global metacount
        if tag == "meta":
            metacount += 1

    def handle_endtag(self, tag):
        print("Encountered an end tag:", tag)

    def handle_data(self, data):
        print("Encountered some data:", data)

    def handle_comment(self, data):
        print("Encountered a comment:", data)


parser = MyHTMLParser()

# parser.feed('<html lang="en"><head><title>Test</title></head>'
#             '<body><h1>Parse me!</h1></body></html>')

with open("samplehtml.html", "r") as f:
    content = f.read()
    parser.feed(content)

print(f"{metacount} meta tags found")
