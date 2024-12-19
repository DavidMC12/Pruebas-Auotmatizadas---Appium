import os
from appium import webdriver
from appium.options.android import UiAutomator2Options

def init_driver():
    # ? Configuración del dispositivo y Appium usando UiAutomator2Options
    
    #! Localmente
    # # Celular Redmi Note 13 Plus
    # options = UiAutomator2Options()
    # options.platform_name = "Android"
    # options.automation_name = "UiAutomator2"
    # options.device_name = "Redmi Note 13 Pro+ 5G"
    # options.udid = "7H4XPVQ4IZ4LEEVC"
    # options.platform_version = "14"
    # options.app_package = "co.picap.passenger"
    # options.app_activity = "co.picap.passenger.MainActivity"
    # options.no_reset = True
    
    # # Celular Huawei Y9 2019
    # options = UiAutomator2Options()
    # options.platform_name = "Android"
    # options.automation_name = "UiAutomator2"
    # options.device_name = "HUAWEI Y9 2019"
    # options.udid = "7ML4C19722005941"
    # options.platform_version = "9"
    # options.app_package = "co.picap.passenger"
    # options.app_activity = "co.picap.passenger.MainActivity"
    # options.no_reset = False
    # options.new_command_timeout = 300  # Espera de 5 minutos (300 segundos)
    
    #! Integración con BrowserStack
    options = UiAutomator2Options()
    options.platform_name = "Android"  # Plataforma objetivo
    options.automation_name = "UiAutomator2"  # Motor de automatización
    options.device_name = "Vivo Y21"  # Cambia el dispositivo si es necesario 
    options.platform_version = "11.0"  # Versión del sistema operativo
    options.app = "bs://169a996b431e6998463e2b7570378896e0e3078f"  # ID de la aplicación subida a BrowserStack
    options.project = "Picap Automation"  # Nombre opcional del proyecto
    options.build = "Build 2"  # Nombre opcional de la build
    options.name = "Register Flow"  # Nombre del caso de prueba
    options.new_command_timeout = 300  # Espera de 5 minutos (300 segundos)
    
    # Configurar idioma y localización para Colombia (Adicionales)
    options.language = "es"  # Idioma español
    options.locale = "CO"  # Localización para Colombia
    options.auto_grant_permissions = True  # Otorga todos los permisos automáticamente
    options.set_capability("browserstack.gpsLocation", "4.710989,-74.072092")  # Bogotá, Colombia
    
    # Credenciales de BrowserStack
    username = "julianaleal_N6O8hI"
    access_key = "zUYoXcuZQsHZpMbEqmsv"

    #! Iniciar y devolver el driver de Appium apuntando al hub de BrowserStack
    driver = webdriver.Remote(f"http://{username}:{access_key}@hub.browserstack.com/wd/hub", options=options)
    
    #! Iniciar y devolver el driver de Appium apuntando al servidor local
    # driver = webdriver.Remote('http://localhost:4723', options=options)
    
    driver.implicitly_wait(1)  # Establecer tiempo de espera implícito
    return driver