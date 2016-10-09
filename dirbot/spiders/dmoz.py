from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.items import Movie
from dirbot.items import Pics
import scrapy
import urllib2 
import time

class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["riaoao3.com"]
    start_urls = [
        "http://riaoao3.com/vodlisthtml/5.html",
	"http://riaoao3.com/vodlisthtml/5-2.html",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
	#print response.body
        sel = Selector(response)
        divs = sel.xpath('//div[@id="k_list-lb-2-a"]')
	for a in divs.xpath(".//a/@href"):
		print a.extract()
        #items = []
	#print "start to spider"
	#print sites
        '''for site in sites:
            item = Website()
            item['name'] = site.xpath('a/text()').extract()
            item['url'] = site.xpath('a/@href').extract()
            item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
            items.append(item)'''
	#print "start to get!"
	#print items
        return items
class ToPaSpider(Spider):
    name = "topa"
    allowed_domains = ["riaoao3.com"]
    '''
    start_urls = [
        "http://riaoao3.com/vodlisthtml/5.html",
	#"http://riaoao3.com/vodlisthtml/6.html",
	#"http://riaoao3.com/vodlisthtml/7.html",
	#"http://riaoao3.com/vodlisthtml/17.html",
    ]
    '''
    kinddict = {"5":67,"6":21,"7":42,"8":15,"9":32,"10":8,"11":12,"17":12}
    start_urls = []
    
    for i in kinddict:
    	for j in range(kinddict[i],0,-1):# include 2 no 0
		if j ==1:
			start_urls.append("http://" + allowed_domains[0] + "/vodlisthtml/" + i + ".html")
		else:
			start_urls.append("http://" + allowed_domains[0] + "/vodlisthtml/" + i + "-" + str(j) + ".html")	
    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        divs = sel.xpath('//div[@id="k_list-lb-2-a"]')
        for a in divs.xpath(".//a/@href").extract():
		#print "*******************" +str(a)	
                yield scrapy.Request("http://"+self.allowed_domains[0]+str(a), callback=self.parse_item)
        #return items
    def parse_item(self, response):
	kind = 0
	xfhref = ""
	flagbofangname = ""
	flagbofangxf1= ""
	flagbofangxf2 = ""
	flagbofang4 = ""
	flagbofang5 = ""
	sel = Selector(response)
	cat_dict = {u"\u4e9a\u6d32\u7cfb\u5217":5,u"\u5077\u62cd\u81ea\u62cd":6,u"\u5236\u670d\u4e1d\u889c":7,u"\u4e71\u4f26\u8650\u5f85":8,u"\u6b27\u7f8e\u7cfb\u5217":9,u"\u52a8\u6f2b\u7cfb\u5217":10,u"\u719f\u5973\u4eba\u59bb":11,u"\u7ecf\u5178\u4e09\u7ea7":17}
	pathlead = sel.xpath('//div[@class = "k_lujing"]/.//li[@class = "k_lujing-3"]/text()').extract()
	for ddd in cat_dict:
		if ddd in pathlead[0]:
			kind =  cat_dict[ddd]
			break
	
	divs = sel.xpath('//div[@id="k_jianjie-3a"]')
	#print len(divs)	
	for i,cell in enumerate(divs[0].xpath('.//div[@class="k_jianjie-3a-5"]/.//a/@href').extract()):
                if i == 0:
                        xfhref = cell
                        break
	for i,cell in enumerate(divs[0].xpath('.//div[@class="k_jianjie-3a-4"]').extract()):
		if i == 0:
			flagbofangxf1 = cell
		if i == 1:
			flagbofang4 = cell
			break
	for i,cell in enumerate(divs[0].xpath('.//div[@class="k_jianjie-3a-5"]').extract()):
		if i == 0:
			flagbofangxf2 = cell
                if i == 1:
                        flagbofang5 = cell 
                        break
	#print flagbofang5
	#print flagbofang4
	div_re = divs[0].extract().replace(flagbofang5,"")
	div_re = div_re.replace(flagbofang4,"")
        div_re = div_re.replace(flagbofangxf1,"")
	div_re = div_re.replace(flagbofangxf2,"")
	for cell in divs[0].xpath('.//div[@class="k_jianjie-3a-1"]/ul/li/text()').extract():
		if len(cell)!=0:
			flagbofangname = cell
			break
		#div_re = div_re.replace(cell,"")
	for cell in divs[0].xpath('.//div[@class="k_jianjie-3a-1"]').extract():
               div_re = div_re.replace(cell,"")
	for cell in divs[0].xpath('.//div[@class="k_jianjie-3a-2"]').extract():
               div_re = div_re.replace(cell,"")
	for cell in divs[0].xpath('.//div[@class="k_jianjie-3a-3"]').extract():
               div_re = div_re.replace(cell,"")

	for cell in divs[0].xpath('.//div[@class="ad-c2"]').extract():
                div_re = div_re.replace(cell,"")
	#modify the img
	sels = sel.xpath('//div[@class="content"]')
        #print len(divs)        
        for cell in sels[0].xpath('.//img').extract():
		div_re = div_re.replace(cell,'<div class="k_s">' + cell + '</div><div class="slice"></div>')
	sels1 = sel.xpath('//div[@id="k_jianjie-2b"]/.//img/@src').extract()
	#print sels1[0]
	

	#end
	div_re = div_re.replace("\r\n","")
	#print "now"
	#print xfhref
	item = Movie()
	cc =  response.url.split("/")
	id_url = cc[-1].replace(".html","")
	item["zone"] = 1
	item["url_id"]= int(id_url)
        item["create_time"] = int(time.time())
        item["kind"] = kind
	item['title'] = flagbofangname
	item['divcontent'] = div_re
	item['topimg'] = sels1[0]
	yield scrapy.Request("http://"+self.allowed_domains[0]+str(xfhref),meta={'item':item}, callback=self.getXflink)
	#print div_re 	
	#print "get divs"
	#print flagbofangname
	#print divs[0]
    def getXflink(self,response):
	items = []
	item = response.meta['item']
	sel = Selector(response)
        divs = sel.xpath('//div[@id="k_play-3a-2"]')
	#print "state"
	#print divs[0].extract()
	jscell =  divs[0].xpath('.//script/@src').extract()
	request = urllib2.Request("http://"+self.allowed_domains[0]+str(jscell[0]))
	request.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6') 
	response = urllib2.urlopen(request)
	html = response.read() 
	cells =  html.split("$$") 
	for cell  in cells:
		if "xfplay://" in cell:
			item['xflink'] = cell
	#print item
	items.append(item)
	yield item
		
	#print html  
	#for i,cell in enumerate(divs[0].xpath('.//div[@class="k_jianjie-3a-5"]/.//a/@href').extract()):
		#print cell


class PicSpider(Spider):
    name = "pic"
    allowed_domains = ["riaoao3.com"]
    '''
    start_urls = [
        "http://riaoao3.com/artlisthtml/22.html",
	#"http://riaoao3.com/vodlisthtml/6.html",
	#"http://riaoao3.com/vodlisthtml/7.html",
	#"http://riaoao3.com/vodlisthtml/17.html",
    ]
    '''
    kinddict = {"15":106,"16":105,"17":103,"18":100,"19":100,"20":14,"21":96,"22":102}
    start_urls = []
    for i in kinddict:
    	for j in range(kinddict[i],0,-1):# include 2 no 0
		if j ==1:
			start_urls.append("http://" + allowed_domains[0] + "/artlisthtml/" + i + ".html")
		else:
			start_urls.append("http://" + allowed_domains[0] + "/artlisthtml/" + i + "-" + str(j) + ".html")
    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        #print response.body
	#items = []
	#item = Movie()
	'''for m in self.start_urls:
		print m
	'''
        sel = Selector(response)
        divs = sel.xpath('//div[@class="k_list-txt"]')
        for a in divs.xpath(".//a/@href").extract():
		#print "*******************" +str(a)	
                yield scrapy.Request("http://"+self.allowed_domains[0]+str(a), callback=self.parse_item)
    def parse_item(self, response):
	items = []
	kind = 0
	flagpicname = ""
	sel = Selector(response)
	cat_dict = {u"\u5077\u62cd\u81ea\u62cd":15,u"\u6b27\u7f8e\u8272\u56fe":16,u"\u4e9a\u6d32\u8272\u56fe":17,u"\u7f8e\u817f\u4e1d\u889c":18,u"\u52a8\u6f2b\u56fe\u7247":19,u"\u6e05\u7eaf\u552f\u7f8e":20,u"\u4e9a\u6d32\u8bf1\u60d1":21,u"\u6b27\u7f8e\u8bf1\u60d1":22}
	pathlead = sel.xpath('//div[@class = "k_lujing"]/.//li[@class = "k_lujing-2"]/text()').extract()
	for ddd in cat_dict:
		if ddd in pathlead[0]:
			kind =  cat_dict[ddd]
			#print kind
			break
	pathlead2 = sel.xpath('//div[@class = "k_lujing"]/.//li[@class = "k_lujing-3"]/text()').extract()
	flagpicname = pathlead2[0]
	divs = sel.xpath('//div[@class="content-img"]').extract()
	div_re = divs[0]
	#modify the img
        sels = sel.xpath('//div[@class="content-img"]')
        #print len(divs)        
        for cell in sels[0].xpath('.//img').extract():
                div_re = div_re.replace(cell,'<div class="k_s">' + cell + '</div><div class="slice"></div>')

	item = Pics()
	item["zone"] = 2
        cc =  response.url.split("/")
        id_url = cc[-1].replace(".html","")
        item["url_id"]= int(id_url)
        item["create_time"] = int(time.time())
        item["kind"] = kind
        item['title'] = flagpicname
        item['divcontent'] = div_re
	yield item	

class TxtSpider(Spider):
    name = "txt"
    allowed_domains = ["riaoao3.com"]
    '''
    start_urls = [
        "http://riaoao3.com/artlisthtml/7.html",
	#"http://riaoao3.com/vodlisthtml/6.html",
	#"http://riaoao3.com/vodlisthtml/7.html",
	"http://riaoao3.com/vodlisthtml/17.html",
    ]
    '''
    kinddict = {"7":46,"8":43,"9":39,"10":49,"11":51,"12":49,"13":50,"14":52}
    start_urls = []
    for i in kinddict:
    	for j in range(kinddict[i],0,-1):# include 2 no 0
		if j ==1:
			start_urls.append("http://" + allowed_domains[0] + "/artlisthtml/" + i + ".html")
		else:
			start_urls.append("http://" + allowed_domains[0] + "/artlisthtml/" + i + "-" + str(j) + ".html")
    #start_urls = start_urls.reverse()
    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        divs = sel.xpath('//div[@class="k_list-txt"]')
        for a in divs.xpath(".//a/@href").extract():	
                yield scrapy.Request("http://"+self.allowed_domains[0]+str(a), callback=self.parse_item)
        #items = []
        #print "start to spider"
        #print sites
        '''for site in sites:
            item = Website()
            item['name'] = site.xpath('a/text()').extract()
            item['url'] = site.xpath('a/@href').extract()
            item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
            items.append(item)'''
        #print "start to get!"
        #print items
        #return items
    def parse_item(self, response):
	items = []
	kind = 0
	flagpicname = ""
	sel = Selector(response)
	cat_dict = {u"\u6821\u56ed\u6625\u8272":7,u"\u53e4\u5178\u6b66\u4fa0":8,u"\u53e6\u7c7b\u5c0f\u8bf4":9,u"\u60c5\u8272\u7b11\u8bdd":10,u"\u90fd\u5e02\u8a00\u60c5":11,u"\u4eba\u59bb\u4ea4\u6362":12,u"\u5bb6\u5ead\u4e71\u4f26":13,u"\u6027\u7231\u6280\u5de7":14}
	pathlead = sel.xpath('//div[@class = "k_lujing"]/.//li[@class = "k_lujing-2"]/text()').extract()
	for ddd in cat_dict:
		if ddd in pathlead[0]:
			kind =  cat_dict[ddd]
			#print kind
			break
	pathlead2 = sel.xpath('//div[@class = "k_lujing"]/.//li[@class = "k_lujing-3"]/text()').extract()
	flagpicname = pathlead2[0]
	divs = sel.xpath('//div[@class="content-txt"]').extract()
	item = Pics()
	item["zone"] = 3
        cc =  response.url.split("/")
        id_url = cc[-1].replace(".html","")
        item["url_id"]= int(id_url)
        item["create_time"] = int(time.time())
        item["kind"] = kind
        item['title'] = flagpicname
        item['divcontent'] = divs[0]
	yield item
