import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import re
import module_other_stx_app
import login_stx_app
import var_stx_app
import requests
import json
from retry import retry
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import homepage_g7
from pynput.keyboard import Key, Controller
keyboard = Controller()
from datetime import datetime





def select_detail(field, row):
    var_stx_app.driver.implicitly_wait(0.05)  # nhiên liệu
    n = 0
    while (n < 10):
        n += 1
        n = str(n)
        path_name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup[1]/android.widget.TextView[1]"
        path_data = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[" + n + "]/android.view.ViewGroup[1]/android.widget.TextView[2]"
        print(n)
        try:
            name = var_stx_app.driver.find_element(By.XPATH, path_name).text
            print(name)
            if name == field:
                data = var_stx_app.driver.find_element(By.XPATH, path_data).text
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", row, 3, data)
                print(data)
                break
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", row, 3, 0)
        n = int(n)







def homepage_g7_drive_back():
    var_stx_app.driver.implicitly_wait(0.1)
    #lai xe huy cuoc 1 - HUY BO
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.CANCEL).click()
        time.sleep(2.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.reasson_other).click()
        time.sleep(3)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.IGREE).click()
        time.sleep(2.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
        print("n1")
    except:
        pass


    #lai xe huy cuoc 2 - TRA KHACH
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.RETURN_GUESTS).click()
        time.sleep(2.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.CASH).click()
        time.sleep(2)
        print("n2")
    except:
        pass


    #Roi sanh
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_stt)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_dispatching1).click()
        time.sleep(2.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_drive).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm1).click()
        time.sleep(2.5)
        print("n3")
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(2.5)
        except:
            pass
    except:
        pass




    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.BACK).click()
        time.sleep(0.5)
        print("n4")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.COME_BACK).click()
        time.sleep(0.5)
        print("n5")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel).click()
        time.sleep(0.5)
        print("n6")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.CANCEL).click()
        time.sleep(0.5)
        print("n7")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.SKIP).click()
        time.sleep(0.5)
        print("n8")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.skip).click()
        time.sleep(0.5)
        print("n9")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
        time.sleep(0.5)
        print("n10")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.IGREE).click()
        time.sleep(0.5)
        print("n11")
    except:
        pass

    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage_g7_drive_back1).click()
        time.sleep(0.5)
        print("n12")
    except:
        pass

    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage_g7_drive_back2).click()
        time.sleep(0.5)
        print("n13")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage_g7_drive_back3).click()
        time.sleep(0.5)
        print("n14")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage_g7_drive_back4).click()
        time.sleep(0.5)
        print("n15")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.pttt1).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.pttt1_g7).click()
        time.sleep(2.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.money_clock_input).send_keys("106000")
        time.sleep(1.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
        time.sleep(2.3)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.payment).click()
        time.sleep(3)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.FILL_CODE_CARD).click()
        time.sleep(3)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.FILL_CODE_CARD_INPUT).send_keys("9999920987715201")
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm1).click()
        time.sleep(2.3)
        print("n16")
    except:
        pass


    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage_g7_drive_back5).click()
        time.sleep(1.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage_g7_drive_back6).click()
        print("n17")
    except:
        pass

    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.WRONG_CUSTOMER).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
        time.sleep(2)
        print("n18")
    except:
        pass

    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.RETURN_GUESTS).click()
        time.sleep(2.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.CASH).click()
        time.sleep(2.5)
        print("n19")
    except:
        pass

    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.DROP_OFF_PASSENGERS).click()
        time.sleep(0.5)
        print("n20")
    except:
        pass

    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver1).click()
        time.sleep(0.5)
        print("n21")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver2).click()
        time.sleep(0.5)
        print("n22")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver3).click()
        time.sleep(0.5)
        print("n23")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver4).click()
        time.sleep(0.5)
        print("n24")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver5).click()
        time.sleep(0.5)
        print("n25")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver6).click()
        time.sleep(0.5)
        print("n26")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver7).click()
        time.sleep(0.5)
        print("n27")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver8).click()
        time.sleep(0.5)
        print("n28")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver9).click()
        time.sleep(0.5)
        print("n29")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver10).click()
        time.sleep(0.5)
        print("n30")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver11).click()
        time.sleep(0.5)
        print("n31")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver12).click()
        time.sleep(0.5)
        print("n32")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver13).click()
        time.sleep(0.5)
        print("n33")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver14).click()
        time.sleep(0.5)
        print("n34")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver15).click()
        time.sleep(0.5)
        print("n35")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver16).click()
        time.sleep(0.5)
        print("n36")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver17).click()
        time.sleep(0.5)
        print("n37")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver18).click()
        time.sleep(0.5)
        print("n38")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver19).click()
        time.sleep(0.5)
        print("n39")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver20).click()
        time.sleep(0.5)
        print("n40")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver21).click()
        time.sleep(0.5)
        print("n41")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver22).click()
        time.sleep(0.5)
        print("n42")
    except:
        pass
    # try:
    #     var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver23).click()
    #     time.sleep(1)
    #     print("n43")
    # except:
    #     pass
    # try:
    #     var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver24).click()
    #     time.sleep(1)
    #     print("n44")
    # except:
    #     pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver25).click()
        time.sleep(0.5)
        print("n45")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver26).click()
        time.sleep(0.5)
        print("n46")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver27).click()
        time.sleep(0.5)
        print("n47")
    except:
        pass
    # try:
    #     var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver28).click()
    #     time.sleep(1)
    #     print("n48")
    # except:
    #     pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver29).click()
        time.sleep(0.5)
        print("n49")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver30).click()
        time.sleep(0.5)
        print("n50")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver31).click()
        time.sleep(0.5)
        print("n51")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver32).click()
        time.sleep(0.5)
        print("n52")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page_driver33).click()
        time.sleep(0.5)
        print("n53")
    except:
        pass
    try:
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage).click()
        time.sleep(0.5)
        print("n54")
    except:
        pass







class home_page:

    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def status_driver(self, type, status):
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification)
        except:
            login_stx_app.login_driverg7(self, type)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.home_page).click()
        time.sleep(1)
        name_status = var_stx_app.driver.find_element(By.XPATH, var_stx_app.name_status_driver).text
        if name_status == status:
            pass
        else:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.name_status_driver_radio).click()
            time.sleep(2)

        time.sleep(1)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_city).click()
        time.sleep(1.5)
        check_text = var_stx_app.driver.find_element(By.XPATH, "//android.widget.Toast").text
        print(check_text)
        if check_text == "Sẵn sàng nhận cuốc phố":
            pass
        else:
            time.sleep(3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_city).click()
            time.sleep(1.5)
            check_text = var_stx_app.driver.find_element(By.XPATH, "//android.widget.Toast").text
            print(check_text)









