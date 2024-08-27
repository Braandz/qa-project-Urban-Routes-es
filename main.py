import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""
    import json
    import time
    from selenium.common import WebDriverException

    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    comfort_option = (By.CSS_SELECTOR, '.tcard-title')  # Localizador para la tarifa Comfort
    phone_field = (By.ID, 'phone')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.ID, 'code')
    link_button = (By.ID, 'link')
    message_field = (By.ID, 'message')
    blanket_checkbox = (By.CSS_SELECTOR, '.switch-input')  # Checkbox para manta y pañuelos
    tissues_checkbox = (By.CSS_SELECTOR, '.switch-input')  # Checkbox para manta y pañuelos
    ice_cream_quantity = (By.CSS_SELECTOR, '.counter')  # Selector para la cantidad de helado
    search_taxi_modal = (By.CSS_SELECTOR, '#search-taxi-modal')  # Modal de búsqueda de taxi
    driver_info_modal = (By.CSS_SELECTOR, '#driver-info-modal')  # Modal de información del conductor

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def select_comfort_tariff(self):
        self.driver.find_element(*self.comfort_option).click()  # Seleccionar la tarifa Comfort

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_field).send_keys(phone_number)

    def add_credit_card(self, card_number, card_code):
        self.driver.find_element(*self.card_number_field).send_keys(card_number)
        card_code_field = self.driver.find_element(*self.card_code_field)
        card_code_field.send_keys(card_code)
        # Cambiar el enfoque para activar el botón de enlace
        card_code_field.send_keys(Keys.TAB)

    def submit_card(self):
        self.driver.find_element(*self.link_button).click()

    def write_message_to_driver(self, message):
        self.driver.find_element(*self.message_field).send_keys(message)

    def request_blanket_and_tissues(self):
        self.driver.find_element(*self.blanket_checkbox).click()
        self.driver.find_element(*self.tissues_checkbox).click()

    def request_ice_cream(self, quantity):
        ice_cream_field = self.driver.find_element(*self.ice_cream_quantity)
        ice_cream_field.clear()
        ice_cream_field.send_keys(quantity)

    def wait_for_driver_info(self):
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(self.driver_info_modal)
        )


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # Actualizar la inicialización del driver sin 'desired_capabilities'
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

        # Agregar la tarjeta de crédito
        routes_page.add_credit_card(data.card_number, data.card_code)
        # Obtener y usar el código de confirmación del teléfono
        confirmation_code = retrieve_phone_code(self.driver)
        routes_page.submit_card()

        # Escribir un mensaje para el conductor
        routes_page.write_message_to_driver(data.message_for_driver)

        # Pedir una manta y pañuelos
        routes_page.request_blanket_and_tissues()

        # Pedir 2 helados
        routes_page.request_ice_cream(2)

        # Esperar a que aparezca la información del conductor en el modal (opcional)
        routes_page.wait_for_driver_info()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
