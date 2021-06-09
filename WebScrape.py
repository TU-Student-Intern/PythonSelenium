from selenium import webdriver
PATH = "C:/Users/Apy/Desktop/Internship/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
#driver.close()
print(driver.title)
driver.quit()