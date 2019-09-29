import os

#Each website is separate project(folder)
def create_project(directory,base_url):
    if not os.path.exists(directory):
        print('Creating new Project : ' + directory)
        os.makedirs(directory)
        create_log_files(directory, base_url)
        create_py_files(directory)
        print('Project created....')
    else:
        print('Project already Exists in : ' + os.path.basename(os.getcwd()))

#crating log files
def create_log_files(project_name , base_url):
    queue = project_name  + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


#creating neccessary python files
def create_py_files(project_name):
    spider = project_name + '/spider.py'
    search = project_name + '/search.py'
    main_file = project_name + '/main.py'
    open(spider, 'w')
    open(search, 'w')
    open(main_file, 'w')

def write_file(path, data):
    file = open(path, 'w')
    file.write(data)
    file.close()


project_name = 'paytmmall'
base_url = 'https://www.amazon.com'
create_project(project_name , base_url)