class waiting_for_a_passenger:


    def waiting_for_a_passenger(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            module_other_stx_app.click_app("Lái xe G7")
            time.sleep(1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification)
        except:
            home_page.status_driver(self, "Xe sân bay", "SẴN SÀNG")




        wait = WebDriverWait(var_stx_app.driver, 5)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.icon_dash_3)))
        element.click()
        time.sleep(2)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.waiting_for_a_passenger).click()
        except:
            time.sleep(3)
            element.click()
            time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.waiting_for_a_passenger).click()
        time.sleep(2)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc",
                                              var_stx_app.check_waiting_for_a_passenger, "G7 Taxi Hà Nội", "_TrangChu_ChoCuoc.png")



    def check_display_icon(self, code, eventname, result, path_icon, name_image):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_waiting_for_a_passenger)
        except:
            waiting_for_a_passenger.waiting_for_a_passenger(self, "", "", "")

        var_stx_app.driver.implicitly_wait(5)

        if name_image == "_TrangChu_IconNhanCuocPho.png" or name_image == "_TrangChu_IconCauHinhXepLot.png":
            var_stx_app.driver.find_element(By.XPATH, path_icon)
        else:
            var_stx_app.driver.find_element(By.XPATH, path_icon).click()
            time.sleep(1.5)
            var_stx_app.driver.find_element(By.XPATH, path_icon).click()
            time.sleep(1.5)
        module_other_stx_app.write_result_displayed_try(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc",
                                              path_icon, name_image)



    def check_icon_help(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_waiting_for_a_passenger)
        except:
            waiting_for_a_passenger.waiting_for_a_passenger(self, "", "", "")

        var_stx_app.driver.implicitly_wait(5)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_help).click()
        time.sleep(1.5)
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            check_icon_name1 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_icon_name1).text
            check_icon_name2 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_icon_name2).text
            check_icon_name3 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_icon_name3).text
            check_icon_name4 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_icon_name4).text

            check_icon_data1 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_icon_data1).text
            check_icon_data2 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_icon_data2).text
            check_icon_data3 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_icon_data3).text
            check_icon_data4 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_icon_data4).text

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "1.{}\n{}\n2.{}\n{}\n3.{}\n{}\n4.{}\n{}"
                                           .format(check_icon_name1, check_icon_data1, check_icon_name2, check_icon_data2,
                                                   check_icon_name3, check_icon_data3, check_icon_name4, check_icon_data4))
            var_stx_app.logging.info("1.{}\n{}\n2.{}\n{}\n3.{}\n{}\n4.{}\n{}"
                                           .format(check_icon_name1, check_icon_data1, check_icon_name2, check_icon_data2,
                                                   check_icon_name3, check_icon_data3, check_icon_name4, check_icon_data4))
            if (check_icon_name1 == "Đường dây nóng" and check_icon_data1 != "") and (check_icon_name2 == "Trung tâm điều hành&CSKH" and check_icon_data2 != "") \
                    and (check_icon_name3 == "Văn Phòng" and check_icon_data3 != "") and (check_icon_name4 == "Hỗ trợ định vị, App" and check_icon_data4 != ""):

                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_IconHoTroKhanCap.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_IconHoTroKhanCap.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_TrangChu_IconHoTroKhanCap.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TrangChu_IconHoTroKhanCap.png")
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_help).click()
        time.sleep(1.5)



    def status(self, code, eventname, result, status, name_image):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_waiting_for_a_passenger)
        except:
            waiting_for_a_passenger.waiting_for_a_passenger(self, "", "", "")

        var_stx_app.driver.implicitly_wait(5)
        name_status = var_stx_app.driver.find_element(By.XPATH, var_stx_app.name_status_driver).text
        print(name_status)
        if name_status == status:
            pass
        else:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.name_status_driver_radio).click()
        time.sleep(2)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc",
                                              var_stx_app.name_status_driver, status, name_image)




    def check_location_car(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_waiting_for_a_passenger)
        except:
            waiting_for_a_passenger.waiting_for_a_passenger(self, "", "", "")


        try:
            var_stx_app.driver.swipe(815, 434, 85, 434, 500)
            var_stx_app.driver.swipe(815, 434, 85, 434, 500)
            var_stx_app.driver.swipe(815, 434, 85, 434, 500)
        except:
            var_stx_app.driver.swipe(610, 500, 100, 500, 500)
            var_stx_app.driver.swipe(610, 500, 100, 500, 500)
            var_stx_app.driver.swipe(610, 500, 100, 500, 500)
        time.sleep(3.5)
        module_other_stx_app.write_result_displayed_try(code, eventname, result, "Trang Chủ(Lái xe g7) - Check vị trí",
                                              var_stx_app.location_car, "_TrangChu_CheckViTri.png")








    def get_info_drive(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_waiting_for_a_passenger)
        except:
            waiting_for_a_passenger.waiting_for_a_passenger(self, "", "", "")

        var_stx_app.driver.implicitly_wait(5)
        overview_drive_name1 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_drive_name1).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 45, 2, overview_drive_name1)

        overview_drive_type_vehicle = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_drive_type_vehicle).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 46, 2, overview_drive_type_vehicle)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_dash_3).click()
        time.sleep(2)
        overview_drive_version = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_drive_version).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 47, 3, overview_drive_version)

        overview_drive_name2 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_drive_name2).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 45, 3, overview_drive_name2)


        #Thông tin xe
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_dash_3_drive_image).click()
        time.sleep(2.5)
        detail_drive_name3 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_drive_name3).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 45, 4, detail_drive_name3)

        detail_drive_review = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_drive_review).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 48, 4, detail_drive_review)

        detail_drive_type_vehicle = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_drive_type_vehicle).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 46, 4, detail_drive_type_vehicle)

        detail_drive_liscense_plate = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_drive_liscense_plate).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 49, 4, detail_drive_liscense_plate)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc - Thông tin cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("True")
        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")

        # try:
        #     var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_drive_back).click()
        #     time.sleep(2)
        # except:
        #     pass



    def check_info_drive_name(self, code, eventname, result):
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 45, 2))
        overview = overview.split("-")[0].strip()
        overview1 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 45, 3))

        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 45, 4))
        detail = detail.split("-")[0].strip()

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình Chờ cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Tên lái xe(Màn hình chờ cuốc): {}".format(overview))
        var_stx_app.logging.info("Tên lái xe(Dấu 3 gạch)       : {}".format(overview1))
        var_stx_app.logging.info("Tên lái xe(Thông tin cá nhân): {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "1.Tên lái xe(Màn hình chờ cuốc): {}\n2.Tên lái xe(Dấu 3 gạch)       : {}\n3.Tên lái xe(Thông tin cá nhân): {}"
                                       .format(overview, overview1, detail))
        if overview == overview1 == detail:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_drive_type_vehicle(self, code, eventname, result):
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 46, 2))
        overview = overview.split("-")[0].strip()
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 46, 4))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình Chờ cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Loại xe(Màn hình chờ cuốc): {}".format(overview))
        var_stx_app.logging.info("Loại xe(Thông tin cá nhân): {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "1.Loại xe(Màn hình chờ cuốc): {}\n2.Loại xe(Thông tin cá nhân): {}"
                                       .format(overview, detail))
        if overview == detail:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_drive_version(self, code, eventname, result):
        overview1 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 47, 3))
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 45, 4))
        detail = detail.split("-")[1].strip()

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình Chờ cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Phiên bản(Dấu 3 gạch)       : {}".format(overview1))
        var_stx_app.logging.info("Phiên bản(Thông tin cá nhân): {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "1.Phiên bản(Dấu 3 gạch)       : {}\n2.Phiên bản(Thông tin cá nhân): {}"
                                       .format(overview1, detail))
        if overview1 == detail:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_drive_star(self, code, eventname, result):
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 48, 4))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình Chờ cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Số sao(Thông tin cá nhân): {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "1.Số sao(Thông tin cá nhân): {}".format(detail))
        if detail != "None":
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def check_info_drive_liscense_plate(self, code, eventname, result):
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 46, 2))
        overview = overview.split("-")[1].strip()
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 49, 4))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Màn hình Chờ cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Biển số xe(Màn hình chờ cuốc): {}".format(overview))
        var_stx_app.logging.info("Biển số xe(Thông tin cá nhân): {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "1.Biển số xe(Màn hình chờ cuốc): {}\n2.Biển số xe(Thông tin cá nhân): {}"
                                       .format(overview, detail))
        if overview == detail:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def change_password(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.personal_information)
        except:
            waiting_for_a_passenger.get_info_drive(self, "", "", "")

        var_stx_app.driver.implicitly_wait(5)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_password).click()
        time.sleep(2.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_password_old).send_keys("atgmj123")
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_password_new1).send_keys("atgmj123")
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_password_new2).send_keys("atgmj123")
        time.sleep(1)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm1).click()
        time.sleep(2)
        module_other_stx_app.write_result_text_try_if_toast(code, eventname, result, "Trang Chủ(Lái xe g7) - Thông tin cá nhân - Đổi mật khẩu",
                                              var_stx_app.personal_information, "Mật khẩu mới trùng với mật khẩu cũ, vui lòng thử lại!", "_TrangChu_DoiMatKhau.png")


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.change_password_back).click()
            time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_drive_back).click()
            time.sleep(2)
        except:
            pass









    def driver_dispatching(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_waiting_for_a_passenger)
        except:
            waiting_for_a_passenger.waiting_for_a_passenger(self, "", "", "")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_stt)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_dispatching1).click()
            time.sleep(2.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_drive).click()
            time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm1).click()
            time.sleep(2.5)
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
                time.sleep(2.5)
            except:
                pass
        except:
            pass

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_dispatching).click()
        time.sleep(2.5)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Xếp tài",
                                              var_stx_app.check_driver_dispatching, "Danh sách sảnh", "_TrangChu_XepTai.png")



    def binhanh_parking_lot(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_driver_dispatching)
        except:
            waiting_for_a_passenger.driver_dispatching(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.binhanh_parking_lot).click()
        time.sleep(3)
        module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Xếp tài",
                                              var_stx_app.check_binhanh_parking_lot, "", "_TrangChu_XepTai_SanhBinhAnh.png")



    def check_info_binhanh_parking_lot(self, code, eventname, result, type, path_check, name_image):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_binhanh_parking_lot)
        except:
            waiting_for_a_passenger.binhanh_parking_lot(self, "", "", "")

        if type == "0":
            module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Xếp tài",
                                                  path_check, "", name_image)
        else:
            var_stx_app.logging.info("--------------")
            var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc - Xếp tài")
            var_stx_app.logging.info("Mã - " + code)
            var_stx_app.logging.info("Tên sự kiện - " + eventname)
            var_stx_app.logging.info("Kết quả - " + result)
            try:
                check_text = var_stx_app.driver.find_element(By.XPATH, path_check).text
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, check_text)
                var_stx_app.logging.info(check_text)
                if check_text != "":
                    var_stx_app.logging.info("True")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + name_image)
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)
            except:
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + name_image)
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)



    def cancel_drive(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_binhanh_parking_lot)
        except:
            waiting_for_a_passenger.binhanh_parking_lot(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_drive).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm1).click()
        time.sleep(2.5)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Xếp tài",
                                              var_stx_app.check_cancel_drive, "Bạn đã hủy tài thành công", "_SanhBinhAnh_HuyTai.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(2.5)
        except:
            pass



    def driver_dispatching_create_order(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_waiting_for_a_passenger)
        except:
            waiting_for_a_passenger.waiting_for_a_passenger(self, "", "", "")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_stt)
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_dispatching).click()
            time.sleep(2.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.binhanh_parking_lot).click()
            time.sleep(3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.binhanh_parking_lot_back).click()
            time.sleep(3)

        waiting_for_a_passenger.cash(self, "", "", "")

        module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Trang Chủ(Lái xe g7) - Xếp tài - Tạo cuốc",
                                              var_stx_app.check_stt, "Số thứ tự", "_SanhBinhAnh_XepTai_TaoCuoc.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_stt)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_dispatching1).click()
            time.sleep(2.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.cancel_drive).click()
            time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm1).click()
            time.sleep(2.5)
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
                time.sleep(2.5)
            except:
                pass
        except:
            pass
        module_other_stx_app.close_app()























    def create_order(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.sanh_back).click()
            time.sleep(2)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification)
        except:
            waiting_for_a_passenger.waiting_for_a_passenger(self, "", "", "")

        var_stx_app.driver.implicitly_wait(5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.create_order).click()
        time.sleep(1)
        wait = WebDriverWait(var_stx_app.driver, 10)
        time.sleep(1)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_create_order)))
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc",
                                              var_stx_app.check_create_order, "TẠO CUỐC", "_ChoCuoc_TaoCuoc.png")



    def create_order_back(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_create_order)
        except:
            waiting_for_a_passenger.create_order(self, "", "", "")

        var_stx_app.driver.implicitly_wait(5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.COME_BACK).click()
        time.sleep(2.5)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc",
                                              var_stx_app.homepage, "Trang chủ", "_TaoCuoc_TroLai.png")



    def create_order_search(self, code, eventname, result, path_search, path_search_input, data, path_check, name_image):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.create_order).click()
            time.sleep(2)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_create_order)
        except:
            waiting_for_a_passenger.create_order(self, "", "", "")

        var_stx_app.driver.implicitly_wait(5)
        var_stx_app.driver.find_element(By.XPATH, path_search).click()
        time.sleep(2)
        try:
            var_stx_app.driver.find_element(By.XPATH, path_search_input).clear()
        except:
            var_stx_app.driver.find_element(By.XPATH, path_search).click()
            time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, path_search_input).clear()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, path_search_input).send_keys(data)
        time.sleep(2)
        wait = WebDriverWait(var_stx_app.driver, 10)
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.select_searh)))
        except:
            var_stx_app.driver.find_element(By.XPATH, path_search_input).clear()
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, path_search_input).send_keys(data)
            time.sleep(2.5)
        name_location = var_stx_app.driver.find_element(By.XPATH, var_stx_app.select_searh).text
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.select_searh).click()
        time.sleep(2.5)

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc",
                                              path_check, name_location, name_image)



    def create_order_note(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_create_order)
        except:
            waiting_for_a_passenger.create_order(self, "", "", "")

        var_stx_app.driver.implicitly_wait(5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.create_order_note).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.create_order_note_input).clear()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.create_order_note_input).send_keys(var_stx_app.data['home_drive']['note'])
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.IGREE).click()
        time.sleep(2)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc",
                                              var_stx_app.check_create_order_note, var_stx_app.data['home_drive']['note'], "_TaoCuoc_GhiChu.png")



    def create_order_icon(self, code, eventname, result, path_icon, name_image):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_create_order)
        except:
            waiting_for_a_passenger.create_order(self, "", "", "")

        var_stx_app.driver.implicitly_wait(5)
        var_stx_app.driver.find_element(By.XPATH, path_icon).click()
        time.sleep(1)
        var_stx_app.driver.find_element(By.XPATH, path_icon).click()
        time.sleep(1)
        module_other_stx_app.write_result_displayed_try(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc",
                                              path_icon, name_image)

        if name_image == "_TaoCuoc_IconDenGiaoThong.png":
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.COME_BACK).click()
                time.sleep(2.5)
            except:
                pass







    def create_order_create_order(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        var_stx_app.driver.implicitly_wait(5)
        waiting_for_a_passenger.create_order_search(self, "", "", "", var_stx_app.create_order_location1,
                                                    var_stx_app.create_order_location1_input, "Ngõ 115 Định Công, TP. Hà Nội", "", "")

        waiting_for_a_passenger.create_order_search(self, "", "", "", var_stx_app.create_order_location2,
                                                    var_stx_app.create_order_location2_input, "Ngõ 433 Bạch Mai, TP. Hà Nội", "", "")

        waiting_for_a_passenger.create_order_note(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.CREATE_ORDER).click()
        time.sleep(1)
        wait = WebDriverWait(var_stx_app.driver, 10)
        time.sleep(1)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.DROP_OFF_PASSENGERS)))
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc",
                                              var_stx_app.DROP_OFF_PASSENGERS, "TRẢ KHÁCH", "_TaoCuoc_TaoCuoc.png")



    def create_order_see_route(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.DROP_OFF_PASSENGERS)
        except:
            waiting_for_a_passenger.create_order_create_order(self, "", "", "")

        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.create_order_see_route).click()
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.create_order_see_route1).click()
        time.sleep(2.5)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.see_route_back)))
        module_other_stx_app.write_result_displayed_try(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc",
                                              var_stx_app.see_route_back, "_TaoCuoc_XemLoTrinh.png")



    def create_order_see_route_icon(self, code, eventname, result, type, path_icon, name_image):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.see_route_back)
        except:
            waiting_for_a_passenger.create_order_see_route(self, "", "", "")

        var_stx_app.driver.implicitly_wait(5)
        if type == "0":
            module_other_stx_app.write_result_displayed_try(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Tạo cuốc - Xem lộ trình",
                                                            path_icon, name_image)

        if type == "1":
            var_stx_app.driver.find_element(By.XPATH, path_icon).click()
            time.sleep(1)
            module_other_stx_app.write_result_displayed_try(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Tạo cuốc - Xem lộ trình",
                                                  path_icon, name_image)


        if name_image == "_TaoCuoc_XemLoTrinh_IconDieuHuong.png":
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.see_route_back).click()
            time.sleep(2.2)



    def see_route_search_location2(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.see_route_search_location2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.see_route_back).click()
            time.sleep(2.2)
        except:
            pass
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.DROP_OFF_PASSENGERS)
        except:
            waiting_for_a_passenger.create_order_create_order(self, "", "", "")

        var_stx_app.driver.implicitly_wait(5)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.see_route_search_location2).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.see_route_search_location2_input).clear()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.see_route_search_location2_input).send_keys(var_stx_app.data['home_drive']['location2'])
        time.sleep(2)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.select_searh)))
        name_location = var_stx_app.driver.find_element(By.XPATH, var_stx_app.select_searh1).text
        data_location = var_stx_app.driver.find_element(By.XPATH, var_stx_app.select_searh2).text
        element.click()
        time.sleep(2.5)
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            location2_name = var_stx_app.driver.find_element(By.XPATH, var_stx_app.location2_name).text
            location2_data = var_stx_app.driver.find_element(By.XPATH, var_stx_app.location2_data).text

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Tên điểm     :{}\nĐịa chỉ điểm:{}".format(location2_name, location2_data))
            var_stx_app.logging.info("Tên điểm     :{}\nĐịa chỉ điểm:{}".format(location2_name, location2_data))
            if (location2_name == var_stx_app.data['home_drive']['location2'] == name_location) and (location2_data == data_location):
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_TaoCuoc_TaoCuoc_DiaChỉTra.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TaoCuoc_TaoCuoc_DiaChỉTra.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_TaoCuoc_TaoCuoc_DiaChỉTra.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TaoCuoc_TaoCuoc_DiaChỉTra.png")



    def see_route_drop_off_passengers(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.DROP_OFF_PASSENGERS)
        except:
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.see_route_back).click()
                time.sleep(2.2)
            except:
                pass
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.DROP_OFF_PASSENGERS)
        except:
            waiting_for_a_passenger.create_order_create_order(self, "", "", "")

        var_stx_app.driver.implicitly_wait(5)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.DROP_OFF_PASSENGERS).click()
        time.sleep(1)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.fee_move)))
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Trả khách",
                                              var_stx_app.fee_move, "Cước di chuyển", "_TaoCuoc_XemLoTrinh.png")



    def add_fee(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.fee_move)
        except:
            waiting_for_a_passenger.see_route_drop_off_passengers(self, "", "", "")

        var_stx_app.driver.implicitly_wait(5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.add_fee).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.ADD_FEE).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.add_fee_input).send_keys("15000")
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.IGREE).click()
        time.sleep(2)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Phụ phí",
                                              var_stx_app.check_add_fee, "15.000 ₫", "_TaoCuoc_ThemPhuPhi.png")



    def add_fee_edit(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_add_fee)
        except:
            waiting_for_a_passenger.add_fee(self, "", "", "")

        var_stx_app.driver.implicitly_wait(5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.add_fee_edit).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.add_fee_input).clear()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.add_fee_input).send_keys("20000")
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.IGREE).click()
        time.sleep(2)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Phụ phí",
                                              var_stx_app.check_add_fee, "20.000 ₫", "_TaoCuoc_ThemPhuPhi_Sua.png")



    def add_fee_delete(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_add_fee)
        except:
            waiting_for_a_passenger.add_fee_edit(self, "", "", "")

        var_stx_app.driver.implicitly_wait(5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.add_fee_delete).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
        time.sleep(2)
        module_other_stx_app.write_result_not_displayed_try(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Phụ phí",
                                              var_stx_app.check_add_fee, "_TaoCuoc_ThemPhuPhi_Xoa.png")


        var_stx_app.driver.find_element(By.XPATH, var_stx_app.ADD_FEE).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.add_fee_input).send_keys("15000")
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.IGREE).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.SAVE_FEE).click()
        time.sleep(2)



    def issue_invoices(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.fee_move)
        except:
            waiting_for_a_passenger.see_route_drop_off_passengers(self, "", "", "")

        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.issue_invoices).click()
            time.sleep(2.5)
            wait = WebDriverWait(var_stx_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.issue_invoices_company)))
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.issue_invoices_company).send_keys("Tiệm tạp hóa Bình An 1")
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.issue_invoices_tax).send_keys("41C8026288")
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.issue_invoices_email).send_keys("taphoabinhan1@gmail.com")
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.issue_invoices_address).send_keys("860 Đ. Kim Giang, Thanh Liệt, Thanh Trì, Hà Nội, Việt Nam")
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.CONFIRM).click()
            time.sleep(2)
            toast_element = var_stx_app.driver.find_element(By.XPATH, "//android.widget.Toast")
            print(toast_element.text)
        except:
            pass
        module_other_stx_app.write_result_text_try_if_toast(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Xuất hóa đơn điện tử",
                                              "", "Cập nhật thành công", "_TaoCuoc_XuatHoaDonDienTu.png")



    def cash(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.fee_move)
        except:
            waiting_for_a_passenger.see_route_drop_off_passengers(self, "", "", "")

        var_stx_app.driver.implicitly_wait(5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.CASH).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.homepage)))

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc",
                                              var_stx_app.homepage, "Trang chủ", "_TaoCuoc_TienMat.png")








    def card_pay_transfer(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage).click()
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")


        var_stx_app.driver.implicitly_wait(5)
        waiting_for_a_passenger.create_order_search(self, "", "", "", var_stx_app.create_order_location1,
                                                    var_stx_app.create_order_location1_input, "14 Nguyễn Cảnh Dị", "", "")

        waiting_for_a_passenger.create_order_search(self, "", "", "", var_stx_app.create_order_location2,
                                                    var_stx_app.create_order_location2_input, "40 Ngõ 40 Ta Quang Bửu", "", "")

        waiting_for_a_passenger.create_order_note(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.CREATE_ORDER).click()
        time.sleep(2.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.DROP_OFF_PASSENGERS).click()
        time.sleep(2)

        #Thêm phụ phí
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.add_fee).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.ADD_FEE).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.add_fee_input).send_keys("15000")
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.IGREE).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.SAVE_FEE).click()
        time.sleep(2)

        #Thêm hóa đơn
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.issue_invoices).click()
            time.sleep(2.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.issue_invoices_company).send_keys("Tiệm tạp hóa Bình An 2")
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.issue_invoices_tax).send_keys("41C8026299")
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.issue_invoices_email).send_keys("taphoabinhan2@gmail.com")
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.issue_invoices_address).send_keys("864 Đ. Kim Giang, Thanh Liệt, Thanh Trì, Hà Nội, Việt Nam")
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.CONFIRM).click()
            time.sleep(2.5)
        except:
            pass


        var_stx_app.driver.find_element(By.XPATH, var_stx_app.pttt1).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.pttt_transfer).click()
        time.sleep(2.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.money_clock_input).send_keys("106000")
        time.sleep(1.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
        time.sleep(2.3)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.payment).click()
        time.sleep(2.5)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Chuyển khoản",
                                              var_stx_app.check_card_pay_transfer, "Bạn chưa liên kết tài khoản ngân hàng nên chưa thể khởi tạo giao dịch", "_TaoCuoc_ChuyenKhoan.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(2.5)
        except:
            pass



    def card_pay_g7_check_info(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.pttt1)
        except:
            waiting_for_a_passenger.card_pay_transfer(self, "", "", "")


        var_stx_app.driver.implicitly_wait(5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.pttt1).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.pttt1_g7).click()
        time.sleep(2.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.money_clock_input).send_keys("106000")
        time.sleep(1.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
        time.sleep(2.3)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.payment).click()
        time.sleep(3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.ALLOW).click()
            time.sleep(3)
        except:
            pass
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.FILL_CODE_CARD).click()
        time.sleep(3)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.FILL_CODE_CARD_INPUT).send_keys("9999992992098174")
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm1).click()
        time.sleep(2.5)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_customer_card_code)
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(2.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.FILL_CODE_CARD_INPUT).clear()
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.FILL_CODE_CARD_INPUT).send_keys("9999920987715201")
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm1).click()
            time.sleep(2.5)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Quét thẻ thành viên G7 Taxi")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            info_customer_card_code = var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_customer_card_code).text
            info_customer_card_date = var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_customer_card_date).text
            info_customer_card_type = var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_customer_card_type).text
            info_customer_card_code_hd = var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_customer_card_code_hd).text
            info_customer_card_customer = var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_customer_card_customer).text
            info_customer_card_phone = var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_customer_card_phone).text
            info_customer_card_fee1 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_customer_card_fee1).text
            info_customer_card_fee2 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_customer_card_fee2).text

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Mã thẻ: {}\nNgày hết hạn: {}\nLoại thẻ: {}\nMã hợp đồng: {}\nKhách hàng: {}\nĐiện thoại: {}\nCước, phí chuyến đi: {}\nThu của khách: {}"
                                           .format(info_customer_card_code, info_customer_card_date, info_customer_card_type, info_customer_card_code_hd,
                                                   info_customer_card_customer, info_customer_card_phone, info_customer_card_fee1, info_customer_card_fee2))
            var_stx_app.logging.info("Mã thẻ: {}\nNgày hết hạn: {}\nLoại thẻ: {}\nMã hợp đồng: {}\nKhách hàng: {}\nĐiện thoại: {}\nCước, phí chuyến đi: {}\nThu của khách: {}"
                                           .format(info_customer_card_code, info_customer_card_date, info_customer_card_type, info_customer_card_code_hd,
                                                   info_customer_card_customer, info_customer_card_phone, info_customer_card_fee1, info_customer_card_fee2))
            if (info_customer_card_code != "") and (info_customer_card_date != "") and (info_customer_card_type != "") and (info_customer_card_code_hd != "") \
                and (info_customer_card_customer != "") and (info_customer_card_phone != "") and (info_customer_card_fee1 != "") and (info_customer_card_fee2 != ""):

                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_TaoCuoc_TheG7_CheckThongTin.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TaoCuoc_TheG7_CheckThongTin.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_TaoCuoc_TheG7_CheckThongTin.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_TaoCuoc_TheG7_CheckThongTin.png")



    def collected_from_customers(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_customer_card_code)
        except:
            waiting_for_a_passenger.card_pay_g7_check_info(self, "", "", "")


        var_stx_app.driver.implicitly_wait(5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.collected_from_customers).click()
        time.sleep(2.5)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Quét thẻ thành viên G7 Taxi",
                                              var_stx_app.check_collected_from_customers, "Chi tiết thanh toán", "_TaoCuoc_ThuCuaKhach.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.collected_from_customers_back).click()
            time.sleep(2)
        except:
            pass



    def pay_card(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.info_customer_card_code)
        except:
            waiting_for_a_passenger.card_pay_g7_check_info(self, "", "", "")


        var_stx_app.driver.implicitly_wait(5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.PAY_CARD).click()
        time.sleep(2.5)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_pay_card)))
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Tạo cuốc - Quét thẻ thành viên G7 Taxi",
                                              var_stx_app.check_pay_card, "Bạn đã thanh toán thành công", "_TaoCuoc_ThanhToanThe.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(2)
        except:
            pass
        module_other_stx_app.close_app()












    def order_fixed(self, type, address):
        var_stx_app.driver.implicitly_wait(10)
        # module_other_stx_app.close_app()
        if type == "1":
            pass
            # login_stx_app.driver_g7.logout_driver_g7(self)

        try:
            module_other_stx_app.click_app("Lái xe G7")
            time.sleep(1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification)
        except:
            home_page.status_driver(self, "Xe sân bay", "SẴN SÀNG")


        try:
            module_other_stx_app.click_app("G7 Taxi")
            time.sleep(1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.promotion)
        except:
            login_stx_app.g7.login_g7(self, "0359667694")
        homepage_g7.home_page.choose_location(self, address)



    def check_order_fixed(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        waiting_for_a_passenger.order_fixed(self, "1", "120 Phố Chùa Láng, phường Láng Thượng, quận Đống Đa, thành phố Hà Nội")

        homepage_g7.select_type_car("7 Chỗ")

        # var_stx_app.driver.find_element(By.XPATH, var_stx_app.car_7_sit).click()
        # time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.pttt).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.CASH).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_car_app).click()
        time.sleep(2.5)
        wait = WebDriverWait(var_stx_app.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.RECEIVE_APP)))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            order_fixed_location_from = var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_fixed_location_from).text
            order_fixed_location_to = var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_fixed_location_to).text
            order_fixed_money = var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_fixed_money).text
            order_fixed_note = var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_fixed_note).text

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Địa chỉ đón: {}\nĐịa chỉ trả: {}\nCước chuyến đi: {}\nGhi chú: {}"
                                           .format(order_fixed_location_from, order_fixed_location_to, order_fixed_money, order_fixed_note))
            var_stx_app.logging.info("Địa chỉ đón: {}\nĐịa chỉ trả: {}\nCước chuyến đi: {}\nGhi chú: {}"
                                           .format(order_fixed_location_from, order_fixed_location_to, order_fixed_money, order_fixed_note))

            if (order_fixed_location_from != "") and (order_fixed_location_to != "") and (order_fixed_money != "") and (order_fixed_note != ""):
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_Cuoc_Fixed_CheckThongTin.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_Cuoc_Fixed_CheckThongTin.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_Cuoc_Fixed_CheckThongTin.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_Cuoc_Fixed_CheckThongTin.png")




    def order_fixed_refuse(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.REFUSE)
        except:
            waiting_for_a_passenger.order_fixed(self, "0", "120 Phố Chùa Láng, phường Láng Thượng, quận Đống Đa, thành phố Hà Nội")
            homepage_g7.select_type_car("7 Chỗ")

            # var_stx_app.driver.find_element(By.XPATH, var_stx_app.car_7_sit).click()
            # time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.pttt).click()
            time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.CASH).click()
            time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_car_app).click()
            time.sleep(2.5)
            wait = WebDriverWait(var_stx_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.REFUSE)))

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.REFUSE).click()
        time.sleep(3)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_order_fixed_refuse)))

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH",
                                              var_stx_app.check_order_fixed_refuse, "Bạn đã từ chối thành công", "_Cuoc_Fixed_TuChoi.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(2)
        except:
            pass



    def order_fixed_receive_app(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            module_other_stx_app.click_app("G7 Taxi")
            time.sleep(1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.RESET_ORDER_CAR).click()
            time.sleep(3)
        except:
            waiting_for_a_passenger.order_fixed(self, "0", "120 Phố Chùa Láng, phường Láng Thượng, quận Đống Đa, thành phố Hà Nội")
            homepage_g7.select_type_car("7 Chỗ")

            # var_stx_app.driver.find_element(By.XPATH, var_stx_app.car_7_sit).click()
            # time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.pttt).click()
            time.sleep(2)
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.CASH).click()
            except:
                time.sleep(2)
                var_stx_app.driver.tap([(200, 1300)])
                time.sleep(0.5)
                var_stx_app.driver.tap([(200, 1300)])
                time.sleep(2)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.CASH).click()
            time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_car_app).click()
            time.sleep(2.5)

        wait = WebDriverWait(var_stx_app.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.RECEIVE_APP)))
        element.click()
        time.sleep(2.5)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            overview_order_fixed_location = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_order_fixed_location).text
            overview_order_fixed_type = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_order_fixed_type).text
            overview_order_fixed_detail = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_order_fixed_detail).text
            overview_order_fixed_location_vehicle = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_order_fixed_location_vehicle).text
            overview_order_fixed_phone = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_order_fixed_phone).text

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Địa chỉ đón: {}\nLoại cuốc: {}\nbutton 1: {}\nbutton 2: {}\nSố điện thoại: {}"
                                           .format(overview_order_fixed_location, overview_order_fixed_type, overview_order_fixed_detail, overview_order_fixed_location_vehicle,
                                                   overview_order_fixed_phone))

            var_stx_app.logging.info("Địa chỉ đón: {}\nLoại cuốc: {}\nbutton 1: {}\nbutton 2: {}\nSố điện thoại: {}"
                                           .format(overview_order_fixed_location, overview_order_fixed_type, overview_order_fixed_detail, overview_order_fixed_location_vehicle,
                                                   overview_order_fixed_phone))

            if (overview_order_fixed_location != "") and (overview_order_fixed_type == "Cuốc fixed theo AppKH") and (overview_order_fixed_detail == "Xem chi tiết") \
                    and (overview_order_fixed_location_vehicle == "Vị trí xe") and (overview_order_fixed_phone != ""):

                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_Cuoc_Fixed_NhanApp.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_Cuoc_Fixed_NhanApp.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_Cuoc_Fixed_NhanApp.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_Cuoc_Fixed_NhanApp.png")



    def order_fixed_see_detail(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.see_detail)
        except:
            waiting_for_a_passenger.order_fixed_receive_app(self, "", "", "")




        #OVERVIEW
        try:
            overview1_location_from = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview1_location_from).text  #địa chỉ đón
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 55, 2, overview1_location_from)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 55, 2, "")


        try:
            overview1_origin = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview1_origin).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 56, 2, overview1_origin)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 56, 2, "")

        try:
            overview1_phone = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview1_phone).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 57, 2, overview1_phone)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 57, 2, "")


        #DETAIL
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.see_detail).click()
        time.sleep(3)
        try:
            detail1_location_from = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail1_location_from).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 55, 3, detail1_location_from)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 55, 3, "")

        try:
            detail1_location_to = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail1_location_to).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 58, 3, detail1_location_to)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 58, 3, "")

        try:
            detail1_money = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail1_money).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 59, 3, detail1_money)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 59, 3, "")

        try:
            detail1_note = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail1_note).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 60, 3, detail1_note)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 60, 3, "")

        try:
            detail1_pttt = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail1_pttt).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 61, 3, detail1_pttt)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 61, 3, "")

        try:
            detail1_origin = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail1_origin).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 56, 3, detail1_origin)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 56, 3, "")

        try:
            detail1_phone = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail1_phone).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 57, 3, detail1_phone)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 57, 3, "")

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc - Cuốc fixed theo AppKH - Xem chi tiết",
                                              var_stx_app.check_order_fixed_see_detail1, "Ghi chú", "_Cuoc_Fixed_XemChiTiet.png")



    def detail_if(self, code, eventname, result, row, name):
        var_stx_app.driver.implicitly_wait(5)
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", row, 2))
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", row, 3))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc - Cuốc fixed theo AppKH - Xem chi tiết")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info(name+"(Thông tin cuốc): {}".format(overview))
        var_stx_app.logging.info(name+"(Xem chi tiết): {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Thông tin cuốc: {}\nXem chi tiết: {}".format(overview, detail))
        if overview == detail:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def detail_other(self, code, eventname, result, row, name):
        var_stx_app.driver.implicitly_wait(5)
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", row, 3))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc - Cuốc fixed theo AppKH - Xem chi tiết")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info(name+"(Xem chi tiết): {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, name+"(Xem chi tiết): {}".format(detail))
        if detail != "None":
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")



    def detail_note(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_order_fixed_see_detail)
        except:
            waiting_for_a_passenger.order_fixed_see_detail(self, "", "", "")


        var_stx_app.driver.find_element(By.XPATH, var_stx_app.see_detail_note).click()
        time.sleep(2.5)
        note = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_note).text
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_note_back).click()
        time.sleep(2.5)
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 60, 3))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Xem chi tiết: {}\nHộp thoại ghi chú: {}".format(note, detail))
            var_stx_app.logging.info("Xem chi tiết: {}\nHộp thoại ghi chú: {}".format(note, detail))
            if note == detail:
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_Cuoc_Fixed_XemChiTiet_GhiChu.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_Cuoc_Fixed_XemChiTiet_GhiChu.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_Cuoc_Fixed_XemChiTiet_GhiChu.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_Cuoc_Fixed_XemChiTiet_GhiChu.png")



    def detail_cancel(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.CANCEL)
        except:
            waiting_for_a_passenger.order_fixed_see_detail(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.CANCEL).click()
        time.sleep(2.5)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.reasson_other).click()
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.reasson_other1).click()
            time.sleep(2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.reasson_other1_input).send_keys("Trường test huy cuốc lái xe")
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.IGREE).click()
        time.sleep(3)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_detail_cancel)))

        module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH",
                                              var_stx_app.check_detail_cancel, '', "_Cuoc_Fixed_HuyBo.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(2.5)
        except:
            pass
        try:
            module_other_stx_app.click_app("G7 Taxi")
            time.sleep(1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(2.5)
        except:
            pass
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_car_back).click()
            time.sleep(2.5)
        except:
            pass



    def order_fixed_location(self, code, eventname, result, desire, name_image):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.see_detail)
        except:
            waiting_for_a_passenger.order_fixed_receive_app(self, "", "", "")

        name_button = var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_fixed_location_button).text
        print("Trước: {}:".format(name_button))
        if name_button == desire:
            pass
        else:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_fixed_location_button).click()
            time.sleep(2)
        name_button = var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_fixed_location_button).text
        print("Sau: {}:".format(name_button))
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH - Vị trí",
                                              var_stx_app.order_fixed_location_button, name_button, name_image)



    def order_fixed_see_customer(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.see_detail)
        except:
            waiting_for_a_passenger.order_fixed_receive_app(self, "", "", "")
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.SEE_CUSTOMER).click()     #Chỉ chạy sever test
            time.sleep(2.5)
        except:
            pass
        module_other_stx_app.write_result_not_displayed_try(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH - Xác nhận tiền thanh toán",
                                              var_stx_app.SEE_CUSTOMER, "_XacNhanTienThanhToan.png")



    def check_info_confirm_pay_money(self, code, eventname, result, path_check, name_image):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        # try:
        #     var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm_pay_money)      #Ch chạy sever test
        # except:
        #     waiting_for_a_passenger.order_fixed_see_customer(self, "", "", "")

        module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH - Xác nhận tiền thanh toán",
                                              path_check, "", name_image)



    def confirm_pay_money_note(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        # try:
        #     var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm_pay_money)
        # except:
        #     waiting_for_a_passenger.order_fixed_see_customer(self, "", "", "")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm_pay_money_note_icon).click()      #Chỉ chạy sever test
            time.sleep(2.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm_pay_money_note_input).clear()
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm_pay_money_note_input).send_keys(var_stx_app.data['home_drive']['note1'])
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.IGREE).click()
            time.sleep(2.5)
        except:
            pass
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH - Xác nhận tiền thanh toán",
                                              var_stx_app.check_confirm_pay_money_note, var_stx_app.data['home_drive']['note1'], "_XacNhanTienThanhToan_GhiChu.png")



    def confirm_pay_money_confirm(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        # try:
        #     var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm_pay_money)
        # except:
        #     waiting_for_a_passenger.order_fixed_see_customer(self, "", "", "")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.CONFIRM).click()      #Chỉ chạy sever test
            time.sleep(2)
            wait = WebDriverWait(var_stx_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.call_customer)))
        except:
            pass

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH - Xác nhận tiền thanh toán",
                                              var_stx_app.call_customer, "Gọi khách hàng:", "_XacNhanTienThanhToan_XacNhan.png")



    def check_confirm_pay_money_confirm(self, code, eventname, result, path_check, name_image):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.call_customer)
        except:
            waiting_for_a_passenger.order_fixed_see_customer(self, "", "", "")

        module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH - G7 Taxi Hà Nội",
                                              path_check, "", name_image)



    def electronic_contract(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.call_customer)
        except:
            waiting_for_a_passenger.order_fixed_see_customer(self, "", "", "")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.electronic_contract).click()
            time.sleep(2)
            wait = WebDriverWait(var_stx_app.driver, 12)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_electronic_contract)))
        except:
            pass

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH - G7 Taxi Hà Nội",
                                              var_stx_app.check_electronic_contract, "HỢP ĐỒNG VẬN CHUYỂN HÀNH KHÁCH", "_Fixed_HopDongDienTu.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.electronic_contract_back).click()
            time.sleep(2)
        except:
            pass



    def wrong_customer(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.call_customer)
        except:
            waiting_for_a_passenger.order_fixed_see_customer(self, "", "", "")




        var_stx_app.driver.find_element(By.XPATH, var_stx_app.WRONG_CUSTOMER).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
        time.sleep(2)
        try:
            wait = WebDriverWait(var_stx_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_wrong_customer)))
        except:
            pass

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH - G7 Taxi Hà Nội",
                                              var_stx_app.check_wrong_customer, "Thông tin nhầm khách đã được gửi lên điều hành", "_Fixed_NhamKhach.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(2.5)
        except:
            pass



    def wrong_customer_return_guests(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.RETURN_GUESTS)
        except:
            waiting_for_a_passenger.wrong_customer(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.RETURN_GUESTS).click()
        time.sleep(2.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.CASH).click()
        time.sleep(2.5)
        try:
            wait = WebDriverWait(var_stx_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.homepage)))
        except:
            pass

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH - G7 Taxi Hà Nội",
                                              var_stx_app.homepage, "Trang chủ", "_Fixed_NhamKhach_TraKhach.png")

        try:
            module_other_stx_app.click_app("G7 Taxi")
            time.sleep(1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(2.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.order_car_back).click()
            time.sleep(2.5)
        except:
            pass






    def return_guests(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(0.3)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.RETURN_GUESTS)
        except:
            waiting_for_a_passenger.order_fixed_see_customer(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.RETURN_GUESTS).click()
        time.sleep(2.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.CASH).click()
        time.sleep(2)
        try:
            wait = WebDriverWait(var_stx_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.homepage)))
        except:
            pass

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trang Chủ(Lái xe g7) - Chờ cuốc -  Cuốc fixed theo AppKH - G7 Taxi Hà Nội",
                                              var_stx_app.homepage, "Trang chủ", "_Fixed_TraKhach.png")
        module_other_stx_app.close_app()





