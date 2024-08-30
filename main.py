import data
from selenium import webdriver
from urban_routes_page import UrbanRoutesPage
from helpers import retrieve_phone_code


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        options = webdriver.ChromeOptions()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from #assert 1
        assert routes_page.get_to() == address_to #assert 1.1

    def test_request_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)

        # Seleccionar la tarifa Comfort
        routes_page.select_comfort_tariff()
        assert routes_page.is_tariff_selected("Comfort") #assert 2

        # Rellenar el número de teléfono
        routes_page.set_phone_number(data.phone_number) #No se requiere un assert en este paso específico ya que solo se introduce el número de teléfono y se pasa al siguiente paso.

        # Clic en el botón "Siguiente" después de ingresar el número de teléfono
        routes_page.click_next_button_after_phone()

        # Obtener y establecer el código de confirmación
        confirmation_code = retrieve_phone_code(self.driver)
        routes_page.set_phone_confirmation_code(confirmation_code)

        # Clic en el botón "Confirmar"
        routes_page.click_confirm_button()
        assert routes_page.is_phone_code_confirmed() #assert 3

        # Abrir el modal de "Método de pago"
        routes_page.open_payment_method()

        # Abrir el modal "Agregar tarjeta"
        routes_page.open_add_card_modal()

        # Ingresar detalles de la tarjeta de crédito
        routes_page.set_card_details(data.card_number, data.card_code)
        routes_page.click_confirm_add_card_button()

        # Cerrar el modal de "Agregar tarjeta"
        routes_page.close_add_card_modal()

        assert routes_page.is_card_linked()  # Método a implementar para verificar que la tarjeta se agregó correctamente
                #assert 4
        # Escribir un mensaje para el conductor
        routes_page.set_message_for_driver(data.message_for_driver)
        assert routes_page.is_message_set(data.message_for_driver)  # Método para verificar que el mensaje fue ingresado correctamente
                #assert 5
        # Pedir una manta y pañuelos
        routes_page.request_blanket_and_tissues()
        assert routes_page.is_blanket_requested()  # Método para verificar que el switch se activó correctamente
                #assert 6
        # Pedir 2 helados
        routes_page.order_two_ice_creams()
        assert routes_page.is_ice_cream_ordered(2)  # Método para verificar que se pidieron 2 helados
                #assert7
        # Pedir el taxi

        routes_page.request_taxi()
        assert routes_page.is_taxi_requested_successfully()  # Método para verificar que el taxi fue pedido correctamente
                #assert8
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
