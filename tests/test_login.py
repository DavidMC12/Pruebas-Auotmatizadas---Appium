from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import time

def main(driver):
    # Constantes
    EMAIL = 'pasajero@mail.prod'
    PASSWORD = '12345678'
    
    # Selectores
    SELECTORS = {
        'accept_button': 'Aceptar',
        'location_permission_button': 'com.android.packageinstaller:id/permission_allow_button',
        'popup_close_button': 'co.picap.passenger:id/collapse_button',
        'email_field': 'new UiSelector().className("android.widget.EditText").instance(0)',
        'password_field': 'new UiSelector().className("android.widget.EditText").instance(1)',
        'login_button': 'Entrar',
        'home_screen': 'Menú\nPestaña 1 de 3',
        'verification_popup': 'Omitir'
    }

    try:
        print("Iniciando el flujo de login en la app...")
        
        # Manejo de permisos iniciales
        print("Validando permisos iniciales...")
        try:
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['accept_button']).click()
            driver.find_element(AppiumBy.ID, SELECTORS['location_permission_button']).click()
            print("Permiso de ubicación concedido.")
        except NoSuchElementException:
            print("No se solicitaron permisos de ubicación.")
        time.sleep(2)

        # Manejo de pop-ups
        print("Validando la presencia de pop-ups...")
        try:
            driver.find_element(AppiumBy.ID, SELECTORS['popup_close_button']).click()
            print("Popup encontrado y cerrado.")
        except NoSuchElementException:
            print("No se encontró ningún popup.")

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

            # Intentar iniciar sesión
            print("Intentando iniciar sesión...")
            login_button.click()
            time.sleep(5)

            # Verificar si el login fue exitoso o si aparece un pop-up de verificación
            print("Verificando el login...")
            try:
                # Intentar localizar un elemento del home
                if driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['home_screen']):
                    print("Login exitoso. Usuario redirigido al home.")
            except NoSuchElementException:
                try:
                    # Intentar localizar un elemento del pop-up de verificación
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