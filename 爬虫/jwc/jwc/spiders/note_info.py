# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import re
from jwc.items import JwcItem

'''本爬虫主要爬取的对象是学校主页上的各个分栏（如上理要闻，校园快讯等）的所有通知以及学校教务处的所有通知公告
，将其各个通知的信息存储为 id,title,body,url,crawltime,releasetime 六个字段，其中爬虫需要爬取的是titled
代表的通知标题，body代表的通知正文（学校主页上的通知正文为该通知网页中正文的源码，教务处的通知正文为网页中通知
源码的text部分），releasetime代表的通知发布时间。其他的id字段为自增，crawltime字段为数据存储时数据库自动生成'''

class QuotesSpider(scrapy.Spider):
	name = "jwc"
	start_urls = [
        'http://www.usst.edu.cn/s/1/t/517/p/1/i/52/list.htm',
	]

	'''引出学校主页的类别1（上理要闻图片）'''
	def parse(self,response):
		page=52 #总页数
		yield scrapy.Request('http://www.usst.edu.cn/s/1/t/517/p/1/i/52/list.htm',meta={'page':page},callback=self.parse1)


	'''获取学校主页分栏1所有通知'''
	def parse1(self, response):
		page=response.meta['page']
		page=page-1
		infos=response.xpath('//a[re:test(@href,"^(http:\/\/\w{2,5}\.usst\.edu\.cn)?\/s\/\d{1,2}\/t\/\d{3}\/\w{2}\/\w{2}\/info\d{5}\.htm")]')
		for info in infos:
			urls=info.xpath('..//a/@href').extract()
			if len(urls)!=0:
				url=urls[0]
				if url[0:4]=='http':
					next_url=url
				else:
					next_url="http://www.usst.edu.cn"+url
				yield scrapy.Request(next_url,callback=self.parse_info)
		if page>0:
			yield scrapy.Request('http://www.usst.edu.cn/s/1/t/517/p/1/i/'+str(page)+'/list.htm',meta={'page':page},callback=self.parse1)
		else:
			page = 385
			yield scrapy.Request('http://www.usst.edu.cn/s/1/t/517/p/2/i/385/list.htm', meta={'page': page},callback=self.parse2)

	'''获取学校主页分栏2（上理要闻）所有通知'''
	def parse2(self, response):
		page=response.meta['page']
		page=page-1
		infos=response.xpath('//a[re:test(@href,"^(http:\/\/\w{2,5}\.usst\.edu\.cn)?\/s\/\d{1,2}\/t\/\d{3}\/\w{2}\/\w{2}\/info\d{4,5}\.htm")]')
		for info in infos:
			urls = info.xpath('..//a/@href').extract()
			if len(urls) != 0:
				url = urls[0]
				if url[0:4] == 'http':
					next_url = url
				else:
					next_url = "http://www.usst.edu.cn" + url
				yield scrapy.Request(next_url, callback=self.parse_info)
		if page > 0:
			yield scrapy.Request('http://www.usst.edu.cn/s/1/t/517/p/2/i/' + str(page) + '/list.htm',
								 meta={'page': page}, callback=self.parse2)
		else:
			page = 230
			yield scrapy.Request('http://www.usst.edu.cn/s/1/t/517/p/4/i/230/list.htm', meta={'page': page},callback=self.parse4)

	'''获取学校主页分栏4（校园快讯）所有通知'''
	def parse4(self, response):
		page = response.meta['page']
		page = page - 1
		infos = response.xpath(
			'//a[re:test(@href,"^(http:\/\/\w{2,5}\.usst\.edu\.cn)?\/s\/\d{1,2}\/t\/\d{3}\/\w{2}\/\w{2}\/info\d{5}\.htm")]')
		for info in infos:
			urls = info.xpath('..//a/@href').extract()
			if len(urls) != 0:
				url = urls[0]
				if url[0:4] == 'http':
					next_url = url
				else:
					next_url = "http://www.usst.edu.cn" + url
				yield scrapy.Request(next_url, callback=self.parse_info)
		if page > 0:
			yield scrapy.Request('http://www.usst.edu.cn/s/1/t/517/p/4/i/' + str(page) + '/list.htm',
								 meta={'page': page}, callback=self.parse4)
		else:
			page = 311
			yield scrapy.Request('http://www.usst.edu.cn/s/1/t/517/p/5/i/311/list.htm', meta={'page': page},
								 callback=self.parse5)

	'''获取学校主页分栏5（学校公告）所有通知'''
	def parse5(self, response):
		page = response.meta['page']
		page = page - 1
		infos = response.xpath(
			'//a[re:test(@href,"^(http:\/\/\w{2,5}\.usst\.edu\.cn)?\/s\/\d{1,2}\/t\/\d{3}\/\w{2}\/\w{2}\/info\d{5}\.htm")]')
		for info in infos:
			urls = info.xpath('..//a/@href').extract()
			if len(urls) != 0:
				url = urls[0]
				if url[0:4] == 'http':
					next_url = url
				else:
					next_url = "http://www.usst.edu.cn" + url
				yield scrapy.Request(next_url, callback=self.parse_info)
		if page > 0:
			yield scrapy.Request('http://www.usst.edu.cn/s/1/t/517/p/5/i/' + str(page) + '/list.htm',
								 meta={'page': page}, callback=self.parse5)
		else:
			page = 134
			yield scrapy.Request('http://www.usst.edu.cn/s/1/t/517/p/6/i/134/list.htm', meta={'page': page},
								 callback=self.parse6)

	'''获取学校主页分栏6（教研信息）所有通知'''
	def parse6(self, response):
		page = response.meta['page']
		page = page - 1
		infos = response.xpath(
			'//a[re:test(@href,"^(http:\/\/\w{2,5}\.usst\.edu\.cn)?\/s\/\d{1,2}\/t\/\d{3}\/\w{2}\/\w{2}\/info\d{5}\.htm")]')
		for info in infos:
			urls = info.xpath('..//a/@href').extract()
			if len(urls) != 0:
				url = urls[0]
				if url[0:4] == 'http':
					next_url = url
				else:
					next_url = "http://www.usst.edu.cn" + url
				yield scrapy.Request(next_url, callback=self.parse_info)
		if page > 0:
			yield scrapy.Request('http://www.usst.edu.cn/s/1/t/517/p/6/i/' + str(page) + '/list.htm',
								 meta={'page': page}, callback=self.parse6)
		else:
			page = 49
			yield scrapy.Request('http://www.usst.edu.cn/s/1/t/517/p/8/i/49/list.htm', meta={'page': page},
								 callback=self.parse8)

	'''获取学校主页分栏8（媒体聚焦）所有通知'''
	def parse8(self, response):
		page = response.meta['page']
		page = page - 1
		infos = response.xpath(
			'//a[re:test(@href,"^(http:\/\/\w{2,5}\.usst\.edu\.cn)?\/s\/\d{1,2}\/t\/\d{3}\/\w{2}\/\w{2}\/info\d{5}\.htm")]')
		for info in infos:
			urls = info.xpath('..//a/@href').extract()
			if len(urls) != 0:
				url = urls[0]
				if url[0:4] == 'http':
					next_url = url
				else:
					next_url = "http://www.usst.edu.cn" + url
				yield scrapy.Request(next_url, callback=self.parse_info)
		if page > 0:
			yield scrapy.Request('http://www.usst.edu.cn/s/1/t/517/p/8/i/' + str(page) + '/list.htm',
								 meta={'page': page}, callback=self.parse8)
		else:
			page=page+1
			yield scrapy.Request('http://jwc.usst.edu.cn/s/9/t/451/p/11/i/1/list.htm', meta={'page': page},
								 callback=self.parse_jwc)

	'''对校园主页上各分栏中所有通知具体信息的爬去'''
	def parse_info(self,response):
		item=JwcItem()
		item['url']=response.url
		item['title']=''
		titles=response.xpath('//td[@class="mc_title"]/span/text()').extract()
		for t in titles:
			item['title']=item['title']+t
		body=response.xpath('//td[@class="content"]').extract()
		item['body']=''
		for b in body:
			item['body']=item['body']+b
		item['releasetime']=''
		releasetime=response.xpath('//td[@class="mc_time"]//td/text()').re(r'\d{4}-\d{2}-\d{2}')
		if(len(releasetime)!=0):
			item['releasetime']=releasetime[0]
		yield item

	'''爬取教务处的所有通知公告'''
	def parse_jwc(self,response):
		page=response.meta['page']
		page=page+1
		infos = response.xpath('//a[re:test(@href,"^(http:\/\/\w{2,5}\.usst\.edu\.cn)?\/s\/\d{1,2}\/t\/\d{3}\/\w{2}\/\w{2}\/info\d{5}\.htm")]')
		for info in infos:
			urls = info.xpath('..//a/@href').extract()
			if len(urls) != 0:
				url = urls[0]
				if url[0:4] == 'http':
					next_url = url
				else:
					next_url = "http://jwc.usst.edu.cn" + url
				yield scrapy.Request(next_url, callback=self.parse_info_jwc)
		if page <=104:
			yield scrapy.Request('http://jwc.usst.edu.cn/s/9/t/451/p/11/i/' + str(page) + '/list.htm',
								 meta={'page': page}, callback=self.parse_jwc)

	'''对教务处中所有通知具体信息的爬去'''
	def parse_info_jwc(self,response):
		item=JwcItem()
		item['url']=response.url
		item['title']=''
		item['body']=''
		titles=response.xpath('//td[@class="title_shadow"]/div/font/text()').extract()
		for t in titles:
			item['title']=item['title']+t
		body=response.xpath('//td[@class="content"]//text()').extract()  #由于教务处的数据过于庞大（过多的table)，所以现在只是将text文本存储，不存网站源码
		for b in body:
			item['body']=item['body']+b
		item['releasetime'] = ''
		releasetime = response.xpath('//td[@class="mc_time"]//td/text()').re(r'\d{4}-\d{2}-\d{2}')
		if (len(releasetime) != 0):
			item['releasetime'] = releasetime[0]
		yield item
