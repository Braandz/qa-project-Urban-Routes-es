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
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        assert routes_page.get_from() == data.address_from  # Assert 1
        assert routes_page.get_to() == data.address_to  # Assert 1.1

    def test_set_comfort_rate(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_comfort_tariff()
        assert routes_page.is_tariff_selected("Comfort")  # Assert 2

    def test_enter_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_phone_number(data.phone_number)
        routes_page.click_next_button_after_phone()
        confirmation_code = retrieve_phone_code(self.driver)
        routes_page.set_phone_confirmation_code(confirmation_code)
        routes_page.click_confirm_button()
        assert routes_page.is_phone_code_confirmed()  # Assert 3

    def test_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.open_payment_method()
        routes_page.open_add_card_modal()
        routes_page.set_card_details(data.card_number, data.card_code)
        routes_page.click_confirm_add_card_button()
        routes_page.close_add_card_modal()
        assert routes_page.is_card_linked()  # Assert 4

    def test_send_message_to_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_message_for_driver(data.message_for_driver)
        assert routes_page.is_message_set(data.message_for_driver)  # Assert 5

    def test_request_blanket_and_tissues(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_blanket_and_tissues()
        assert routes_page.is_blanket_requested()  # Assert 6

    def test_order_two_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_two_ice_creams()
        assert routes_page.is_ice_cream_ordered(2)  # Assert 7

    def test_request_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_taxi()
        assert routes_page.is_taxi_requested_successfully()  # Assert 8

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