class notification:


    def notification(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage).click()
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_dash_3).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification1).click()
        time.sleep(2)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Thông báo(Lái xe)",
                                              var_stx_app.personal, "Cá nhân", "_ThongBao.png")



    def notification_search(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.personal)
        except:
            notification.notification(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification_search_icon).click()
        time.sleep(2)
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Thông báo(Lái xe)")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            notification_fromday = var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification_fromday).text
            notification_today = var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification_today).text
            notification_input = var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification_input).text

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Từ ngày: {}\nĐến ngày: {}\ninput: {}".
                                           format(notification_fromday, notification_today, notification_input))
            var_stx_app.logging.info("Từ ngày: {}\nĐến ngày: {}\ninput: {}".
                                           format(notification_fromday, notification_today, notification_input))

            if (notification_fromday != "") and (notification_today != "") and (notification_input == "Nhập tiêu đề tìm kiếm"):
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_ThongBao_TimKiem.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_ThongBao_TimKiem.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_ThongBao_TimKiem.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_ThongBao_TimKiem.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification_search_icon).click()
            time.sleep(2)
        except:
            pass



    def check_info_notification(self, code, eventname, result, path_button, type, name_image):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.personal)
        except:
            notification.notification_search(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, path_button).click()
        time.sleep(2.5)
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Thông báo(Lái xe)")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        if type == "0":
            try:
                notification_name = var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification_name).text
                notification_date = var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification_date).text
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Tên thông báo: {}\nNgày thông báo: {}". format(notification_name, notification_date))
                var_stx_app.logging.info("Tên thông báo: {}\nNgày thông báo: {}".format(notification_name, notification_date))

                if (notification_name != "") and (notification_date != ""):
                    var_stx_app.logging.info("True")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    var_stx_app.logging.info("False")
                    var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + name_image)
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)
            except:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + name_image)
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)

        if type == "1":
            try:
                not_result = var_stx_app.driver.find_element(By.XPATH, var_stx_app.not_result).text
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, not_result)
                var_stx_app.logging.info(not_result)
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            except:
                notification_name = var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification_name).text
                notification_date = var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification_date).text
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Tên thông báo: {}\nNgày thông báo: {}". format(notification_name, notification_date))
                var_stx_app.logging.info("Tên thông báo: {}\nNgày thông báo: {}".format(notification_name, notification_date))

                if (notification_name != "") and (notification_date != ""):
                    var_stx_app.logging.info("True")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
                else:
                    var_stx_app.logging.info("False")
                    var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + name_image)
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                    module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + name_image)



    def check_info_notification_detail(self, code, eventname, result, path_button, name_image):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.personal)
        except:
            notification.notification_search(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, path_button).click()
        time.sleep(2.5)

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification_detail).click()
            time.sleep(1)
            wait = WebDriverWait(var_stx_app.driver, 5)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_info_notification_detail)))
            time.sleep(0.5)
        except:
            pass

        module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Thông báo(Lái xe) - Chi tiết",
                                              var_stx_app.check_info_notification_detail, "", name_image)

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification_detail_back).click()
            time.sleep(2)
        except:
            pass

        if name_image == "_ThongBao_QuanTrong_ChiTiet.png":
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.notification_back1).click()
                time.sleep(2)
            except:
                pass





