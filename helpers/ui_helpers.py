from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import math

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

#! Función para tocar la pantalla
def tap_screen(driver, x_ratio, y_ratio):
    """
    Realiza un toque en la pantalla basado en proporciones relativas al tamaño del dispositivo.
    Imprime en consola las coordenadas calculadas para depuración.

    Args:
        driver: Instancia del Appium WebDriver.
        x_ratio (float): Proporción horizontal (0.0 a 1.0) donde 0.0 es el borde izquierdo y 1.0 es el borde derecho.
        y_ratio (float): Proporción vertical (0.0 a 1.0) donde 0.0 es el borde superior y 1.0 es el borde inferior.
    """
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    x = int(width * x_ratio)
    y = int(height * y_ratio)
    print(f"Clic en coordenadas: ({x}, {y})")
    driver.tap([(x, y)])
    
#! Función para tocar la pantalla en forma de circunferencia
def tap_circle(driver, x_center_ratio, y_center_ratio, radius_ratio, num_points=36):
    """
    Realiza múltiples taps en la pantalla formando una circunferencia.

    Args:
        driver: Instancia del Appium WebDriver.
        x_center_ratio (float): Proporción horizontal (0.0 a 1.0) del centro de la circunferencia.
        y_center_ratio (float): Proporción vertical (0.0 a 1.0) del centro de la circunferencia.
        radius_ratio (float): Proporción del radio en relación con el tamaño más pequeño de la pantalla.
        num_points (int): Número de puntos en la circunferencia. Más puntos = mayor precisión.
    """
    # Obtener dimensiones de la pantalla
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']

    # Calcular el centro de la circunferencia
    x_center = int(width * x_center_ratio)
    y_center = int(height * y_center_ratio)

    # Calcular el radio relativo al tamaño más pequeño de la pantalla
    radius = int(min(width, height) * radius_ratio)

    print(f"Centro: ({x_center}, {y_center}), Radio: {radius}")

    # Calcular los puntos de la circunferencia y realizar taps
    for i in range(num_points):
        angle = 2 * math.pi * i / num_points  # Ángulo actual
        x = int(x_center + radius * math.cos(angle))
        y = int(y_center + radius * math.sin(angle))
        print(f"Tap en coordenadas: ({x}, {y})")  # Para depuración
        driver.tap([(x, y)])