#geturl: 返回请求对象的url
#info: 请求反馈对象的meta信息
#getcode; 返回的http code

from urllib import  request

if __name__=='__main__':
    url='https://movie.douban.com/'#打开相应的url并把相应的页面作为一个返回
    rsp= request.urlopen(url)
    #把返回的结果读取出来
    # 读取出来的内容为bytes
    print(type(rsp))
    print(rsp)
    print('url:{0}',format(rsp.geturl()))
    print('info:{0}',format(rsp.info()))
    print('code:{0}',format(rsp.getcode()))

    html = rsp.read()
