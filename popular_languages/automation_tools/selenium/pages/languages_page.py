from selenium.webdriver.common.by import By
from automation_tools.selenium.base_element import BaseElement as Be
from automation_tools.selenium.base_page import BasePage as Bp
from automation_tools.selenium.locator import Locator


class LanguagesPage(Bp):
    def cell_contents_by_row_cell(self, row: int, cell: int):
        return Be(
            driver=self.driver, locator=Locator(
                by=By.CSS_SELECTOR,
                value=f"table.wikitable:nth-of-type(1) tbody tr:nth-of-type({row}) td:nth-of-type({cell})"))
