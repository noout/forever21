import csv

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import unittest
from selenium.webdriver.common.by import By as by









class TablTest(unittest.TestCase):
    @classmethod

    def setUpClass(self):



        desired_cap = {}
        desired_cap['platformName'] = 'Android'
        desired_cap['app'] = 'C:\\Users\\qoxot\\Downloads\\app\\forever21.apk'
        desired_cap['platformVersion'] = '12'
        desired_cap['automationName'] = 'Appium'
        desired_cap['deviceName'] = 'R3CT20326HZ'
        desired_cap['noReset'] = True


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        self.driver.implicitly_wait(10)








    def test_search1(self):
        driver = self.driver







        search = driver.find_element(by.ID,"com.rarewire.forever21:id/ll_search_title_container")
        search.click()
        time.sleep(1)
        search_edit = driver.find_element(by.ID,"com.rarewire.forever21:id/et_search_bar_edit")
        time.sleep(1)
        search_edit.send_keys("red dress")
        time.sleep(1)
        driver.press_keycode(66)
        time.sleep(3)
        driver.save_screenshot('search.png')


        #Sort
        sort_title = driver.find_element(by.ID,"com.rarewire.forever21:id/tv_product_sort_title")
        print(sort_title)
        sort_title.click()

        time.sleep(3)
        #newest
        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.TextView").click()

        # Sort
        time.sleep(3)
        print(sort_title)
        sort_title.click()
        time.sleep(3)
        #price high to low
        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView").click()
        time.sleep(3)
        # Sort
        sort_title.click()

        time.sleep(3)
        #price low to high
        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView").click()
        time.sleep(3)
        # Sort
        sort_title.click()
        time.sleep(3)
        #Best match
        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.TextView").click()

    def test_search2(self):
        driver = self.driver

        time.sleep(3)
        for i in range(1,7):
            driver.find_element(by.ID,"com.rarewire.forever21:id/tv_product_refine").click()
            time.sleep(3)
            filter = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{}]/android.widget.TextView[2]".format(i)
            driver.find_element(by.XPATH,filter).click()
            time.sleep(3)

            driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView").click()
            time.sleep(3)
            driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView").click()
            time.sleep(6)

        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.ImageView").click()
        time.sleep(3)
        driver.back()

    def test_discover(self):

        driver = self.driver




        driver.find_element(by.ID,"com.rarewire.forever21:id/tv_bottom_home_title").click()
        driver.find_element(by.ID,"com.rarewire.forever21:id/tv_global_bar").click()
        time.sleep(3)
        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.RelativeLayout/android.widget.TextView[1]").click()
        time.sleep(3)

        driver.find_element(by.ID,"com.rarewire.forever21:id/tv_specialoffer_shopnow").click()
        time.sleep(3)
        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.ImageView").click()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.back()

        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView[2]/android.view.ViewGroup[1]/android.widget.ImageView").click()
        time.sleep(3)
        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.ImageView").click()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.back()
        
        driver.swipe(545, 1200, 545, 500)
        time.sleep(1)
        driver.swipe(545, 1200, 545, 500)
        time.sleep(1)
        driver.swipe(545, 1200, 545, 500)
        time.sleep(1)


        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[1]").click()
        driver.back()

        driver.find_element(by.ID,"com.rarewire.forever21:id/tv_home_recent_clear").click()



    def test_shop(self):
        driver = self.driver
        driver.find_element(by.ID,"com.rarewire.forever21:id/iv_bottom_shop").click()
        time.sleep(3)
        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView[1]").click()
        time.sleep(3)
        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[8]/android.widget.RelativeLayout/android.widget.TextView").click()
        time.sleep(3)

        # Sort
        sort_title = driver.find_element(by.ID, "com.rarewire.forever21:id/tv_product_sort_title")
        print(sort_title)
        sort_title.click()

        time.sleep(3)
        # newest
        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView").click()

        # Sort
        time.sleep(3)
        print(sort_title)
        sort_title.click()
        time.sleep(3)
        # price high to low
        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.TextView").click()
        time.sleep(3)
        # Sort
        sort_title.click()

        time.sleep(3)
        # price low to high
        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.TextView").click()
        time.sleep(3)
        # Sort
        sort_title.click()
        time.sleep(3)
        # Best match
        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]/android.widget.TextView").click()
        time.sleep(3)
        sort_title.click()
        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView").click()

        time.sleep(3)

        for i in range(1,6):
            driver.find_element(by.ID,"com.rarewire.forever21:id/tv_product_refine").click()
            time.sleep(3)
            filter = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{}]/android.widget.TextView[2]".format(i)
            driver.find_element(by.XPATH,filter).click()
            time.sleep(3)

            driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView").click()
            time.sleep(3)
            driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView").click()
            time.sleep(3)


    def test_aPDP(self):

        driver = self.driver
        search = driver.find_element(by.ID,"com.rarewire.forever21:id/ll_search_title_container")
        search.click()
        time.sleep(1)
        search_edit = driver.find_element(by.ID,"com.rarewire.forever21:id/et_search_bar_edit")
        time.sleep(1)
        search_edit.send_keys("red dress")
        time.sleep(1)
        driver.press_keycode(66)
        time.sleep(3)
        driver.save_screenshot('search.png')

        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.ImageView").click()
        time.sleep(3)
        for i in range(6):
            driver.swipe(800, 850, 110, 850)
            time.sleep(2)

        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.RelativeLayout[1]/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout[1]/android.widget.ImageView").click()

        for i in range(6):
            driver.swipe(110, 850, 800, 850)
            time.sleep(2)

        driver.back()
        time.sleep(3)

        driver.find_element(by.ID,"com.rarewire.forever21:id/iv_detail_wish").click()
        time.sleep(3)

        driver.find_element(by.ID,"com.rarewire.forever21:id/tv_detail_item_price").click()
        time.sleep(3)

        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageView[2]").click()
        time.sleep(3)

        #driver.swipe(545, 1200, 545, 500)
        #time.sleep(1)

        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView[2]/android.widget.RelativeLayout[1]/android.widget.TextView").click()
        time.sleep(3)

        driver.swipe(545, 1200, 545, 500)
        time.sleep(1)

        driver.swipe(545, 1200, 545, 500)
        time.sleep(1)



        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[1]").click()
        time.sleep(3)
        driver.back()
        time.sleep(2)
        driver.swipe(545, 1200, 545, 500)
        time.sleep(1)

        time.sleep(2)
        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[1]").click()
        time.sleep(3)
        driver.back()
        time.sleep(2)



        #driver.find_element(by.ID,"com.rarewire.forever21:id/btn_change_location").click()
        #time.sleep(3)

        #driver.find_element(by.ID,"com.rarewire.forever21:id/inputField").send_keys("91030")
        #time.sleep(3)

        #driver.find_element(by.ID,"com.rarewire.forever21:id/tv_store_search").click()
        #time.sleep(3)

        #driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView[2]").click()
        #time.sleep(3)

        driver.find_element(by.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button").click()
        time.sleep(3)



















        #driver.swipe(545, 1200, 545, 500)
        #time.sleep(1)
        #driver.swipe(545, 1200, 545, 500)
        #time.sleep(1)
        #driver.swipe(545, 1200, 545, 500)
        #time.sleep(1)
        #driver.find_element_by_xpath("/ hierarchy / android.widget.FrameLayout / android.widget.LinearLayout / android.widget.FrameLayout / android.widget.LinearLayout / android.widget.FrameLayout / androidx.drawerlayout.widget.DrawerLayout / android.view.ViewGroup / android.widget.FrameLayout / android.widget.RelativeLayout / android.widget.LinearLayout /android.widget.RelativeLayout[4] / android.widget.TextView").click()






if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TablTest)
    unittest.TextTestRunner(verbosity=2).run(suite)