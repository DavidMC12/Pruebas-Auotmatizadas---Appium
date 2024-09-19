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
    
    SERVICE_PIBOX_SELECTOR_ID = 'Mensajería'
    DELIVERY_DESTINATION_SELECTOR_XPATH = '//android.view.View[@text="Dirección de entrega"]'
    DELIVERY_DESTINATION_SELECTOR_ClASSNAME_2 = 'android.widget.EditText'
    INPUT_ADDRESS = 'Cl 50 #24-34'
    ADITIONAL_INFO_SELECTOR_XPATH = '//android.widget.EditText'
    CONFIRM_SERVICE_ID = 'Continuar'
    
    # ? Formulario de paquete
    INDICATIONS_SELECTOR_XPATH = '//android.widget.ScrollView/android.widget.EditText[1]'
    TARGET_SELECTOR_XPATH = '//android.widget.ScrollView/android.widget.EditText[2]'
    PHONE_SELECTOR_XPATH = '//android.widget.ScrollView/android.widget.EditText[3]'
    DECLARED_VALUE_SELECTOR_XPATH = '//android.widget.ScrollView/android.widget.EditText[4]'
    PACKAGE_SIZE_SELECTOR_ID = 'Pequeño (Max 20x20x20)'
    
    CREATE_PIBOX_BUTTON_SELECTOR_ID = 'Crear'
    REQUEST_BUTTON_ID = 'Solicitar'
    REQUEST_BUTTON_ID_2 = 'Solicitar'
    
    # ? Cancelar servicio
    CANCEL_SERVICE_X_ID = 'Cancelar viaje'
    CONFIRMATION_POPUP = 'Si'
    TESTING_APP_OP = 'Solo probando la aplicación'
    CANCELATION_BUTTON = 'Aceptar'
    
    try:
        try:
            print("Iniciando el proceso de solicitud de servicio de Pibox...")
            # Seleccionar el servicio de Pibox
            service_pibox = driver.find_element(AppiumBy.ACCESSIBILITY_ID, SERVICE_PIBOX_SELECTOR_ID)
            service_pibox.click()
            
            # Ingresar la dirección de destino
            delivery_destination_field = driver.find_element(AppiumBy.XPATH, DELIVERY_DESTINATION_SELECTOR_XPATH)
            delivery_destination_field.click()
            time.sleep(1)
            
            delivery_destination_field_2 = driver.find_element(AppiumBy.CLASS_NAME, DELIVERY_DESTINATION_SELECTOR_ClASSNAME_2)
            delivery_destination_field_2.click()
            delivery_destination_field_2.send_keys(INPUT_ADDRESS)
            driver.back()  # Ocultar el teclado
            time.sleep(4)  # Esperar que aparezcan las sugerencias dinámicas
            
            print("Se puso la dirección de destino!!")
            
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
            
            # Ingresar información adicional
            aditional_info = driver.find_element(AppiumBy.XPATH, ADITIONAL_INFO_SELECTOR_XPATH)
            aditional_info.click()
            aditional_info.send_keys("Entregar a la recepción.")
            driver.back()  # Ocultar el teclado
            
            # Confirmar la solicitud del envío
            confirmation_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONFIRM_SERVICE_ID)
            confirmation_button.click()
            
            time.sleep(2)
            
            # ! Formulario de paquete
            # * Indicaciones
            indications = driver.find_element(AppiumBy.XPATH, INDICATIONS_SELECTOR_XPATH)
            indications.click()
            indications.send_keys("Dejarlo en portería.")
            
            # * Destinatario
            target = driver.find_element(AppiumBy.XPATH, TARGET_SELECTOR_XPATH)
            target.click()
            target.send_keys("Juan Perez")
            
            # * Teléfono
            phone = driver.find_element(AppiumBy.XPATH, PHONE_SELECTOR_XPATH)
            phone.click()
            phone.send_keys("3001234567")
            driver.back()
            
            # * Valor declarado
            declared_value = driver.find_element(AppiumBy.XPATH, DECLARED_VALUE_SELECTOR_XPATH)
            declared_value.click()
            declared_value.send_keys("12000")
            driver.back()
            
            # * Scroll
            driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=1000, duration=1000)
            
            # * Seleccionar tamaño del paquete
            package_size = driver.find_element(AppiumBy.ACCESSIBILITY_ID, PACKAGE_SIZE_SELECTOR_ID)
            package_size.click()
            
            time.sleep(1)
            
            # Crear el servicio de Pibox
            create_pibox_service_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CREATE_PIBOX_BUTTON_SELECTOR_ID)
            create_pibox_service_button.click()
            time.sleep(1)
            
            # Solicitar el servicio de Pibox
            request_service_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, REQUEST_BUTTON_ID)
            request_service_button.click()
            time.sleep(2)
            
            # Confirmacion de final de solicitud
            request_service_button_2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, REQUEST_BUTTON_ID_2)
            request_service_button_2.click()
            time.sleep(2)
            
            print("Solicitud de Booking confirmada con éxito!!")
            
            # # ! Swipe para cancelar el servicio
            driver.swipe(start_x=driver.get_window_size()['width'] // 2, start_y=driver.get_window_size()['height'] * 0.9, end_x=driver.get_window_size()['width'] // 2, end_y=driver.get_window_size()['height'] * 0.1, duration=500)
            time.sleep(1)
            
            # Cancelar el servicio
            cancel_service = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CANCEL_SERVICE_X_ID)
            cancel_service.click()
            
            pop_up_close = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONFIRMATION_POPUP)
            pop_up_close.click()
            
            testing_app_op = driver.find_element(AppiumBy.ACCESSIBILITY_ID, TESTING_APP_OP)
            testing_app_op.click()
            
            cancel_service_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CANCELATION_BUTTON)
            cancel_service_button.click()
            time.sleep(1)
            driver.back()
            
            print("Servicio cancelado con éxito!!")
        
        except NoSuchElementException:
            print("Objeto no encontrado en pantalla.")

    except Exception as e:
        print(f"Error al ejecutar el caso de prueba: {e}.")
    finally:
        print("Finalizando el caso de prueba.")
        #driver.quit()
