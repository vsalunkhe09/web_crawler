from builtins import str
from urllib.request  import urlopen
from urllib import parse
from link_finder import LinkFinder

class Spider:
    project_name = ''
    base_url = ''
    queue = set()

    def __init__(self, project_name, base_url):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.queue = '/queue.txt'

    def print_data(self):
        print(Spider.project_name)
        print(Spider.base_url)
        print(Spider.queue)

    def get_menu_links(self, page_url):
        html_string =''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
                finder = LinkFinder()
                finder.feed(html_string)
                menu_links = finder.get_links()
                return menu_links
        except Exception as error:
            print(str(error))
            return ''
