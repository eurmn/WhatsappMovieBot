from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys

# d_options = webdriver.ChromeOptions()
# d_options.add_argument('--user-data-dir=C:/Users/user/AppData/Local/Google/Chrome/User Data/Profile 2')
# driver = webdriver.Chrome(options=d_options)
driver = webdriver.Chrome()

movie = str(sys.argv[1]) + '.txt'
script = open(movie, 'r', encoding='utf-8').read().split()
target = str(sys.argv[2])

driver.get('https://web.whatsapp.com/')

try:
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//span[@title='{target}'][contains(@class, '_3ko75 _5h6Y_ _3Whw5')]"))
    )
finally:
    driver.find_element_by_xpath("//span[@title='{target}'][contains(@class, '_3ko75 _5h6Y_ _3Whw5')]").click()

winput = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
winput.click()

sleep(2)

def is_sent():
    status = driver.find_elements_by_xpath("//div[@class='_1qPwk']")[-1].get_attribute('innerHTML')
    sent = '<span data-testid="msg-time" aria-label=" Pending " data-icon="msg-time" class=""><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 15" width="16" height="15"><path fill="currentColor" d="M9.75 7.713H8.244V5.359a.5.5 0 0 0-.5-.5H7.65a.5.5 0 0 0-.5.5v2.947a.5.5 0 0 0 .5.5h.094l.003-.001.003.002h2a.5.5 0 0 0 .5-.5v-.094a.5.5 0 0 0-.5-.5zm0-5.263h-3.5c-1.82 0-3.3 1.48-3.3 3.3v3.5c0 1.82 1.48 3.3 3.3 3.3h3.5c1.82 0 3.3-1.48 3.3-3.3v-3.5c0-1.82-1.48-3.3-3.3-3.3zm2 6.8a2 2 0 0 1-2 2h-3.5a2 2 0 0 1-2-2v-3.5a2 2 0 0 1 2-2h3.5a2 2 0 0 1 2 2v3.5z"></path></svg></span>'
    if status == sent:
        return True
    else:
        return False

for word in script:
    winput.send_keys(word)
    sent = is_sent()
    sleep(0.3)

    while sent:
        sent = is_sent()
        sleep(1)

    sleep(0.1)
    winput.send_keys(Keys.ENTER)
    sleep(1)
    sent = False
    


