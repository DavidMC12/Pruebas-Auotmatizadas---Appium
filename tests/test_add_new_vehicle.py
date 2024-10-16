from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import time
import sys

# Definir la función de Registro
def addNewVehicle(driver):
    # Definir constantes para XPaths, IDs y otros selectores
    MENU_SELECTOR = 'Menú\nPestaña 1 de 3'
    VEHICLES_SELECTOR = 'Vehículos'
    ADD_VEHICLE_SELECTOR = 'Agregar'
    CONTINUE_BUTTON_SELECTOR = 'Continuar'
    
    DRIVER_LICENSE_SELECTOR = 'Foto'
    OPEN_CAMERA_OPTION_SELECTOR = 'Abrir cámara'
    TAKE_PHOTO_SELECTOR_XPATH = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]'
    CONTINUE_BUTTON_SELECTOR_PROCESS = 'Continuar'
    
    SOAT_SELECTOR = 'SOAT'
    EXPIRE_DATE_SELECTOR_XPATH = '//android.view.View[@text="DD-MM-YYYY"]'
    ACCEPT_DATE_BUTTON_SELECTOR = 'Aceptar'
    
    MODEL_SELECTO_XPATH = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1]'
    COLOR_SELECTOR_XPATH = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2]'
    TP_SELECTOR = 'Tarjeta de propiedad'
    BRAND_SELECTOR_XPATH = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[3]'
    CYLINDER_SELECTOR_XPATH = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2]'
    PLATE_SELECTOR_XPATH = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[3]'
    REFERENCE_SELECTOR_XPATH = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[4]'
    DOCUMENT_NUMBER_PROPERTY_SELECTOR_XPATH = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[5]'
    
    REGISTER_CONFIRMATION_SELECTOR = 'Aceptar'
    
    try:
        print("Iniciando el proceso de registro de nuevo vehículo...")\
        
        menu_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, MENU_SELECTOR)
        menu_button.click()
        time.sleep(1)
        
        vehicles_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, VEHICLES_SELECTOR)
        vehicles_button.click()
        time.sleep(2)
        
        add_vehicle_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, ADD_VEHICLE_SELECTOR)
        add_vehicle_button.click()
        time.sleep(2)
        
        # ? Despliegue de la Lista de Vehículos
        # Obtener el tamaño de la pantalla del dispositivo
        screen_size = driver.get_window_size()
        # Hacer tap en una posición relativa en la pantalla (50% ancho, 17% altura)
        driver.tap([(screen_size['width'] * 0.5, screen_size['height'] * 0.18)], 500)
        time.sleep(2)
        
        # ? Selección de tipo de vehículo
        print("Seleccionando el tipo de vehículo...")
        vehicle_type = 'Carro'	# ? Poner el @content-desc del botón deseado:
        # XPATHS:
        # Carro: //android.widget.Button[@content-desc="Carro"]
        # Moto: //android.widget.Button[@content-desc="Moto"]
        # Vehículo de Carga: //android.widget.Button[@content-desc="Vehículo de carga"]
        # Taxi: //android.widget.Button[@content-desc="Taxi"]
        # Moto Vagon: //android.widget.Button[@content-desc="Moto-Vagón"]
        # Carry: //android.widget.Button[@content-desc="Carry"]
        # NHR: //android.widget.Button[@content-desc="NHR"]
        # NKR: //android.widget.Button[@content-desc="NKR"]
        # NPR: //android.widget.Button[@content-desc="NPR"]
        # Bicitaxi: //android.widget.Button[@content-desc="bicitaxi"]
        # Grúa: //android.widget.Button[@content-desc="Grúa"]
        
        # Buscar elementos que contengan la palabra específica en su descripción
        vehicle_elements = driver.find_elements(AppiumBy.XPATH, f"//*[contains(@content-desc, '{vehicle_type}')]")
        
        # Revisar si se encontró al menos un elemento y hacer clic en el primero
        if vehicle_elements:
            vehicle_elements[0].click()
        else:
            print(f"No se encontraron elementos para '{vehicle_type}'")
        
        print("Tipo de vehículo sleccionado, continuando...")
        continue_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONTINUE_BUTTON_SELECTOR)
        continue_button.click()
        time.sleep(2)
        
        # ? Proceso de registro de los documnentos del vehículo
        print("Iniciando el proceso de registro de documentos...")
        
        # * 1. Licencia de Conducción (Driver)
        print("Registrando la Licencia de Conducción...")
        driver_license = driver.find_element(AppiumBy.ACCESSIBILITY_ID, DRIVER_LICENSE_SELECTOR)
        driver_license.click()
        
        open_camera_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, OPEN_CAMERA_OPTION_SELECTOR)
        open_camera_option.click()
        time.sleep(1)
        
        take_photo_button = driver.find_element(AppiumBy.XPATH, TAKE_PHOTO_SELECTOR_XPATH)
        take_photo_button.click()
        time.sleep(16)
        
        continue_button_process = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONTINUE_BUTTON_SELECTOR_PROCESS)
        continue_button_process.click()
        time.sleep(5)
        print("Licencia de conducción registrada!")
        
        # * 2. Seguro Obligatorio (SOAT)
        print("Registrando el Seguro Obligatorio (SOAT)...")
        soat = driver.find_element(AppiumBy.ACCESSIBILITY_ID, SOAT_SELECTOR)
        soat.click()
        time.sleep(1)
        
        open_camera_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, OPEN_CAMERA_OPTION_SELECTOR)
        open_camera_option.click()
        time.sleep(1)
        
        take_photo_button = driver.find_element(AppiumBy.XPATH, TAKE_PHOTO_SELECTOR_XPATH)
        take_photo_button.click()
        time.sleep(5)
        
        expire_date = driver.find_element(AppiumBy.XPATH, EXPIRE_DATE_SELECTOR_XPATH)
        expire_date.click()
        
        confirm_date_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, ACCEPT_DATE_BUTTON_SELECTOR)
        confirm_date_button.click()
        
        continue_button_process = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONTINUE_BUTTON_SELECTOR_PROCESS)
        continue_button_process.click()
        time.sleep(5)
        print("Seguro Obligatorio (SOAT) registrado!")
        
        # * 3. Tarjeta de propiedad (LC. Tránsito)
        print("Registrando la Tarjeta de Propiedad (LC. Tránsito)...")
        model_year = driver.find_element(AppiumBy.XPATH, MODEL_SELECTO_XPATH)
        model_year.click()
        model_year.send_keys("2024")
        
        color_vehicle = driver.find_element(AppiumBy.XPATH, COLOR_SELECTOR_XPATH)
        color_vehicle.click()
        color_vehicle.send_keys("Negro")
        driver.back()
        
        ownership_target = driver.find_element(AppiumBy.ACCESSIBILITY_ID, TP_SELECTOR)
        ownership_target.click()
        time.sleep(2)
        
        open_camera_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, OPEN_CAMERA_OPTION_SELECTOR)
        open_camera_option.click()
        
        take_photo_button = driver.find_element(AppiumBy.XPATH, TAKE_PHOTO_SELECTOR_XPATH)
        take_photo_button.click()
        time.sleep(5)
        driver.back()
        time.sleep(15)
        
        brand_vehicle = driver.find_element(AppiumBy.XPATH, BRAND_SELECTOR_XPATH)
        brand_vehicle.click()
        brand_vehicle.send_keys("Prueba")
        driver.back()
        
        cylinder_vehicle = driver.find_element(AppiumBy.XPATH, CYLINDER_SELECTOR_XPATH)
        cylinder_vehicle.click()
        cylinder_vehicle.send_keys("1400")
        driver.back()
        
        plates_vehicle = driver.find_element(AppiumBy.XPATH, PLATE_SELECTOR_XPATH)
        plates_vehicle.click()
        plates_vehicle.send_keys("EFE003")
        driver.back()
        
        reference_vehicle = driver.find_element(AppiumBy.XPATH, REFERENCE_SELECTOR_XPATH)
        reference_vehicle.click()
        reference_vehicle.send_keys("Referencia de Prueba")
        driver.back()
        
        document_number = driver.find_element(AppiumBy.XPATH, DOCUMENT_NUMBER_PROPERTY_SELECTOR_XPATH)
        document_number.click()
        document_number.send_keys("10000003")
        driver.back()
        
        continue_button_process = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONTINUE_BUTTON_SELECTOR_PROCESS)
        continue_button_process.click()
        time.sleep(8)
        
        accept_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, REGISTER_CONFIRMATION_SELECTOR)
        accept_button.click()
        time.sleep(3)
        print("Tarjeta de Propiedad (LC. Tránsito) registrada!")

    except Exception as e:
        print(f"Error al ejecutar el caso de prueba: {e}.")
    finally:
        print("Finalizando el caso de prueba...")
        #driver.quit()