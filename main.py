# main.py

from selenium import webdriver
from urban_routes_page import UrbanRoutesPage
from helpers import retrieve_phone_code
import data

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
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_request_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)

        # Seleccionar la tarifa Comfort
        routes_page.select_comfort_tariff()

        # Rellenar el número de teléfono
        routes_page.set_phone_number(data.phone_number)

        # Hacer clic en el primer XPath
        routes_page.click_first_xpath()

        # Hacer clic en el segundo XPath
        routes_page.click_second_xpath()

        # Agregar el número de tarjeta y el código
        routes_page.set_card_number(data.card_number)
        routes_page.set_card_code(data.card_code)

        # Obtener y usar el código de confirmación del teléfono
        confirmation_code = retrieve_phone_code(self.driver)
        routes_page.set_card_code(confirmation_code)  # Asumiendo que necesitas ingresar el código de confirmación en el campo de código de tarjeta

        # Hacer clic en el botón "Submit"
        routes_page.click_request_taxi_button()

        # Escribir un mensaje para el conductor
        routes_page.set_message_for_driver(data.message_for_driver)

        # Pedir una manta y pañuelos
        routes_page.select_blanket_checkbox()

        # Pedir 2 helados
        routes_page.set_ice_cream_quantity(2)

        # Esperar a que aparezca la información del conductor en el modal (opcional)
        routes_page.handle_driver_info_modal()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
