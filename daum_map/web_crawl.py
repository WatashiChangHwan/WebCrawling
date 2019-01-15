# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 22:03:38 2019

@author: User
"""

from selenium import webdriver
import time
import pandas as pd

# file
data = pd.read_csv(r'D:\graduated_school\Thesis\data/station2.csv')

n = len(data)
lent_col = data['lent'].values
return_col = data['return'].values
url_col = data['url'].values

# Create a new cromedriver

#driver = webdriver.PhantomJS(r'D:\graduated_school\phantomjs\bin\phantomjs.exe')

#options = webdriver.ChromeOptions()
#options.add_argument('headless')
#options.add_argument('window-size=1920x1080')
#options.add_argument("disable-gpu")
driver = webdriver.Chrome(r'D:\graduated_school\chrome_driver/chromedriver.exe')
driver.set_window_size(1920, 1080)

# code 실행
for i in range(n):
    time.sleep(10)
    driver.get(url_col[i])
    # Saves a .png file with name my_screenshot_name to the directory that
    # you are running the program from.
    time.sleep(2)
    directory = r'C:\Users\User\Desktop\temp_file/'
    screenshot_name = directory+str(lent_col[i])+'_'+str(return_col[i])+'.png'
    driver.save_screenshot(screenshot_name)

# http://cafe.daum.net/_c21_/bbs_search_read?grpid=XnQY&fldid=CuSo&datanum=28430
