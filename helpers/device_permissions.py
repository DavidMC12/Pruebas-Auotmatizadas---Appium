from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Constantes
TIMEOUT = 10

# Selectores
SELECTORS = {
    'location_permission_button': 'com.android.packageinstaller:id/permission_allow_button',
    'phone_permission_button': 'com.android.packageinstaller:id/permission_allow_button',
}

#! Función genérica para manejar permisos
def handle_permission(driver, selector, permission_name):
    """
    Maneja el clic en los botones de permiso según el selector.
    
    Args:
        driver: instancia del WebDriver de Appium.
        selector: el selector del elemento del botón de permiso.
        permission_name: nombre del permiso para los logs.
    """
    print(f"Validando permisos de {permission_name}.")
    try:
        element = WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located((AppiumBy.ID, selector))
        )
        element.click()
        print(f"Permiso de {permission_name} concedido.")
    except NoSuchElementException:
        print(f"No se solicitaron permisos de {permission_name}.")
    except Exception as e:
        print(f"Error al manejar el permiso de {permission_name}: {e}")

#! Función para permisos de ubicación
def location_permission(driver):
    """
    Maneja los permisos relacionados con la ubicación.
    
    Args:
        driver: instancia del WebDriver de Appium.
    """
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Aceptar').click()
    time.sleep(2)
    handle_permission(driver, SELECTORS['location_permission_button'], "ubicación")

#! Función para permisos de teléfono
def phone_permission(driver):
    """
    Maneja los permisos relacionados con el teléfono.
    
    Args:
        driver: instancia del WebDriver de Appium.
    """
    time.sleep(1)
    handle_permission(driver, SELECTORS['phone_permission_button'], "teléfono")