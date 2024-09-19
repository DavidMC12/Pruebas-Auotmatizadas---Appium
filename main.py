# main.py
from setup import driver_setup as ds
from tests import login, service_moto_request, service_motovip_request, signup, service_pibox_request, programed_service_moto

def main():
    # Inicializar el driver
    driver = ds.init_driver()

    # Ejecutar el proceso de login
    #login.login(driver)
    
    # Ejecutar el proceso de registro
    #signup.signUp(driver)
    
    # Pedir un Servicio de Moto
    #service_moto_request.booking_request(driver)
    
    # Pedir un Servicio de Moto VIP
    #service_motovip_request.booking_request(driver)

    # Pedir un Servicio de Pibox
    #service_pibox_request.booking_request(driver)
    
    # Servicio de Moto programado
    programed_service_moto.booking_request(driver)
    
if __name__ == "__main__":
    main()