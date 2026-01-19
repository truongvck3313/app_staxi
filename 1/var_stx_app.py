import subprocess
import logging
import os
import time
import re

from appium import webdriver
from appium.options.android import UiAutomator2Options


def get_var_stx_app.driver_driver():
    if var_stx_app.driver_driver is None:
        raise RuntimeError("❌ var_stx_app.driver_driver chưa được khởi tạo")
    return var_stx_app.driver_driver


def get_var_stx_app.driver_customer():
    if var_stx_app.driver_customer is None:
        raise RuntimeError("❌ var_stx_app.driver_customer chưa được khởi tạo")
    return var_stx_app.driver_customer


APP_DRIVER = {
    "appPackage": "com.binhanh.driver.g7",
    "appActivity": "crc64e6eba20b85d3d07a.SplashActivity",
}

APP_CUSTOMER = {
    "appPackage": "com.binhanh.g7taxi",
    "appActivity": "crc64b459bed81738e44c.SplashActivity",
}


def get_all_android_devices():
    output = subprocess.check_output(["adb", "devices"], text=True)
    devices = [
        line.split()[0]
        for line in output.strip().splitlines()[1:]
        if line.endswith("device")
    ]
    if not devices:
        raise RuntimeError("❌ Không tìm thấy thiết bị Android")
    return devices


def get_device_info(udid):
    platform_version = subprocess.check_output(
        ["adb", "-s", udid, "shell", "getprop", "ro.build.version.release"],
        text=True
    ).strip()

    device_name = subprocess.check_output(
        ["adb", "-s", udid, "shell", "getprop", "ro.product.model"],
        text=True
    ).strip()

    return platform_version, device_name


def get_running_app(udid):
    try:
        cmd = f'adb -s {udid} shell dumpsys window | findstr mCurrentFocus'
        out = subprocess.check_output(cmd, shell=True, text=True)
        match = re.search(r'(\S+)/(\S+)', out)
        if match:
            return match.group(1)
    except Exception:
        pass
    return None


# =====================================================
# AUTO ASSIGN DEVICE ROLE
# =====================================================

def auto_assign_devices():
    devices = get_all_android_devices()
    roles = {}

    for udid in devices:
        pkg = get_running_app(udid)
        if pkg == APP_DRIVER["appPackage"]:
            roles["var_stx_app.driver_driver"] = udid
        elif pkg == APP_CUSTOMER["appPackage"]:
            roles["var_stx_app.driver_customer"] = udid

    remain = [d for d in devices if d not in roles.values()]

    if "var_stx_app.driver_driver" not in roles:
        roles["var_stx_app.driver_driver"] = remain.pop(0)

    if "var_stx_app.driver_customer" not in roles:
        roles["var_stx_app.driver_customer"] = remain.pop(0)

    return roles



def cleanup_uiautomator(udid):
    logging.info(f"🧹 Cleanup UiAutomator2 on {udid}")
    os.system(f"adb -s {udid} shell pm clear io.appium.uiautomator2.server")
    os.system(f"adb -s {udid} shell pm clear io.appium.uiautomator2.server.test")
    time.sleep(1)



def create_driver(udid, system_port):
    platform_version, device_name = get_device_info(udid)

    caps = {
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:udid": udid,
        "appium:deviceName": device_name,
        "appium:platformVersion": platform_version,
        "appium:systemPort": system_port,
        "appium:noReset": True,

        # 🔥 CHỐT: Appium KHÔNG được tự mở app
        "appium:autoLaunch": False,
        "appium:newCommandTimeout": 300,
    }

    options = UiAutomator2Options().load_capabilities(caps)

    logging.info(f"🚀 Create driver for {udid}")

    return webdriver.Remote(
        "http://localhost:4723/wd/hub",
        options=options
    )


# =====================================================
# START APP (ANDROID LEVEL – 100% ĐÚNG APP)
# =====================================================

def launch_app(udid, app_cfg):
    pkg = app_cfg["appPackage"]
    act = app_cfg["appActivity"]

    logging.info(f"📱 Launch {pkg} on {udid}")
    os.system(
        f"adb -s {udid} shell am start -n {pkg}/{act}"
    )
    time.sleep(2)


# =====================================================
# START BOTH DRIVERS (ĐÚNG YÊU CẦU CỦA BẠN)
# =====================================================

def start_drivers():
    global var_stx_app.driver_driver, var_stx_app.driver_customer

    roles = auto_assign_devices()

    # DRIVER APP
    cleanup_uiautomator(roles["var_stx_app.driver_driver"])
    var_stx_app.driver_driver = create_driver(roles["var_stx_app.driver_driver"], 8200)
    launch_app(roles["var_stx_app.driver_driver"], APP_DRIVER)

    # CUSTOMER APP
    cleanup_uiautomator(roles["var_stx_app.driver_customer"])
    var_stx_app.driver_customer = create_driver(roles["var_stx_app.driver_customer"], 8201)
    launch_app(roles["var_stx_app.driver_customer"], APP_CUSTOMER)

    return var_stx_app.driver_driver, var_stx_app.driver_customer


# =====================================================
# RESTART 1 DRIVER (GIỮ ĐÚNG APP)
# =====================================================

def restart_driver(driver):
    caps = driver.capabilities
    udid = caps["udid"]
    system_port = caps["systemPort"]

    pkg = get_running_app(udid)

    if pkg == APP_DRIVER["appPackage"]:
        app_cfg = APP_DRIVER
    elif pkg == APP_CUSTOMER["appPackage"]:
        app_cfg = APP_CUSTOMER
    else:
        raise RuntimeError(f"❌ Không xác định được app để restart: {pkg}")

    try:
        driver.quit()
    except Exception:
        pass

    cleanup_uiautomator(udid)

    new_driver = create_driver(udid, system_port)
    launch_app(udid, app_cfg)

    return new_driver


var_stx_app.driver_driver, var_stx_app.driver_customer = start_drivers()