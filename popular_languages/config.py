from selenium import webdriver


class Config:
    def __init__(self, configuration):
        # Path to logs
        LOG_PATH = configuration['log-path']

        self.log_path = LOG_PATH

        # Choose browser
        BROWSER = configuration["browser"]

        SUPPORTED_BROWSERS = ["remote"]

        if BROWSER.lower() not in SUPPORTED_BROWSERS:
            raise Exception(f"{BROWSER} is not supported (supported browsers: {SUPPORTED_BROWSERS})")

        # window size parameters
        height = "1080"
        width = "1920"

        # remote options
        remote_options = webdriver.ChromeOptions()
        remote_options.add_argument(f"--window-size={width},{height}")

        supported_browsers_dict = {
            "remote": [webdriver.Remote, "http://selenium-hub:4444", remote_options],
        }

        self.browser = supported_browsers_dict[BROWSER]
