from models.shopping_cart_models import ShoppingCart


class TestCreateShoppingCart:
    def test_create_cart(self):
        cart = ShoppingCart()
        assert cart.items == []
        assert not cart.items


class TestAddItem:
    def test_add_new_item(self):
        cart = ShoppingCart()
        cart.add_item('маракуйя', 37, 4)
        print(cart.__dict__)
        assert cart.items == [{'name': 'маракуйя', 'price': 37, 'quantity': 4}]

    def test_add_different_items(self):
        cart = ShoppingCart()
        cart.add_item('маракуйя', 37, 4)
        cart.add_item('дуріан', 83, 6)
        assert len(cart.items) == 2

    def test_add_existing_item_sums_quantity(self):
        cart = ShoppingCart()
        cart.add_item('маракуйя', 37, 4)
        cart.add_item('маракуйя', 37, 9)
        assert len(cart.items) == 1
        assert cart.items[0]['quantity'] == 13

    def test_add_existing_item_overwrites_price(self):
        cart = ShoppingCart()
        cart.add_item('маракуйя', 37, 4)
        cart.add_item('маракуйя', 52, 9)
        print(cart.__dict__)
        assert cart.items == [{'name': 'маракуйя', 'price': 52, 'quantity': 13}]


class TestRemoveItem:
    def test_remove_item(self):
        cart = ShoppingCart()
        cart.add_item('маракуйя', 37, 4)
        cart.add_item('дуріан', 83, 6)
        cart.remove_item('маракуйя')
        assert cart.items == [{'name': 'дуріан', 'price': 83, 'quantity': 6}]

    def test_remove_last_item(self):
        cart = ShoppingCart()
        cart.add_item('маракуйя', 37, 4)
        cart.remove_item('маракуйя')
        assert not cart.items

    def test_remove_missing_item_does_nothing(self):
        cart = ShoppingCart()
        cart.add_item('маракуйя', 37, 4)
        cart.remove_item('пітахая')
        assert cart.items == [{'name': 'маракуйя', 'price': 37, 'quantity': 4}]

    def test_remove_from_empty_cart(self):
        cart = ShoppingCart()
        cart.remove_item('пітахая')
        assert cart.items == []