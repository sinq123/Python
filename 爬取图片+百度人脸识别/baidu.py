from selenium import webdriver

'''
driver = webdriver.Firefox()   # Firefox浏览器

driver = webdriver.Chrome()    # Chrome浏览器

driver = webdriver.Ie()        # Internet Explorer浏览器

driver = webdriver.Edge()      # Edge浏览器

driver = webdriver.Opera()     # Opera浏览器

driver = webdriver.PhantomJS()   # PhantomJS
'''
# 增加浏览器的绝对路径
driver = webdriver.Edge(executable_path= 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')

driver.get('https://www.baidu.com')
print(driver.title)
print(driver.page_source)
driver.quit()
