class CartPage:
    def __init__(self, page):
        self.page = page

        self.cart_item = ".inventory_item_name"
        self.cart_badge = ".shopping_cart_badge"

    def get_product_name(self):
        return self.page.text_content(self.cart_item)

    def get_cart_count(self):
        return self.page.text_content(self.cart_badge)