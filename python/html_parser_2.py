from html.parser import HTMLParser
import sys


class MyHTMLParser(HTMLParser):
    def handle_comment(self, comment):
        if '\n' in comment:
            print('>>> Multi-line Comment', comment, sep='\n')
        else:
            print('>>> Single-line Comment', comment, sep='\n')

    def handle_data(self, data):
        if not data == '\n':
            print('>>> Data', data, sep='\n')


html_chunk = sys.stdin.read()[1:].strip()

parser = MyHTMLParser()
parser.feed(html_chunk)
parser.close()
