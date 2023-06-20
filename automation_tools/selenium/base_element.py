from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time


class BaseElement:
    def __init__(self, driver, locator, wait_time=3):
        self.driver = driver
        self.locator = locator
        self.wait_time = wait_time

        self.web_element = None
        self.find()

    def find(self) -> None:
        element = WebDriverWait(self.driver, self.wait_time).until(
            ec.presence_of_element_located(locator=self.locator))
        self.web_element = element

    def click(self) -> None:
        element = WebDriverWait(self.driver, self.wait_time).until(
            ec.element_to_be_clickable(self.locator), ec.staleness_of(self.locator))
        element.click()

    def press_enter(self) -> None:
        element = WebDriverWait(self.driver, self.wait_time).until(
            ec.element_to_be_clickable(self.locator))
        element.send_keys(Keys.RETURN)

    def input_text(self, text: str) -> None:
        element = WebDriverWait(self.driver, self.wait_time).until(
            ec.element_to_be_clickable(self.locator))
        element.send_keys(Keys.CONTROL, "a", Keys.DELETE)
        element.send_keys(text)

    def attach_file(self, file_path: str) -> None:
        self.web_element.send_keys(file_path)

    def display_hidden(self) -> None:
        self.driver.execute_script(f"arguments[0].setAttribute(arguments[1], arguments[2])",
                                   self.web_element, "style", "display: yes;")

    def hide_element(self) -> None:
        self.driver.execute_script(f"arguments[0].setAttribute(arguments[1], arguments[2])",
                                   self.web_element, "style", "display: none;")

    def attach_file_to_hidden_input(self, file_path: str) -> None:
        self.display_hidden()
        self.attach_file(file_path)
        self.hide_element()

    @property
    def text(self) -> str:
        text = self.web_element.text
        return text

    def attribute_by_name(self, attr_name: str) -> str:
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    def has_attribute(self, attr_name: str) -> bool:
        inner_html = self.attribute_by_name("innerHTML")
        if attr_name in inner_html:
            return True
        else:
            return False

    def is_visible(self) -> bool:
        try:
            WebDriverWait(self.driver, 0).until(
                ec.visibility_of_element_located(self.locator))
            return True
        except TimeoutException:
            return False

    def exists(self) -> bool:
        try:
            WebDriverWait(self.driver, 0).until(
                ec.presence_of_element_located(self.locator))
            return True
        except TimeoutException:
            return False

    def is_not_visible(self) -> bool:
        try:
            WebDriverWait(self.driver, self.wait_time).until(
                ec.invisibility_of_element_located(self.locator))
            return True
        except TimeoutException:
            return False

    def wait_until_text_changes_to(self, required_text: str) -> None:

        timeout = time.time() + self.wait_time

        while self.web_element.text != required_text:
            time.sleep(1)
            if time.time() > timeout:
                raise TimeoutException("Text has not changed")

    def scroll_to_element(self) -> None:
        self.driver.execute_script("arguments[0].scrollIntoView();", self.web_element)
