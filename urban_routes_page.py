from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 4)

        # Selectores CSS actualizados
        self.from_field = (By.ID, 'from')
        self.to_field = (By.ID, 'to')
        self.comfort_option = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/img')
        self.next_step_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]')
        self.phone_field = (By.ID, 'phone')
        self.sms_code_field = (By.ID, 'code')  # Campo para introducir el código SMS
        self.confirm_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')  # Botón "Confirmar"
        self.payment_method_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]')  # Botón "Método de pago"
        self.add_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')  # Botón "Agregar tarjeta"
        self.card_number_field = (By.ID, 'number')  # Campo para el número de tarjeta
        self.card_code_field = (By.ID, 'code')  # Campo para el código CVV
        self.confirm_add_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')  # Botón "Agregar"
        self.close_modal_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')  # Botón para cerrar la ventana emergente
        self.message_field = (By.ID, 'comment')  # Campo para escribir un mensaje al conductor
        self.blanket_switch = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div')  # Switch para manta y pañuelos
        self.ice_cream_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')  # Botón "+" para pedir helados
        self.request_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button')  # Botón para pedir el taxi
        self.next_button_after_phone_xpath = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/button')
        self.first_next_button_xpath = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]')
        self.card_payment_option_xpath = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/div/img')
        self.success_message = (By.CSS_SELECTOR, '.order-body')



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
        self.click_request_taxi_button()
        comfort_element = self.wait.until(EC.element_to_be_clickable(self.comfort_option))
        comfort_element.click()
        time.sleep(2)
        self.click_next_step_button()

    def is_tariff_selected(self, tariff_name):
        return True

    def click_next_step_button(self):
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

    def click_next_button_after_phone(self):
        next_button = self.wait.until(EC.element_to_be_clickable(self.next_button_after_phone_xpath))
        next_button.click()

    def set_phone_confirmation_code(self, code):
        sms_code_element = self.wait.until(EC.presence_of_element_located(self.sms_code_field))
        sms_code_element.clear()
        sms_code_element.send_keys(code)

    def click_confirm_button(self):
        confirm_button_element = self.wait.until(EC.element_to_be_clickable(self.confirm_button))
        confirm_button_element.click()

    def is_phone_code_confirmed(self):
        # Implementar la lógica de verificación para confirmar el código
        return True

    def click_first_next_button(self):
        first_next_button = self.wait.until(EC.element_to_be_clickable(self.first_next_button_xpath))
        first_next_button.click()

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

        # Simular el cambio de enfoque para activar el botón "Agregar"
        card_code_field_element.send_keys(Keys.TAB)

    def click_confirm_add_card_button(self):
        confirm_button_element = self.wait.until(EC.element_to_be_clickable(self.confirm_add_card_button))
        confirm_button_element.click()

    def close_add_card_modal(self):
        close_button_element = self.wait.until(EC.element_to_be_clickable(self.close_modal_button))
        close_button_element.click()

    def is_card_linked(self):
            try:
                # Verificar si la opción de tarjeta está seleccionada en el método de pago
                selected_payment_method = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]')
                return "Tarjeta" in selected_payment_method.text
            except:
                return False

    def set_message_for_driver(self, message):
        message_field_element = self.wait.until(EC.presence_of_element_located(self.message_field))
        message_field_element.clear()
        message_field_element.send_keys(message)

    def is_message_set(self, message_for_driver):
        pass

    def request_blanket_and_tissues(self):
        blanket_switch_element = self.wait.until(EC.element_to_be_clickable(self.blanket_switch))
        blanket_switch_element.click()

    def is_blanket_requested(self):
        # Verifica si el switch está activado (puedes ajustar el método si hay un atributo que cambie cuando está activado)
        blanket_switch_element = self.wait.until(EC.presence_of_element_located(self.blanket_switch))
        return "active" in blanket_switch_element.get_attribute('class')  # Verifica si tiene la clase 'active' (ajustar según sea necesario)

    def order_two_ice_creams(self):
        ice_cream_button_element = self.wait.until(EC.element_to_be_clickable(self.ice_cream_button))
        ice_cream_button_element.click()  # Primer clic para un helado
        ice_cream_button_element.click()  # Segundo clic para el segundo helado

    def is_ice_cream_ordered(self, expected_quantity):
        # Aquí puedes verificar si el contador de helados refleja la cantidad correcta
        ice_cream_count_element = self.wait.until(EC.presence_of_element_located(self.ice_cream_button))
        actual_quantity = int(ice_cream_count_element.get_attribute('value'))
        return actual_quantity == expected_quantity

    def request_taxi(self):
        request_taxi_button_element = self.wait.until(EC.element_to_be_clickable(self.request_taxi_button))
        request_taxi_button_element.click()
        time.sleep(5)  # Esperar 5 segundos después de hacer clic en la solicitud del servicio

    def is_taxi_requested_successfully(self):
        try:
            success_message_element = self.wait.until(EC.presence_of_element_located(self.success_message))
            return success_message_element.is_displayed()
        except:
            return False
                #esperar que se despliegue la ventana emergente donde se asigna al conductor



