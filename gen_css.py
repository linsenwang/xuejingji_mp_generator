# %%
def gen_li(li_content):
    li = r'<li style="box-sizing: border-box;  visibility: visible; "> <p style="margin: 0px;  padding: 0px;  box-sizing: border-box;  visibility: visible; ">' + li_content +'</p> </li>'
    return li 

# %%
def gen_li_list(list):
    li_list = '' 
    for i in list:
        li_list +=  gen_li(str(i)) + ' '
    return li_list 

# %%
def gen_content_from_list(list):    
    content_list_item = gen_li_list(list)    
    content_list = r'<section style="text-align: center; line-height: 1.8; justify-content: center; display: flex; flex-flow: row; box-sizing: border-box; visibility: visible;"><section style="display: inline-block; width: 95%; vertical-align: top; border-width: 0px; border-radius: 10px; border-style: none; border-color: rgb(62, 62, 62); overflow: hidden; padding: 0px 10px; background-color: #fafafa; align-self: flex-start; flex: 0 0 auto; box-sizing: border-box; visibility: visible;"><section style="justify-content: center; display: flex; flex-flow: row; box-sizing: border-box; visibility: visible;"><section style="display: inline-block; vertical-align: top; width: 12%; align-self: flex-start; flex: 0 0 auto; box-sizing: border-box; visibility: visible;"><section style="margin: -10px 0% 0px; font-size: 11px; box-sizing: border-box; visibility: visible;"><section style="display: inline-block; vertical-align: top; box-sizing: border-box; visibility: visible;"><section style="width: 2em; padding: 0.3em 0.5em; background-color: rgba(57, 113, 18, 0.85); color: transparent; box-sizing: border-box; visibility: visible;"><p style="margin: 0px 0px 5px; padding: 0px; box-sizing: border-box; visibility: visible;">输</p><p style="margin: 0px; padding: 0px; box-sizing: border-box; visibility: visible;"><br style="box-sizing: border-box; visibility: visible;"></p></section><section style="height: 0.5em; width: 2em; border-left: 1em solid rgba(57, 113, 18, 0.85); border-right: 1em solid rgba(57, 113, 18, 0.85); box-sizing: border-box; border-bottom: 1em solid transparent !important; visibility: visible;"><svg viewBox="0 0 1 1" style="float: left; line-height: 0; width: 0px; vertical-align: top; visibility: visible;"></svg></section></section></section></section><section style="display: inline-block; vertical-align: top; width: 88%; padding: 0px 0px 0px 10px; align-self: flex-start; flex: 0 0 auto; box-sizing: border-box; visibility: visible;"><section style="margin: 10px 0% 0px; box-sizing: border-box; visibility: visible;"><section style="text-align: justify; color: rgb(83, 82, 105); box-sizing: border-box; visibility: visible;"><p style="white-space: normal; margin: 0px; padding: 0px; box-sizing: border-box; visibility: visible;"><br style="box-sizing: border-box; visibility: visible;"></p></section></section></section></section><section style="padding: 0px 2px; letter-spacing: 1px; text-align: justify; font-size: 16px; box-sizing: border-box; visibility: visible;"><ul class="list-paddingleft-1" style="list-style-type: disc; box-sizing: border-box; padding-left: 40px; list-style-position: outside; visibility: visible;">'+ content_list_item +'</ul></section></section></section>'    
    return content_list

# %%
def gen_title(index, title):    
    return r'<section style="margin: 0.5em 0px; text-align: center; box-sizing: border-box; "> <section style="display: inline-block; vertical-align: top; min-width: 4.6em; max-width: 100%; height: 2.3em; border-radius: 3em 3em 0px 0px; border-width: 2px; border-style: solid; border-color: rgba(57, 113, 18, 0.85); padding: 0.3em 0.3em 0px; box-sizing: border-box; "> <section style="display: inline-block; width: 100%; height: 100%; line-height: 1.6em; border-radius: 3em 3em 0px 0px; background-color: rgba(57, 113, 18, 0.85); color: rgb(255, 255, 255); font-size: 17px; box-sizing: border-box; "> <p style="margin: 0px; padding: 0px; box-sizing: border-box; "> <strong style="box-sizing: border-box; "> '+f'{index:02}'+' </strong> </p> </section> </section> </section> <section style="margin: 10px 0% 0px; box-sizing: border-box; "> <section style="font-size: 16px; color: rgb(44, 41, 41); text-align: center; letter-spacing: 1px; box-sizing: border-box; "> <p style="line-height: 1.8; margin: 0px; padding: 0px; box-sizing: border-box; "> '+title+'</p> </section> </section>'

