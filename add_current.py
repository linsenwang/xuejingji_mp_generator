# %%
import time
from bs4 import BeautifulSoup

# %%
def html_add(html_content, name, date, link):
    # 解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 创建新的item
    new_item = soup.new_tag('div', **{'class': 'item'})
    new_value_name = soup.new_tag('div', **{'class': 'value'})
    new_value_name.string = name
    new_value_date = soup.new_tag('div', **{'class': 'value'})
    new_value_date.string = date
    new_a_tag = soup.new_tag('a', href=link)
    new_a_tag.string = 'Click here'
    new_value_link = soup.new_tag('div', **{'class': 'value'})
    new_value_link.append(new_a_tag)

    new_item.append(new_value_name)
    new_item.append(new_value_date)
    new_item.append(new_value_link)

    # 将新的item插入body的最开头
    soup.main.insert(0, new_item)

    return soup.prettify()

def html_add_error(html_content, url):
    # 解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 创建新的item
    new_item = soup.new_tag('div', **{'class': 'item'})
    new_value_name = soup.new_tag('div', **{'class': 'value'})
    new_value_name.string = url
    new_value_date = soup.new_tag('div', **{'class': 'value'})
    new_value_date.string = str(time.ctime())
    new_value_link = soup.new_tag('div', **{'class': 'value', 'style': 'color:red'})
    new_value_link.string = 'error'

    new_item.append(new_value_name)
    new_item.append(new_value_date)
    new_item.append(new_value_link)

    # 将新的item插入body的最开头
    soup.main.insert(0, new_item)

    return soup.prettify()


# %%
def add(name, date, link):
    with open('index.html', 'r') as f:
        html = html_add(f, name, date, link)
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(html)

def add_error(url):
    with open('index.html', 'r') as f:
        html = html_add_error(f, url)
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(html)

