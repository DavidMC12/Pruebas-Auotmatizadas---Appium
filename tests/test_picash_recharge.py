from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ! Nota: El usuario ya debe contar con una cuenta picash 
# (debe tener documento y telefono verificados, y el pin creado)


def main(driver):
    # Constantes
    
    
    # Selectores
    SELECTORS = {
        'picash_selector': 'Picash\nPestaña 2 de 3',
        'recharge_selector': 'Recargar',
        'recharge_value_xpath': '//android.widget.EditText',
        'payment_method_xpath': '//android.widget.ScrollView/android.widget.ImageView[5]',
        'op_su_red_selector': 'Su Red',
        'continue_selector': 'Continuar',
        'pay_selector': 'Pagar'
    }
    
    try:
        print("Iniciando el proceso de recarga Picash...")
        # Acceder al apartado de Picash
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['picash_selector']).click()
        time.sleep(2)
        
        # Regacargar Picash
        print("Recargando Picash...")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['recharge_selector']).click()
        time.sleep(2)
        
        # Ingresar el monto de recarga
        print("Ingresando monto de recarga...")
        recharge_field = driver.find_element(AppiumBy.XPATH, SELECTORS['recharge_value_xpath'])
        recharge_field.click()
        recharge_field.send_keys('21000')
        
        # Seleccioanr el método de pago
        print("Seleccionando método de pago...")
        driver.find_element(AppiumBy.XPATH, SELECTORS['payment_method_xpath']).click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['op_su_red_selector']).click()
        time.sleep(1)
        
        # Continuar con la recarga
        print("Continuando con la recarga...")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['continue_selector']).click()
        time.sleep(1)
        
        # Pagar
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['pay_selector']).click()
        time.sleep(4)
        
        # Verificar que se haya completado la recarga
        try:
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Presenta estos datos en cualquier Su Red y listo.')
            print("Recarga Picash exitosa!!")
        except NoSuchElementException:
            print("Recarga Picash fallida.")
        
        # Continuar 
        print("Continuando a la pantalla inicial...")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['continue_selector']).click()
        time.sleep(3)
        
        # Verifica los datos de la recarga
        print("Verificando los datos de la recarga...")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['recharge_selector']).click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Volver')
        time.sleep(4)
        driver.back()
        
        print("Proceso de recarga Picash finalizado.")
    
    except NoSuchElementException:
        print("Objeto no encontrado en pantalla.")
    except Exception as e:
        print(f"Error al ejecutar el caso de prueba: {e}.")
    finally:
        print("Finalizando el caso de prueba...")