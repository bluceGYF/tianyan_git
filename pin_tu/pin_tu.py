# from os import listdir
# from PIL import Image
#
#
# im = Image.open('下载.png')
#
# im2 = Image.open('的富豪捐款.png')
#
# im3 = Image.open('tips.png')
#
# width, height = im.size
#
# width2, height2 = im2.size
#
# width3, height3 = im3.size
#
# print(width, height)
#
# result = Image.new(im2.mode, (width, height+height2+height3), '#fff')
#
# result.paste(im2, box=(0, 0))
#
# result.paste(im3, box=(0, height2))
#
# result.paste(im, box=(0, height2+height3))
#
# result.save('result.png')

# score = ('144,53|295,50', 775773990)
# target = score[0]
# id = score[1]
# tar_list = target.split('|')
# new_tar_list = []
# for tar in tar_list:
#     tar = tar.split(',')
#     new_tar_list.append(tar)
# print(new_tar_list)
# import time
#
#
# def test1():
#     for i in range(10000):
#         time.sleep(1)
#     return 2
#
#
# def test2(a):
#     print(a, '1-------')
#
#
# while True:
#     t = test1()
#     test2(t)
#     time.sleep(3)
from selenium import webdriver
import time
import json


# cookies_y = 'TYCID=c81836b0de6611e7959b9f7e5158aacc; undefined=c81836b0de6611e7959b9f7e5158aacc; ssuid=760532176; aliyungf_tc=AQAAAOHUSG8IOAYA0zBBcKdJgjx330fI; csrfToken=PykbCyYKZtpY9oGgtDxOozaV; jsid=SEM-BAIDU-PZPC-000000; tyc-user-info=%257B%2522isExpired%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzAxMzA0ODc5MCIsImlhdCI6MTUxMzQyNTcwNSwiZXhwIjoxNTI4OTc3NzA1fQ.9WnewxpJPPgrz5T3F5T8ba35w6aVs6vYUUKJTvijzGecDILRXPi3BvHYkO8sG3oAwg_G5sWRKKtNmVYDrf7Oyg%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25223%2522%252C%2522surday%2522%253A%2522221%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25222%2522%252C%2522onum%2522%253A%2522631%2522%252C%2522mobile%2522%253A%252213013048790%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzAxMzA0ODc5MCIsImlhdCI6MTUxMzQyNTcwNSwiZXhwIjoxNTI4OTc3NzA1fQ.9WnewxpJPPgrz5T3F5T8ba35w6aVs6vYUUKJTvijzGecDILRXPi3BvHYkO8sG3oAwg_G5sWRKKtNmVYDrf7Oyg; bannerFlag=true; RTYCID=6a62fb894b014200bfea1cdfcfc6dfae; _csrf=iVjn4tL81b6PvX0H15YL+w==; OA=w51spWm8LuMdfpX4ZX0UW0GtLHAAi7pW2/G8BN+ZcfM=; _csrf_bk=4114c716d385875e4e6658585eb11d32; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1512991951,1512993044,1512993052,1513425618; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1513428542'
# cookies = {}
# c_list = cookies_y.split('; ')
# for c in c_list:
#     c_lis = c.split('=')
#     key = c_lis[0]
#     value = c_lis[1]
#     cookies[key] = value
#
driver = webdriver.Chrome()
# driver.get('https://www.tianyancha.com/login')
# driver.implicitly_wait(10)
# user_el = driver.find_element_by_xpath('//*[@id="web-content"]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/input')
# time.sleep(1)
# user_el.send_keys('13013048790')
# pas_el = driver.find_element_by_xpath('//*[@id="web-content"]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[3]/input')
# time.sleep(1)
# pas_el.send_keys('meed6488')
# sub_el = driver.find_element_by_xpath('//*[@id="web-content"]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[5]')
# time.sleep(1)
# sub_el.click()
# time.sleep(3)
# dictCookies = driver.get_cookies()
# jsonCookies = json.dumps(dictCookies)
#
# with open('cookies.json', 'w') as f:
#     f.write(jsonCookies)

# driver.delete_all_cookies()
# driver.add_cookie(cookies)
# driver.get('https://www.tianyancha.com/')
driver.get('https://www.tianyancha.com/')