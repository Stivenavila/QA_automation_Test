class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    '''El método find_element(self, *locator) tomará como argumento el localizador que le especifiquemos'''


