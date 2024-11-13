from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from difflib import SequenceMatcher
import time

# Función para medir la similitud entre dos textos
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Clase para el formulario de solicitud de booking
class BookingPage:
    def __init__(self, driver):
        self.driver = driver
        # Definir constantes para XPaths, IDs y otros selectores
        self.SERVICE_PIBOX_SELECTOR_ID = 'Mensajería'
        self.DELIVERY_DESTINATION_SELECTOR_XPATH = '//android.view.View[@text="Dirección de entrega"]'
        self.DELIVERY_DESTINATION_SELECTOR_CLASSNAME_2 = 'android.widget.EditText'
        self.INPUT_ADDRESS = 'Cl 50 #24-34'
        self.ADITIONAL_INFO_SELECTOR_XPATH = '//android.widget.EditText'
        self.CONFIRM_SERVICE_ID = 'Continuar'
        self.INDICATIONS_SELECTOR_XPATH = '//android.widget.ScrollView/android.widget.EditText[1]'
        self.TARGET_SELECTOR_XPATH = '//android.widget.ScrollView/android.widget.EditText[2]'
        self.PHONE_SELECTOR_XPATH = '//android.widget.ScrollView/android.widget.EditText[3]'
        self.DECLARED_VALUE_SELECTOR_XPATH = '//android.widget.ScrollView/android.widget.EditText[4]'
        self.PACKAGE_SIZE_SELECTOR_ID = 'Pequeño (Max 20x20x20)'
        self.CREATE_PIBOX_BUTTON_SELECTOR_ID = 'Crear'
        self.REQUEST_BUTTON_ID = 'Solicitar'

    def enter_booking_details(self):
        print("Iniciando el proceso de solicitud de servicio de Pibox...")
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.SERVICE_PIBOX_SELECTOR_ID).click()
        print("Servicio Pibox seleccionado.")
        time.sleep(2)

        # Ingresar la dirección de destino
        self.driver.find_element(AppiumBy.XPATH, self.DELIVERY_DESTINATION_SELECTOR_XPATH).click()
        print("Campo de dirección de entrega seleccionado.")
        time.sleep(1)

        self.driver.find_element(AppiumBy.CLASS_NAME, self.DELIVERY_DESTINATION_SELECTOR_CLASSNAME_2).click()
        self.driver.find_element(AppiumBy.CLASS_NAME, self.DELIVERY_DESTINATION_SELECTOR_CLASSNAME_2).send_keys(self.INPUT_ADDRESS)
        self.driver.back()  # Ocultar el teclado
        time.sleep(4)  # Esperar que aparezcan las sugerencias dinámicas
        print("Dirección de destino ingresada.")

        # Seleccionar la mejor coincidencia
        self.select_best_address_match()

        # Ingresar información adicional
        self.driver.find_element(AppiumBy.XPATH, self.ADITIONAL_INFO_SELECTOR_XPATH).click()
        self.driver.find_element(AppiumBy.XPATH, self.ADITIONAL_INFO_SELECTOR_XPATH).send_keys("Entregar a la recepción.")
        self.driver.back()  # Ocultar el teclado
        print("Información adicional ingresada.")

        # Confirmar la solicitud del envío
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.CONFIRM_SERVICE_ID).click()
        print("Servicio confirmado.")

        # Llenar el formulario del paquete
        self.fill_package_form()
        print("Formulario de paquete completado.")

        print("Solicitud de Booking confirmada con éxito.")

    def select_best_address_match(self):
        print("Buscando la mejor coincidencia de dirección...")
        suggestions = self.driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.ImageView')
        suggestions_with_desc = [s for s in suggestions if s.get_attribute('content-desc')]
        max_similarity = 0
        best_match = None
        for suggestion in suggestions_with_desc:
            suggestion_desc = suggestion.get_attribute('content-desc')
            similarity = similar(self.INPUT_ADDRESS, suggestion_desc)
            print(f"Comparando con sugerencia '{suggestion_desc}', similitud: {similarity}")
            if similarity > max_similarity:
                max_similarity = similarity
                best_match = suggestion
        if best_match:
            best_match.click()
            time.sleep(4)
            print("Dirección seleccionada con éxito.")
        else:
            print("No se encontró una coincidencia adecuada para la dirección.")

    def fill_package_form(self):
        print("Llenando detalles del paquete...")
        self.driver.find_element(AppiumBy.XPATH, self.INDICATIONS_SELECTOR_XPATH).click()
        self.driver.find_element(AppiumBy.XPATH, self.INDICATIONS_SELECTOR_XPATH).send_keys("Dejarlo en portería.")
        print("Indicaciones ingresadas.")

        self.driver.find_element(AppiumBy.XPATH, self.TARGET_SELECTOR_XPATH).click()
        self.driver.find_element(AppiumBy.XPATH, self.TARGET_SELECTOR_XPATH).send_keys("Juan Perez")
        print("Nombre del destinatario ingresado.")

        self.driver.find_element(AppiumBy.XPATH, self.PHONE_SELECTOR_XPATH).click()
        self.driver.find_element(AppiumBy.XPATH, self.PHONE_SELECTOR_XPATH).send_keys("3001234567")
        self.driver.back()
        print("Teléfono del destinatario ingresado.")

        self.driver.find_element(AppiumBy.XPATH, self.DECLARED_VALUE_SELECTOR_XPATH).click()
        self.driver.find_element(AppiumBy.XPATH, self.DECLARED_VALUE_SELECTOR_XPATH).send_keys("12000")
        self.driver.back()
        print("Valor declarado ingresado.")

        # Desplazamiento y selección del tamaño del paquete
        self.driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=1000, duration=1000)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.PACKAGE_SIZE_SELECTOR_ID).click()
        print("Tamaño del paquete seleccionado.")

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.CREATE_PIBOX_BUTTON_SELECTOR_ID).click()
        time.sleep(2)
        print("Servicio de Pibox creado.")

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.REQUEST_BUTTON_ID).click()
        time.sleep(2)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.REQUEST_BUTTON_ID).click()
        print("Servicio solicitado.")
        time.sleep(4)

