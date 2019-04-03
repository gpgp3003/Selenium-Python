# -*- coding: utf-8 -*-
# sudo apt-get install -y python
# sudo apt install -y python-pip
# pip install selenium

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument('-headless')
        self.driver = Firefox(executable_path='geckodriver', options=options)
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        

    def test_untitled_test_case(self):
        driver = self.driver
        action = ActionChains(driver)
        driver.get("https://dev.imotopecas.com.br/")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Política de Cookies'])[2]/following::span[1]").click()
        action.move_to_element(driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Olá!'])[1]/following::div[1]") ).perform();
        driver.find_element_by_id("login").click()
        driver.save_screenshot('./evidenc/evidencia7.png');
        driver.find_element_by_id("login").clear()
        driver.save_screenshot('./evidenc/evidencia8.png');
        driver.find_element_by_id("login").send_keys("gianpgp@primeinformatica.com.br")
        driver.save_screenshot('./evidenc/evidencia9.png');
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("102030")
        driver.save_screenshot('./evidenc/evidencia10.png');
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Esqueci a senha'])[1]/following::button[1]").click()
        i = 1
        while i < 7:
            driver.get("https://dev.imotopecas.com.br/")
            driver.find_element_by_link_text("Capacete Nasa Elegance SH-881").click()
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='X'])[1]/following::img[1]").click()
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='X'])[5]/following::span[1]").click()
            driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Informe as opções do Produto'])[1]/following::span[3]").click()
            driver.save_screenshot('./evidenc/evidencia' + str(i) + '.png');
            i += 1
        

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

    


