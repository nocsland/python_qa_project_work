import allure

from page_objects.BasePage import BasePage


class CatalogPage(BasePage):
    path = '/index.php?route=product/category&path=20'

    @allure.step('Найти элемент "top div"')
    def find_top_menu(self):
        self.browser.find_element_by_css_selector('#top > div.container')
        self.logger.info("top div was found")
        return self

    @allure.step('Найти элемент "column-left"')
    def find_left_menu(self):
        self.browser.find_element_by_id('column-left')
        self.logger.info("left column was found")
        return self

    @allure.step('Найти элемент "Product Compare"')
    def find_link_product_compare(self):
        self.browser.find_element_by_partial_link_text('Product Compare')
        self.logger.info("Product Compare was found")
        return self

    @allure.step('Найти элемент "input-group"')
    def find_class_input_group(self):
        self.browser.find_element_by_class_name('input-group')
        self.logger.info("class input-group was found")
        return self

    @allure.step('Найти кнопку "search"')
    def find_search_button(self):
        self.browser.find_element_by_xpath('//*[@id="search"]/span/button')
        self.logger.info("search button was found")
        return self

    @allure.step('Добавить в лист сравнения товары')
    def add_compare_list(self, number):
        self.browser.find_elements_by_css_selector('.fa-exchange')[number].click()
        self.logger.info("add to compare list")
        return self

    @allure.step('Открыть лист сравнения')
    def open_compare_list(self):
        self.browser.find_element_by_partial_link_text('product comparison').click()
        self.logger.info("compare list opened")
        return self
