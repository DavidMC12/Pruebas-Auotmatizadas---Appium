# main.py
from setup import driver_setup as ds
from tests import login, signup, service_request

def main():
    # Inicializar el driver
    driver = ds.init_driver()

    # Ejecutar el proceso de login
    #login.login(driver)
    
    # Ejecutar el proceso de registro
    #signup.signUp(driver)
    
    # Pedir un Servicio de Booking
    service_request.booking_request(driver)

if __name__ == "__main__":
    main()