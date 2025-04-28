from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if attrs:
            print(f"Start : {tag}")
            for attr in attrs:
                attr_name = attr[0]
                attr_value = attr[1] if len(attr) > 1 else None
                print(f"-> {attr_name} > {attr_value}")
        else:
            print(f"Start : {tag}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        if attrs:
            print(f"Empty : {tag}")
            for attr in attrs:
                attr_name = attr[0]
                attr_value = attr[1] if len(attr) > 1 else None
                print(f"-> {attr_name} > {attr_value}")
        else:
            print(f"Empty : {tag}")

    def handle_comment(self, data):
        pass


parser = MyHTMLParser()
N = int(input())

html_code = '\n'.join([input() for _ in range(N)])
parser.feed(html_code)
