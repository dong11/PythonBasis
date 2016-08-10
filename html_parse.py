from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):

        if tag == 'script':
            pass
        else:
            print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()


url = input("Enter url:")

from urllib import request

with request.urlopen(url) as f:
    data = f.read()
    print(data, 'Status:' + str(f.status))
    print('****************解析后******************')
    parser.feed(data.decode('utf-8'))  # utf-8的HTML

