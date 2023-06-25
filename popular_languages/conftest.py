from pytest import fixture
from config import Config
from utilities.logs import CaseLogs


@fixture(scope="function")
def driver(app_config, get_parameters):
    # create browser instance
    new_browser = app_config.browser[0]

    selenium_hub_address = app_config.browser[1]
    options = app_config.browser[2]
    driver = new_browser(command_executor=selenium_hub_address, options=options)

    yield driver

    driver.quit()


@fixture(scope='session')
def log(app_config):
    case_logs = CaseLogs(app_config.log_path)
    case_logs.clean_artifacts()

    return case_logs


def pytest_addoption(parser):
    parser.addoption('--browser',
                     action='store',
                     help='Specify browser, for example, "remote".',
                     default='remote')
    parser.addoption('--log-path',
                     action='store',
                     help='Specify where to store test case logs.')


@fixture(scope="session")
def get_parameters(request):
    config_param = {
        'browser': request.config.getoption('--browser'),
        'log-path': request.config.getoption('--log-path'),
    }
    return config_param


@fixture(scope="session")
def app_config(get_parameters):
    configuration = Config(get_parameters)
    return configuration
