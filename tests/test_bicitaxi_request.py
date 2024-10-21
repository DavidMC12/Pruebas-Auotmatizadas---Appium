from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from difflib import SequenceMatcher
import time

# ! Variable para definir si se debe ingresar una dirección o no
ingresar_direccion = "No ingresar"  # ? Cambiar a "No ingresar" para el otro caso

# Función para medir la similitud entre dos textos
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# ? Método para ejecutar sin dirección de destino
def bicitaxi_request_without_adresss(driver):
    # Definir constantes para XPaths, IDs y otros selectores
    BICITAXI_SELECTOR_ID = 'Bicitaxi'
    CONFIRM_TRIP_BUTTON_ID = 'Confirmar'
    SELECT_BICITAXI_BUTTON_ID = 'Seleccionar bicitaxi'
    
    OFFERED_PRICE_FIELD_SELECTOR_ID = 'Cuanto quieres ofertar por el servicio\n$ 2.000 COP'
    OFFER_FARE_SELECTOR_XPATH = '//android.widget.EditText[@text="$ 2.000"]'
    CONFIRM_OFERR_BUTTON_ID = 'Confirmar'
    OFFER_BUTTON_ID = 'Ofertar'
    
    CANCEL_SERVICE_X_ID = 'Cancelar viaje'
    TESTING_APP_OP = 'Solo probando la aplicación'
    CANCEL_SERVICE_BUTTON_ID = 'Cancelar servicio'
    CANCEL_CONFIRMATION_OP = 'Aceptar'
    
    try:
        print("Iniciando el proceso de solicitud de Bicitaxi sin dirección...")
        # Selección del Bicitaxi - Home
        bicitaxi_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, BICITAXI_SELECTOR_ID)
        bicitaxi_button.click()
        time.sleep(1)
        
        # Confirmar viaje
        print("Confirmando el viaje...")
        confirm_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONFIRM_TRIP_BUTTON_ID)
        confirm_button.click()
        time.sleep(8)
        
        # Confirma el Botón del Eta
        print("Confirmando el botón del ETA...")
        confirm_eta_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECT_BICITAXI_BUTTON_ID)
        confirm_eta_button.click()
        time.sleep(1)
        
        # ! Envíos de Tarifa, si son requeridos: No está del todo funcional
        # to_offer_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, OFFERED_PRICE_FIELD_SELECTOR_ID)
        # to_offer_field.click()
        
        # # Campo tarifa
        # offer_field = driver.find_element(AppiumBy.XPATH, OFFER_FARE_SELECTOR_XPATH)
        # offer_field.click()
        # driver.back()
        # offer_field.send_keys(Keys.CONTROL, 'a')  # Reemplazo de texto
        # time.sleep(1)
        # offer_field.send_keys("2500")
        # driver.back()
        
        # # Botón de confirmación de la tarifa
        # confirm_fare_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONFIRM_OFERR_BUTTON_ID)
        # confirm_fare_button.click()
        # time.sleep(1)
        
        #Solicitud de servicio
        print("Solicitando el servicio...")
        offer_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, OFFER_BUTTON_ID)
        offer_button.click()
        time.sleep(3)
        
        # ! Cancelar el servicio
        driver.swipe(start_x=driver.get_window_size()['width'] // 2, start_y=driver.get_window_size()['height'] * 0.9, end_x=driver.get_window_size()['width'] // 2, end_y=driver.get_window_size()['height'] * 0.1, duration=500)
        time.sleep(3)
        
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
        print("Finalizando el caso de prueba...")

# ? Método para ejecutar ingresando una dirección
def bicitaxi_request_with_adress(driver):
    # Definir constantes para XPaths, IDs y otros selectores
    BICITAXI_SELECTOR_ID = 'Bicitaxi'
    CONFIRM_TRIP_BUTTON_ID = 'Confirmar'
    SELECT_BICITAXI_BUTTON_ID = 'Seleccionar bicitaxi'
    
    OFFERED_PRICE_FIELD_SELECTOR_ID = 'Cuanto quieres ofertar por el servicio\n$ 2.000 COP'
    OFFER_FARE_SELECTOR_XPATH = '//android.widget.EditText[@text="$ 2.000"]'
    CONFIRM_OFERR_BUTTON_ID = 'Confirmar'
    OFFER_BUTTON_ID = 'Ofertar'
    
    # Con dirección
    SKIP_CONFIRMATION_BUTTON_ID = 'Saltar'
    DESTINATION_SELECTOR_XPATH = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]'
    INPUT_ADDRESS = 'Cl 150A #99-50'
    
    
    CANCEL_SERVICE_X_ID = 'Cancelar viaje'
    TESTING_APP_OP = 'Solo probando la aplicación'
    CANCEL_SERVICE_BUTTON_ID = 'Cancelar servicio'
    CANCEL_CONFIRMATION_OP = 'Aceptar'
    
    try:
        print("Iniciando el proceso de solicitud de Bicitaxi ingresando una dirección...")
        # Selección del Bicitaxi - Home
        bicitaxi_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, BICITAXI_SELECTOR_ID)
        bicitaxi_button.click()
        time.sleep(1)
        
        # Saltar confirmación
        print("Saltando la confirmación...")
        skip_confirmation_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, SKIP_CONFIRMATION_BUTTON_ID)
        skip_confirmation_button.click()
        
        # Ingresar la dirección de destino
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
            time.sleep(4)
            print("Dirección seleccionada!!")
        else:
            print("No se encontró una coincidencia adecuada.")
        
        time.sleep(4)
        
        # # Confirmar viaje
        # print("Confirmando el viaje...")
        # confirm_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONFIRM_TRIP_BUTTON_ID)
        # confirm_button.click()
        # time.sleep(8)
        
        # Confirma el Botón del Eta
        print("Confirmando el botón del ETA...")
        confirm_eta_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECT_BICITAXI_BUTTON_ID)
        confirm_eta_button.click()
        time.sleep(1)
        
        # ! Envíos de Tarifa, si son requeridos: No está del todo funcional
        # to_offer_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, OFFERED_PRICE_FIELD_SELECTOR_ID)
        # to_offer_field.click()
        
        # # Campo tarifa
        # offer_field = driver.find_element(AppiumBy.XPATH, OFFER_FARE_SELECTOR_XPATH)
        # offer_field.click()
        # driver.back()
        # offer_field.send_keys(Keys.CONTROL, 'a')  # Reemplazo de texto
        # time.sleep(1)
        # offer_field.send_keys("2500")
        # driver.back()
        
        # # Botón de confirmación de la tarifa
        # confirm_fare_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONFIRM_OFERR_BUTTON_ID)
        # confirm_fare_button.click()
        # time.sleep(1)
        
        #Solicitud de servicio
        print("Solicitando el servicio...")
        offer_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, OFFER_BUTTON_ID)
        offer_button.click()
        time.sleep(3)
        
        # ! Cancelar el servicio
        driver.swipe(start_x=driver.get_window_size()['width'] // 2, start_y=driver.get_window_size()['height'] * 0.9, end_x=driver.get_window_size()['width'] // 2, end_y=driver.get_window_size()['height'] * 0.1, duration=500)
        time.sleep(3)
        
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
        print("Finalizando el caso de prueba...")

# Ejecutar el caso de prueba basado en el valor de la variable
def main(driver):
    if ingresar_direccion == "Ingresar":
        bicitaxi_request_with_adress(driver)
    elif ingresar_direccion == "No ingresar":
        bicitaxi_request_without_adresss(driver)
    else:
        print(f"Opción no válida: {ingresar_direccion}")
