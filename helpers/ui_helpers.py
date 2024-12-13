from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

#! Función para manejar pop-ups
def handle_popups(driver, selector):
    """
    Cierra pop-ups si están presentes.

    Args:
        driver: instancia del WebDriver de Appium.
        selector: el selector del botón de cierre de pop-up.
    """
    print("Validando la presencia de pop-ups...")
    try:
        driver.find_element(AppiumBy.ID, selector).click()
        print("Popup encontrado y cerrado.")
    except NoSuchElementException:
        print("No se encontró ningún popup.")

#! Función para tocar la pantalla usando W3C Actions
def tap_screen(driver, x_ratio, y_ratio):
    """
    Realiza un toque en la pantalla basado en proporciones relativas al tamaño del dispositivo.

    Args:
        driver: Instancia del Appium WebDriver.
        x_ratio (float): Proporción horizontal (0.0 a 1.0) donde 0.0 es el borde izquierdo y 1.0 es el borde derecho.
        y_ratio (float): Proporción vertical (0.0 a 1.0) donde 0.0 es el borde superior y 1.0 es el borde inferior.
    """
    driver.tap([(int(driver.get_window_size()['width'] * x_ratio), int(driver.get_window_size()['height'] * y_ratio))])