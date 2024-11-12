from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ! Nota: El usuario ya debe contar con una cuenta picash 
# (debe tener documento y telefono verificados, y el pin creado)


def main(driver):
    # Constantes
    NEW_CONTACT_NUMBRER = '3001234567'
    PICASH_PASSWORD = '0000'
    
    # Selectores
    SELECTORS = {
        'picash_selector': 'Picash\nPestaña 2 de 3',
        'send_money_selector': 'Enviar dinero',
        'contacts_permision_id': 'com.android.packageinstaller:id/permission_allow_button',
        'amount_to_send_xpath': '//android.widget.EditText[@text="0"]',
        'add_new_contact_xpath': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView[2]',
        'number_field_xpath': '//android.widget.EditText',
        'add_number_selector': 'Agregar',
        'message_xpath': '//android.widget.EditText',
        'picash_password_xpath': '//android.view.View[@content-desc="Ingresa tu clave para finalizar la compra"]/android.view.View[2]',
        'continue_selector': 'Continuar',
    }
    
    try:
        print("Iniciando el proceso de recarga Picash...")
        # Acceder al apartado de Picash
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['picash_selector']).click()
        time.sleep(2)
        
        # Ingresar al envío de dinero
        print("Ingresando al envío de dinero...")
        driver.swipe(start_x=500, start_y=1300, end_x=500, end_y=1000, duration=1000)
        time.sleep(1)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['send_money_selector']).click()
        time.sleep(1)
        
        # Validación de permisos a contactos
        print("Validando permisos de acceso a contactos...")
        try:
            driver.find_element(AppiumBy.ID, SELECTORS['contacts_permision_id']).click()
            print("Permiso a contactos concedido!!")
        except NoSuchElementException:
            print("No se solicitaron permisos a contactos.")

        
        # Ingresar el monto y envio
        print("Ingresando monto de recarga...")
        driver.find_element(AppiumBy.XPATH, SELECTORS['amount_to_send_xpath']).click()
        driver.find_element(AppiumBy.XPATH, SELECTORS['amount_to_send_xpath']).send_keys('1000')
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['continue_selector']).click()
        time.sleep(1)
        
        #Agregar nuevo contacto
        print("Agregando nuevo contacto...")
        driver.find_element(AppiumBy.XPATH, SELECTORS['add_new_contact_xpath']).click()
        driver.find_element(AppiumBy.XPATH, SELECTORS['number_field_xpath']).send_keys(NEW_CONTACT_NUMBRER)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['add_number_selector']).click()
        time.sleep(1)
        
        # Continuar con el envío
        print("Conitnuando...")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['continue_selector']).click()
        
        # Enviar mensaje
        print("Enviando mensaje...")
        driver.find_element(AppiumBy.XPATH, SELECTORS['message_xpath']).click()
        driver.find_element(AppiumBy.XPATH, SELECTORS['message_xpath']).send_keys('Mensaje de prueba')
        driver.back()
        driver.tap([(480, 2115)], 800)
        
        # Ingresar clave Picash
        print("Ingresando clave Picash...")
        # Enviar el texto simulando el uso del teclado físico del dispositivo
        driver.execute_script("mobile: shell", {
            "command": "input",
            "args": ["text", PICASH_PASSWORD]
        })
        time.sleep(5)
        
        # # Verificar que se haya completado la recarga
        # try:
        #     driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'TEXTO QUE DEBE SALIR')
        #     print("Recarga Picash exitosa!!")
        # except NoSuchElementException:
        #     print("Recarga Picash fallida.")
        
        print("Proceso de envío de dinero Picash finalizado.")
    
    except NoSuchElementException:
        print("Objeto no encontrado en pantalla.")
    except Exception as e:
        print(f"Error al ejecutar el caso de prueba: {e}.")
    finally:
        print("Finalizando el caso de prueba...")