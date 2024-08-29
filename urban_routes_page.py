
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # Selectores CSS actualizados
        self.from_field = (By.ID, 'from')
        self.to_field = (By.ID, 'to')
        self.comfort_option = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/img')
        self.next_step_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]')
        self.phone_field = (By.ID, 'phone')
        self.card_number_field = (By.ID, 'number')
        self.card_code_field = (By.ID, 'code')
        self.link_button = (By.ID, 'link')
        self.message_field = (By.ID, 'message')
        self.blanket_checkbox = (By.CSS_SELECTOR, '.switch-input')
        self.ice_cream_quantity = (By.CSS_SELECTOR, '.counter')
        self.search_taxi_modal = (By.CSS_SELECTOR, '#search-taxi-modal')
        self.driver_info_modal = (By.CSS_SELECTOR, '#driver-info-modal')
        self.request_taxi_button = (By.CSS_SELECTOR, 'button.button.round')

        # Nuevos selectores para los elementos a hacer clic
        self.click_first_xpath = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]')
        self.click_second_xpath = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/div/img')

    def click_element_by_xpath(self, xpath):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
        time.sleep(2)

    def set_from(self, address):
        from_field_element = self.wait.until(EC.presence_of_element_located(self.from_field))
        from_field_element.clear()
        from_field_element.send_keys(address)
        time.sleep(2)

    def set_to(self, address):
        to_field_element = self.wait.until(EC.presence_of_element_located(self.to_field))
        to_field_element.clear()
        to_field_element.send_keys(address)
        time.sleep(2)

    def get_from(self):
        return self.wait.until(EC.presence_of_element_located(self.from_field)).get_attribute('value')

    def get_to(self):
        return self.wait.until(EC.presence_of_element_located(self.to_field)).get_attribute('value')

    def select_comfort_tariff(self):
        self.click_element_by_xpath(self.comfort_option[1])
        time.sleep(2)
        self.click_next_button_after_phone()

    def click_next_button_after_phone(self):
        next_step_element = self.wait.until(EC.element_to_be_clickable(self.next_step_button))
        next_step_element.click()
        time.sleep(2)

    def click_request_taxi_button(self):
        request_taxi_button = self.wait.until(EC.element_to_be_clickable(self.request_taxi_button))
        request_taxi_button.click()
        time.sleep(2)

    def set_phone_number(self, phone_number):
        phone_field_element = self.wait.until(EC.presence_of_element_located(self.phone_field))
        phone_field_element.clear()
        phone_field_element.send_keys(phone_number)

    def click_first_xpath(self):
        self.click_element_by_xpath(self.click_first_xpath[1])

    def click_second_xpath(self):
        self.click_element_by_xpath(self.click_second_xpath[1])

    def set_card_number(self, card_number):
        card_number_field_element = self.wait.until(EC.presence_of_element_located(self.card_number_field))
        card_number_field_element.clear()
        card_number_field_element.send_keys(card_number)

    def set_card_code(self, card_code):
        card_code_field_element = self.wait.until(EC.presence_of_element_located(self.card_code_field))
        card_code_field_element.clear()
        card_code_field_element.send_keys(card_code)

    def set_message_for_driver(self, message):
        message_field_element = self.wait.until(EC.presence_of_element_located(self.message_field))
        message_field_element.clear()
        message_field_element.send_keys(message)

    def select_blanket_checkbox(self):
        blanket_checkbox_element = self.wait.until(EC.element_to_be_clickable(self.blanket_checkbox))
        if not blanket_checkbox_element.is_selected():
            blanket_checkbox_element.click()

    def set_ice_cream_quantity(self, quantity):
        ice_cream_quantity_element = self.wait.until(EC.presence_of_element_located(self.ice_cream_quantity))
        ice_cream_quantity_element.clear()
        ice_cream_quantity_element.send_keys(quantity)

    def handle_search_taxi_modal(self):
        search_taxi_modal = self.wait.until(EC.presence_of_element_located(self.search_taxi_modal))
        # Añadir acciones necesarias con el modal aquí

    def handle_driver_info_modal(self):
        driver_info_modal = self.wait.until(EC.presence_of_element_located(self.driver_info_modal))
        # Añadir acciones necesarias con el modal aquí
