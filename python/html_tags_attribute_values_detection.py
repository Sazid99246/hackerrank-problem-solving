from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attr):
        print(tag)
        for name, value in attr:
            print(f"-> {name} > {value}")


parser = MyHTMLParser()
for i in range(int(input())):
    parser.feed(input())
