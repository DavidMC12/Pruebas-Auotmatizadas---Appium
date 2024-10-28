from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def wait_for_duration(driver, duration):
    # Dividir el tiempo en intervalos cortos para mantener la sesión activa
    elapsed_time = 0
    wait_interval = 5  # Espera de 5 segundos por cada iteración
    
    while elapsed_time < duration:
        time.sleep(wait_interval)  # Pausa corta
        elapsed_time += wait_interval
        
        # Verificar si la sesión sigue activa
        if not driver.session_id:
            raise Exception("La sesión de Appium ha terminado.")
        
        print(f"Esperando... {elapsed_time}/{duration} segundos transcurridos")


def main(driver):
    # Constantes
    MAX_WAIT_TIME = 120
    
    # Selectores
    SELECTORS = {
        'accept_service': 'Aceptar',
        'popup_selector': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView[1]',
        'mene_home_selector': 'Menú\nPestaña 1 de 3',
        'conducotr_mode_selector': 'Cambiar a modo conductor', 
        'save_selector': 'Guardar',
        'activate_pipro_xpath': '//android.widget.Switch',
        'transport_of': 'Persona(s)', # Poner 'Paquete(s)' si es Pibox
        'rate_service': '//android.widget.ScrollView/android.widget.ImageView[4]', # Cambiar el último número para seleccionar la cantidad de estrellas
        'send_rate': 'Enviar'
    }
    
    try:
        print("Iniciando el proceso de aceptación de servicios PiPro...")
        # Pasar a modo conudctor
        print("Cambiando a modo conductor...")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['mene_home_selector']).click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['conducotr_mode_selector']).click()
        time.sleep(3)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['save_selector']).click()
        time.sleep(5)
        
        driver.find_element(AppiumBy.XPATH, SELECTORS['activate_pipro_xpath']).click()
        time.sleep(5)
        
        # Esperar a que salga la pantalla del viaje para continuar
        print("Esperando a que llegue un servicio...")
        # Línea 36 - Código para esperar a que aparezca un elemento relacionado con la pantalla del servicio en curso
        WebDriverWait(driver, MAX_WAIT_TIME).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Ir')))
        print("Servicio encontrado.")
        
        time.sleep(8)
        
        # Swipe llegada a punto de recogida
        print("Llegando al punto de recogida...")
        driver.swipe(start_x=65, start_y=2100, end_x=1025, end_y=2110, duration=1000)
        time.sleep(2)
        
        # Swipe recogida de pasajero
        print("Recogiendo pasajero...")
        driver.swipe(start_x=65, start_y=2100, end_x=1025, end_y=2110, duration=1000)
        print("Esperando 2 minutos para finalizar el servicio...")
        wait_for_duration(driver, 125)
        
        # Swipe para finalizar el servicio
        print("Finalizando el servicio...")
        driver.swipe(start_x=65, start_y=2100, end_x=1025, end_y=2110, duration=1300)
        time.sleep(7)
        
        # Envío de calificación
        print("Calificando el servicio...")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['transport_of']).click()
        driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=1000, duration=1000)
        driver.find_element(AppiumBy.XPATH, SELECTORS['rate_service']).click()
        driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=1000, duration=1000)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['send_rate']).click()
        print("Enviando calificación...")
        time.sleep(6)
        
        print("Proceso de aceptación de servicios completado.")
    
    except NoSuchElementException:
        print("Objeto no encontrado en pantalla.")
    except Exception as e:
        print(f"Error al ejecutar el caso de prueba: {e}.")
    finally:
        print("Finalizando el caso de prueba...")