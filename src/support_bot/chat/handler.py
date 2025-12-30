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

    # identify product search term - look for quoted phrases first, then extract nouns
    prod_term = None
    # Prefer quoted phrases but avoid matching contractions (e.g., What's)
    qmatch = re.search(
        r"(?:(?<=\s)|(?<=^))'([^']+?)'(?=(?:\s|[.,?!]|$))|\"([^\"]+?)\"", text
    )
    if qmatch:
        prod_term = qmatch.group(1) or qmatch.group(2)
    else:
        # Extract potential product names (words after articles/verbs like "sell", "have", "price of")
        # Try common patterns: "sell X", "have X", "price of X", "about X"
        patterns = [
            r"(?:sell|have|price\s+of|about)\s+(?:a\s+)?(?:the\s+)?(\w+)",
            r"(?:treadmill|skateboard|router|chair|lamp|headphone|camera|monitor|speaker|keyboard|mouse|phone|tablet|watch|charger|cable)",
        ]
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                prod_term = match.group(1) if match.lastindex else match.group(0)
                break
        
        # If still no match, try to extract the longest meaningful word (skip common words)
        if not prod_term:
            common_words = {"do", "you", "sell", "have", "what", "can", "is", "it", "the", "a", "an", "or", "and", "price", "of", "for", "with", "in", "on", "at", "to", "that", "this", "about", "does"}
            words = re.findall(r"\b[a-z]{3,}\b", text.lower())
            for word in sorted(words, key=len, reverse=True):
                if word not in common_words:
                    prod_term = word
                    break
        
        # Remove trailing 's' for plurals to improve matching
        if prod_term and prod_term.endswith('s'):
            singular = prod_term[:-1]
            if len(singular) >= 3:  # Only if it makes sense
                prod_term = singular

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