class history:


    def history(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage).click()
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_dash_3).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.history1).click()
        time.sleep(2)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Lịch sử(Lái xe)",
                                              var_stx_app.check_history1, "Lịch sử", "_LichSu.png")



    def history_calendar(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_history1)
        except:
            history.history(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_calendar).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.in_30day).click()
        time.sleep(1)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.history_detail_day)))

        module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Lịch sử(Lái xe) - Tìm kiếm",
                                              var_stx_app.history_detail_day, "", "_LichSu.png")
        time.sleep(1)



    def history_detail_status(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_detail_day)
        except:
            history.history_calendar(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_detail_status_icon).click()
        time.sleep(2)
        var_stx_app.driver.tap([(100, 500)])
        time.sleep(2.5)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Lịch sử(Lái xe) - Tìm kiếm",
                                              var_stx_app.history_detail_status, "Hoàn thành", "_LichSu_ChiTiet_TrangThai.png")



    def get_info_history_detail(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_detail_day)
        except:
            history.history_detail_status(self, "", "", "")



        overview_history_day = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_history_day).text
        module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 65, 2, overview_history_day)


        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_history_location2a)      #check có dòng thứ 6 không

            try:
                overview_history_time = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_history_time).text
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 66, 2, overview_history_time)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 66, 2, "")

            try:
                overview_history_money = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_history_money).text
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 67, 2, overview_history_money)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 67, 2, 0)

            try:
                overview_history_origin = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_history_origin).text
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 68, 2, overview_history_origin)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 68, 2, "")

            try:
                overview_history_pttt = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_history_pttt).text
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 69, 2, overview_history_pttt)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 69, 2, "")

            try:
                overview_history_status = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_history_status).text
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 70, 2, overview_history_status)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 70, 2, "")

            try:
                overview_history_note = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_history_note).text
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 71, 2, overview_history_note)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 71, 2, "")

            try:
                overview_history_location1a = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_history_location1a).text
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 72, 2, overview_history_location1a)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 72, 2, "")

            try:
                overview_history_location2a = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_history_location2a).text
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 73, 2, overview_history_location2a)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 73, 2, "")


        except:
            overview_history_time = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_history_time).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 66, 2, overview_history_time)

            try:
                overview_history_money = var_stx_app.driver.find_element(By.XPATH,var_stx_app.overview_history_money).text
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 67, 2, overview_history_money)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 67, 2, 0)

            try:
                overview_history_origin1 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_history_origin1).text
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 68, 2, overview_history_origin1)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 68, 2, "")

            try:
                overview_history_pttt1 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_history_pttt1).text
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 69, 2, overview_history_pttt1)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 69, 2, "")

            try:
                overview_history_status = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_history_status).text
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 70, 2, overview_history_status)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 70, 2, "")

            try:
                overview_history_note1 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_history_note1).text
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 71, 2, overview_history_note1)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 71, 2, "")

            try:
                overview_history_location1b = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_history_location1b).text
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 72, 2, overview_history_location1b)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 72, 2, "")

            try:
                overview_history_location2b = var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_history_location2b).text
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 73, 2, overview_history_location2b)
            except:
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 73, 2, "")






        #Detail
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.overview_history_time).click()
        time.sleep(3)

        try:
            detail_history_location1 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_history_location1).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 72, 3, detail_history_location1)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 72, 3, "")

        try:
            detail_history_location2 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_history_location2).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 73, 3, detail_history_location2)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 73, 3, "")

        try:
            detail_history_time = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_history_time).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 77, 3, detail_history_time)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 77, 3, "")


        try:
            detail_history_pttt = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_history_pttt).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 69, 3, detail_history_pttt)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 69, 3, "")

        try:
            detail_history_status = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_history_status).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 70, 3, detail_history_status)
        except:
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 70, 3, "")


        var_stx_app.driver.swipe(350, 900, 350, 500, 1000)
        time.sleep(1)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_detail_history_note)
            detail_history_note = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_history_note_a).text
            module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 71, 3, detail_history_note)
        except:
            try:
                detail_history_note = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_history_note).text
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 71, 3, detail_history_note)
            except:
                detail_history_note1 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_history_note1).text
                module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 71, 3, detail_history_note1)



        select_detail("Cước di chuyển", 74)
        select_detail("phụ phí 1", 75)
        select_detail("KH thanh toán", 76)
        select_detail("Khung giờ", 78)


        # #Cước di chuyển
        # try:
        #     detail_history_fee1 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_history_fee1).text
        #     module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 74, 3, detail_history_fee1)
        # except:
        #     try:
        #         detail_history_fee1 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_history_fee1b).text
        #         module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 74, 3, detail_history_fee1)
        #     except:
        #         module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 74, 3, 0)
        #
        # #Phụ phí
        # try:
        #     detail_history_fee2 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_history_fee2).text
        #     module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 75, 3, detail_history_fee2)
        # except:
        #     try:
        #         detail_history_fee2b = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_history_fee2b).text
        #         module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 75, 3, detail_history_fee2b)
        #     except:
        #         pass
        #     module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 75, 3, 0)


        # try:
        #     var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_detail_history_time2)
        #     detail_history_time2 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_history_time2).text
        #     module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 78, 3, detail_history_time2)
        # except:
        #     module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 78, 3, 0)

        # try:
        #     detail_history_kh_pay = var_stx_app.driver.find_element(By.XPATH, var_stx_app.detail_history_kh_pay).text
        #     module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 76, 3, detail_history_kh_pay)
        # except:
        #     try:
        #         detail_history_kh_pay = var_stx_app.driver.find_element(By.XPATH,var_stx_app.detail_history_kh_pay1).text
        #         module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 76, 3, detail_history_kh_pay)
        #     except:
        #         module_other_stx_app.writeData1(var_stx_app.path_luutamthoi, "Sheet1", 76, 3, 0)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Lịch sử(Lái xe) - Tìm kiếm")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("True")
        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")



    def check_info_history_other(self, code, eventname, result, row, column):
        data = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", row, column))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Lịch sử(Lái xe) - Chi tiết - Thông tin cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("{}".format(data))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "{}".format(data))
        if data != "None":
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_LichSu_ThongTinCuoc.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_LichSu_ThongTinCuoc.png")



    def check_info_history_if(self, code, eventname, result, row1, column1, row2, column2):
        overview = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", row1, column1))
        detail = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", row2, column2))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Lịch sử(Lái xe) - Chi tiết - Thông tin cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Lịch sử cuốc  : {}".format(overview))
        var_stx_app.logging.info("Thông tin cuốc: {}".format(detail))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Lịch sử cuốc  : {}\nThông tin cuốc: {}".format(overview, detail))
        if overview == detail:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_LichSu_ThongTinCuoc.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_LichSu_ThongTinCuoc.png")



    def check_info_history_time(self, code, eventname, result):
        day = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 65, 2))
        time = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 66, 2))
        fulltime = time+"-"+day
        fulltime1 = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 77, 3))

        print("time1: {}".format(fulltime))
        print("time2: {}".format(fulltime1))

        dt1 = datetime.strptime(fulltime, "%H:%M-%d-%m-%Y")  # Dùng dấu '-'
        dt2 = datetime.strptime(fulltime1, "%H:%M-%d/%m/%Y")  # Dùng dấu '/'

        # So sánh
        print(dt1 == dt2)

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Lịch sử(Lái xe) - Chi tiết - Thông tin cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Giờ:Phút          : {}".format(time))
        var_stx_app.logging.info("Ngày - Tháng - Năm: {}".format(day))
        var_stx_app.logging.info("Thời gian         : {}".format(fulltime1))
        var_stx_app.logging.info(fulltime)

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Giờ:Phút          : {}\nNgày - Tháng - Năm: {}\nThời gian         : {}"
                                       .format(time, day, fulltime1))
        if dt1 == dt2:
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_LichSu_ThongTinCuoc.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_LichSu_ThongTinCuoc.png")



    def check_info_history_other1(self, code, eventname, result, row, column):
        data = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", row, column))

        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Lịch sử(Lái xe) - Chi tiết - Thông tin cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("{}".format(data))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "{}".format(data))
        if data != "None":
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")



    def check_info_history_pay(self, code, eventname, result):
        fee_move = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 74, 3))
        fee_move = ''.join(re.findall(r'\d+', fee_move))
        fee_move = int(fee_move)

        fee = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 75, 3))
        fee = ''.join(re.findall(r'\d+', fee))
        fee = int(fee)


        kh_pay = str(module_other_stx_app.readData(var_stx_app.path_luutamthoi, "Sheet1", 76, 3))
        kh_pay = ''.join(re.findall(r'\d+', kh_pay))
        kh_pay = int(kh_pay)


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Lịch sử(Lái xe) - Chi tiết - Thông tin cuốc")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        var_stx_app.logging.info("Cước di chuyển: {}".format(fee_move))
        var_stx_app.logging.info("Phụ phí       : {}".format(fee))
        var_stx_app.logging.info("KH Thanh toán : {}".format(kh_pay))

        module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Cước di chuyển: {}\nPhụ phí       : {}\nKH Thanh toán : {}"
                                       .format(fee_move, fee, kh_pay))
        print(kh_pay)
        print(type(kh_pay))
        print(fee_move)
        print(type(fee_move))
        print(fee)
        print(type(fee))
        if kh_pay == (fee_move + fee):
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        else:
            var_stx_app.logging.info("False")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_LichSu_ThongTinCuoc.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_LichSu_ThongTinCuoc.png")



    def history_detail_qr(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.status)
        except:
            history.get_info_history_detail(self, "", "", "")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.CODE_QRPAY).click()
        except:
            var_stx_app.driver.swipe(350, 900, 350, 500, 1000)
            time.sleep(1)
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.CODE_QRPAY).click()
            except:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_detail_qr_back).click()
                time.sleep(2)

        time.sleep(2.5)
        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Lịch sử(Lái xe) - Thông tin cuốc, Mã QR")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_history_detail_qr).is_displayed()
            var_stx_app.logging.info("True")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
        except NoSuchElementException:
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_LichSu_ThongTinCuoc_MaQr.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_LichSu_ThongTinCuoc_MaQr.png")

        var_stx_app.driver.press_keycode(4)
        time.sleep(2)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.history_detail_qr_back).click()
            time.sleep(2)
        except:
            pass





    def statistical(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_history1)
        except:
            history.history_calendar(self, "", "", "")


        var_stx_app.driver.find_element(By.XPATH, var_stx_app.statistical).click()
        time.sleep(2.5)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Lịch sử(Lái xe) - THỐNG KÊ",
                                              var_stx_app.check_statistical, "Tổng cuốc", "_LichSu_ThongKe.png")



    def statistical_sum_order(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_statistical)
        except:
            history.statistical(self, "", "", "")


        var_stx_app.logging.info("--------------")
        var_stx_app.logging.info("Lịch sử(Lái xe) - THỐNG KÊ")
        var_stx_app.logging.info("Mã - " + code)
        var_stx_app.logging.info("Tên sự kiện - " + eventname)
        var_stx_app.logging.info("Kết quả - " + result)
        try:
            statistical1 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.statistical1).text
            statistical2 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.statistical2).text
            statistical3 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.statistical3).text
            statistical4 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.statistical4).text
            statistical5 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.statistical5).text
            statistical6 = var_stx_app.driver.find_element(By.XPATH, var_stx_app.statistical6).text
            statistical_sum = var_stx_app.driver.find_element(By.XPATH, var_stx_app.statistical_sum).text

            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 6, "Hoàn thành: {}\nQuá giờ không nhận: {}\nTừ chối: {}\nHủy: {}"
                                                                                            "\nNhầm khách: {}\nKhông được chọn: {}\nTổng cuốc: {}"
                                           .format(statistical1, statistical2, statistical3, statistical4, statistical5, statistical6, statistical_sum))
            var_stx_app.logging.info("Hoàn thành: {}\nQuá giờ không nhận: {}\nTừ chối: {}\nHủy: {}"
                                            "\nNhầm khách: {}\nKhông được chọn: {}\nTổng cuốc: {}"
                                           .format(statistical1, statistical2, statistical3, statistical4, statistical5, statistical6, statistical_sum))

            if (int(statistical1) + int(statistical2) + int(statistical3) + int(statistical4) + int(statistical5) + int(statistical6)) == int(statistical_sum):
                var_stx_app.logging.info("True")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Pass")
            else:
                var_stx_app.logging.info("False")
                var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_LichSu_ThongKe_TongCuoc.png")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
                module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_LichSu_ThongKe_TongCuoc.png")
        except:
            var_stx_app.logging.info("False")
            var_stx_app.driver.save_screenshot(var_stx_app.imagepath + code + "_LichSu_ThongKe_TongCuoc.png")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 7, "Fail")
            module_other_stx_app.writeData(var_stx_app.checklistpath, "Checklist", code, 13, code + "_LichSu_ThongKe_TongCuoc.png")



    def check_statistical_other(self, code, eventname, result, path_check, name_image):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_statistical)
        except:
            history.statistical(self, "", "", "")


        module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Lịch sử(Lái xe) - THỐNG KÊ",
                                              path_check, "", name_image)

        if name_image == "_LichSu_ThongKe_KhongDuocChon.png":
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.history1_back).click()
            time.sleep(2.5)






