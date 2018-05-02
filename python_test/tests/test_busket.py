import pytest


def test_busket(app):

    for i in range(2):
        app.add_product_to_card()
    app.remove_all_from_cart()
