"""Chat handler: parse a user message and call services."""

from __future__ import annotations

import re
from typing import Any

from support_bot.services.order_status import getOrderStatus
from support_bot.services.product_catalog import file_search_products


def handle_user_query(user_input: str, debug: bool = False):
    """Handle a simple user query by using the product-search and order-status tools.

    If `debug` is True, also return a dict describing which tools were called and
    with what arguments.
    """

    tools_called: list[dict[str, Any]] = []
    text = (user_input or "").strip()

    # find order id like #12345 or ORD123 or just digits
    order_match = re.search(r"#?([0-9]{3,})", text)
    order_info = None
    if order_match:
        oid = order_match.group(1)
        order_info = getOrderStatus(oid)
        tools_called.append({"tool": "getOrderStatus", "args": [oid]})

    # identify product search term - look for quoted phrases, or tokens like 'pro'
    prod_term = None
    # Prefer quoted phrases but avoid matching contractions (e.g., What's)
    qmatch = re.search(
        r"(?:(?<=\s)|(?<=^))'([^']+?)'(?=(?:\s|[.,?!]|$))|\"([^\"]+?)\"", text
    )
    if qmatch:
        prod_term = qmatch.group(1) or qmatch.group(2)
    else:
        if "pro" in text.lower():
            prod_term = "pro"

    products_found = []
    if prod_term:
        products_found = file_search_products(prod_term)
        tools_called.append({"tool": "file_search_products", "args": [prod_term]})

    # build response
    parts: list[str] = []
    if products_found:
        p = products_found[0]
        parts.append(f"{p['name']} — {p.get('description','')} Price: ${p['price']}")
        if len(products_found) > 1:
            parts.append(f"({len(products_found)-1} more matches found.)")
    elif prod_term:
        parts.append(f"No products found matching '{prod_term}'.")

    if order_info:
        parts.append(f"Order {order_info['order_id']} is currently {order_info['status']}.")
        if order_info.get("estimated_delivery"):
            parts.append(f"Estimated delivery: {order_info['estimated_delivery']}")

    if not parts:
        parts.append("Sorry — I couldn't find product or order information in your question.")

    response = " ".join(parts)
    if debug:
        return response, {"tools_called": tools_called}
    return response


def create_thread_and_ask(question: str):
    """Simulate creating a thread and asking the assistant; returns response and debug info."""

    return handle_user_query(question, debug=True)
