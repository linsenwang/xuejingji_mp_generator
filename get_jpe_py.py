
from curl_cffi import requests
from bs4 import BeautifulSoup
import re
import time
import gen_css
import gen_css_sans
import add_current


headers={
    "user-agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}
proxies = {"https": "socks://localhost:7890"}

jpe_requests = requests.get('https://www.journals.uchicago.edu/toc/jpe/current', impersonate='chrome120', headers=headers, proxies=proxies)
jpe_data = BeautifulSoup(jpe_requests.text, 'html.parser')

jpe_data

issue = re.sub(' \n', '',jpe_data.find(class_='citation-line').text)
issue

issue_item = jpe_data.find_all(class_='issue-item')

item = issue_item[2]

abstract = []
names = []
title = []

for item in issue_item:
    try:
        abstract_ori = item.find_all(class_='accordion__content')
        if abstract_ori == []:
            raise KeyError
        for i in abstract_ori:
            abstract.append(i.text)

        name_ori = item.find_all(attrs={'aria-label': "author"})
        for i in name_ori:
            names.append(re.sub('\xa0', ' ' ,i.text))

        title_ori = item.find_all(class_='issue-item__title')
        for i in title_ori:
            title.append(i.text)
    except:
        pass


article = [*zip(title, names, abstract)]
article


with open('jpe/JPE_' + issue + '.html','w',encoding='UTF-8') as f:
    f.write(gen_css.gen_content_from_list(title))
    f.write(gen_css.gen_abstract_list(list(article)))
add_current.add('JPE_' + issue, time.ctime(), 'jpe/JPE_' + issue + '.html')

with open('jpe/JPE_' + issue + '.html','w',encoding='UTF-8') as f:
    f.write(gen_css_sans.gen_content_from_list(title))
    f.write(gen_css_sans.gen_abstract_list(list(article)))
add_current.add('JPE_' + issue, time.ctime(), 'jpe/JPE_' + issue + '.html')


issue_item[0].text
abstract_ori = issue_item[0].find_all(class_='accordion__content')
abstract_ori









import BaiduTrans
title_cn = []
for i in title:
    te = BaiduTrans.trans(i)
    title_cn.append(te['trans_result'][0]['dst'])
    #l_cn.append(te)
    time.sleep(1)
title_cn


'''abstract_cn = []
for i in abstract:
    te = BaiduTrans.trans(i)
    abstract_cn.append(te['trans_result'][0]['dst'])
    #l_cn.append(te)
    time.sleep(1)
abstract_cn'''
abstract_cn = BaiduTrans.trans_list(abstract)


article_cn = [*zip(title_cn, names, abstract_cn)]
article_cn


with open('jpe/JPE_CN_' + issue + '.html','w',encoding='UTF-8') as f:
    f.write(gen_css.gen_content_from_list(title_cn))
    f.write(gen_css.gen_abstract_list(list(article_cn)))
add_current.add('JPE_CN_' + issue, time.ctime(), 'jpe/JPE_CN_' + issue + '.html')

with open('jpe/JPE_CN_' + issue + '.html','w',encoding='UTF-8') as f:
    f.write(gen_css_sans.gen_content_from_list(title_cn))
    f.write(gen_css_sans.gen_abstract_list(list(article_cn)))
add_current.add('JPE_CN_' + issue, time.ctime(), 'jpe/JPE_CN_' + issue + '.html')


abstract_cn = BaiduTrans.trans_list(abstract)
title_cn = BaiduTrans.trans_list(title)
article_cn = [*zip(title_cn, names, abstract_cn)]
with open('jpe/JPE_CN_' + issue + '.html','w',encoding='UTF-8') as f:
    f.write(gen_css.gen_content_from_list(title_cn))
    f.write(gen_css.gen_abstract_list(list(article_cn)))
add_current.add('JPE_CN_' + issue, time.ctime(), 'jpe/JPE_CN_' + issue + '.html')


