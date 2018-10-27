#利用request下载页面
#自动检测页面的编码
'''
-网页编码问题解决：
- chardet 可以自动解决页面文件的编码格式。但是可能有误
- 需要安装，conda install chardet

'''
from urllib import request
import chardet
if  __name__=='__main__':
    url='https://movie.douban.com/'
    rsp =request.urlopen(url)
    html= rsp.read()
    cs=chardet.detect(html)
    print(type(cs))
    print(cs)
    html= html.decode(cs.get('encoding','utf-8'))
    print(html)
