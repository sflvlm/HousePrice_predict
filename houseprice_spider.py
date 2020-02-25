import re
import requests
from lxml import html
import csv
import time
etree = html.etree



f=open('C:\\Users\sunfang\Desktop\houseprice_predict\data\sh_price.csv','wt',newline='',encoding='utf-8')
writer=csv.writer(f)
writer.writerow(('name','loc','size','area','price','price_sum','dire','floor','buildtime','advantage'))
headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "cookie" : "global_cookie=kley71ky44h4njodu8n9jyavn1wk6uox2tu; fang_hao123_layed=1; city=sh; __utma=147393320.959764305.1582199999.1582199999.1582199999.1; __utmc=147393320; __utmz=147393320.1582199999.1.1.utmcsr=sh.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/; g_sourcepage=esf_fy%5Elb_pc; __utmb=147393320.6.10.1582199999; Integrateactivity=notincludemc; unique_cookie=U_kley71ky44h4njodu8n9jyavn1wk6uox2tu*4; csrfToken=0I3DbFOTdGunNy_i_gOIODcG",
        "referer": "https://sz.esf.fang.com/",
        "sec - fetch - mode": "navigate",
        "sec - fetch - site" : "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests" : "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
    }
city_list=[]

def get_info(city_url):
    # requests.packages.urllib3.disable_warnings()
    response=requests.get(city_url,headers=headers,timeout=None,verify=False)
    selector=etree.HTML(response.text)
    infos = selector.xpath('//dl[@dataflag="bg"]')
    try:
        for info in infos:
            name = info.xpath('dd/p[2]/a/@title')
            name = name[0] if len(name) != 0 else ' '
            loc = info.xpath('dd/p[2]/span/text()')[0]
            size = info.xpath('dd/p/text()[1]')[0].strip()
            area = info.xpath('dd/p/text()[2]')[0].strip()[:-2]
            dire = info.xpath('dd/p/text()[4]')[0].strip()
            floor = info.xpath('dd/p/text()[3]')[0].strip()
            buildtime = info.xpath('dd/p/text()[5]')
            buildtime = buildtime[0].strip() if len(buildtime) != 0 else '未知'
            price = info.xpath('dd[2]/span[2]/text()')[0].strip()[:-4]
            pricesum = info.xpath('dd[2]/span/b/text()')[0].strip()
            advantage = info.xpath('dd/p[3]')
            advantage = advantage[0].xpath('string(.)').strip()#获取连续多个标签的文本
            advantage = advantage if len(advantage) != 0 else '无'
            print(name,loc,size,area,dire,floor,buildtime,price,pricesum,advantage)
            writer.writerow((name, loc, size, area, price, pricesum, dire, floor, buildtime, advantage))
    except IndexError:
        pass

if __name__=='__main__':
    url = 'https://sh.esf.fang.com'
    try:
        response = requests.get(url,headers=headers,timeout=None)
        page = re.findall('<p>共(.*?)页</p>', response.text)[0]
        city_urls = [url +'/house/i3' + str(i) + '/' for i in range(1, int(page) + 1)]
        for city_url in city_urls:
            city_list.append(city_url)

    except IndexError:
        pass


    for city_ in city_list:
        try:
            get_info(city_)
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            time.sleep(5)
            print("now let me continue...")
            continue

f.close()