from selenium import webdriver
import requests
import base64


driver = webdriver.PhantomJS()
driver.get('https://antirobot.tianyancha.com/captcha/verify?return_url=https%3A%2F%2Fln.tianyancha.com%2Fsearch%2Fp10%3Frnd%3D%26rnd%3D%26rnd%3D&rnd=')
el_img1 = driver.find_element_by_xpath('//img[@id="targetImgie"]')
src1 = el_img1.get_attribute('src')
# print(src1)
data = src1.split(',')[1]
result = base64.b64decode(data)
print(result)
with open('img_up.png', 'wb') as f:
    f.write(result)