from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Función para hacer clic en una opción visible usando el texto
def click_option_by_text(driver, option_text):
    try:
        # Espera hasta que el elemento sea visible y clickeable
        option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, option_text))
        )
        option.click()
        print(f"Se hizo clic en la opción: {option_text}")
    except Exception as e:
        print(f"No se encontró la opción: {option_text}, error: {str(e)}")
        return False
    return True

# Función para navegar a la opción principal y luego a la sub-opción
def select_chat_option(driver):
    print("Accediendo al chat central...")
    
    # Definimos las opciones principales
    ACTIVATIONS_SELECTOR_ID = 'Activaciones'
    PIBOX_SELECTOR_ID = 'Pibox'
    PICASH_SELECTOR_ID = 'Picash'
    PICAP_RENT_SELECTOR_ID = 'Picap Rent'
    
    main_option = "Picash"  # Ejemplo de opción principal
    sub_option = "Sub Opción 4"  # Ejemplo de sub-opción

    main_options = {
        "Activaciones": ACTIVATIONS_SELECTOR_ID,
        "Pibox": PIBOX_SELECTOR_ID,
        "Picash": PICASH_SELECTOR_ID,
        "Picap Rent": PICAP_RENT_SELECTOR_ID
    }

    # Intenta hacer clic en la opción principal
    option_selected = click_option_by_text(driver, main_options[main_option])
    
    if not option_selected:
        print(f"La opción {main_options[main_option]} no se encontró.")
        return

    time.sleep(2)  # Espera para asegurarse de que la opción principal se cargue

    # Selección de la sub-opción (aquí asumimos que las sub-opciones son accesibles)
    sub_options = {
        "Activaciones": ["Sub Opción 1", "Sub Opción 2", "Sub Opción 3"],
        "Pibox": ["Sub Opción 1", "Sub Opción 2", "Sub Opción 3", "Sub Opción 4", "Sub Opción 5", "Sub Opción 6"],
        "Picash": ["Sub Opción 1", "Sub Opción 2", "Sub Opción 3", "Sub Opción 4", "Sub Opción 5", "Sub Opción 6", "Sub Opción 7", "Sub Opción 8"],
        "Picap Rent": ["Sub Opción 1", "Sub Opción 2", "Sub Opción 3", "Sub Opción 4", "Sub Opción 5", "Sub Opción 6"]
    }

    # Intenta hacer clic en la sub-opción deseada
    option_selected = click_option_by_text(driver, sub_option)
    
    if not option_selected:
        print(f"La sub-opción {sub_option} no se encontró después de varios intentos.")
    else:
        print(f"Se seleccionó correctamente la sub-opción: {sub_option}")

