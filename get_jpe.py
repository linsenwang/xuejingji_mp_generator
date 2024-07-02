# %%
from curl_cffi import requests
from bs4 import BeautifulSoup
import re
import time
import gen_css
import add_current

# %%
headers={
    "user-agent":'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
}

# %%
jpe_requests = requests.get('https://www.journals.uchicago.edu/toc/jpe/current', impersonate='chrome110', headers=headers)
jpe_data = BeautifulSoup(jpe_requests.text, 'html.parser')

# %%
issue = re.sub(' \n', '',jpe_data.find(class_='citation-line').text)
issue

# %%
abstract = []
abstract_ori = jpe_data.find_all(class_='accordion__content')
for i in abstract_ori:
    abstract.append(i.text)
abstract

# %%
names = []
name_ori = jpe_data.find_all(attrs={'aria-label': "author"})
for i in name_ori:
    names.append(re.sub('\xa0', ' ' ,i.text))
names

# %%
title = []
title_ori = jpe_data.find_all(class_='issue-item__title')
for i in title_ori:
    title.append(i.text)
title = title[1:]

# %%
article = [*zip(title, names, abstract)]
article

# %%
with open('jpe/JPE_' + issue + '.html','w',encoding='UTF-8') as f:
    f.write(gen_css.gen_content_from_list(title))
    f.write(gen_css.gen_abstract_list(list(article)))
add_current.add('JPE_' + issue, time.ctime(), 'jpe/JPE_' + issue + '.html')

# %%
import BaiduTrans
title_cn = []
for i in title:
    te = BaiduTrans.trans(i)
    title_cn.append(te['trans_result'][0]['dst'])
    #l_cn.append(te)
    time.sleep(1)
title_cn

# %%
'''abstract_cn = []
for i in abstract:
    te = BaiduTrans.trans(i)
    abstract_cn.append(te['trans_result'][0]['dst'])
    #l_cn.append(te)
    time.sleep(1)
abstract_cn'''
abstract_cn = BaiduTrans.trans_list(abstract)

# %%
article_cn = [*zip(title_cn, names, abstract_cn)]
article_cn

# %%
with open('jpe/JPE_CN_' + issue + '.html','w',encoding='UTF-8') as f:
    f.write(gen_css.gen_content_from_list(title_cn))
    f.write(gen_css.gen_abstract_list(list(article_cn)))
add_current.add('JPE_CN_' + issue, time.ctime(), 'jpe/JPE_CN_' + issue + '.html')

# %%
abstract_cn = BaiduTrans.trans_list(abstract)
title_cn = BaiduTrans.trans_list(title)
article_cn = [*zip(title_cn, names, abstract_cn)]
with open('jpe/JPE_CN_' + issue + '.html','w',encoding='UTF-8') as f:
    f.write(gen_css.gen_content_from_list(title_cn))
    f.write(gen_css.gen_abstract_list(list(article_cn)))
add_current.add('JPE_CN_' + issue, time.ctime(), 'jpe/JPE_CN_' + issue + '.html')


