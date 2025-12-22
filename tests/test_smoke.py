from support_bot import handle_user_query
from support_bot.services.order_status import getOrderStatus
from support_bot.services.product_catalog import file_search_products


def test_order_status_shape():
    data = getOrderStatus("#12345")
    assert data["order_id"]
    assert data["status"]


def test_product_search_returns_list():
    res = file_search_products("pro")
    assert isinstance(res, list)


def test_handle_user_query_returns_string():
    out = handle_user_query("What's the price of the 'Pro' model?")
    assert isinstance(out, str)
    assert out
