from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from difflib import SequenceMatcher
import time

# Función para medir la similitud entre dos textos
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# ! Definir la función de Solicitud de Booking
def booking_request(driver):
    # Definir constantes para XPaths, IDs y otros selectores
    LOCATION_PERMISSION_BUTTON_ID = "com.android.packageinstaller:id/permission_allow_button"
    POPUP_CLOSE_BUTTON_ID = "co.picap.passenger:id/collapse_button"
    
    SERVICE_MOTO_SELECTOR_ID = 'Moto\ncon conductor'
    DESTINATION_SELECTOR_XPATH = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]'
    INPUT_ADDRESS = 'Cl 50 #24-34'
    CONFIRM_SERVICE_ID = 'Seleccionar Moto'
    CONTRACT_CONFIRMATION_ID = 'Confirmar'
    REQUEST_SERVICE_BUTTON_ID = 'Confirmar y pedir'
    CANCEL_SERVICE_X_ID = 'Cancelar viaje'
    TESTING_APP_OP = 'Solo probando la aplicación'
    CANCEL_SERVICE_BUTTON_ID = 'Cancelar servicio'
    CANCEL_CONFIRMATION_OP = 'Aceptar'
    
    try:
        try:
            # Seleccionar el servicio de moto
            service_moto = driver.find_element(AppiumBy.ACCESSIBILITY_ID, SERVICE_MOTO_SELECTOR_ID)
            service_moto.click()
            
            # Ingresar la dirección de destino
            destination_field = driver.find_element(AppiumBy.XPATH, DESTINATION_SELECTOR_XPATH)
            destination_field.click()
            destination_field.send_keys(INPUT_ADDRESS)
            driver.back()  # Ocultar el teclado
            time.sleep(3)  # Esperar que aparezcan las sugerencias dinámicas
            
            # Capturar las sugerencias dinámicas de direcciones a través del atributo content-desc
            suggestions = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.ImageView')
            
            # Filtrar aquellas sugerencias que tengan un content-desc no vacío
            suggestions_with_desc = [s for s in suggestions if s.get_attribute('content-desc')]
            
            # Inicializar variables para la mejor coincidencia
            max_similarity = 0
            best_match = None
            
            print("Comparando...")
            
            # Comparar cada sugerencia con la dirección ingresada
            for suggestion in suggestions_with_desc:
                suggestion_desc = suggestion.get_attribute('content-desc')
                similarity = similar(INPUT_ADDRESS, suggestion_desc)
                if similarity > max_similarity:
                    max_similarity = similarity
                    best_match = suggestion
            
            print("Buscando la mejor coincidencia...")
            
            # Seleccionar la mejor coincidencia
            if best_match:
                best_match.click()
                time.sleep(3)
                print("Dirección seleccionada!!")
            else:
                print("No se encontró una coincidencia adecuada.")
            
            time.sleep(4)
            
            
            # Confirmar la solicitud de Booking
            confirmation_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONFIRM_SERVICE_ID)
            confirmation_button.click()
            
            time.sleep(1)
            
            contract_confirmation = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONTRACT_CONFIRMATION_ID)
            contract_confirmation.click()
            
            time.sleep(4)
            
            request_service_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, REQUEST_SERVICE_BUTTON_ID)
            request_service_button.click()
            
            time.sleep(7)
            
            print("Solicitud de Booking confirmada con éxito!!")
            
            # ! Swipe para cancelar el servicio
            driver.swipe(start_x=driver.get_window_size()['width'] // 2, start_y=driver.get_window_size()['height'] * 0.9, end_x=driver.get_window_size()['width'] // 2, end_y=driver.get_window_size()['height'] * 0.1, duration=500)
            time.sleep(1)
            
            # Cancelar el servicio
            cancel_service = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CANCEL_SERVICE_X_ID)
            cancel_service.click()
            
            testing_app_op = driver.find_element(AppiumBy.ACCESSIBILITY_ID, TESTING_APP_OP)
            testing_app_op.click()
            
            cancel_service_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CANCEL_SERVICE_BUTTON_ID)
            cancel_service_button.click()
            
            cancel_confirmation_op = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CANCEL_CONFIRMATION_OP)
            cancel_confirmation_op.click()
            
            print("Servicio cancelado con éxito!!")
        
        except NoSuchElementException:
            print("Objeto no encontrado en pantalla.")

    except Exception as e:
        print(f"Error al ejecutar el caso de prueba: {e}.")
    finally:
        print("Finalizando el caso de prueba.")
        #driver.quit()
