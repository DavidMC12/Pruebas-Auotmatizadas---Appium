from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import time
import sys

# Definir la función de Registro
def signUp(driver):
    # Definir constantes para XPaths, IDs y otros selectores
    LOCATION_PERMISSION_BUTTON_ID = "com.android.packageinstaller:id/permission_allow_button"
    POPUP_CLOSE_BUTTON_ID = "co.picap.passenger:id/collapse_button"
    
    REGISTER_BUTTON_SECTION_ID = "Registrate\nPestaña 2 de 2"
    PHONE_PERMISSION_BUTTON_ID = "com.android.packageinstaller:id/permission_allow_button"
    
    NAME_SELECTOR = 'new UiSelector().className("android.widget.EditText").instance(0)'
    LAST_NAME_SELECTOR = 'new UiSelector().className("android.widget.EditText").instance(1)'
    EMAIL_SELECTOR = 'new UiSelector().className("android.widget.EditText").instance(2)'
    PASSWORD_SELECTOR = 'new UiSelector().className("android.widget.EditText").instance(3)'
    REGION_LIST_SELECTOR = '+57'
    COLOMBIA = '+57   Colombia'
    PHONE_NUMBER_SELECTOR = 'new UiSelector().className("android.widget.EditText").instance(4)'
    SEX_SELECTOR = 'new UiSelector().className("android.widget.RadioButton").instance(1)'
    REGISTER_BUTTON_ACCESSIBILITY_ID = "Entrar"
    
    VERIFICATION_USER_POPUP_ACCESSIBILITY_ID = "Omitir"    
    HOME_SCREEN_ACCESSIBILITY_ID = "Menú\nPestaña 1 de 3"
    
    try:
        # ? 1. Manejo de permisos de ubicación
        try:
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Aceptar").click()  # Modal inicial
            driver.find_element(AppiumBy.ID, LOCATION_PERMISSION_BUTTON_ID).click()  # Permiso de ubicación
            print("Permiso de ubicación concedido!!")
        except NoSuchElementException:
            print("No se solicitaron permisos de ubicación.")

        # * Manejo de pop-ups (si existen)
        try:
            driver.find_element(AppiumBy.ID, POPUP_CLOSE_BUTTON_ID).click()
            print("Validación 1: Popup encontrado y cerrado!!")
        except NoSuchElementException:
            print("Validación 1: No se encontró ningún popup. Continuando...")
        
        # ? 2. Localizar botón de registro
        try:
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, REGISTER_BUTTON_SECTION_ID).click()
            print("Botón de registro encontrado y clickeado!!")
        except NoSuchElementException:
            print("No se encontró el botón de registro. Finalizando...")
            sys.exit(1) # ! Salir del script
        
        time.sleep(2)  # Esperar 2 segundos
        
        # * Manejo de pop-ups (si existen)
        try:
            driver.find_element(AppiumBy.ID, POPUP_CLOSE_BUTTON_ID).click()
            print("Validación 2: Popup encontrado y cerrado!!")
        except NoSuchElementException:
            print("Validación 2: No se encontró ningún popup. Continuando...")
        
        # ? 3. Permisos de Telefono
        try:
            driver.find_element(AppiumBy.ID, PHONE_PERMISSION_BUTTON_ID).click()
            print("Permiso de telefono concedido!!")
        except NoSuchElementException:
            print("No se solicitaron permisos de telefono.")
        
        time.sleep(2)  # Esperar 2 segundos
        
        # * Manejo de pop-ups (si existen)
        try:
            driver.find_element(AppiumBy.ID, POPUP_CLOSE_BUTTON_ID).click()
            print("Validación 3: Popup encontrado y cerrado!!")
        except NoSuchElementException:
            print("Validación 3: No se encontró ningún popup. Continuando...")
        
        # ? 4. Localizar los elementos de registro
        try:
            name_field = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, NAME_SELECTOR)
            last_name_field = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, LAST_NAME_SELECTOR)
            email_field = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, EMAIL_SELECTOR)
            password_field = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, PASSWORD_SELECTOR)
            
            list_region = driver.find_element(AppiumBy.ACCESSIBILITY_ID, REGION_LIST_SELECTOR)
            
            phone_filed = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, PHONE_NUMBER_SELECTOR)
            sex_to_set = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, SEX_SELECTOR)
            
            register_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, REGISTER_BUTTON_ACCESSIBILITY_ID)
            
            # * Manejo de pop-ups (si existen)
            try:
                driver.find_element(AppiumBy.ID, POPUP_CLOSE_BUTTON_ID).click()
                print("Validación 4: Popup encontrado y cerrado!!")
            except NoSuchElementException:
                print("Validación 4: No se encontró ningún popup. Continuando...")

            # ? 5. Ingresar credenciales
            name_field.click()
            name_field.send_keys('Usuario Prueba')
            
            last_name_field.click()
            last_name_field.send_keys('Automatizado Prod')
            
            email_field.click()
            email_field.send_keys('u.aut2@mail.prod')
            
            password_field.click()
            password_field.send_keys('123456')
            driver.back()
            
            # ? 6. Listar regiones y seleccionar Colombia
            list_region.click()
            driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=130, duration=180)
            colombia = driver.find_element(AppiumBy.ACCESSIBILITY_ID, COLOMBIA)
            colombia.click()
            
            phone_filed.click()
            phone_filed.send_keys('3214445552')
            driver.back()
            
            # Setear sexo hombre
            sex_to_set.click()
            
            # Hacer clic en el botón de registro
            register_button.click()
            
            # Esperar unos segundos para que el registro se procese
            time.sleep(15)
            
            # ? 7. Manejo de pop-up (Omitir verificación del usuario)
            try:
                driver.find_element(AppiumBy.ACCESSIBILITY_ID, VERIFICATION_USER_POPUP_ACCESSIBILITY_ID).click()
                print("Popup de verificación encontrado y cerrado!!")
            except NoSuchElementException:
                print("No se encontró ningún popup. Continuando...")
            time.sleep(3)
            
            # ? 7.2. Manejo de pop-up (Omitir verificación del usuario, seguridad)
            # Obtener el tamaño de la pantalla del dispositivo
            screen_size = driver.get_window_size()
            screen_width = screen_size['width']
            screen_height = screen_size['height']
            
            x_relative = 0.5  # Ejemplo: 50% del ancho de la pantalla
            y_relative = 0.85  # Ejemplo: 85% de la altura de la pantalla
            
            # Convertir las coordenadas relativas a coordenadas absolutas
            x = int(screen_width * x_relative)
            y = int(screen_height * y_relative)
            
            driver.tap([(x, y)], 500)
            print(f"Se hizo clic en las coordenadas: X={x}, Y={y}")
            time.sleep(2)            
            
            # ? 8. Verificar si el registro fue exitoso
            try:
                driver.find_element(AppiumBy.ACCESSIBILITY_ID, HOME_SCREEN_ACCESSIBILITY_ID)
                print("Registro exitoso. Elemento de pantalla principal encontrado!!")
            except NoSuchElementException:
                print("Registro fallido o no se encontró el elemento de la pantalla principal.")
        
        except NoSuchElementException as e:
            print(f"Error al intentar localizar un elemento del registro: {e}.")

    except Exception as e:
        print(f"Error al ejecutar el caso de prueba: {e}.")
    finally:
        print("Finalizando el proceso de registro...")
        #driver.quit()