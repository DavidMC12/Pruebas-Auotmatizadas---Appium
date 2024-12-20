from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from difflib import SequenceMatcher
from helpers.ui_helpers import cancel_service_flow
import time

# Función para medir la similitud entre dos textos
def calculate_similarity(text1, text2):
    return SequenceMatcher(None, text1, text2).ratio()

def booking_request(driver):
    """
    Flujo para realizar una solicitud de booking en la aplicación móvil.

    Args:
        driver: Instancia del controlador de Appium.
    """
    # Constantes de selectores
    SELECTORS = {
        "location_permission_button": "com.android.packageinstaller:id/permission_allow_button",
        "popup_close_button": "co.picap.passenger:id/collapse_button",
        "service_moto": "Moto\ncon conductor",
        "destination_field": '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]',
        "confirm_service": "Seleccionar Moto",
        "contract_confirmation": "Confirmar",
        "request_service_button": "Confirmar y pedir"
    }

    INPUT_ADDRESS = "Cl 50 #24-34"

    try:
        print("Iniciando flujo de booking...")

        # Seleccionar el servicio de moto
        print("Seleccionando el servicio de moto...")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS["service_moto"]).click()
        print("Servicio de moto seleccionado.")

        # Ingresar la dirección de destino
        print("Ingresando la dirección de destino...")
        destination_field = driver.find_element(AppiumBy.XPATH, SELECTORS["destination_field"])
        destination_field.click()
        destination_field.send_keys(INPUT_ADDRESS)
        driver.back()  # Ocultar el teclado
        time.sleep(2)
        print(f"Dirección ingresada: {INPUT_ADDRESS}")

        # Capturar sugerencias dinámicas y encontrar la mejor coincidencia
        print("Capturando sugerencias dinámicas...")
        suggestions = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.ImageView')
        suggestions_with_desc = [s for s in suggestions if s.get_attribute('content-desc')]

        max_similarity = 0
        best_match = None

        print("Comparando sugerencias...")
        for suggestion in suggestions_with_desc:
            suggestion_desc = suggestion.get_attribute('content-desc')
            similarity = calculate_similarity(INPUT_ADDRESS, suggestion_desc)
            print(f"Sugerencia: {suggestion_desc}, Similitud: {similarity}")
            if similarity > max_similarity:
                max_similarity = similarity
                best_match = suggestion

        if best_match:
            print("Seleccionando la mejor coincidencia...")
            best_match.click()
            time.sleep(2)
            print("Mejor coincidencia seleccionada.")
        else:
            print("No se encontró una coincidencia adecuada.")
            raise NoSuchElementException("No se encontró una coincidencia adecuada para la dirección.")

        time.sleep(5)

        # Confirmar la solicitud de booking
        print("Confirmando la solicitud de booking...")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS["confirm_service"]).click()
        print("Solicitud de booking confirmada.")

        time.sleep(1)

        print("Confirmando el contrato...")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS["contract_confirmation"]).click()
        print("Contrato confirmado.")

        time.sleep(5)

        print("Realizando la solicitud de servicio...")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS["request_service_button"]).click()
        time.sleep(5)
        print("Solicitud de servicio realizada con éxito.")

        #! Cancelar el servicio
        print("Iniciando flujo para cancelar el servicio...")
        cancel_service_flow(driver)
        print("Servicio cancelado correctamente.")

        driver.quit()  # Finalizar la sesión de Appium (Dejar la línea si se ejecuta en la nube)

    except NoSuchElementException as e:
        print(f"Elemento no encontrado: {e}")

    except Exception as e:
        print(f"Error durante el flujo de booking: {e}")

    finally:
        print("Finalizando el caso de prueba.")