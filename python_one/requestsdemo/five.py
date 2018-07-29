import requests

headers = {
'Cookie': '_zap=d199b4c3-21c4-4508-ba0e-3e60f13aa5e6; d_c0="AIAncSSA9A2PToCZpnWGfkqx-ElA51pYOe0=|1532526453"; '
          'q_c1=8795257b04b149e18d61da562636453a|1532526453000|1532526453000; '
          'capsion_ticket="2|1:0|10:1532526465|14:capsion_ticket|44:NmJlYzYxMzM5YzFkNDg3YmI5ZjgyYzI3OWY0ZDcyYjY=|62fcffb45544c52819014418bf1be402fb44a49e319c512098639c9b02aa150f";'
          ' z_c0="2|1:0|10:1532526467|4:z_c0|92:Mi4xa0ZUbEFRQUFBQUFBZ0NkeEpJRDBEU1lBQUFCZ0FsVk5nODFGWEFDLW91dUJ3eFlJMVpyY21kNlRHcWZOZHFfVkJR|edcefce985cf2de915a63b7d48474f0bb18ad218cc6b25ff10e41fd2f8f3e667";'
          ' _xsrf=e0cd1078fe14c7d33af4e92cc9a3276d; __utma=51854390.1061122485.1532860553.1532860553.1532860553.1; __utmb=51854390.0.10.1532860553; '
          '__utmc=51854390; __utmz=51854390.1532860553.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100--|2=registration_date=20150723=1^3=entry_date=20150723=1',
'Host': 'www.zhihu.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
}


r = requests.get('https://www.zhihu.com',headers=headers)
print(r.text)