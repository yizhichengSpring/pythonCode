import requests
from lxml import etree


#模拟浏览器请求
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
    result = html.xpath('//a/div[@class="job-title"]/text()')
    #薪水
    salary = html.xpath('//a/span[@class="red"]/text()')
    #公司名称
    name = html.xpath('//div[@class="company-text"]//h3[@class="name"]/a/text()')
    #详细信息
    jobDetail = html.xpath('//div[@class="company-text"]//p')
    #公司链接
    href = html.xpath('//div[@class="info-primary"]//h3[@class="name"]/a/@href')
    return result,salary,name,jobDetail,href


r = requests.get('https://www.zhipin.com/job_detail/?query=&scity=101010100&industry=&position=100101',headers=headers)
prefix = 'https://www.zhipin.com'
gangwei,money,name,content,href = parse_one_page(r.text)
for n in range(30):
     jobdetail = prefix+href[n]
     detailWork = content[n].xpath('string(.)').strip()
     print(gangwei[n],money[n],name[n],jobdetail,detailWork)


