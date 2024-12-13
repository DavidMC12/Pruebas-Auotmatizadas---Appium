from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from difflib import SequenceMatcher
import time

# Función para medir la similitud entre dos textos
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def schedule_service(driver):
    # Establecer los puntos de inicio y fin para el swipe en cada sección
    day_start_x, day_start_y, day_end_x, day_end_y = 280, 1682, 280, 1550 # * El último dígito debe cambiarse para hacer swipe en la fecha deseada
    hour_start_x, hour_start_y, hour_end_x, hour_end_y = 573, 1682, 573, 1450
    minute_start_x, minute_start_y, minute_end_x, minute_end_y = 718, 1682, 718, 1350
    ampm_start_x, ampm_start_y, ampm_end_x, ampm_end_y = 905, 1682, 905, 1550
    
    # Realizar el swipe para el día
    driver.swipe(day_start_x, day_start_y, day_end_x, day_end_y, 800)
    
    # Realizar el swipe para la hora
    driver.swipe(hour_start_x, hour_start_y, hour_end_x, hour_end_y, 800)
    
    # Realizar el swipe para los minutos
    driver.swipe(minute_start_x, minute_start_y, minute_end_x, minute_end_y, 800)
    
    # Realizar el swipe para AM/PM
    #driver.swipe(ampm_start_x, ampm_start_y, ampm_end_x, ampm_end_y, 500)


# ! Definir la función de Solicitud de Booking
def booking_request(driver):
    # Definir constantes para XPaths, IDs y otros selectores
    LOCATION_PERMISSION_BUTTON_ID = "com.android.packageinstaller:id/permission_allow_button"
    POPUP_CLOSE_BUTTON_ID = "co.picap.passenger:id/collapse_button"
    
    DESTINATION_ADDRESS = 'Cl 24 Sur #52-20'
    
    PROGRAMED_SERVCIE_SELECTOR_ID = 'new UiSelector().className("android.widget.ImageView").instance(2)'
    BUTTON_PROGRAMED_SERVICE_ID = 'Agendar'
    DESTINATION_ADDRESS_SELECTOR_XPATH = '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]'
    CONTRACT_CONFIRMATION_SELECTOR_ID = 'Confirmar'
    CONFIRMATION_SERVICE_SELECTOR_ID = 'Confirmar'
    PROGRAMED_TRIP_BUTTON_SELECTOR_ID = 'Programar viaje'
    UNDERSTOOD_BUTTON_ID = 'Entendido'
    
    # ? Cancelar servicio
    CANCEL_SERVICE_ID = 'Cancelar'
    CONFIRM_CANCELATION_ID = 'SI'
    
    
    try:
        try:
            print("Iniciando el proceso de solicitud de servicio programado...")
            
            programed_service_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, PROGRAMED_SERVCIE_SELECTOR_ID)
            programed_service_button.click()
            
            schedule_service(driver)
            
            button_to_programed = driver.find_element(AppiumBy.ACCESSIBILITY_ID, BUTTON_PROGRAMED_SERVICE_ID)
            button_to_programed.click()
            
            destination_adress_field = driver.find_element(AppiumBy.XPATH, DESTINATION_ADDRESS_SELECTOR_XPATH)
            destination_adress_field.click()
            destination_adress_field.send_keys(DESTINATION_ADDRESS)
            driver.back()
            time.sleep(4)
            
            print("Buscando...")
            # Capturar las sugerencias dinámicas de direcciones a través del atributo content-desc
            suggestions = driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.ImageView')
            
            # Filtrar aquellas sugerencias que tengan un content-desc no vacío
            suggestions_with_desc = [s for s in suggestions if s.get_attribute('content-desc')]
            
            # Inicializar variables para la mejor coincidencia
            max_similarity = 0
            best_match = None
            
            print("Comparando las sugerencias...")
            time.sleep(2)
            
            # Comparar cada sugerencia con la dirección ingresada
            for suggestion in suggestions_with_desc:
                suggestion_desc = suggestion.get_attribute('content-desc')
                similarity = similar(DESTINATION_ADDRESS, suggestion_desc)
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
            
            time.sleep(5)
            
            # ! Elementos de la pantalla de selección de servicio
            
            vehicle_type = 'Carro'	# ? Poner únicamente 'Moto' o 'Carro'
            
            # Buscar elementos que contengan la palabra específica en su descripción
            vehicle_elements = driver.find_elements(AppiumBy.XPATH, f"//*[contains(@content-desc, '{vehicle_type}')]")
            
            # Revisar si se encontró al menos un elemento y hacer clic en el primero
            if vehicle_elements:
                vehicle_elements[0].click()
            else:
                print(f"No se encontraron elementos para '{vehicle_type}'")
            
            # Confirmar el agendamiento del servicio
            button_agenda_confirmation = driver.find_element(AppiumBy.XPATH, f"//*[contains(@content-desc, 'Agendar')]")
            button_agenda_confirmation.click()
            time.sleep(1)
            
            # Aceptación de contrato
            confirm_contract = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONTRACT_CONFIRMATION_SELECTOR_ID)
            confirm_contract.click()
            time.sleep(4)
            
            # Confirmación de punto de recogida
            confirm_service = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONFIRMATION_SERVICE_SELECTOR_ID)
            confirm_service.click()
            time.sleep(3)
            
            driver.swipe(start_x=driver.get_window_size()['width'] // 2, start_y=driver.get_window_size()['height'] * 0.9, end_x=driver.get_window_size()['width'] // 2, end_y=driver.get_window_size()['height'] * 0.1, duration=500)
            time.sleep(1)
            
            # Confirmación final de servicio programdo
            confirm_service = driver.find_element(AppiumBy.ACCESSIBILITY_ID, PROGRAMED_TRIP_BUTTON_SELECTOR_ID)
            confirm_service.click()
            time.sleep(5)
            
            # Bonton de 'Entiendo'
            understood_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, UNDERSTOOD_BUTTON_ID)
            understood_button.click()
            
            print("Solicitud de Booking confirmada con éxito!!")
            
            # ! Cancelar el servicio
            # Encuentra el Servicio programado
            programed_trip = driver.find_element(AppiumBy.XPATH, f"//*[contains(@content-desc, 'Tienes un viaje programado')]")
            programed_trip.click()
            time.sleep(2)
            
            driver.swipe(start_x=driver.get_window_size()['width'] // 2, start_y=driver.get_window_size()['height'] * 0.9, end_x=driver.get_window_size()['width'] // 2, end_y=driver.get_window_size()['height'] * 0.1, duration=500)
            time.sleep(1)
            
            cancelation_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CANCEL_SERVICE_ID)
            cancelation_button.click()
            
            confirm_cancelation = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CONFIRM_CANCELATION_ID)
            confirm_cancelation.click()
            time.sleep(3)
            
            # Verificar si la cancelación fue exitosa
            try:
                # Intentar encontrar el elemento que indica que el viaje está programado
                driver.find_element(AppiumBy.XPATH, f"//*[contains(@content-desc, 'Tienes un viaje programado')]")
                print("Error: El servicio no se canceló correctamente, el viaje sigue programado.")
            except NoSuchElementException:
                # Si el elemento no se encuentra, la cancelación fue exitosa
                print("Servicio cancelado correctamente.")
        
        except NoSuchElementException:
            print("Objeto no encontrado en pantalla.")

    except Exception as e:
        print(f"Error al ejecutar el caso de prueba: {e}.")
    finally:
        print("Finalizando el caso de prueba.")
        # driver.quit() # Cierra el driver al finalizar, descomentar para ejecutar en la nube
