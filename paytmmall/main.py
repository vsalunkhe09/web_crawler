import threading
from spider import Spider


file = open('queue.txt', 'r')
base_url = file.readline()
project_name = 'paytmmall'
QUEUE_FILE = 'queue.txt'

spider = Spider(project_name, base_url)

spider.print_data()
links = spider.get_menu_links(base_url)
print(links)


# for link in links:
#     submenulinks = spider.get_menu_links(link)
#     print(submenulinks)
#     break


