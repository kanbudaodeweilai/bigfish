from urllib import request,parse
if __name__ =='__main__':
    qs ={
        'kw':'%BA%A3%D4%F4%CD%F5',
        'ie':'utf-8',
        'pn':0
    }
urls = []
baseurl = 'https://tieba.baidu.com/f?'
for i in range(10):
    pn = i * 50
    qs['pn']=str(pn)
    urls.append(baseurl + parse.urlencode(qs))
print(urls)
for url in urls:
    rsp = request.urlopen(url)
    html = rsp.read().decode('utf-8')
    print(url)
    print(html)
'''
把抓到的内容保存到文件中，后缀为html
'''
fileOb = open('海贼王贴吧爬虫.txt','w',encoding='utf-8')
fileOb.write(html)
fileOb.close()

