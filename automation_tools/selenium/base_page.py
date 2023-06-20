class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go(self, url: str) -> None:
        self.driver.get(url)

    def refresh(self) -> None:
        self.driver.refresh()

    def switch_to_tab(self, tab: int) -> None:
        self.driver.switch_to.window(self.driver.window_handles[tab])

    def scroll(self, to: str = "bottom") -> None:
        """
        .scroll(50px)
        """
        if to == "bottom":
            value = "document.body.scrollHeight"
        elif to == "top":
            value = 0
        else:
            value = int(to[:-2])
        self.driver.execute_script(f"window.scrollTo(0, {value});")
