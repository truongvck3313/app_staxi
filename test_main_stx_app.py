import logging
import time
import module_other_stx_app
#pip install selenium==4.21.0
module_other_stx_app.timerun()
import unittest
from concurrent.futures import ThreadPoolExecutor
import caseid_stx_app
from var_stx_app import start_drivers
import module_stx_app
import var_stx_app
import homepage_g7
import homepage_driver
from caseid_stx_app import CaseIdStxApp


# interaction_cases = [
#     # "HomePage22",
#     # "HomePage23",
#     # "HomePage24",
#     # "HomePage25",
#     # "HomePage26",
#     # "HomePage27",
#     # "HomePage28",
#     # "HomePage28_1",
#     # "HomePage29",
#     # "HomePage30",
#     # "HomePage31",
#     # "HomePage32",
#     # "HomePage33",
#     # "HomePage34",
#     # "HomePage35",
#     # "HomePage36",
#     # "HomePage37",
#     # "HomePage38",
#     # "HomePage39",
#     # "HomePage40",
#     # "HomePage41",
#     # "HomePage42",
#     # "HomePage42_1",
#     # "HomePage43",
#     # "HomePage43_1",
#     # "HomePage43_2",
#     # "HomePage66",
#     # "HomePage67",
#     # "HomePage68",
#     # "HomePage69",
#     # "App01",
#     # "App02",
#     # "App03",
#     # "App04",
#     # "App05",
#     # "Web01",
#     # "Web02",
#     # "Web03",
#     # "Web04",
#     # "Web05",
#     # "Home53",
#     # "Home54",
#     # "Home55",
#     # "Home56",
#     # "Home57",
#     # "Home58",
#     # "Home59",
#     # "Home60",
#     # "Home61",
#     # "Home62",
#     # "Home63",
#     # "Home64",
#     # "Home65",
#     # "Home66",
#     # "Home67",
#     # "Home68",
#     # "Home69",
#     # "Home70",
#     # "Home71",
#     # "Home72",
#     # "Home73",
#     # "Home74",
#     # "Home75",
#     # "Home76",
#     # "Home77",
#     # "Home78",
#     # "Home79",
#     # "Home79_1",
#     # "Home80",
#     # "Home81",
#     # "Home82",
# ]
#
# driver_cases = [
#     # "Login09",
#     # "Login10",
#     # "Home01",
#     # "Home02",
#     # "Home03",
#     # "Home04",
#     # "Home05",
#     # "Home06",
#     # "Home07",
#     # "Home08",
#     # "Home09",
#     # "Home09_1",
#     # "Home09_2",
#     # "Home10",
#     # "Home11",
#     # "Home12",
#     # "Home13",
#     # "Home14",
#     # "Home15",
#     # "Home16",
#     # "Home17",
#     # "Home18",
#     # "Home19",
#     # "Home20",
#     # "Home21",
#     # "Home22",
#     # "Home23",
#     # "Home24",
#     # "Home25",
#     # "Home25_1",
#     # "Home26",
#     # "Home27",
#     # "Home28",
#     # "Home29",
#     # "Home30",
#     # "Home30_1",
#     # "Home31",
#     # "Home32",
#     # "Home33",
#     # "Home34",
#     # "Home35",
#     # "Home36",
#     # "Home37",
#     # "Home38",
#     # "Home39",
#     # "Home40",
#     # "Home41",
#     # "Home43",
#     # "Home43_1",
#     # "Home44",
#     # "Home45",
#     # "Home46",
#     # "Home47",
#     # "Home48",
#     # "Home48_1",
#     # "Home48_2",
#     # "Home48_3",
#     # "Home48_4",
#     # "Home48_5",
#     # "Home48_6",
#     # "Home48_7",
#     # "Home49",
#     # "Home50",
#     # "Home51",
#     # "Home52",
#     # "Notification01",
#     # "Notification02",
#     # "Notification03",
#     # "Notification04",
#     # "Notification05",
#     # "Notification06",
#     # "Notification07",
#     # "Notification08",
#     # "Notification09",
#     # "Notification10",
#     # "History01",
#     # "History02",
#     # "History02_1",
#     # "History03",
#     # "History04",
#     # "History05",
#     # "History06",
#     # "History07",
#     # "History08",
#     # "History09",
#     # "History10",
#     # "History11",
#     # "History12",
#     # "History13",
#     # "History13_1",
#     # "History13_2",
#     # "History13_3",
#     # "History13_4",
#     # "History13_5",
#     # "History14",
#     # "History15",
#     # "History16",
#     # "History17",
#     # "History18",
#     # "History19",
#     # "History19_1",
#     # "History19_2",
#     # "History20",
#     # "History21",
#     # "History22",
#     # "History23",
#     # "History24",
#     # "History25",
#     # "History26",
#     # "History27",
#     # "History28",
#     # "CashWallet01",
#     # "CashWallet02",
#     # "CashWallet03",
#     # "CashWallet04",
#     # "CashWallet05",
#     # "CashWallet06",
#     # "CashWallet07",
#     # "CashWallet08",
#     # "CashWallet09",
#     # # "CashWallet10",
#     # "TripPayment01",
#     # "TripPayment02",
#     # "TripPayment03",
#     # "TripPayment04",
#     # "VnPayWallet01",
#     # "VnPayWallet02",
#     # "Setting01",
#     # "Setting02",
#     # "Setting03",
#     # "Setting04",
#     # "Setting05",
#     # "Setting06",
#     # "Setting07",
#     # "Setting08",
#     # "Setting09",
#     # "Setting10",
#     # "Setting11",
#     # "Report01",
#     # "Report02",
#     # "Report03",
#     # "Report04",
#     # "Report05",
#     # "Report06",
#     # "Report07",
#     # "Report08",
#     # "Report09",
#     # "Report10",
#     # "Report11",
#     # "Report12",
#     # "Report13",
#     # "Report14",
#     # "Report15",
#     # "Report16",
#     # "Help01",
#     # "Help02",
#     # "Help03",
#     # "Help04",
#     # "Help05",
#     # "Logout01",
# ]
#
#
# customer_cases = [
#     # "Login01",
#     # "Login02",
#     # "Login03",
#     # "Login04",
#     # "Login05",
#     # "Login06",
#     # "Login07",
#     # "Login08",
#     # "HomePage01",
#     # "HomePage02",
#     # "HomePage03",
#     # "HomePage04",
#     # "HomePage05",
#     # "HomePage06",
#     # "HomePage07",
#     # "HomePage08",
#     # "HomePage09",
#     # "HomePage10",
#     # "HomePage11",
#     # "HomePage12",
#     # "HomePage12_1",
#     # "HomePage12_2",
#     # "HomePage13",
#     # "HomePage14",
#     # "HomePage15",
#     # "HomePage16",
#     # "HomePage17",
#     # "HomePage18",
#     # "HomePage19",
#     # "HomePage20",
#     # "HomePage21",
#     # "HomePage21_1",
#     # "HomePage21_2",
#     # "HomePage44",
#     # "HomePage45",
#     # "HomePage46",
#     # "HomePage47",
#     # "HomePage48",
#     # "HomePage49",
#     # "HomePage50",
#     # "HomePage51",
#     # "HomePage52",
#     # "HomePage53",
#     # "HomePage54",
#     # "HomePage55",
#     # "HomePage57",
#     # "HomePage58",
#     # "HomePage59",
#     # "HomePage60",
#     # "HomePage61",
#     # "HomePage62",
#     # "HomePage63",
#     # "FavoriteSpot01",
#     # "FavoriteSpot02",
#     # "FavoriteSpot03",
#     # "FavoriteSpot04",
#     # "FavoriteSpot05",
#     # "FavoriteSpot06",
#     # "FavoriteSpot07",
#     # "FavoriteSpot08",
#     # "FavoriteSpot09",
#     # "FavoriteSpot10",
#     # "FavoriteSpot11",
#     # "FavoriteSpot12",
#     # "Promotion01",
#     # "Promotion02",
#     # "Promotion03",
#     # "Promotion04",
#     # "Promotion05",
#     # "Promotion06",
#     # "Promotion07",
#     # "Account01",
#     # "Account02",
#     # "Account03",
#     # "Account04",
#     # "Account05",
#     # "Account06",
#     # "Account07",
#     # "Account08",
#     # "Account09",
#     # "Account10",
#     # "Account11",
#     # "Account12",
#     # "Account12_1",
#     # "Account12_2",
#     # "Account12_3",
#     # "Account12_4",
#     # "Account12_5",
#     # "Account12_6",
#     # "Account13",
#     # "Account13_1",
#     # "Account14",
#     # "Account15",
#     # "Account16",
#     # "Account17",
#     # "Account18",
#     # "Account19",
#     # "Account20",
#     # "Account21",
#     # "Account22",
#     # "Account23",
#     # "Account24",
#     # "Account25",
#     # "Account26",
#     # "Account27",
#     # "Account28",
#     # "Account29",
#     # "Account30",
#     # "Account31",
#     # "Account32",
#     # "Account33",
#     # "Account34",
#     # "Account35",
#     # "Account36",
#     # "Account37",
#     # "Account38",
#     # "Account39",
#     # "Account40",
#     # "Account41",
#     # "Account42",
#     # "Account43",
#     # "Account44",
#     # "Account45",
#     # "Account46",
#     # "Account47",
#     # "Account48",
#     # "Account49",
#     # "Account50",
#     # "Account50_1",
#     # "Account51",
#     # "Account51_1",
#     # "Account51_2",
#     # "Account52",
#     # "Account53",
#     # "Account54",
#     # "Account55",
#     # "Account56",
#     # "Account57",
#     # "Account58",
#     # "Account59",
#     # "Account60",
#     # "Account61",
#     # "Account62",
#     # "Account63",
#     # "Account64",
#     # "Account65",
#     # "Account66",
#     # "Account67",
#     # "Account68",
#     # "Account69",
#     # "Account70",
#     # "Account71",
# ]










