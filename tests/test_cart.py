import allure

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestCartPage:
    @allure.title("Add product to cart and verify")
    def test_add_to_cart(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        cart_page = CartPage(logged_in_page)

        with allure.step("Add product to cart"):
            inventory_page.add_product_to_cart()
        with allure.step("Go to cart page"):
            inventory_page.go_to_cart()
        with allure.step("Verify product name in cart"):
            assert "Sauce Labs Backpack" in cart_page.get_product_name()

    @allure.title("Verify cart count after adding product")
    def test_cart_count(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        cart_page = CartPage(logged_in_page)

        with allure.step("Add product to cart"):
            inventory_page.add_product_to_cart()
        with allure.step("Go to cart page"):
            inventory_page.go_to_cart()

        with allure.step("Verify cart count after adding product"):
            assert "1" == cart_page.get_cart_count()
