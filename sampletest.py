from selenium.webdriver import Chrome, ChromeOptions
import time

BASE_URL = "http://127.0.0.1:5000/index"
EMAIL_ID = "agrawalkaran123@gmail.com"
EXPECTED_COLOR = "rgba(222, 20, 33, 1)"


class BrowserstackCrawler(object):
    def __init__(self):
        options = ChromeOptions().add_argument("--user-data-dir=<chrome user profile>")
        self.browser = Chrome(executable_path=r"C:\\Users\\hp\\Downloads\\chromedriver_win32\\chromedriver.exe",chrome_options=options)
        self.browser.get(BASE_URL)
        time.sleep(5)
    def signup(self):      
        self.browser.find_element_by_link_text("Sign Up").click()
        time.sleep(2)
        username = self.browser.find_element_by_id('username')
        self.slow_typing(username, 'KaranAg')
        time.sleep(1)
        email = self.browser.find_element_by_id('email')
        self.slow_typing(email, EMAIL_ID)
        time.sleep(2)
        password = self.browser.find_element_by_id('password')
        with open('password.txt', 'r') as myfile:
            Password = myfile.read().replace('\n', '')
        self.slow_typing(password, Password)
        time.sleep(2)
        confirm_password = self.browser.find_element_by_id('confirm_password')
        with open('password.txt', 'r') as myfile:
            Password = myfile.read().replace('\n', '')
        self.slow_typing(confirm_password, Password)
        time.sleep(1)
        submit = self.browser.find_element_by_id('submit')
        submit.click()
        time.sleep(10)
        self.close_browser()


    
    def userlogin(self):      
        self.browser.find_element_by_link_text("Login").click()
        time.sleep(2)
        email = self.browser.find_element_by_id('email')
        self.slow_typing(email, EMAIL_ID)
        time.sleep(2) 
        password = self.browser.find_element_by_id('password')
        with open('password.txt', 'r') as myfile:
            Password = myfile.read().replace('\n', '')
        self.slow_typing(password, Password)       
        time.sleep(1)
        submit = self.browser.find_element_by_id('submit')
        submit.click()
        time.sleep(3)
        self.browser.find_element_by_link_text("ANALYSIS").click()
        time.sleep(10)
        self.browser.find_element_by_link_text("LOGOUT").click()
        self.close_browser()

    def slow_typing(self, element, text):
        for character in text:
            element.send_keys(character)
            time.sleep(0.3)

    def check_color(self, color, orginal_color):
        return color == orginal_color

    def close_browser(self):
        self.browser.close()


b1 = BrowserstackCrawler()
b1.signup()

b3 = BrowserstackCrawler()
b3.userlogin()