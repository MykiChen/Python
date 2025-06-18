# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['http://accounts.douban.com/login']
    login_url = 'http://accounts.douban.com/login'
    profile_url = 'https://www.douban.com/people/208513061/'
    editsignature_url = 'https://www.douban.com/j/people/208513061/edit_signature'

    def parse(self, response):
        formdata = {
            'source': 'None',
            'redir': 'https://www.douban.com/',
            'form_email': '136640850@qq.com',
            'remember': 'on',
            'login': '登录'
        }
        captcha_url = response.css('img#captcha_image::attr(src)').get()
        
        if captcha_url:
            captcha = self.regonize_captcha(captcha_url)
            formdata['captcha-solution'] = captcha
            captcha_id = response.xpath("//input[@name = 'captcha-id']/@value").get()
            formdata['captcha-id'] = captcha_id
           
        yield scrapy.FormRequest(url = self.login_url, formdata = formdata, callback = self.parse_after_login)
        
    def parse_after_login(self, response):
        if response.url = 'https://www.douban.com/':
            yield scrapy.Request(self.profile_url, callback = self.parse_prfile)
            
            print('登录成功!')
        else:
            print('登录失败!')
            
    def parse_profile(self, response):
        print(response.url)
        if response.url == self.profile_url:
            print('已经进入到个人中心')
            ck = response.xpath("//input[@name = 'ck']/@value").get()
            formdata = {
                'ck': ck, 
                'signature': 'Hello World'
            }
            yield scrapy.FormRequest(self.editsignature_url, formdata = formdata)
                
        else:
            print('进入个人中心失败')
          
        
    def regonize_captcha(self, image_url):
        request.urlretrieve(image_url, 'captcha.png')
        image = Image.open('captcha.png')
        image.show()
        captcha = input('请输入验证码')
        return captcha
