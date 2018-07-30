import requests
from lxml import etree
import csv
import datetime

class Work(object):
    #地区
    area = ''
    #薪资
    salary = ''
    #公司名称
    companyName = ''
    #公司信息
    companyDetail = ''
    #链接
    companyHref = ''
    #公司要求
    companyRequirement = ''
    #本科数量
    undergraduate = 0
    #发布时间
    releaseTime = ''

    def fakerBrowser(self):
        # 模拟浏览器请求
        headers = {
            'authority': 'www.zhipin.com',
            'method': 'GET',
            'path': '/c101010100-p100101/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': "zh-CN,zh;q=0.9",
            'cache-control': 'max-age=0',
            'cookie': 'sid=sem_pz_bdpc_dasou_title; lastCity=101010100; JSESSIONID=""; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1532866950; __g=sem_pz_bdpc_dasou_title; toUrl=https%3A%2F%2Fwww.zhipin.com%2Fc101010100-p100101%2F; __c=1532866953; __l=r=https%3A%2F%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&l=%2Fwww.zhipin.com%2Fc101010100-p100101%2F&g=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_ti; t=GPBUHQg2RhcUKXps; wt=GPBUHQg2RhcUKXps; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1532867068; __a=42616347.1532870679.1532870679.1532866953.9.2.8.9',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
        }
        return headers



    def parse_one_page(self,text):
        html = etree.HTML(text, etree.HTMLParser())
        work = html.xpath('//a/div[@class="job-title"]/text()')
        # 薪水
        salary = html.xpath('//a/span[@class="red"]/text()')
        # 公司名称
        name = html.xpath('//div[@class="company-text"]//h3[@class="name"]/a/text()')
        # 详细信息
        jobDetail = html.xpath('//div[@class="company-text"]//p')
        # 公司链接
        href = html.xpath('//div[@class="info-primary"]//h3[@class="name"]/a/@href')
        # 要求
        requirement = html.xpath('//div[@class="info-primary"]//p')
        #发布时间
        releaseTime=html.xpath('//div[@class="info-publis"]//p//text()')
        return work,salary,name,jobDetail,href,requirement,releaseTime


    def getData(self,pageNum):
        undergraduateNum = 0
        workList = list()
        findWork = Work()
        # 获得requestheaders
        headers = findWork.fakerBrowser()
        # 循环三次 1次30条 一次请求90条数据
        # #boss直聘默认每页显示30个岗位
        num = 30
        r = requests.get('https://www.zhipin.com/c101010100-p100101/?page='+str(pageNum)+'&ka=page-'+str(pageNum)+'', headers=headers)
        prefix = 'https://www.zhipin.com'
        area, salary, companyName, companyDetails, companyHrefs,companyRequirements,releaseTimes = findWork.parse_one_page(r.text)
        for n in range(num):
            companyHref = prefix + companyHrefs[n]
            companyDetail = companyDetails[n].xpath('string(.)').strip()
            companyRequirement = companyRequirements[n].xpath('string(.)').strip()
            print(area[n] + "\t", salary[n] + "\t", companyName[n] + "\t", companyHref + "\t", companyDetail + "\t",companyRequirement+"\t",releaseTimes[n]+"\t")
            workEntity = Work()
            workEntity.area = area[n]
            workEntity.salary = salary[n]
            workEntity.companyName = companyName[n]
            workEntity.companyDetail = companyDetail
            workEntity.companyHref = companyHref
            workEntity.companyRequirement = companyRequirement
            workEntity.releaseTime = releaseTimes[n]
            workList.append(workEntity)

        findWork.setCsv(workList,pageNum)


    #将90条数据存进csv文件
    def setCsv(self,list,pageNum):
            dataName = "data"+str(pageNum);
            with open(dataName+".csv", 'w') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['岗位', '薪水', '公司名称', '详细信息', '公司链接','公司要求','发布时间'])
                for work in list:
                    writer.writerow([work.area, work.salary, work.companyName, work.companyDetail, work.companyHref,work.companyRequirement,work.releaseTime])


    def findUndergraduate(self,companyRequirement):
        if companyRequirement.find("本科")>=0:
            return True


num = 1;
while (num):
    work = Work()
    work.getData(num)
    num = num + 1
    if num > 3:
        break





