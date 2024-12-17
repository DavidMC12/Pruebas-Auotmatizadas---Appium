from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
from helpers.device_permissions import location_permission, phone_permission
from helpers.ui_helpers import handle_popups, tap_circle

# Selectores
SELECTORS = {
    "location_permission_button": "com.android.packageinstaller:id/permission_allow_button",
    "popup_close_button": "co.picap.passenger:id/collapse_button",
    "register_button_section": "Registrate\nPestaña 2 de 2",
    "phone_permission_button": "com.android.packageinstaller:id/permission_allow_button",
    "name_field": 'new UiSelector().className("android.widget.EditText").instance(0)',
    "last_name_field": 'new UiSelector().className("android.widget.EditText").instance(1)',
    "email_field": 'new UiSelector().className("android.widget.EditText").instance(2)',
    "password_field": 'new UiSelector().className("android.widget.EditText").instance(3)',
    "region_list": "+57",
    "colombia": "+57   Colombia",
    "phone_field": 'new UiSelector().className("android.widget.EditText").instance(4)',
    "sex_field": 'new UiSelector().className("android.widget.RadioButton").instance(1)',
    "register_button": "Entrar",
    "verification_user_popup": "Omitir",
    "home_screen_popup": "Omitir",
}

# Función de registro
def main(driver):
    try:
        print("Iniciando el proceso de registro...")
        
        # # Manejo de permisos iniciales
        # #! Comentar este bloque si se ejecuta en BrowserStack
        # print("Validando permisos iniciales...")
        # location_permission(driver)  # Llama al método del helper para manejar permisos de ubicación

        # Localizar y hacer clic en el botón de registro
        print("Intentando acceder a la sección de registro...")
        try:
            time.sleep(1)
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS["register_button_section"]).click()
            print("Sección de registro abierta.")
        except NoSuchElementException:
            print("No se encontró el botón de registro. Finalizando...")
            sys.exit(1)

        # # Manejo de permisos adicionales
        # #! Comentar este bloque si se ejecuta en BrowserStack
        # print("Validando permisos adicionales...")
        # phone_permission(driver)

        # Manejo de pop-ups posteriores
        handle_popups(driver, SELECTORS["popup_close_button"])

        # Ingresar credenciales y datos de registro
        print("Ingresando datos de registro...")
        fields = {
            "name": (SELECTORS["name_field"], "Usuario Prueba"),
            "last_name": (SELECTORS["last_name_field"], "Automatizado Prod"),
            "email": (SELECTORS["email_field"], "u.aut25@mail.prod"),
            "password": (SELECTORS["password_field"], "123456"),
            "phone": (SELECTORS["phone_field"], "3214445525"),
        }

        for key, (selector, value) in fields.items():
            field = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
            field.click()
            field.send_keys(value)
            print(f"{key.capitalize()} ingresado: {value}")
            if key != "password":
                driver.back()

        # # Seleccionar región
        # print("Seleccionando región...") #! Deprecated online
        # driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS["region_list"]).click()
        # time.sleep(1)
        # driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=130, duration=180)
        # driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS["colombia"]).click()
        # driver.back()
        # time.sleep(1)

        # Seleccionar sexo
        print("Seleccionando sexo...")
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, SELECTORS["sex_field"]).click()

        # Hacer clic en el botón de registro
        print("Finalizando registro...")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS["register_button"]).click()

        # Manejo de pop-ups de verificación
        print("Verificando el registro...")
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, SELECTORS["verification_user_popup"]))
            ).click()
            print("Popups de verificación cerrado.")
        except NoSuchElementException:
            print("No se encontró ningún popup de verificación. Continuando...")
        time.sleep(2)
        tap_circle(driver, x_center_ratio=0.49, y_center_ratio=0.87, radius_ratio=0.05, num_points=3) # Toca la pantalla para cerrar el segundo banner de verificación
        time.sleep(1)

        # Verificar éxito del registro
        print("Verificando si el registro fue exitoso...")
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, SELECTORS["home_screen_popup"]))
            ).click()
            print("Registro exitoso. Pantalla principal cargada.")
        except NoSuchElementException:
            print("Registro fallido. No se cargó la pantalla principal.")

    except Exception as e:
        print(f"Error al ejecutar el caso de prueba: {e}")
    finally:
        print("Finalizando el proceso de registro...")
        driver.quit() # Cierra el driver al finalizar, descomentar para ejecutar en la nube