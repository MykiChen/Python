# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random
import requests
import json
#from boss.models import ProxyModel

class UserAgentDownloadMiddleware(object):
    USER_AGENTS = [
        'Mozilla/5.0 (X11; U; UNICOS lcLinux; en-US) Gecko/20140730 (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.4; en; rv:1.9.2.24) Gecko/20111114 Camino/2.1 (like Firefox/3.6.24)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.4; en; rv:1.9.0.19) Gecko/2010051911 Camino/2.0.3 (like Firefox/3.0.19)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36'
    ]
    
    def process_request(self, request, spider):
        user_agent = random.choice(self.USER_AGENTS)
        request.headers['User-Agent'] = user_agent
        
        
class IPProxyDownloadMiddleware(object):
    PROXIES = [
        '223.199.25.245:9999','59.52.186.117:9999', '117.95.201.34:9999', '222.190.198.238:9999', '123.160.1.123:9999'
    ]
    #PROXY_URL = '..........'
    
    def __init__(self):
        super(IPProxyDownloadMiddleware, self).__init__()
        self.current_proxy = None
    
    def process_request(self, request, spider):
        if 'proxy' not in request.meta:
            proxy = random.choice(self.PROXIES)
            request.meta['proxy'] = proxy
            
            #请求代理 
            #proxy_model = self.get_proxy()
            
        #request.meta['proxy'] = self.current_proxy.proxy
"""    
    def process_response(self, request, response, spider):
        id response.statue != 200:
            self.update_proxy()
            #如果程序走到这一步，说明该请求已经被识别为爬虫
            #若不返回request，则程序不会再获取数据
            #重新return request后，请求重新加入到调度中，下次再继续发送
            return request
        
        #若程序正常执行，则需要return response
        return response
    
    def get_proxy(self):
        response = requests.get(self.PROXY_URL)
        text = response.text
        result = json.loads(text)
        
        if len(result(['data']) > 0:
            data = result['data'][0]
            proxy_model = ProxyModel(data)
            self.current_proxy = proxy_model
"""        
    