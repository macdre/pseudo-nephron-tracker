import pytest
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestBasicloginandrecordtreatment():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
    self.wait = WebDriverWait(self.driver, 20)
    self.test_email = os.environ['TEST_EMAIL']
    self.test_pass = os.environ['TEST_PASS']
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_basicloginandrecordtreatment(self):
    self.driver.get("http://localhost:8080/")
    self.driver.maximize_window()
    self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn")))
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()

    self.wait.until(EC.url_changes("http://localhost:8080/"))
    self.wait.until(EC.visibility_of_element_located((By.ID, "Web/Submit/Active")))
    self.driver.find_element(By.ID, "1-email").send_keys(self.test_email)
    self.driver.find_element(By.NAME, "password").send_keys(self.test_pass)
    self.driver.find_element(By.CSS_SELECTOR, ".auth0-label-submit").click()

    self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".fa-notes-medical")))
    self.driver.find_element(By.CSS_SELECTOR, ".fa-notes-medical").click()


    self.wait.until(EC.visibility_of_element_located((By.ID, "entry_date")))
    self.driver.find_element(By.ID, "entry_date").click()

    self.driver.find_element(By.CSS_SELECTOR, "#\\__BVID__102__cell-2020-12-16_ > .btn").click()

    self.driver.find_element(By.ID, "systolic_pressure").send_keys("8")
    
    self.driver.find_element(By.ID, "diastolic_pressure").send_keys("7")
    
    self.driver.find_element(By.ID, "weight_in_kg").send_keys("6")

    
    
    ActionChains(self.driver).move_to_element(self.driver.find_element_by_id("initial_drain")).perform()
    self.driver.find_element(By.ID, "initial_drain").send_keys("5")
    
    self.driver.find_element(By.ID, "total_uf").send_keys("4")
    
    self.driver.find_element(By.ID, "average_dwell").click()
    self.driver.find_element(By.CSS_SELECTOR, ".focus > .btn:nth-child(3) > .bi-chevron-up").click()
    self.driver.find_element(By.CSS_SELECTOR, ".focus > .btn:nth-child(1) > .bi-chevron-up").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-outline-secondary").click()    
    
    self.driver.find_element(By.ID, "added_lost_dwell_type").click()
    dropdown = self.driver.find_element(By.ID, "added_lost_dwell_type")
    dropdown.find_element(By.XPATH, "//option[. = 'Added']").click()
    self.driver.find_element(By.ID, "added_lost_dwell_type").click()

    element = self.driver.find_element(By.ID, "added_lost_dwell_value")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.ID, "added_lost_dwell_value__value_").click()
    self.driver.find_element(By.CSS_SELECTOR, ".focus > .btn:nth-child(3) > .bi-chevron-up").click()
    self.driver.find_element(By.CSS_SELECTOR, ".focus > .btn:nth-child(1) > .bi-chevron-up").click()
    self.driver.find_element(By.CSS_SELECTOR, ".focus > .btn:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-outline-secondary").click()



    ActionChains(self.driver).move_to_element(self.driver.find_element_by_id("drain_color")).perform()
    self.driver.find_element(By.ID, "drain_color").click()
    dropdown = self.driver.find_element(By.ID, "drain_color")
    dropdown.find_element(By.XPATH, "//*[@id=\"drain_color\"]/option[. = 'No Color']").click()
    
    self.driver.find_element(By.ID, "drain_clarity").click()
    dropdown = self.driver.find_element(By.ID, "drain_clarity")
    dropdown.find_element(By.XPATH, "//*[@id=\"drain_clarity\"]/option[. = 'Clear']").click()

    self.driver.find_element(By.ID, "fibrin_present").click()
    dropdown = self.driver.find_element(By.ID, "fibrin_present")
    dropdown.find_element(By.XPATH, "//*[@id=\"fibrin_present\"]/option[. = 'No']").click()



    ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(".btn-primary")).perform()  
    ActionChains(self.driver).move_to_element(self.driver.find_element_by_id("exit_condition")).perform()
    self.driver.find_element(By.ID, "exit_color").click()
    dropdown = self.driver.find_element(By.ID, "exit_color")
    dropdown.find_element(By.XPATH, "//*[@id=\"exit_color\"]/option[. = 'Normal']").click()

    self.driver.find_element(By.ID, "exit_sensitivity").click()
    dropdown = self.driver.find_element(By.ID, "exit_sensitivity")
    dropdown.find_element(By.XPATH, "//*[@id=\"exit_sensitivity\"]/option[. = 'Normal']").click()

    self.driver.find_element(By.ID, "exit_condition").click()
    dropdown = self.driver.find_element(By.ID, "exit_condition")
    dropdown.find_element(By.XPATH, "//*[@id=\"exit_condition\"]/option[. = 'Normal']").click()



    ActionChains(self.driver).move_to_element(self.driver.find_element_by_id("bowel_obs")).perform()
    self.driver.find_element(By.ID, "bowel_obs").click()
    dropdown = self.driver.find_element(By.ID, "bowel_obs")
    dropdown.find_element(By.XPATH, "//*[@id=\"bowel_obs\"]/option[. = 'Liquid']").click()

    self.driver.find_element(By.ID, "treatment_problems").click()
    dropdown = self.driver.find_element(By.ID, "treatment_problems")
    dropdown.find_element(By.XPATH, "//*[@id=\"treatment_problems\"]/option[. = 'No']").click()



    ActionChains(self.driver).move_to_element(self.driver.find_element_by_id("comments")).perform()
    self.driver.find_element(By.ID, "comments").click()
    self.driver.find_element(By.ID, "comments").send_keys("blah blah blah")

    ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(".btn-primary")).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    time.sleep(20)
    self.driver.close()