class account_wallet:


    def account_wallet(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage).click()
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_dash_3).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_wallet).click()
        time.sleep(2)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Ví tài khoản(Lái xe)",
                                              var_stx_app.check_account_wallet, "Ví tài khoản", "_ViTaiKhoan.png")



    def account_wallet_calendar(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_account_wallet)
        except:
            account_wallet.account_wallet(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_wallet_calendar).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.in_30day).click()
        time.sleep(1)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.account_wallet_balance2)))

        module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Ví tài khoản(Lái xe)",
                                              var_stx_app.account_wallet_balance2, "", "_ViTaiKhoan_Loc.png")
        time.sleep(1)



    def check_info_account_wallet_other(self, code, eventname, result, path_check, name_image):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_wallet_balance2)
        except:
            account_wallet.account_wallet_calendar(self, "", "", "")

        module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Ví tài khoản(Lái xe) - Check thông tin",
                                              path_check, "", name_image)


        if name_image == "_ViTaiKhoan_GhiChu.png":
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.account_wallet_back).click()
            time.sleep(2.5)





class cash_wallet:


    def cash_wallet(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage).click()
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_dash_3).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.cash_wallet).click()
        time.sleep(2)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Ví tiền mặt(Lái xe)",
                                              var_stx_app.check_cash_wallet, "Ví tiền mặt", "_ViTienMat.png")



    def cash_wallet_calendar(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_account_wallet)
        except:
            cash_wallet.cash_wallet(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.cash_wallet_calendar).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.in_30day).click()
        time.sleep(1)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.cash_wallet_balance1)))

        module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Ví tiền mặt(Lái xe)",
                                              var_stx_app.cash_wallet_balance1, "", "_ViTienMat_Loc.png")
        time.sleep(1)



    def cash_wallet_transfer_money(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.cash_wallet_balance2)
        except:
            cash_wallet.cash_wallet_calendar(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.TRANSFER_MONEY).click()
        time.sleep(2.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.TRANSFER_MONEY_input).clear()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.TRANSFER_MONEY_input).send_keys("10000")
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.CONFIRM_TRANSFER_MONEY).click()
        time.sleep(2.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.cash_confirm).click()
        time.sleep(2)
        try:
            wait = WebDriverWait(var_stx_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.cash_wallet_money)))
            time.sleep(1)
        except:
            pass
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Ví tiền mặt(Lái xe) - Chuyển tiền",
                                              var_stx_app.cash_wallet_money, ": 10.000 ₫", "_ViTienMat_ChuyenTien.png")

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.CONFIRM_TRANSFER_MONEY)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.cash_wallet_transfer_money_back).click()
            time.sleep(2.5)
        except:
            pass




    def check_info_cash_wallet_other(self, code, eventname, result, path_check, name_image):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass


        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.cash_wallet_money)
        except:
            cash_wallet.cash_wallet_calendar(self, "", "", "")

        module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Ví tin mặt(Lái xe) - Check thông tin",
                                              path_check, "", name_image)

        if name_image == "_ViTienMat_GhiChu.png":
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.cash_wallet_back).click()
            time.sleep(2.5)