# Clase para la cancelación de servicio
class ServiceCancellationPage:
    def __init__(self, driver):
        self.driver = driver
        self.CANCEL_SERVICE_X_ID = 'Cancelar viaje'
        self.CONFIRMATION_POPUP = 'Si'
        self.TESTING_APP_OP = 'Solo probando la aplicación'
        self.CANCELATION_BUTTON = 'Aceptar'

    def cancel_service(self):
        print("Iniciando la cancelación del servicio...")
        self.driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=300, duration=800)
        time.sleep(2)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.CANCEL_SERVICE_X_ID).click()
        print("Botón de cancelar servicio seleccionado.")

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.CONFIRMATION_POPUP).click()
        print("Popup de confirmación aceptado.")

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.TESTING_APP_OP).click()
        print("Opción 'Solo probando la aplicación' seleccionada.")

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.CANCELATION_BUTTON).click()
        time.sleep(2)
        self.driver.tap([(800, 1310)], 500)
        print("Servicio cancelado exitosamente.")
        time.sleep(3)

# Función principal para ejecutar el flujo de la prueba
def main(driver):
    try:
        print("Ejecutando el flujo de booking y cancelación de servicio.")
        booking_page = BookingPage(driver)
        booking_page.enter_booking_details()

        cancellation_page = ServiceCancellationPage(driver)
        cancellation_page.cancel_service()

    except NoSuchElementException:
        print("Objeto no encontrado en pantalla.")
    except Exception as e:
        print(f"Error al ejecutar el caso de prueba: {e}.")
    finally:
        print("Finalizando el caso de prueba.")
        # driver.quit()