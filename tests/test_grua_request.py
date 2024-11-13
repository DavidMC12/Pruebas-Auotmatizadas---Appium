from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from difflib import SequenceMatcher
import time

# Función para medir la similitud entre dos textos
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Función Principal
def gura_request(driver):
    # Definir constantes para XPaths, IDs y otros selectores
    GRUA_SELECTOR_ID = 'Grúa'
    CONTINUE_BUTTON_ID = 'Continuar'
    DESTINATION_SELECTOR_XPATH = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]'
    
    INPUT_ADDRESS = 'Cl 50 #24-34'
    
    GRUA_ETA_SELECTOR_ID = 'Seleccionar Grúa'
    
    BRAND_SELECTOR_XPATH = '//android.widget.ImageView[@content-desc="Confirma los datos del vehiculo"]/android.widget.EditText[1]'
    PLATES_SELECTOR_XPATH = '//android.widget.ImageView[@content-desc="Confirma los datos del vehiculo"]/android.widget.EditText[2]'
    CONTINUE_BUTTON_ID_2 = 'Continuar'
    CONFIRM_AND_ORDER_BUTTON_ID = 'Confirmar y pedir'
    
    CANCEL_SERVICE_X_ID = 'Cancelar viaje'
    TESTING_APP_OP = 'Solo probando la aplicación'
    CANCEL_SERVICE_BUTTON_ID = 'Cancelar servicio'
    CANCEL_CONFIRMATION_OP = 'Aceptar'
    
    try:
        try:
            print("Iniciando el proceso de solicitud de Grúa...")\
            
            # * 1. Seleccionar el servicio de grúa
            grua_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, GRUA_SELECTOR_ID)
            grua_button.click()
            time.sleep(1)
            
            continue_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONTINUE_BUTTON_ID)
            continue_button.click()
            time.sleep(2)
            
            # * 2. Ingresar la dirección de destino
            destination_field = driver.find_element(AppiumBy.XPATH, DESTINATION_SELECTOR_XPATH)
            destination_field.click()
            destination_field.send_keys(INPUT_ADDRESS)
            driver.back()  # Ocultar el teclado
            time.sleep(5)  # Esperar que aparezcan las sugerencias dinámicas
            
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
                print("Dirección seleccionada!!")
                time.sleep(4)
            else:
                print("No se encontró una coincidencia adecuada.")
            
            time.sleep(4)
            
            # * 3. Confirmar la solicitud de Booking
            selector_grua = driver.find_element(AppiumBy.ACCESSIBILITY_ID, GRUA_ETA_SELECTOR_ID)
            selector_grua.click()
            time.sleep(1)
            
            brand_field = driver.find_element(AppiumBy.XPATH, BRAND_SELECTOR_XPATH)
            brand_field.click()
            brand_field.send_keys('Suzuki')
            driver.back()
            
            plates_field = driver.find_element(AppiumBy.XPATH, PLATES_SELECTOR_XPATH)
            plates_field.click()
            plates_field.send_keys('ABC123')
            driver.back()
            
            continue_button_2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONTINUE_BUTTON_ID_2)
            continue_button_2.click()
            time.sleep(5)
            
            confirm_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONFIRM_AND_ORDER_BUTTON_ID)
            confirm_button.click()
            time.sleep(6)
            
            # ! 4. Cancelación de la solicitud
            # Swipe para cancelar el servicio
            driver.swipe(start_x=500, start_y=1700, end_x=500, end_y=300, duration=500)
            time.sleep(2)
            
            # Cancelar el servicio
            cancel_service = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CANCEL_SERVICE_X_ID)
            cancel_service.click()
            
            testing_app_op = driver.find_element(AppiumBy.ACCESSIBILITY_ID, TESTING_APP_OP)
            testing_app_op.click()
            
            cancel_service_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CANCEL_SERVICE_BUTTON_ID)
            cancel_service_button.click()
            
            cancel_confirmation_op = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CANCEL_CONFIRMATION_OP)
            cancel_confirmation_op.click()
            driver.back()
            
            print("Servicio cancelado con éxito!!")
            time.sleep(3)
            
        except NoSuchElementException:
            print("Objeto no encontrado en pantalla.")

    except Exception as e:
        print(f"Error al ejecutar el caso de prueba: {e}.")
    finally:
        print("Finalizando el caso de prueba...")
        #driver.quit()