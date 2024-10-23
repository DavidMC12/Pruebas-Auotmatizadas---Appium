from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import time

def main(driver):
    # Constantes
    MAX_WAIT_TIME = 120  # Tiempo máximo para monitorear la aparición del pop-up en segundos
    POPUP_VISIBLE_TIME = 5  # Tiempo que el pop-up estará visible en segundos
    
    # Selectores
    SELECTORS = {
        'accept_service': 'Aceptar',
        'popup_selector': '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView[1]',
        'transport_of': 'Persona(s)', # Poner 'Paquete(s)' si es Pibox
        'rate_service': '//android.widget.ScrollView/android.widget.ImageView[4]', # Cambiar el último número para seleccionar la cantidad de estrellas
        'send_rate': 'Enviar'
    }
    
    start_time = time.time()
    
    try:
        print('Iniciando monitoreo para la aceptación de servicios...')
        
        # Monitorear hasta que el pop-up aparezca o se agote el tiempo
        while time.time() - start_time < MAX_WAIT_TIME:
            try:
                # Intentar encontrar el pop-up
                popup_element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['accept_service'])
                print("Pop-up encontrado.")
                
                if popup_element.is_displayed():
                    print("Pop-up visible. Intentando aceptar el servicio...")
                    driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['accept_service']).click()
                    # time.sleep(POPUP_VISIBLE_TIME)  # Espera el tiempo que el pop-up se mantendría visible
                    print("Servicio aceptado correctamente.")
                    break  # Salir del ciclo ya que el servicio fue aceptado
            except NoSuchElementException:
                # Si el pop-up no se encuentra, seguir esperando
                time.sleep(1)  # Evita sobrecargar el sistema con muchas consultas
        else:
            print("El pop-up no apareció dentro del tiempo límite de monitoreo.")
        time.sleep(5)
        
        # Swipe llegada a punto de recogida
        print("Llegando al punto de recogida...")
        driver.swipe(start_x=65, start_y=2100, end_x=1025, end_y=2110, duration=1300)
        time.sleep(2)
        
        # Swipe recogida de pasajero
        print("Recogiendo pasajero...")
        driver.swipe(start_x=65, start_y=2100, end_x=1025, end_y=2110, duration=1300)
        print("Esperando 2 minutos para finalizar el servicio...")
        time.sleep(122)
        
        # Swipe para finalizar el servicio
        print("Finalizando el servicio...")
        driver.swipe(start_x=65, start_y=2100, end_x=1025, end_y=2110, duration=1300)
        time.sleep(7)
        
        # Envío de calificación
        print("Calificando el servicio...")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS['transport_of']).click()
        driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=1000, duration=1000)
        driver.find_element(AppiumBy.XPATH, SELECTORS['rate_service']).click()
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