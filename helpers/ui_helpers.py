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