class trip_payment:


    def trip_payment(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage).click()
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_dash_3).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.trip_payment).click()
        time.sleep(2)
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Thanh toán chuyến đi(Lái xe)",
                                              var_stx_app.check_trip_payment, "Thanh toán chuyến đi", "_ThanhToanChuyenDi.png")



    def trip_payment_address(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_trip_payment)
        except:
            trip_payment.trip_payment(self, "", "", "")

        module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Thanh toán chuyến đi(Lái xe)",
                                              var_stx_app.trip_payment_address1, "", "_ThanhToanChuyenDi_DiaChi.png")



    def trip_payment_qr_drive(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_trip_payment)
        except:
            trip_payment.trip_payment(self, "", "", "")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.trip_payment_input).click()
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.trip_payment_input_a).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.trip_payment_input1).clear()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.trip_payment_input1).send_keys("25000")
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.continue2).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.qr_drive).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.payment).click()
        time.sleep(2)

        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_trip_payment_qr_drive)))

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Thanh toán chuyến đi(Lái xe)",
                                              var_stx_app.check_trip_payment_qr_drive, "25.000 ₫", "_ThanhToanChuyenDi_QRLaiXe.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.trip_payment_qr_drive_back).click()
            time.sleep(2)
        except:
            pass



    def trip_payment_qr_customer(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_trip_payment)
        except:
            trip_payment.trip_payment(self, "", "", "")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.trip_payment_input).click()
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.trip_payment_input_a).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.trip_payment_input1).clear()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.trip_payment_input1).send_keys("15000")
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.continue2).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.qr_customer).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.payment).click()
        time.sleep(2.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.FILL_CODE_CARD).click()
        time.sleep(3)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.FILL_CODE_CARD_INPUT).send_keys("9999992992098174")
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm1).click()
        time.sleep(2.5)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.PAY_CARD).click()
        except:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.FILL_CODE_CARD_INPUT).clear()
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.FILL_CODE_CARD_INPUT).send_keys("9999920987715201")
            time.sleep(0.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.confirm1).click()
            time.sleep(2.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.PAY_CARD).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_trip_payment_qr_customer)))

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Thanh toán chuyến đi(Lái xe)",
                                              var_stx_app.check_trip_payment_qr_customer, "Thanh toán qua thẻ thành công", "_ThanhToanChuyenDi_QRKhachHang.png")
        time.sleep(1)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(2)
        except:
            pass





