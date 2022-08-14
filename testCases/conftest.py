from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Inspire Test Challenge'
    config._metadata['Module Name'] = 'Creating Post'
    config._metadata['Tester'] = 'Naveen Vikraman'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)