# %%
def gen_name(name):     
    return '<p style="white-space: normal; margin: 0px; padding: 0px; box-sizing: border-box; "> <span style="font-size: 16px; box-sizing: border-box; "> <strong style="box-sizing: border-box; "> <span style="color: rgba(57, 113, 18, 0.85); box-sizing: border-box; "> 作者 | </span> </strong> </span> </p> <p style="white-space: normal;margin: 0px;padding: 0px;box-sizing: border-box;"><span style="color: rgb(0, 0, 0);box-sizing: border-box;">'+name+'</span></p>'

# %%
def gen_abstract(abstract):
    return r'<p style="white-space: normal; margin: 0px; padding: 0px; box-sizing: border-box; "> <span style="font-size: 16px; box-sizing: border-box; "> <strong style="box-sizing: border-box; "> <span style="color: rgba(57, 113, 18, 0.85); box-sizing: border-box; "> 摘要 |&nbsp; </span> </strong> </span> <span style="color: rgba(57, 113, 18, 0.85); box-sizing: border-box; "> <br style="box-sizing: border-box; "> </span> </p> <p style="line-height: 1.8; white-space: normal; margin: 0px; padding: 0px; box-sizing: border-box; "> <span style="color: rgb(0, 0, 0); font-size: 16px; box-sizing: border-box; "> '+abstract+'</span> </p>'

# %%
def gen_abstract_item(index,ulist):
    try:
        t = gen_title(index,str(ulist[0]))
        n = gen_name(str(ulist[1]))
        a = gen_abstract(str(ulist[2]))
        item = n + a
    except:
        pass
    return t + '<section style="margin: 10px 0%; text-align: center; justify-content: center; display: flex; flex-flow: row; box-sizing: border-box; "> <section style="display: inline-block; width: 100%; vertical-align: top; padding: 15px; background-position: 25.8037% -43.1473%; background-repeat: repeat; background-size: 29.7866%; background-attachment: scroll; border-style: solid; border-width: 1px; border-radius: 8px; border-color: transparent; overflow: hidden; align-self: flex-start; flex: 0 0 auto; background-color: #fafafa; box-sizing: border-box; "> <section style="font-size: 15px; color: rgb(142, 139, 139); text-align: justify; line-height: 1.8; letter-spacing: 1px; box-sizing: border-box; "> '+ item +'     </section> </section> </section>'

# %%
#with open('py_gen_test.html', 'w',encoding='UTF-8') as f:    
#    f.write(gen_abstract_item(1,['iuehiuhi hiaihiuh aih  huiuhuh iuh  hiuhiu iuh huiuhi hiu iuehiuhi hiaihiuh aih  huiuhuh iuh  hiuhiu iuh huiuhi hiu','tii','cool']))

# %%
def gen_abstract_list(ulist):
    abstract_list = ''
    for index,i in enumerate(ulist):
        abstract_list += str(gen_abstract_item(index+1, i))
    return abstract_list


