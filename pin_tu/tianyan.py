import requests
import random
from lxml import etree
import pandas as pd
import json
import re
import time
from selenium import webdriver
import base64
from PIL import Image
from test_damatu_jiekou import *
from selenium.webdriver.common.action_chains import ActionChains

USER_AGENT_LIST = ["Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0) ",
                   "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; DigExt) ",
                   "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; TUCOWS) ",
                   "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; .NET CLR 1.1.4322) ",
                   "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 ) ",
                   "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0) ",
                   "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; by TSG) ",
                   "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.0.3705) ",
                   "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322) ",
                   "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.0 ",
                   "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) ",
                   "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0;) ",
                   "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; T312461) "
                  ]


class TianYan(object):
    def __init__(self):
        self.start_url = 'https://shenyang.tianyancha.com/search/p{}'
        cookies_y = 'aliyungf_tc=AQAAAP7P5hLfFwkA0zBBcJ9bksXxe1jg; csrfToken=lVnt7gyOaKlBUVmvfs8vBK4T; TYCID=e04fe9b0e26411e78e42abd79a6c613a; undefined=e04fe9b0e26411e78e42abd79a6c613a; ssuid=7577342018; tyc-user-info=%257B%2522isExpired%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzAxMzA0ODc5MCIsImlhdCI6MTUxMzQzMDYxOSwiZXhwIjoxNTI4OTgyNjE5fQ.01kQuihg8P85nH86e2haeAa0grVuZaz9HInfRdOsSGT594rIM8qMUZrIFwYJPFS8XGh0swZSOp6p9NShjqTrQw%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25223%2522%252C%2522surday%2522%253A%2522221%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25222%2522%252C%2522onum%2522%253A%2522631%2522%252C%2522mobile%2522%253A%252213013048790%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzAxMzA0ODc5MCIsImlhdCI6MTUxMzQzMDYxOSwiZXhwIjoxNTI4OTgyNjE5fQ.01kQuihg8P85nH86e2haeAa0grVuZaz9HInfRdOsSGT594rIM8qMUZrIFwYJPFS8XGh0swZSOp6p9NShjqTrQw; _csrf=4qA416YRvJpzjcfNA/eLqg==; OA=l5Mz4M2V+pEMkkiTDmdfWvZSYHrCJ8yQmO22Cbwfv4A=; _csrf_bk=93b8aa5513d75ddd715c1f55c19d5667; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1513430857; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1513430865'
        self.cookies = {}
        c_list = cookies_y.split('; ')
        for c in c_list:
            c_lis = c.split('=')
            key = c_lis[0]
            value = c_lis[1]
            self.cookies[key] = value
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36',
        }
        self.list_data = []
        self.file = open('qiye.json', 'a+')
        self.pn = 6

    def get_data(self, url):
        response = requests.get(url, cookies=self.cookies, headers=self.headers)
        print(response.url, '-----------')
        # 判断是否是要点击验证码了
        if re.search(r'https://antirobot\.tianyancha\.com/captcha/verify\?', response.url):
            driver = webdriver.Chrome()
            driver.get('https://www.tianyancha.com/')
            time.sleep(3)
            driver.delete_all_cookies()
            # 获取 本地cookies selenium模拟登陆
            with open('cookies.json', 'r', encoding='utf-8') as f:
                list_cookies = json.loads(f.read())
            print(list_cookies)
            #{'domain': '.tianyancha.com', 'path': '/', 'name': 'undefined', 'secure': False, 'httpOnly': True,
            # 'value': 'e04fe9b0e26411e78e42abd79a6c613a', 'expiry': 1576502854.687774}
            for cookie in list_cookies:
                driver.add_cookie({
                    'domain': cookie['domain'],  # 此处xxx.com前，需要带点
                    'name': cookie['name'],
                    'value': cookie['value'],
                    'path': cookie['path'],
                    'secure': cookie['secure'],
                    'httpOnly': cookie['httpOnly'],
                    'expires': None,
                })

            driver.get('https://www.tianyancha.com/')
            driver.maximize_window()
            # 处于登陆状态以后
            driver.get(response.url)
            time.sleep(3)
            el_img1 = driver.find_element_by_xpath('//img[@id="targetImgie"]')
            el_img2 = driver.find_element_by_xpath('//img[@id="bgImgie"]')
            el_sub = driver.find_element_by_xpath('//div[@id="submitie"]')
            src1 = el_img1.get_attribute('src')
            src2 = el_img2.get_attribute('src')
            print(src1)
            print(src2)
            src1_data = src1.split(',')[1]
            src2_data = src2.split(',')[1]
            src1_bytes = base64.b64decode(src1_data)
            src2_bytes = base64.b64decode(src2_data)
            # 下载验证码上部分图片
            with open('img_up.png', 'wb') as f:
                f.write(src1_bytes)
            # 下载验证码下部分图片
            with open('img_down.png', 'wb') as f:
                f.write(src2_bytes)
            time.sleep(1)
            # 拼接上下两张图片
            im = Image.open('img_up.png')

            im2 = Image.open('img_down.png')

            im3 = Image.open('tips.png')

            width, height = im.size

            width2, height2 = im2.size

            width3, height3 = im3.size

            result = Image.new(im2.mode, (width, height+height2+height3), '#fff')

            result.paste(im2, box=(0, 0))

            result.paste(im3, box=(0, height2))

            result.paste(im, box=(0, height2+height3))

            result.save('result.png')
            time.sleep(1)
            # 连接打码兔平台，返回要点击的坐标
            # 1\创建连接实例
            # dmt = DamatuApi("bluceG", "a097111")
            # 2\查看是否还有余额
            money = dmt.getBalance()
            print(money)
            # # 如果有钱，进行打码
            if int(money) > 100:

                while True:
                    score = dmt.decode('result.png', 308)
                    print(score, '---------')
                    id = str(score[1])
                    # 检测返回是否异常，异常上报异常
                    try:
                        target = score[0]
                        tar_list = target.split('|')
                        new_tar_list = []
                        for tar in tar_list:
                            tar = tar.split(',')
                            new_tar_list.append(tar)
                        # print(new_tar_list)
                        # 模拟顺序点击
                        time.sleep(1)
                        actions = ActionChains(driver)
                        for i in range(len(new_tar_list)):
                            actions.move_to_element_with_offset(el_img2, new_tar_list[i][0], new_tar_list[i][1])
                            actions.click()
                            actions.perform()
                            time.sleep(3)
                        actions.move_to_element(el_sub)
                        actions.click()
                        actions.perform()

                        time.sleep(3)
                        if re.search(r'https://antirobot\.tianyancha\.com/captcha/verify\?', driver.current_url):
                            raise Exception


                    except:
                        # 上报异常
                        dmt.reportError(id)
                        print('验证码错误')
                        time.sleep(20000)
                    else:
                        response = requests.get(driver.current_url, cookies=self.cookies, headers=self.headers)
                        time.sleep(1)
                        driver.close()
                        return response.content.decode()

            # print('stop------------------------')
            # time.sleep(20000)

        # if url == 'https://shenyang.tianyancha.com/search/p2':
        #     print('test1111----1111')
        # print('stop----------')
        # time.sleep(3000)

        return response.content.decode()

    def parse_url_list(self, data):
        self.pn += 1
        next_url = 'https://shenyang.tianyancha.com/search/p{}'.format(self.pn)
        html = etree.HTML(data)
        reg_money_list = html.xpath('//div[@class="search_row_new pt20"]/div[1]/div[2]/span/@title')
        reg_date_list = html.xpath('//div[@class="search_row_new pt20"]/div[1]/div[3]/span/text()')
        url_list = html.xpath('//div[@class="search_right_item"]/div/a/@href')
        return url_list, next_url, reg_money_list, reg_date_list

    def parse_detail_page(self, data, reg_money_list, reg_date_list):
        html = etree.HTML(data)
        dict_data = {}
        dict_data['name'] = html.xpath('//span[@class="f18 in-block vertival-middle sec-c2"]/text()')[0] if html.xpath('//span[@class="f18 in-block vertival-middle sec-c2"]/text()') else '-'
        dict_data['addr'] = html.xpath('//span[@class="in-block overflow-width vertical-top pr10"]/text()')[0] if html.xpath('//span[@class="in-block overflow-width vertical-top pr10"]/text()') else '-'
        dict_data['legal_person'] = html.xpath('//div[@class="f18 overflow-width sec-c3"]/a/text()')[0] if html.xpath('//div[@class="f18 overflow-width sec-c3"]/a/text()') else '-'
        dict_data['reg_money_list'] = reg_money_list
        dict_data['reg_date_list'] = reg_date_list
        return dict_data

    def run(self):
        next_url = self.start_url.format(self.pn)
        while True:
            if next_url:
                # 发送起始url
                data = self.get_data(next_url)
                # print(data)
                # 解析列表页
                url_list, next_url, reg_money_list, reg_date_list = self.parse_url_list(data)
                # 循环解析详情页
                for i, url in enumerate(url_list):
                    data2 = self.get_data(url)
                    dict_data = self.parse_detail_page(data2, reg_money_list[i], reg_date_list[i])
                    self.list_data.append(dict_data)
                    self.file.write(json.dumps(dict_data, ensure_ascii=False) + ',\n')
                print(self.list_data)

    def __del__(self):
        self.file.close()


if __name__ == '__main__':
    tianyan = TianYan()
    tianyan.run()