from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import time

# Función para tomar una foto con la cámara
def take_photo(driver, open_camera_selector, photo_xpath):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, open_camera_selector).click()
    time.sleep(2)
    driver.find_element(AppiumBy.XPATH, photo_xpath).click()
    time.sleep(4)

# Función para ingresar texto en un campo
def input_text(driver, field_xpath, text_value):
    field = driver.find_element(AppiumBy.XPATH, field_xpath)
    field.click()
    time.sleep(1)
    field.send_keys(text_value)
    time.sleep(1)
    driver.back()

# Método reutilizable para hacer clic en el botón "Continuar"
def click_continue_button(driver, id, wait_time):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, id).click()
    time.sleep(wait_time)

# Función principal de registro
def main(driver):
    # Definir constantes para XPaths, IDs y otros selectores
    CURP_VALUE = "CURP000002"
    RFC_VALUE = "RFC000002"
    PLATES_VALUE = "0XX02"

    SELECTORS = {
        "menu": 'Menú\nPestaña 1 de 3',
        "driver_convert": 'Convertirme en conductor',
        "accept_convert": 'Si',
        "continue": 'Continuar',
        "curp_photo": 'Selecciona tu foto',
        "open_camera": 'Abrir cámara',
        "take_photo_xpath": '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]',
        "curp_field": '//android.widget.EditText',
        "rfc_photo": 'Sube una foto de tu constancia de situación fiscal (RFC)',
        "rfc_field_xpath": '//android.widget.EditText',
        "ine_back_photo": 'Foto de la parte trasera de tu INE',
        "ine_front_photo": 'Foto de la parte frontal de tu INE',
        "proof_of_address": 'Sube una foto de tu comprobante de domicilio (La dirección debe coincidir con tu INE). No mayor a 3 meses',
        "civil_liability": 'Foto',
        "driver_license": 'Foto',
        # Formulario Tarjeta Circulación
        "model_xpath": '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[1]',
        "brand_xpath": '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[2]',
        "cilinder_xpath": '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[3]',
        "reference_xpath": '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[4]',
        "plates_xpath": '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[4]',
        "circulation_card": 'Tarjeta de circulación',
        "color_xpath": '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.EditText[3]',
        "final_confirmation": 'Aceptar'
    }

    try:
        print("Iniciando el proceso de registro de conductor...")

        # Acciones principales
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['menu']).click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['driver_convert']).click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['accept_convert']).click()
        time.sleep(3)
        click_continue_button(driver, SELECTORS['continue'], 5)

        # Proceso de cargar documentos (CURP, RFC, INE, etc.)
        print("Cargando CURP...")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['curp_photo']).click()
        take_photo(driver, SELECTORS['open_camera'], SELECTORS['take_photo_xpath'])
        input_text(driver, SELECTORS['curp_field'], CURP_VALUE)
        click_continue_button(driver, SELECTORS['continue'], 5)

        # RFC
        print("Cargando RFC...")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['rfc_photo']).click()
        take_photo(driver, SELECTORS['open_camera'], SELECTORS['take_photo_xpath'])
        input_text(driver, SELECTORS['rfc_field_xpath'], RFC_VALUE)
        click_continue_button(driver, SELECTORS['continue'], 5)

        # INE (parte trasera y frontal)
        print("Cargando parte trasera INE...")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['ine_back_photo']).click()
        take_photo(driver, SELECTORS['open_camera'], SELECTORS['take_photo_xpath'])
        click_continue_button(driver, SELECTORS['continue'], 5)

        print("Cargando parte frontal INE...")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['ine_front_photo']).click()
        take_photo(driver, SELECTORS['open_camera'], SELECTORS['take_photo_xpath'])
        click_continue_button(driver, SELECTORS['continue'], 5)

        # Comprobante de domicilio
        print("Cargando comprobante de domicilio...")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['proof_of_address']).click()
        take_photo(driver, SELECTORS['open_camera'], SELECTORS['take_photo_xpath'])
        click_continue_button(driver, SELECTORS['continue'], 5)

        # Tipo de Vehículo
        click_continue_button(driver, SELECTORS['continue'], 5)

        # Póliza de responsabilidad civil
        print("Cargando póliza de responsabilidad civil...")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['civil_liability']).click()
        take_photo(driver, SELECTORS['open_camera'], SELECTORS['take_photo_xpath'])
        click_continue_button(driver, SELECTORS['continue'], 5)

        # Licencia de conducir
        print("Cargando licencia de conducir...")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['driver_license']).click()
        take_photo(driver, SELECTORS['open_camera'], SELECTORS['take_photo_xpath'])
        click_continue_button(driver, SELECTORS['continue'], 5)

        # Datos de la tarjeta de circulación
        print("Cargando datos de tarjeta de circulación...")
        input_text(driver, SELECTORS['model_xpath'], "2023")
        input_text(driver, SELECTORS['brand_xpath'], "Suzuki")
        input_text(driver, SELECTORS['cilinder_xpath'], "149")
        input_text(driver, SELECTORS['reference_xpath'], "GSXR 150")
        input_text(driver, SELECTORS['plates_xpath'], PLATES_VALUE)

        # Foto de la tarjeta de circulación
        driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=1000, duration=1000)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['circulation_card']).click()
        take_photo(driver, SELECTORS['open_camera'], SELECTORS['take_photo_xpath'])
        time.sleep(8)

        # Color del vehículo
        input_text(driver, SELECTORS['color_xpath'], "Negro")
        time.sleep(2)

        # Continuar
        click_continue_button(driver, SELECTORS['continue'], 5)

        # Confirmación final
        print("Confirmando registro...")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['final_confirmation']).click()
        time.sleep(3)

        print("Proceso de registro finalizado.")
    except NoSuchElementException:
        print("Objeto no encontrado en pantalla.")
    except Exception as e:
        print(f"Error al ejecutar el caso de prueba: {e}.")
    finally:
        print("Finalizando el caso de prueba...")