class vnpay_wallet:


    def vnpay_wallet(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage)
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_dash_3).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.vnpay_wallet).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_vnpay_wallet)))

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Ví VNPAY(Lái xe)",
                                              var_stx_app.check_vnpay_wallet, "Liên kết Ví", "_ViVNPay.png")



    def vnpay_wallet_link(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_vnpay_wallet).click()
        except:
            vnpay_wallet.vnpay_wallet(self, "", "", "")


        name = var_stx_app.driver.find_element(By.XPATH, var_stx_app.vnpay_wallet_name_input).text
        password = var_stx_app.driver.find_element(By.XPATH, var_stx_app.vnpay_wallet_password_input).text

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.vnpay_wallet_name_input).clear()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.vnpay_wallet_name_input).send_keys(name)
        time.sleep(0.5)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.vnpay_wallet_password_input).clear()
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.vnpay_wallet_password_input).send_keys(password)
        time.sleep(0.5)

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.CONFIRM).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx_app.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_vnpay_wallet_link)))
        time.sleep(0.5)
        module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Ví VNPAY(Lái xe)",
                                              var_stx_app.check_vnpay_wallet_link, "Có lỗi khi liên kết tài khoản VNPAY", "_ViVNPay_LienKet.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(2.2)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.vnpay_wallet_back).click()
            time.sleep(2.5)
        except:
            pass





