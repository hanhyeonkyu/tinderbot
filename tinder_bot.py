from selenium import webdriver
from time import sleep
from secret import username, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://tinder.com/")

        sleep(5)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        fb_btn.click()

        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        sleep(2)
        
        self.driver.switch_to.window(base_window)

        sleep(2)

        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        sleep(2)

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

        sleep(5)

        try:
            confirm_email_later = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/button[2]')
            confirm_email_later.click()
        except Exception:
            print("not confirm email today")

    def interest_popup(self):
        nointerest_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        nointerest_btn.click()
    
    def payment_popup(self):
        nopayment_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
        nopayment_btn.click()

    def close_match(self):
        confirm_match = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        confirm_match.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def auto_swipe(self):
        from random import random
        left_count, right_count = 0, 0
        while True:
            sleep(0.5)
            try:
                rand = random()
                if rand < .9:
                    self.like()
                    right_count += 1
                    print('{}th right swipe'.format(right_count))
                else:
                    self.dislike()
                    left_count += 1
                    print('{}th left swipe'.format(left_count))
            except Exception:
                try:
                    self.interest_popup()
                except Exception:
                    try:
                        self.close_match()
                    except Exception:
                        self.payment_popup()
                        break
                        
bot = TinderBot()
bot.login()
