import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginRegister(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_Login_Negatif_Saus(self): 
        driver = self.driver
        driver.get("https://www.saucedemo.com/") 
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("riza") 
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("123") 
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()

        response_message = driver.find_element(By.CLASS_NAME,"error-message-container").text
        self.assertEqual(response_message, 'Epic sadface: Username and password do not match any user in this service')

    def test_Register_Positif(self): 
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar ") 
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"signUp").click()
        time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys("acuna") 
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys("acuna@riza.com") 
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys("Boiko12") 
        time.sleep(1)
        driver.find_element(By.ID,"signup_register").click()


        response_message = driver.find_element(By.ID,"swal2-content").text
        self.assertEqual(response_message, 'created user!')

    def test_Register_Negatif(self): 
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar ") 
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"signUp").click()
        time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys("riza") 
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys("riza@riza.com") 
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys("Akupada17") 
        time.sleep(1)
        driver.find_element(By.ID,"signup_register").click()


        response_message = driver.find_element(By.ID,"swal2-content").text
        self.assertEqual(response_message, 'Gagal Register!!')
  
        
    def test_Login_Negatif(self): 
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar") 
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("acuna") 
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("acuna@riza.com") 
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click()

        response_message = driver.find_element(By.ID,"swal2-content").text
        self.assertEqual(response_message, 'Email atau Password Anda Salah')
    
    def test_Login_Positif(self): 
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar") 
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("daring@mail.com") 
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("aku123") 
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click()

        response_message = driver.find_element(By.ID,"swal2-title").text
        self.assertEqual(response_message, 'Welcome daring')


    

unittest.main()