class setting:


    def setting(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage)
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_dash_3).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.setting).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_setting)))

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Cài đặt(Lái xe)",
                                              var_stx_app.check_setting, "Cài đặt", "_CaiDat.png")



    def setting_vesion(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_setting)
        except:
            setting.setting(self, "", "", "")



        var_stx_app.driver.find_element(By.XPATH, var_stx_app.setting_vesion).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_setting_vesion)))
        module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Cài đặt - (Lái xe)",
                                              var_stx_app.check_setting_vesion, "Kiểm tra cập nhật phần mềm", "_CaiDat_PhienBan.png")

        time.sleep(1)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(2)
        except:
            pass



    def setting_checkbox(self, code, eventname, result, button, name_image):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_setting)
        except:
            setting.setting(self, "", "", "")


        try:
            var_stx_app.driver.find_element(By.XPATH, button).click()
        except:
            var_stx_app.driver.swipe(350, 900, 350, 450, 1000)
            time.sleep(1)
            var_stx_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)
        var_stx_app.driver.find_element(By.XPATH, button).click()
        time.sleep(1)

        module_other_stx_app.write_result_displayed_try(code, eventname, result, "Cài đặt - (Lái xe)",
                                              button, name_image)



    def setting_sync(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_setting)
        except:
            setting.setting(self, "", "", "")



        var_stx_app.driver.find_element(By.XPATH, var_stx_app.setting_sync).click()
        time.sleep(2)
        try:
            wait = WebDriverWait(var_stx_app.driver, 15)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_setting_sync)))
        except:
            pass

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Cài đặt - (Lái xe)",
                                              var_stx_app.check_setting_sync, "Dữ liệu đã đồng bộ thành công, Khởi động lại ứng dụng để cập nhật", "_CaiDat_Dongbo.png")
        time.sleep(1)

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.igree).click()
            time.sleep(4)
            wait = WebDriverWait(var_stx_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.homepage)))
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.login_buttonlogin1).click()
            time.sleep(4)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.setting1).click()
            time.sleep(3)
        except:
            pass



    def setting_send_error(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_setting)
        except:
            setting.setting(self, "", "", "")

        time.sleep(3)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.setting_send_error).click()
        time.sleep(2.5)
        try:
            var_stx_app.driver.find_element(By.XPATH, "//android.widget.Toast")
            module_other_stx_app.write_result_text_try_if_toast(code, eventname, result, "Cài đặt - (Lái xe)",
                                                  "", "Gửi báo cáo lỗi thành công.", "_CaiDat_GuiBaoCaoLoi.png")
        except:
            pass

        try:
            time.sleep(2)
            check_text = var_stx_app.driver.find_element(By.XPATH, "//android.widget.Toast").text
            module_other_stx_app.write_result_text_try_if_toast(code, eventname, result, "Cài đặt - (Lái xe)",
                                                  "", "Gửi báo cáo lỗi thành công.", "_CaiDat_GuiBaoCaoLoi.png")
        except:
            pass


    def setting_change_size_word(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_setting)
        except:
            setting.setting(self, "", "", "")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.setting_change_size_word).click()
        except:
            var_stx_app.driver.swipe(350, 900, 350, 500, 1000)
            time.sleep(1)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.setting_change_size_word).click()
        time.sleep(1.5)

        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.confirm1)))
        time.sleep(1)
        element.click()
        time.sleep(2)


        module_other_stx_app.write_result_text_try_if_toast(code, eventname, result, "Cài đặt - (Lái xe)",
                                              "", "Không có sự thay đổi nào về font chữ.", "_CaiDat_ThayDoiCoChu.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.setting_back).click()
            time.sleep(2)
        except:
            pass





class report:


    def report(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage)
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_dash_3).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.report).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_report)))

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Cài đặt(Lái xe)",
                                              var_stx_app.check_report, "Báo cáo", "_BaoCao.png")



    def report_violate(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_report)
        except:
            report.report(self, "", "", "")


        var_stx_app.driver.find_element(By.XPATH, var_stx_app.report_violate).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_report_violate)))

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Báo cáo(Lái xe) - Vi phạm",
                                              var_stx_app.check_report_violate, "Lịch sử vi phạm", "_BaoCao_ViPham.png")



    def check_report_violate(self, code, eventname, result, button, name_image):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_report_violate)
        except:
            report.report_violate(self, "", "", "")


        var_stx_app.driver.find_element(By.XPATH, button).click()
        time.sleep(2.5)

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Báo cáo(Lái xe) - Vi phạm",
                                              var_stx_app.not_result, "Không có kết quả", name_image)


        if name_image == "_BaoCao_ViPham_ViPham.png":
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.report_violate_back).click()
            time.sleep(2.5)



    def report_fee_dam(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_report)
        except:
            report.report(self, "", "", "")


        var_stx_app.driver.find_element(By.XPATH, var_stx_app.report_fee_dam).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_report_fee_dam)))

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Báo cáo(Lái xe) - PhiDam",
                                              var_stx_app.check_report_fee_dam, "Phí đàm", "_BaoCao_PhiDam.png")

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.report_fee_dam_back).click()
            time.sleep(2.5)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.report_back).click()
            time.sleep(2.5)
        except:
            pass





class help:


    def help(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage)
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_dash_3).click()
        time.sleep(2)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.help).click()
        time.sleep(2)
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_help)))

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trợ giúp(Lái xe)",
                                              var_stx_app.check_help, "Trợ giúp", "_TroGiup.png")



    def help_comments(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_help)
        except:
            help.help(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.comment).click()
        time.sleep(2)

        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_comment1)))

        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Trợ giúp(Lái xe) - Góp ý",
                                              var_stx_app.check_comment1, "Chúng tôi mong muốn nhận góp ý của bạn để hoàn thiện dịch vụ tốt hơn", "_TroGiup_GopY.png")



    def help_comments_sdt(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_comment1)
        except:
            help.help_comments(self, "", "", "")

        module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Trợ giúp(Lái xe) - Góp ý",
                                              var_stx_app.help_comments_sdt, "", "_TroGiup_GopY_SDT.png")



    def help_comments_send(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_comment1)
        except:
            help.help_comments(self, "", "", "")


        var_stx_app.driver.find_element(By.XPATH, var_stx_app.comment_title_input).send_keys("Test chức năng góp ý")
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.comment_content_input).send_keys("Không")
        time.sleep(0.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.SEND_COMMENT).click()
        time.sleep(2)
        module_other_stx_app.write_result_text_try_if_toast(code, eventname, result, "Trợ giúp(Lái xe) - Góp ý",
                                              "", "Cảm ơn bạn đã gửi góp ý cho chúng tôi", "_TroGiup_GopY_GuiGopY.png")



    def help_comments_help(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_help)
        except:
            help.help(self, "", "", "")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.help_comments_help).click()
        time.sleep(2)

        try:
            wait = WebDriverWait(var_stx_app.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_help_comments_help)))
        except:
            pass

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.check_help_comments_help)
            module_other_stx_app.write_result_text_try_if_other(code, eventname, result, "Trợ giúp(Lái xe) - Góp ý",
                                                  var_stx_app.check_help_comments_help, "", "_TroGiup_GopY_HuongDan.png")
        except:
            module_other_stx_app.write_result_not_displayed_try(code, eventname, result, "Trợ giúp(Lái xe) - Góp ý",
                                                  var_stx_app.help_comments_help, "_TroGiup_GopY_HuongDan.png")

        time.sleep(1)
        var_stx_app.driver.press_keycode(4)
        time.sleep(2)

        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.help_back).click()
            time.sleep(2.5)
        except:
            pass




class end_of_shift:


    def end_of_shift(self, code, eventname, result):
        var_stx_app.driver.implicitly_wait(5)
        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.driver_g7).click()
            time.sleep(3)
        except:
            pass

        try:
            var_stx_app.driver.implicitly_wait(0.3)
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.homepage)
        except:
            login_stx_app.login_driverg7(self, "Xe sân bay")

        var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_dash_3).click()
        time.sleep(2)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.end_of_shift).click()
        except:
            var_stx_app.driver.swipe(200, 900, 200, 500, 1000)
            time.sleep(1)
            try:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.end_of_shift).click()
            except:
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.icon_dash_3).click()
                time.sleep(2)
                var_stx_app.driver.swipe(200, 900, 200, 500, 1000)
                time.sleep(1)
                var_stx_app.driver.find_element(By.XPATH, var_stx_app.end_of_shift).click()
        time.sleep(2.5)
        var_stx_app.driver.find_element(By.XPATH, var_stx_app.END_OF_SHIFT).click()
        time.sleep(2.5)
        try:
            var_stx_app.driver.find_element(By.XPATH, var_stx_app.END_OF_SHIFT).click()
            time.sleep(2.5)
        except:
            pass
        wait = WebDriverWait(var_stx_app.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var_stx_app.check_end_of_shift)))
        module_other_stx_app.write_result_text_try_if(code, eventname, result, "Rời ca(Lái xe)",
                                              var_stx_app.check_end_of_shift, "VÀO CA", "_RoiCa.png")

        













