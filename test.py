import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # ตั้งค่าให้รอ 10 วินาที

    def tearDown(self):
        self.driver.quit()

    def test_signup_form(self):
        driver = self.driver
        driver.get("https://sc.npru.ac.th/sc_shortcourses/signup")

        # กรอกข้อมูลในฟอร์ม
        driver.find_element(By.ID, "firstnameTha").send_keys("กฤษณะ")
        driver.find_element(By.ID, "lastnameTha").send_keys("ผิวงาม")
        driver.find_element(By.ID, "firstnameEng").send_keys("Kritsana")
        driver.find_element(By.ID, "lastnameEng").send_keys("Piwgram")
        driver.find_element(By.ID, "email").send_keys("664259002@webmail.npru.ac.th")

        # เลือกวัน เดือน ปีเกิด
        Select(driver.find_element(By.ID, "birthDate")).select_by_visible_text("30")
        Select(driver.find_element(By.ID, "birthMonth")).select_by_visible_text("กันยายน")
        Select(driver.find_element(By.ID, "birthYear")).select_by_visible_text("2547")

        driver.find_element(By.ID, "idCard").send_keys("1749900994967")
        driver.find_element(By.ID, "password").send_keys("Dayz01gg")
        driver.find_element(By.ID, "mobile").send_keys("0959042353")
        driver.find_element(By.ID, "address").send_keys("168/24")

        # เลือกจังหวัด อำเภอ ตำบล และรหัสไปรษณีย์
        Select(driver.find_element(By.ID, "province")).select_by_visible_text("สมุทรสาคร")
        driver.find_element(By.ID, "district").send_keys("เมือง")
        driver.find_element(By.ID, "subDistrict").send_keys("ท่าทราย")
        driver.find_element(By.ID, "postalCode").send_keys("74000")

        # เลื่อนหน้าให้เห็นปุ่ม "ยอมรับเงื่อนไข"
        accept_checkbox = driver.find_element(By.ID, "accept")
        driver.execute_script("arguments[0].scrollIntoView();", accept_checkbox)
        time.sleep(1)  # รอให้หน้าเว็บเลื่อนก่อนคลิก

        # ใช้ JavaScript คลิกแทน Selenium ธรรมดา
        driver.execute_script("arguments[0].click();", accept_checkbox)

        # พักสักครู่ก่อนปิด
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
