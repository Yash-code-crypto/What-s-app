from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://web.whatsapp.com/")


input("Please scan your qr code of whats app and press any button to continue")

nam=driver.find_element_by_css_selector('span[title="Mom"]')
nam.click()

testinput=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
text=input("Enter the text")
for i in range(0,20):
    testinput.send_keys(text)
    testinput.send_keys(Keys.RETURN)