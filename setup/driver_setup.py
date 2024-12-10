import os
from appium import webdriver
from appium.options.android import UiAutomator2Options

def init_driver():
    # ? Configuración del dispositivo y Appium usando UiAutomator2Options
    
    # #! Localmente
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
    # options.no_reset = True
    # options.new_command_timeout = 300  # Espera de 5 minutos (300 segundos)
    
    #! Integración con BrowserStack
    options = UiAutomator2Options()
    options.platform_name = "Android"  # Plataforma objetivo
    options.automation_name = "UiAutomator2"  # Motor de automatización
    options.device_name = "Google Pixel 5"  # Cambia el dispositivo si es necesario
    options.platform_version = "12.0"  # Versión del sistema operativo
    options.app = "bs://e98b452f837e855b55455ca3a6a0091b5ca7f433"  # ID de la aplicación subida a BrowserStack
    options.project = "Picap Automation"  # Nombre opcional del proyecto
    options.build = "Build 1"  # Nombre opcional de la build
    options.name = "Test Login Flow"  # Nombre del caso de prueba
    options.new_command_timeout = 300  # Espera de 5 minutos (300 segundos)
    
    # Configurar idioma y localización para Colombia
    options.language = "es"  # Idioma español
    options.locale = "CO"  # Localización para Colombia
    options.auto_grant_permissions = True  # Otorga todos los permisos automáticamente
    
    # Credenciales de BrowserStack
    username = "davidmadrid_0ljp8h"
    access_key = "pxSyizAozTvJRgRr2hpB"

    #! Iniciar y devolver el driver de Appium apuntando al hub de BrowserStack
    driver = webdriver.Remote(f"http://{username}:{access_key}@hub.browserstack.com/wd/hub", options=options)
    
    #! Iniciar y devolver el driver de Appium apuntando al servidor local
    # driver = webdriver.Remote('http://localhost:4723', options=options)
    
    driver.implicitly_wait(1)  # Establecer tiempo de espera implícito
    return driver