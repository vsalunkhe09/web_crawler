from html.parser import HTMLParser
from urllib.request  import urlopen
from urllib import parse

class LinkFinder(HTMLParser):

    links = set()
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin('https://www.paytmmall.com/',value)
                    self.links.add(url)

    def get_links(self):
        return self.links
