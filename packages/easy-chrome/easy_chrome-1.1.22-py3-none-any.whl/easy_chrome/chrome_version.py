import os
import subprocess
import winreg
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.core.utils import get_browser_version_from_os, ChromeType, os_name, OSType
from webdriver_manager.core.constants import DEFAULT_USER_HOME_CACHE_PATH
import shutil
import requests
import xml.etree.ElementTree as elemTree
import functools


def get_web_chrome_link(version):
    """get selenium chromedriver version by major version got from local chrome"""
    print(f"Try to get target chrome driver in web: {version}")

    res = requests.get("https://chromedriver.storage.googleapis.com")
    root = elemTree.fromstring(res.content)
    for k in root.iter('{http://doc.s3.amazonaws.com/2006-03-01}Key'):
        if k.text.find(version + '.') == 0:
            ver = k.text.split('/')[0]
            print(f"found web_version: {ver}")
            return ver
    print(f"not found matched version of chrome: {version}, use latest")
    return "latest"


def get_driver_path():
    # USE WDM chrome_version
    v = get_browser_version_from_os(ChromeType.GOOGLE)

    if not v:
        # use custom window chrome_version
        v = _custom_get_win_chrome_version()

    if not v:
        version = "latest"
    else:
        version = v.split(".")[0]

    _os_name = os_name()

    if _os_name == OSType.WIN:
        file_name = f"chromedriver_{version}.exe"
    else:
        file_name = f"chromedriver_{version}"

    expect_path = os.path.join(DEFAULT_USER_HOME_CACHE_PATH, file_name)
    if not os.path.exists(expect_path):
        wdm_path = ChromeDriverManager(version=get_web_chrome_link(version), cache_valid_range=1000).install()
        shutil.copy(wdm_path, expect_path)

    return expect_path


class DriverPath:

    @functools.cached_property
    def path(self):
        return get_driver_path()


driver_path = DriverPath()


def _get_chrome_installed(hive, flag):
    """get installed chrome version from winreg"""
    try:
        a_reg = winreg.ConnectRegistry(None, hive)
        a_key = winreg.OpenKey(a_reg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", 0, winreg.KEY_READ | flag)
        a_sub = winreg.OpenKey(a_key, "Google Chrome")
        return winreg.QueryValueEx(a_sub, "DisplayVersion")[0]
    except:
        pass


def _custom_get_win_chrome_version():
    """get chromedriver version, download if needed"""
    try:
        if os.path.exists("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"):
            output = subprocess.check_output(
                r'wmic datafile where name="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" '
                r'get Version /value', shell=True)
        else:
            output = subprocess.check_output(
                r'wmic datafile where name="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" '
                r'get Version /value', shell=True)

        version = output.decode('utf-8').strip().split("=")[1]

        return version

    except:
        for hive, flag in ((winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY),
                           (winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY),
                           (winreg.HKEY_CURRENT_USER, 0)):
            cr_ver = _get_chrome_installed(hive, flag)
            if cr_ver is not None:
                return cr_ver
