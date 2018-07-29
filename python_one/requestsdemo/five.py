import requests
import re
from lxml import etree
headers = {
'authority': 'www.zhipin.com',
'method': 'GET',
'path': '/c101010100-p100101/',
'scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language':"zh-CN,zh;q=0.9",
'cache-control':'max-age=0',
'cookie': 'sid=sem_pz_bdpc_dasou_title; lastCity=101010100; JSESSIONID=""; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1532866950; __g=sem_pz_bdpc_dasou_title; toUrl=https%3A%2F%2Fwww.zhipin.com%2Fc101010100-p100101%2F; __c=1532866953; __l=r=https%3A%2F%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&l=%2Fwww.zhipin.com%2Fc101010100-p100101%2F&g=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_ti; t=GPBUHQg2RhcUKXps; wt=GPBUHQg2RhcUKXps; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1532867068; __a=42616347.1532870679.1532870679.1532866953.9.2.8.9',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
}





def parse_one_page(text):
    html = etree.HTML(text, etree.HTMLParser())
    #//h3/a
    #result = html.xpath('//li[@class="item-0"]/a/text()')
    result = html.xpath('//a/div[@class="job-title"]/text()')
    result2 = html.xpath('//a/span[@class="red"]/text()')
    result3 = html.xpath('//div[@class="company-text"]//h3[@class="name"]/a/text()')
    result4 = html.xpath('//div[@class="company-text"]//p/text()')
    # print('result', result)
    # print('result[0]', result[0])
    # print('result2', result2)
    return result,result2,result3,result4
    #print('result2[0]', result2[0])

r = requests.get('https://www.zhipin.com/job_detail/?query=&scity=101010100&industry=&position=100101',headers=headers)
#print(r.text)
gangwei,money,name,content =parse_one_page(r.text)
for n in range(30):
    print(gangwei[n],money[n],name[n])
#print(len(money))