def run_case_list(case_ids, before_each_case=None):
    case_instance = CaseIdStxApp()

    for case_id in case_ids:
        if not hasattr(case_instance, case_id):
            raise RuntimeError(f"❌ Không tìm thấy case: {case_id}")

        case_func = getattr(case_instance, case_id)

        # ===== Hook chạy trước mỗi case =====
        if before_each_case:
            try:
                before_each_case()
            except:
                logging.info(f"Không cần chạy case back; {case_id}")

        # ------------------------ check session
        try:
            var_stx_app.driver_customer.get_window_size()
        except:
            var_stx_app.restart_driver(var_stx_app.driver_customer)

        try:
            var_stx_app.driver_driver.get_window_size()
        except:
            var_stx_app.restart_driver(var_stx_app.driver_driver)

        time.sleep(3)

        # ------------------------ chạy case
        try:
            print(f"bắt đầu chạy case: {case_id}")
            case_func()
        except Exception as e:
            print(f"❌ Lỗi khi chạy {case_id}: {e}")
            var_stx_app.logging.info(f"❌ Lỗi khi chạy {case_id}: {e}")
            time.sleep(3)







class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        start_drivers()

    def test_run_mixed_mode(self):
        module_other_stx_app.clearData(var_stx_app.checklistpath, "Checklist", "", "", "")
        module_other_stx_app.clear_log()
        module_other_stx_app.delete_image()



        # LUỒNG TUẦN TỰ – CASE TƯƠNG TÁC 2 APP
        interaction_cases = module_stx_app.get_cases_interaction()
        run_case_list(interaction_cases)#case bắt đầu

        interaction_none = module_stx_app.get_cases_none_interaction()
        run_case_list(interaction_none)#case none(retest)

        interaction_fail = module_stx_app.get_cases_fail_interaction()
        run_case_list(interaction_fail)#case fail(retest)




        # LUỒNG SONG SONG – CASE ĐƠN APP
        customer_cases = module_stx_app.get_cases_customer()
        driver_cases = module_stx_app.get_cases_driver()
        with ThreadPoolExecutor(max_workers=2) as executor:#case bắt đầu
            f_driver = executor.submit(run_case_list, driver_cases)
            f_customer = executor.submit(run_case_list, customer_cases)
            f_driver.result()
            f_customer.result()



        customer_none = module_stx_app.get_cases_none_customer()
        driver_none = module_stx_app.get_cases_none_driver()
        with ThreadPoolExecutor(max_workers=2) as executor:
            # Driver: mỗi case đều back bằng homepage_driver.homepage_g7_drive_back()
            f_driver = executor.submit(
                run_case_list,
                driver_none,
                homepage_driver.homepage_g7_drive_back)
            # Customer: mỗi case đều back bằng homepage_g7.homepage_g7_back()
            f_customer = executor.submit(
                run_case_list,
                customer_none,
                homepage_g7.homepage_g7_back)

            f_driver.result()
            f_customer.result()



        customer_fail = module_stx_app.get_cases_fail_customer()
        driver_fail = module_stx_app.get_cases_fail_driver()
        with ThreadPoolExecutor(max_workers=2) as executor:  # case fail (retest)
            # Driver: mỗi case fail đều back về homepage driver trước
            f_driver = executor.submit(
                run_case_list,
                driver_fail,
                homepage_driver.homepage_g7_drive_back)
            # Customer: mỗi case fail đều back về homepage customer trước
            f_customer = executor.submit(
                run_case_list,
                customer_fail,
                homepage_g7.homepage_g7_back)

            f_driver.result()
            f_customer.result()

        module_other_stx_app.send_viber()





if __name__ == "__main__":
    unittest.main()








