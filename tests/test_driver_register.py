from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import time

# Función de Registro
def main(driver):
    # Definir constantes para XPaths, IDs y otros selectores
    curp = "CURP000001"
    rfc = "RFC000001"
    plcas = "0XX01"

    MENU_SELECTOR = 'Menú\nPestaña 1 de 3'
    DRIVER_CONVERT_SELECTOR = 'Convertirme en conductor'
    ACCEPT_CONVERT_SELECTOR = 'Si'
    CONTINUE_SELECTOR = 'Continuar'
    
    PHOTO_CURP_SELECTOR = 'Selecciona tu foto'
    OPEN_CAMERA_SELECTOR = 'Abrir cámara'
    TAKE_PHOTO_XPATH = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]'
    CURP_SELECTOR = 'CURP'
    
    PHOTO_RFC_SELECTOR_2 = 'Sube una foto de tu constancia de situación fiscal (RFC)'
    RFC_XPATH = '//android.widget.EditText'
    
    PHOTO_BACK_INE_SELECTOR = 'Foto de la parte trasera de tu INE'
    PHOTO_FRONT_INE_SELECTOR = 'Foto de la parte frontal de tu INE'
    
    PROOF_OF_ADDRESS_SELECTOR = 'Sube una foto de tu comprobante de domicilio (La dirección debe coincidir con tu INE). No mayor a 3 meses'
    
    CIVIL_LIABILITY_POLICY_SELECTOR = 'Foto'
    
    DRIVER_LICENSE_SELECTOR = 'Foto'
    
    # Formulario Tarjeta Circulación
    MODEL_SELECTOR = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1]'
    BRAND_SELECTOR = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2]'
    CILINDER_SELECTOR = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[3]'
    REFERENCE_SELECTOR = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[4]'
    PLATES_SELECTOR = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[4]'
    CIRCULATION_CARD_SELECTOR = 'Tarjeta de circulación'
    COLOR_SELECTOR = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[3]'
    
    FINAL_CONFIRMATION_SELECTOR = 'Aceptar'
    try:
        print("Iniciando el proceso de registro de conductor...")
        
        # Acceder a menú y seleccionar opción de convertirse en conductor
        menu_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, MENU_SELECTOR)
        menu_button.click()
        
        driver_convert_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, DRIVER_CONVERT_SELECTOR)
        driver_convert_button.click()
        
        accept_convert_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, ACCEPT_CONVERT_SELECTOR)
        accept_convert_button.click()
        print("Pasando al registro del conductor.")
        time.sleep(3)
        
        continue_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONTINUE_SELECTOR)
        continue_button.click()
        time.sleep(2)
        
        # * 1. Cargar CURP
        print("Iniciando proceso de cargue de documentos.")
        photo = driver.find_element(AppiumBy.ACCESSIBILITY_ID, PHOTO_CURP_SELECTOR)
        photo.click()
        
        open_camera_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, OPEN_CAMERA_SELECTOR)
        open_camera_button.click()
        time.sleep(2)
        
        take_photo = driver.find_element(AppiumBy.XPATH, TAKE_PHOTO_XPATH)
        take_photo.click()
        time.sleep(4)
        
        curp = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CURP_SELECTOR)
        curp.click()
        curp.send_keys(curp)
        driver.back()
        
        continue_button_2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONTINUE_SELECTOR)
        continue_button_2.click()
        time.sleep(2)
        
        # * 2. Cargar RFC
        print("Cargando RFC...")
        photo_rfc = driver.find_element(AppiumBy.ACCESSIBILITY_ID, PHOTO_RFC_SELECTOR_2)
        photo_rfc.click()
        
        open_camera_button_2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, OPEN_CAMERA_SELECTOR)
        open_camera_button_2.click()
        time.sleep(2)
        
        take_photo_2 = driver.find_element(AppiumBy.XPATH, TAKE_PHOTO_XPATH)
        take_photo_2.click()
        time.sleep(4)
        
        screen_size = driver.get_window_size()
        driver.tap([(screen_size['width'] * 0.5, screen_size['height'] * 0.55)], 500)
        rfc = driver.find_element(AppiumBy.XPATH, RFC_XPATH)
        rfc.send_keys(rfc)
        driver.back()
        
        continue_button_3 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONTINUE_SELECTOR)
        continue_button_3.click()
        time.sleep(2)
        
        # * 3. Cargar INE
        print("Cargando parte trasera INE ...")
        photo_ine_back = driver.find_element(AppiumBy.ACCESSIBILITY_ID, PHOTO_BACK_INE_SELECTOR)
        photo_ine_back.click()
        
        open_camera_button_ine = driver.find_element(AppiumBy.ACCESSIBILITY_ID, OPEN_CAMERA_SELECTOR)
        open_camera_button_ine.click()
        time.sleep(2)
        
        take_photo_ine = driver.find_element(AppiumBy.XPATH, TAKE_PHOTO_XPATH)
        take_photo_ine.click()
        time.sleep(4)
        
        continue_button_4 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONTINUE_SELECTOR)
        continue_button_4.click()
        time.sleep(2)
        
        # * 4. Cargar INE
        print("Cargando parte forntal INE ...")
        photo_ine_front = driver.find_element(AppiumBy.ACCESSIBILITY_ID, PHOTO_FRONT_INE_SELECTOR)
        photo_ine_front.click()
        
        open_camera_button_ine = driver.find_element(AppiumBy.ACCESSIBILITY_ID, OPEN_CAMERA_SELECTOR)
        open_camera_button_ine.click()
        time.sleep(2)
        
        take_photo_ine = driver.find_element(AppiumBy.XPATH, TAKE_PHOTO_XPATH)
        take_photo_ine.click()
        time.sleep(4)
        
        continue_button_4 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONTINUE_SELECTOR)
        continue_button_4.click()
        time.sleep(2)
        
        # * 5. Cargar comprobante de domicilio
        print("Cargando comprobante de domicilio...")
        proof_of_address = driver.find_element(AppiumBy.ACCESSIBILITY_ID, PROOF_OF_ADDRESS_SELECTOR)
        proof_of_address.click()
        
        open_camera_button_proof = driver.find_element(AppiumBy.ACCESSIBILITY_ID, OPEN_CAMERA_SELECTOR)
        open_camera_button_proof.click()
        time.sleep(2)
        
        take_photo_proof = driver.find_element(AppiumBy.XPATH, TAKE_PHOTO_XPATH)
        take_photo_proof.click()
        time.sleep(4)
        
        continue_button_5 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONTINUE_SELECTOR)
        continue_button_5.click()
        time.sleep(3)
        
        continue_button_6 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONTINUE_SELECTOR)
        continue_button_6.click()
        time.sleep(2)
        
        # * 6. Cargar poliza de responsabilidad civil
        print("Cargando poliza de responsabilidad civil...")
        civil_liability = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CIVIL_LIABILITY_POLICY_SELECTOR)
        civil_liability.click()
        
        open_camera_button_civil = driver.find_element(AppiumBy.ACCESSIBILITY_ID, OPEN_CAMERA_SELECTOR)
        open_camera_button_civil.click()
        time.sleep(2)
        
        take_photo_civil = driver.find_element(AppiumBy.XPATH, TAKE_PHOTO_XPATH)
        take_photo_civil.click()
        time.sleep(4)
        
        continue_button_7 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONTINUE_SELECTOR)
        continue_button_7.click()
        time.sleep(2)
        
        # * 7. Licencia de Conducir
        print("Cargando licencia de conducir...")
        driver_license = driver.find_element(AppiumBy.ACCESSIBILITY_ID, DRIVER_LICENSE_SELECTOR)
        driver_license.click()
        
        open_camera_button_license = driver.find_element(AppiumBy.ACCESSIBILITY_ID, OPEN_CAMERA_SELECTOR)
        open_camera_button_license.click()
        time.sleep(2)
        
        take_photo_license = driver.find_element(AppiumBy.XPATH, TAKE_PHOTO_XPATH)
        take_photo_license.click()
        time.sleep(4)
        
        continue_button_8 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONTINUE_SELECTOR)
        continue_button_8.click()
        time.sleep(5)
        
        # * 8. Tarjeta de Circulación
        print("Cargando datos de tarjeta de circulación...")
        model = driver.find_element(AppiumBy.XPATH, MODEL_SELECTOR)
        model.click()
        model.send_keys("2023")
        
        brand = driver.find_element(AppiumBy.XPATH, BRAND_SELECTOR)
        brand.click()
        brand.send_keys("Suzuki")
        
        cc = driver.find_element(AppiumBy.XPATH, CILINDER_SELECTOR)
        cc.click()
        cc.send_keys("149")
        driver.back()
        
        reference = driver.find_element(AppiumBy.XPATH, REFERENCE_SELECTOR)
        reference.click()
        reference.send_keys("GSXR 150")
        driver.back()
        
        plates = driver.find_element(AppiumBy.XPATH, PLATES_SELECTOR)
        plates.click()
        plates.send_keys(plcas)
        driver.back()
        
        driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=1000, duration=1000)
        
        circulation_card = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CIRCULATION_CARD_SELECTOR)
        circulation_card.click()
        
        open_camera_button_card = driver.find_element(AppiumBy.ACCESSIBILITY_ID, OPEN_CAMERA_SELECTOR)
        open_camera_button_card.click()
        time.sleep(2)
        
        take_photo_card = driver.find_element(AppiumBy.XPATH, TAKE_PHOTO_XPATH)
        take_photo_card.click()
        time.sleep(5)
        driver.back()
        time.sleep(8)
        
        color = driver.find_element(AppiumBy.XPATH, COLOR_SELECTOR)
        color.click()
        color.send_keys("Negro")
        driver.back()
        
        continue_button_9 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONTINUE_SELECTOR)
        continue_button_9.click()
        time.sleep(5)
        
        accept = driver.find_element(AppiumBy.ACCESSIBILITY_ID, FINAL_CONFIRMATION_SELECTOR)
        accept.click()
        time.sleep(2)
        
        print("Proceso de registro finalizado.")
    except NoSuchElementException:
        print("Objeto no encontrado en pantalla.")
    except Exception as e:
        print(f"Error al ejecutar el caso de prueba: {e}.")
    finally:
        print("Finalizando el caso de prueba...")