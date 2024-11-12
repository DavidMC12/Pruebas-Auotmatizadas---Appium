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
        time.sleep(1)
        
        
        print("Proceso de recarga Picash finalizado.")
    
    except NoSuchElementException:
        print("Objeto no encontrado en pantalla.")
    except Exception as e:
        print(f"Error al ejecutar el caso de prueba: {e}.")
    finally:
        print("Finalizando el caso de prueba...")