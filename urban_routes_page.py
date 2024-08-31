from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import data


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


        self.from_field = (By.ID, 'from')
        self.to_field = (By.ID, 'to')
        self.comfort_option = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/img')
        self.active_comfort_option = (By.CSS_SELECTOR, '.tcard.active .tcard-title')
        self.next_step_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]')
        self.phone_field = (By.ID, 'phone')
        self.sms_code_field = (By.ID, 'code')
        self.confirm_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
        self.payment_method_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]')
        self.add_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')
        self.card_number_field = (By.ID, 'number')
        self.card_code_field = (By.ID, 'code')
        self.confirm_add_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
        self.close_modal_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
        self.message_field = (By.ID, 'comment')
        self.blanket_switch = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div')
        self.ice_cream_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
        self.ice_cream_counter = (By.CSS_SELECTOR, '.counter-value')
        self.request_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button')
        self.first_next_button_xpath = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]')
        self.card_payment_option_xpath = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/div/img')
        self.success_message = (By.CSS_SELECTOR, '.order-body')

    def set_from(self, address):
        from_field_element = self.wait.until(EC.presence_of_element_located(self.from_field))
        from_field_element.clear()
        from_field_element.send_keys(address)

    def set_to(self, address):
        to_field_element = self.wait.until(EC.presence_of_element_located(self.to_field))
        to_field_element.clear()
        to_field_element.send_keys(address)

    def get_from(self):
        return self.wait.until(EC.presence_of_element_located(self.from_field)).get_attribute('value')

    def get_to(self):
        return self.wait.until(EC.presence_of_element_located(self.to_field)).get_attribute('value')

    def select_comfort_tariff(self):
        comfort_element = self.wait.until(EC.element_to_be_clickable(self.comfort_option))
        comfort_element.click()

    def is_tariff_selected(self, tariff_name):
        active_tariff_element = self.wait.until(EC.presence_of_element_located(self.active_comfort_option))
        return active_tariff_element.text == tariff_name

    def set_phone_number(self, phone_number):
        phone_field_element = self.wait.until(EC.presence_of_element_located(self.phone_field))
        phone_field_element.clear()
        phone_field_element.send_keys(phone_number)

    def click_next_button_after_phone(self):
        next_button = self.wait.until(EC.element_to_be_clickable(self.first_next_button_xpath))
        next_button.click()

    def set_phone_confirmation_code(self, code):
        sms_code_element = self.wait.until(EC.presence_of_element_located(self.sms_code_field))
        sms_code_element.clear()
        sms_code_element.send_keys(code)

    def click_confirm_button(self):
        confirm_button_element = self.wait.until(EC.element_to_be_clickable(self.confirm_button))
        confirm_button_element.click()

    def is_phone_code_confirmed(self):
        phone_field_element = self.wait.until(EC.presence_of_element_located(self.phone_field))
        return phone_field_element.get_attribute('value') == data.phone_number

    def open_payment_method(self):
        payment_method_button_element = self.wait.until(EC.element_to_be_clickable(self.payment_method_button))
        payment_method_button_element.click()

    def open_add_card_modal(self):
        add_card_button_element = self.wait.until(EC.element_to_be_clickable(self.add_card_button))
        add_card_button_element.click()

    def set_card_details(self, card_number, card_code):
        card_number_field_element = self.wait.until(EC.presence_of_element_located(self.card_number_field))
        card_number_field_element.clear()
        card_number_field_element.send_keys(card_number)

        card_code_field_element = self.wait.until(EC.presence_of_element_located(self.card_code_field))
        card_code_field_element.clear()
        card_code_field_element.send_keys(card_code)

        card_code_field_element.send_keys(Keys.TAB)  # Simular cambio de enfoque para activar el botón "Agregar"

    def click_confirm_add_card_button(self):
        confirm_button_element = self.wait.until(EC.element_to_be_clickable(self.confirm_add_card_button))
        confirm_button_element.click()

    def close_add_card_modal(self):
        close_button_element = self.wait.until(EC.element_to_be_clickable(self.close_modal_button))
        close_button_element.click()

    def is_card_linked(self):
        payment_method_element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'pp-value-text')))
        return "Tarjeta" in payment_method_element.text

    def set_message_for_driver(self, message):
        message_field_element = self.wait.until(EC.presence_of_element_located(self.message_field))
        message_field_element.clear()
        message_field_element.send_keys(message)

    def is_message_set(self, expected_message):
        message_field_element = self.wait.until(EC.presence_of_element_located(self.message_field))
        return message_field_element.get_attribute('value') == expected_message

    def request_blanket_and_tissues(self):
        blanket_switch_element = self.wait.until(EC.element_to_be_clickable(self.blanket_switch))
        blanket_switch_element.click()

    def is_blanket_requested(self):
        blanket_switch_element = self.wait.until(EC.presence_of_element_located(self.blanket_switch))
        return blanket_switch_element.is_selected()

    def order_two_ice_creams(self):
        ice_cream_button_element = self.wait.until(EC.element_to_be_clickable(self.ice_cream_button))
        ice_cream_button_element.click()  # Primer clic
        ice_cream_button_element.click()  # Segundo clic

    def is_ice_cream_ordered(self, expected_quantity):
        ice_cream_counter_element = self.wait.until(EC.presence_of_element_located(self.ice_cream_counter))
        actual_quantity = int(ice_cream_counter_element.text)
        return actual_quantity == expected_quantity

    def request_taxi(self):
        request_taxi_button_element = self.wait.until(EC.element_to_be_clickable(self.request_taxi_button))
        request_taxi_button_element.click()
        self.wait.until(EC.presence_of_element_located(self.success_message))  # Esperar hasta que aparezca el mensaje de éxito

    def is_taxi_requested_successfully(self):
        try:
            success_message_element = self.wait.until(EC.presence_of_element_located(self.success_message))
            return success_message_element.is_displayed()
        except:
            return False
