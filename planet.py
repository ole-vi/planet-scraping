import selenium
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import os


browser = webdriver.Firefox()
browser.get('http://localhost:3100/eng/login?returnUrl=%2F')


# Select username and password boxes
username = browser.find_element_by_id('mat-input-0')
password = browser.find_element_by_id('mat-input-1')

# Get password and username from environment variable
pword = os.getenv('LOGIN_PASSWORD')
uname = os.getenv('LOGIN_USERNAME')
file_path = os.getenv('FILE_LOCATION')

select = browser.find_element_by_css_selector('#mat-input-0')

# Send username and password from environment variables
username.send_keys(uname)
password.send_keys(pword)

# Click login button
browser.find_element_by_class_name('mat-raised-button').click()

time.sleep(2)

# Click add item button
browser.find_element_by_id('cdk-drop-list-0').click()

# Need this to allow angular to load 
time.sleep(2)

# Click resource "+" button
browser.find_element_by_class_name('mat-mini-fab').click()

time.sleep(2)

# Upload file
browse_button = browser.find_element_by_css_selector('div.inner-gaps:nth-child(17) > input:nth-child(2)')
browser.execute_script("arguments[0].style.display = 'block';", browse_button)
browse_button = browser.find_element_by_css_selector('div.inner-gaps:nth-child(17) > input:nth-child(2)')
browse_button.send_keys(file_path + '/treehouses.zip')

time.sleep(2)

# Fill in "open which file" box
which_file = browser.find_element_by_id('mat-input-9')
which_file.send_keys("treehouses.github.io/index.md")

# Fill in title field
title = browser.find_element_by_id('mat-input-3')
title.send_keys('treehouses.io')

#description = browser.find_element_by_class_name('CodeMirror')
description = browser.find_element_by_css_selector('.CodeMirror > div:nth-child(1) > textarea:nth-child(1)')
description.send_keys('Treehouses website') 

# Fill in subject drop - cannot get it to select an option in the dropdown
#subject = browser.find_element_by_css_selector('#mat-form-field-label-29').click

select = browser.find_element_by_css_selector('#mat-form-field-label-29')

select.send_keys('Agriculture')
#for option in subject.find_elements_by_tag_name('aria-owns'):
#	if option.text == "Agriculture":
#		option.click()
#		break

# Click submit button
# browser.find_element_by_class_name('mat-primary').click()

