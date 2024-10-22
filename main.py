import pytest
import allure
from setup import driver_setup as ds
from tests import test_driver_register, test_bicitaxi_request, test_grua_request, test_chat_central, test_add_new_vehicle, service_moto_request, service_motovip_request, signup, service_pibox_request, programed_service_moto, test_login

# Caso de prueba para pytest
# @pytest.mark.allure
# def test_login():
#     # Inicializar el driver
#     driver = ds.init_driver()

#     # Ejecutar el proceso de login
#     with allure.step("Ejecutar flujo de login"):
#         test_login.test_login_flow(driver)

#     # Finalizar driver después de las pruebas
#     driver.quit()

# Más casos de prueba pueden ir aquí
# @pytest.mark.allure
# def test_signup():
#     driver = ds.init_driver()
#     with allure.step("Ejecutar flujo de registro"):
#         signup.signUp(driver)
#     driver.quit()

# Función principal, no para pytest, solo para ejecución manual
def main():
    # Inicializar el driver
    driver = ds.init_driver()

    # Ejecutar el proceso de login manualmente
    # test_login.test_login_flow(driver)

    # Ejecutar otros procesos comentados si es necesario
    # signup.signUp(driver)
    # service_moto_request.booking_request(driver)
    # service_motovip_request.booking_request(driver)
    # service_pibox_request.booking_request(driver)
    # programed_service_moto.booking_request(driver)
    # test_add_new_vehicle.addNewVehicle(driver)
    # test_chat_central.main(driver)
    # test_grua_request.gura_request(driver)
    # test_bicitaxi_request.main(driver)
    test_driver_register.main(driver)

    # Finalizar el driver
    # driver.quit()

# Esto solo se ejecuta cuando se corre manualmente
if __name__ == "__main__":
    main()