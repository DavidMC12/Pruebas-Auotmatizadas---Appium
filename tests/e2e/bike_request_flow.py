from tests import test_login, service_moto_request  # Importar las funciones
from appium import webdriver
import time

def e2e_login_and_service_flow(driver):
    """
    Flujo E2E para realizar login y solicitar un servicio.

    Args:
        driver: Instancia del controlador de Appium.
        username (str): Nombre de usuario para login.
        password (str): Contraseña para login.
    """
    try:
        print("Iniciando flujo E2E: Login y solicitud de servicio...")

        # Paso 1: Realizar el login
        print("Ejecutando el flujo de login...")
        test_login.main(driver)
        print("Login realizado con éxito.")

        time.sleep(5) # Esperar a que la app cargue completamente

        # Paso 2: Realizar la solicitud de servicio
        print("Ejecutando el flujo de solicitud de servicio...")
        service_moto_request.booking_request(driver)
        print("Solicitud de servicio completada con éxito.")

        print("Flujo E2E completado exitosamente.")

    except Exception as e:
        print(f"Error durante el flujo E2E: {e}")

    finally:
        print("Finalizando el flujo E2E.")