from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import math, time

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
    # Obtener el tamaño de la pantalla
    screen_size = driver.get_window_size()
    width = screen_size['width']
    height = screen_size['height']

    # Validar que las proporciones estén en el rango [0.0, 1.0]
    if not (0.0 <= x_ratio <= 1.0) or not (0.0 <= y_ratio <= 1.0):
        raise ValueError("Las proporciones x_ratio y y_ratio deben estar entre 0.0 y 1.0")

    # Calcular coordenadas basadas en proporciones
    x = int(width * x_ratio)
    y = int(height * y_ratio)

    # Imprimir las coordenadas calculadas (para depuración)
    print(f"Tamaño de pantalla: {width}x{height}")
    print(f"Realizando clic en coordenadas relativas: ({x}, {y})")

    # Realizar tap en las coordenadas calculadas
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

# ! Función para deslizar y cancelar un servicio
def cancel_service_flow(driver, swipe_duration=500, sleep_time=1):
    """
    Realiza el flujo para cancelar un servicio en la aplicación móvil.

    Args:
        driver: Instancia del controlador de Appium.
        swipe_duration (int): Duración del gesto de swipe en milisegundos (opcional, default: 500).
        sleep_time (int): Tiempo de espera entre interacciones en segundos (opcional, default: 1).

    Raises:
        NoSuchElementException: Si algún elemento no se encuentra en el flujo.
    """
    # Constantes de selectores
    SELECTORS = {
        "cancel_service": "Cancelar viaje",
        "testing_app_op": "Solo probando la aplicación",
        "cancel_service_button": "Cancelar servicio",
        "cancel_confirmation_op": "Aceptar",
    }

    try:
        # Realizar swipe para cancelar el servicio
        window_size = driver.get_window_size()
        start_x = window_size['width'] // 2
        start_y = int(window_size['height'] * 0.9)
        end_x = start_x
        end_y = int(window_size['height'] * 0.1)

        print(f"Realizando swipe desde ({start_x}, {start_y}) hasta ({end_x}, {end_y})")
        driver.swipe(start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y, duration=swipe_duration)
        time.sleep(sleep_time)
        print("Swipe realizado con éxito.")

        # Cancelar el servicio
        cancel_service_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS["cancel_service"])
        cancel_service_button.click()
        time.sleep(sleep_time)

        # Operación adicional en la app
        testing_app_op_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS["testing_app_op"])
        testing_app_op_button.click()
        time.sleep(sleep_time)

        # Confirmar cancelación del servicio
        cancel_service_confirm_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS["cancel_service_button"])
        cancel_service_confirm_button.click()
        time.sleep(sleep_time)

        # Confirmar la acción final
        cancel_confirmation_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, SELECTORS["cancel_confirmation_op"])
        cancel_confirmation_button.click()
        time.sleep(sleep_time)
        print("Servicio cancelado con éxito.")

    except NoSuchElementException as e:
        raise NoSuchElementException(f"Error al localizar un elemento durante el flujo de cancelación: {str(e)}")