from urllib import request,error
#构建代理群
#每次访问随机选区代理并执行。


#使用代理的步骤：
#1，设置代理地址
proxy_list = [
    {'http':'24.237.235.245:8080'},
    {'http':'60.250.79.187:80'},
    {'http':'94.242.55.108:10010'},
    {'http':'188.166.69.172:8080'}
    ]
#2.创建proxyHandler列表
proxy_handler_list =[]
for proxy in proxy_list:
    proxy_handler=request.ProxyHandler(proxy)
    proxy_handler_list.append(proxy_handler)
#3.创建opener

opener_list =[]
for proxy_handler in proxy_handler_list:
    opener = request.build_opener(proxy_handler)
    opener_list.append(opener)
for opener in opener_list:
    request.install_opener(opener)


import  random
url ='http://www.baidu.com'
# 现在如果访问url，则使用代理服务器
try:
    #安装opener
    opener =random.choice(opener_list)
    request.install_opener(opener)

    rsp = request.urlopen(url)
    html = rsp.read().decode()
    print(html)

#反馈错误原因
except error.URLError as e:
    print(e)
except Exception as e :
    print(e)
