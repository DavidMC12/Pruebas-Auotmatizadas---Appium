from appium.webdriver.common.appiumby import AppiumBy
import time

# Variables globales
main_option = "Picash"
sub_option = "Transacciones realizadas"

POPUP_ACCEPT_SELECTOR = 'Si'
POPUP_REJECT_SELECTOR = 'No'

HELP_SELECTOR = 'Ayuda\nPestaña 3 de 3'
CHAT_CENTRAL_SELECTOR = '¿Aún necesitas ayuda?\nhabla con un asesor'

# * Método para hacer un tap en coordenadas
def tap_screen(driver, x, y, duration=500):
    driver.tap([(x, y)], duration)
    print(f"Tap realizado en las coordenadas: X={x}, Y={y}\n")
    time.sleep(1)

# * 1. Activaciones
def access_activations(driver):
    print("Accediendo a Activaciones...")
    tap_screen(driver, 530, 1115)  # Coordenadas para Activaciones
    time.sleep(1)

    if sub_option == "Actualización de datos":
        tap_screen(driver, 530, 1110)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        time.sleep(2)
    
    elif sub_option == "¿Cómo convertirme en usuario prestador?":
        tap_screen(driver, 530, 1315)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        time.sleep(2)
    
    elif sub_option == "Otros":
        tap_screen(driver, 530, 1510)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        time.sleep(2)
    
    else:
        print(f"Sub opción {sub_option} no encontrada en Activaciones.")
        
# * 2. Pibox
def access_pibox(driver):
    print("Accediendo a Pibox...")
    tap_screen(driver, 530, 1315)  # Coordenadas para Pibox
    time.sleep(1)

    if sub_option == "Bloqueos":
        tap_screen(driver, 530, 1110)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        time.sleep(2)
    
    elif sub_option == "Emergencia":
        tap_screen(driver, 530, 1315)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        time.sleep(2)
    
    elif sub_option == "Paquete":
        tap_screen(driver, 530, 1520)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        time.sleep(2)
    
    elif sub_option == "Tarifas":
        tap_screen(driver, 530, 1720)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        time.sleep(2)
    
    elif sub_option == "Reclamaciones":
        tap_screen(driver, 530, 1925)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        time.sleep(2)
    
    elif sub_option == "Otros":
        tap_screen(driver, 530, 2130)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        time.sleep(2)
    
    else:
        print(f"Sub opción {sub_option} no encontrada en Pibox.")

# * 3. Picash
def access_picash(driver):
    print("Accediendo a Picash...")
    tap_screen(driver, 530, 1520)  # Coordenadas para Picash
    time.sleep(1)

    if sub_option == "Bonos promocionales":
        tap_screen(driver, 530, 1120)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        # driver.back()
        time.sleep(2)
    
    elif sub_option == "Compras":
        tap_screen(driver, 530, 1315)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        # driver.back()
        time.sleep(2)
    
    elif sub_option == "Multas por cancelación":
        tap_screen(driver, 530, 1515)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        # driver.back()
        time.sleep(2)
    
    elif sub_option == "Otros":
        tap_screen(driver, 530, 1710)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        # driver.back()
        time.sleep(2)
    
    elif sub_option == "Recargas":
        tap_screen(driver, 530, 1920)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        # driver.back()
        time.sleep(2)
    
    elif sub_option == "Retiros":
        driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=1000, duration=1000)
        tap_screen(driver, 530, 1660)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        # driver.back()
        time.sleep(2)
    
    elif sub_option == "Servicios":
        driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=1000, duration=1000)
        tap_screen(driver, 530, 1850)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        # driver.back()
        time.sleep(2)
    
    elif sub_option == "Transacciones realizadas":
        driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=1000, duration=1000)
        tap_screen(driver, 530, 2060)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        # driver.back()
        time.sleep(2)
    
    else:
        print(f"Sub opción {sub_option} no encontrada en Picash.")

# * 4. Picap Rent
def access_picap_rent(driver):
    print("Accediendo a Picap Rent...")
    tap_screen(driver, 530, 1720)  # Coordenadas para Picap Rent
    time.sleep(1)

    if sub_option == "Bloqueos":
        tap_screen(driver, 530, 1110)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        time.sleep(2)
    
    elif sub_option == "Emergencia":
        tap_screen(driver, 530, 1330)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        time.sleep(2)
    
    elif sub_option == "Otros":
        tap_screen(driver, 530, 1510)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        time.sleep(2)
    
    elif sub_option == "Reclamaciones":
        tap_screen(driver, 530, 1720)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        time.sleep(2)
    
    elif sub_option == "Servicios":
        tap_screen(driver, 530, 1920)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        time.sleep(2)
    
    elif sub_option == "Tarifas":
        tap_screen(driver, 530, 2120)
        option_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, POPUP_ACCEPT_SELECTOR)
        option_button.click()
        time.sleep(2)
    
    else:
        print(f"Sub opción {sub_option} no encontrada en Picap Rent.")

# ? Función principal para determinar la navegación según la opción principal seleccionada
def select_main_option(driver):
    if main_option == "Activaciones":
        access_activations(driver)
    elif main_option == "Pibox":
        access_pibox(driver)
    elif main_option == "Picash":
        access_picash(driver)
    elif main_option == "Picap Rent":
        access_picap_rent(driver)
    else:
        print(f"Opción principal {main_option} no encontrada.")

# * Ejecución del caso de prueba
def main(driver):
    print("Iniciando caso de prueba Chat Central...")
    help_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, HELP_SELECTOR)
    help_option.click()
    time.sleep(1)
    
    print("Accediendo a Chat Central...")
    chat_central = driver.find_element(AppiumBy.ACCESSIBILITY_ID, CHAT_CENTRAL_SELECTOR)
    chat_central.click()
    time.sleep(1)
    
    select_main_option(driver)