# %%
def gen_header():
    return r'<section style="color: rgba(54, 92, 28, 0.92);  text-align: left;  padding: 0px 10px;  box-sizing: border-box;  visibility: visible; "> <p style="margin: 0px;  padding: 0px;  box-sizing: border-box;  visibility: visible; "> <span style="color: rgb(19, 19, 17);  box-sizing: border-box;  visibility: visible; "> 这是 </span> <span style="color: rgba(57, 113, 18, 0.92);  box-sizing: border-box;  visibility: visible; "> <em style="box-sizing: border-box;  visibility: visible; "> <strong style="box-sizing: border-box;  visibility: visible; "> 《学经济》 </strong> </em> </span> <span style="color: rgb(19, 19, 17);  box-sizing: border-box;  visibility: visible; "> 的一篇推送 </span> <br style="box-sizing: border-box;  visibility: visible; "> </p> </section>  <section style="text-align: center;  margin-top: 10px;  margin-bottom: 10px;  line-height: 0;  box-sizing: border-box;  visibility: visible; "> <section style="max-width: 100%;  vertical-align: middle;  display: inline-block;  line-height: 0;  box-shadow: rgb(0, 0, 0) 0px 0px 0px;  width: 100%;  box-sizing: border-box;  visibility: visible; "> <img class="rich_pages wxw-img" src="https://linsenwang.com/src_xjj/xjj_head.PNG" style="vertical-align: middle;  width: 80%;  box-sizing: border-box;  height: auto !important;  visibility: visible !important; "> </section> </section>  <section style="margin-top: 10px;  margin-bottom: 10px;  text-align: center;  box-sizing: border-box;  visibility: visible; "> <section style="border-bottom: 1px solid rgba(57, 113, 18, 0.85);  padding-top: 3px;  width: 100%;  margin-bottom: -3px;  box-sizing: border-box;  visibility: visible; "> <svg viewBox="0 0 1 1" style="float: left;  line-height: 0;  width: 0px;  vertical-align: top;  visibility: visible; "> </svg> </section> <section style="height: 5px;  line-height: 5px;  box-sizing: border-box;  visibility: visible; "> <section style="display: inline-block;  vertical-align: top;  background-color: rgb(255, 255, 255);  box-sizing: border-box;  visibility: visible; "> <span style="width: 5px;  height: 5px;  float: left;  border-radius: 50%;  background-color: rgba(57, 113, 18, 0.85);  box-sizing: border-box;  visibility: visible; "> </span>   <span style="width: 5px;  height: 5px;  float: left;  border-radius: 50%;  margin-left: 5px;  background-color: rgba(57, 113, 18, 0.85);  box-sizing: border-box;  visibility: visible; "> </span>   <span style="width: 5px;  height: 5px;  float: left;  border-radius: 50%;  margin-left: 5px;  background-color: rgba(57, 113, 18, 0.85);  box-sizing: border-box;  visibility: visible; "> </span>   <span style="width: 5px;  height: 5px;  float: left;  border-radius: 50%;  margin-left: 5px;  background-color: rgba(57, 113, 18, 0.85);  box-sizing: border-box;  visibility: visible; "> </span>   <span style="width: 5px;  height: 5px;  float: left;  border-radius: 50%;  margin-left: 5px;  background-color: rgba(57, 113, 18, 0.85);  box-sizing: border-box;  visibility: visible; "> </span>   </section> <section style="clear: both;  box-sizing: border-box;  visibility: visible; "> <svg viewBox="0 0 1 1" style="float: left;  line-height: 0;  width: 0px;  vertical-align: top;  visibility: visible; "> </svg> </section> </section> </section>'

# %%
def tech_support(name):
    return r'<section style="margin: 10px 0%; text-align: center; justify-content: center; display: flex; flex-flow: row; box-sizing: border-box; "> <section style="display: inline-block; width: 100%; vertical-align: top; background-color: #f0f0f0; padding: 8px; align-self: flex-start; flex: 0 0 auto; box-sizing: border-box; border-radius: 10px; "> <section style="padding: 0.5em 10px; line-height: 1.8; text-align: justify; letter-spacing: 2px; color: rgb(19, 19, 17); box-sizing: border-box; "> <p style="text-indent: 2em; white-space: normal; margin: 0px; padding: 0px; box-sizing: border-box; "> &nbsp; 微信公众号“经经有道”每周推送经济学科前沿文献与马克思政治经济学师生研讨的相关最新内容。本账号由厦门大学经济学院习近平新时代中国特色社会主义思想读书社、马克思主义政治经济学学习社与资本论研习社所属《学经济》编辑部负责。投稿联系邮箱xmuxjj@126.com。查看以前推送：点“经经有道”并选择“查看历史消息”。搜寻账号：xmujjyd或扫描下方二维码 </p> </section> <section style="margin: 0px 0%; line-height: 0; box-sizing: border-box; "> <section style="max-width: 100%; vertical-align: middle; display: inline-block; line-height: 0; width: 70%; box-shadow: rgb(0, 0, 0) 0px 0px 0px; box-sizing: border-box; "> <img class="rich_pages wxw-img js_img_placeholder wx_img_placeholder" data-ratio="1" data-s="300,640" data-src="https://mmbiz.qpic.cn/mmbiz_jpg/63Td0uSWUOibRhicusicrVmOMmaBr9475jY1XJM2bniaYaPG419iaicOKC0BnauRspQtxUCJYWyNUxWeu5cEMxiaOVkCg/640?wx_fmt=jpeg" style="vertical-align: middle;  box-sizing: border-box;  width: 75%;  border-radius: 10px; " src="https://linsenwang.com/src_xjj/qrcode_xjj.JPG"> </section> </section> <section style="font-size: 13px; padding: 0px 10px; line-height: 1.8; text-align: justify; letter-spacing: 2px; color: rgb(19, 19, 17); box-sizing: border-box; "> <p style="text-indent: 2em; margin: 0px; white-space: normal; padding: 0px; box-sizing: border-box; "> <br style="box-sizing: border-box; "> </p> </section> <section style="text-align: right; box-sizing: border-box; "> <p style="margin: 0px; padding: 0px; box-sizing: border-box; "> 技术支持：'+name+' </p> </section> </section> </section>'

# %%
with open('py_gen_test.html', 'a',encoding='UTF-8') as f:    
    f.write(tech_support('cool'))

# %%



