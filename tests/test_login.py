from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import time
from helpers.device_permissions import location_permission # Importa desde el helper de permisos
from helpers.ui_helpers import handle_popups  # Importa la función de manejo de pop-ups

def main(driver):
    # Constantes
    EMAIL = 'pasajero@mail.prod'
    PASSWORD = '12345678'
    
    # Selectores
    SELECTORS = {
        'popup_close_button': 'co.picap.passenger:id/collapse_button',
        'email_field': 'new UiSelector().className("android.widget.EditText").instance(0)',
        'password_field': 'new UiSelector().className("android.widget.EditText").instance(1)',
        'login_button': 'Entrar',
        'home_screen': 'Menú\nPestaña 1 de 3',
        'verification_popup': 'Omitir'
    }

    try:
        print("Iniciando el flujo de login en la app...")
        time.sleep(3)
        
        # Manejo de permisos iniciales
        # #! Comentar este bloque si se ejecuta en BrowserStack
        # print("Validando permisos iniciales...")
        # location_permission(driver)  # Llama al método del helper para manejar permisos de ubicación

        # Manejo de pop-ups (al inicio)
        handle_popups(driver, SELECTORS['popup_close_button'])

        # Ingresar credenciales
        print("Ingresando credenciales...")
        try:
            email_field = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, SELECTORS['email_field'])
            password_field = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, SELECTORS['password_field'])
            login_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['login_button'])

            email_field.click()
            email_field.send_keys(EMAIL)
            password_field.click()
            password_field.send_keys(PASSWORD)
            driver.back()  # Ocultar teclado
            print("Credenciales ingresadas correctamente.")

            # Manejo de pop-ups (después de credenciales)
            handle_popups(driver, SELECTORS['popup_close_button'])

            # Intentar iniciar sesión
            print("Intentando iniciar sesión...")
            login_button.click()
            time.sleep(5)

            # Verificar si el login fue exitoso o si aparece un pop-up de verificación
            print("Verificando el login...")
            handle_popups(driver, SELECTORS['popup_close_button'])  # Manejo de pop-ups antes de verificar

            try:
                if driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['home_screen']):
                    print("Login exitoso. Usuario redirigido al home.")
            except NoSuchElementException:
                try:
                    if driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['verification_popup']):
                        print("Login requiere verificación. Pop-up de verificación encontrado.")
                except NoSuchElementException:
                    print("Login fallido o no se encontró el elemento esperado (home o pop-up).")
        except NoSuchElementException:
            print("Error al localizar los elementos de login.")
    except Exception as e:
        print(f"Error al ejecutar el caso de prueba: {e}.")
    finally:
        print("Finalizando el caso de prueba.")
        driver.quit() # Cerrar el driver al finalizar en la nube