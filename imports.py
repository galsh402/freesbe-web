from selenium.webdriver.chrome import webdriver
from selenium.common import TimeoutException
import pdb
import time
import pytest
import allure
import requests
import pyautogui
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pynput.keyboard import Controller, Key  #keyboard = Controller()
from pynput.mouse import Controller, Button
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from openpyxl import workbook, load_workbook
from datetime import datetime
from conftest import driver
from base_page import Base

def hold():
    pdb.set_trace()
