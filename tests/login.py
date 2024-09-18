# login.py
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import time

# Definir la función de login
def login(driver):
    # Definir constantes para XPaths, IDs y otros selectores
    LOCATION_PERMISSION_BUTTON_ID = "com.android.packageinstaller:id/permission_allow_button"
    POPUP_CLOSE_BUTTON_ID = "co.picap.passenger:id/collapse_button"
    
    EMAIL_SELECTOR = 'new UiSelector().className("android.widget.EditText").instance(0)'
    PASSWORD_SELECTOR = 'new UiSelector().className("android.widget.EditText").instance(1)'
    LOGIN_BUTTON_ACCESSIBILITY_ID = "Entrar"
    HOME_SCREEN_ACCESSIBILITY_ID = "Menú\nPestaña 1 de 3"

    try:
        # Manejo de permisos de ubicación
        try:
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Aceptar").click()  # Modal inicial
            driver.find_element(AppiumBy.ID, LOCATION_PERMISSION_BUTTON_ID).click()  # Permiso de ubicación
            print("Permiso de ubicación concedido!!")
        except NoSuchElementException:
            print("No se solicitaron permisos de ubicación.")
            
        time.sleep(2)  # Esperar 2 segundos

        # Manejo de pop-ups (si existen)
        try:
            driver.find_element(AppiumBy.ID, POPUP_CLOSE_BUTTON_ID).click()
            print("Popup encontrado y cerrado!!")
        except NoSuchElementException:
            print("No se encontró ningún popup. Continuando...")

        # Localizar los elementos de login
        try:
            email_field = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, EMAIL_SELECTOR)
            password_field = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, PASSWORD_SELECTOR)
            login_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, LOGIN_BUTTON_ACCESSIBILITY_ID)

            # Ingresar credenciales
            email_field.click()
            email_field.send_keys('pasajero@mail.prod')

            password_field.click()
            password_field.send_keys('12345678')
            driver.back()  # Ocultar el teclado

            # Hacer clic en el botón de login
            login_button.click()
            print("Intentando iniciar sesión...")

            # Esperar unos segundos para que el login se procese
            time.sleep(5)

            # Verificar si el login fue exitoso
            try:
                driver.find_element(AppiumBy.ACCESSIBILITY_ID, HOME_SCREEN_ACCESSIBILITY_ID)
                print("Login exitoso. Elemento de pantalla principal encontrado!!")
            except NoSuchElementException:
                print("Login fallido o no se encontró el elemento de la pantalla principal.")

        except NoSuchElementException as e:
            print(f"Error al intentar localizar un elemento de login: {e}.")
    
    except Exception as e:
        print(f"Error al ejecutar el caso de prueba: {e}.")
    finally:
        driver.quit()
