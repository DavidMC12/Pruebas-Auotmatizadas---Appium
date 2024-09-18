from appium import webdriver
from appium.options.android import UiAutomator2Options

def init_driver():
    # Configuración del dispositivo y Appium usando UiAutomator2Options
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "HUAWEI Y9 2019"
    options.udid = "7ML4C19722005941"
    options.platform_version = "9"
    options.app_package = "co.picap.passenger"
    options.app_activity = "co.picap.passenger.MainActivity"
    options.no_reset = True

    # Iniciar y devolver el driver de Appium
    driver = webdriver.Remote('http://localhost:4723', options=options)
    driver.implicitly_wait(1)  # Establecer tiempo de espera implícito
    return driver