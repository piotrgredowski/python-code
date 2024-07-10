from __future__ import annotations


def view_cart(cart: dict[str, float]) -> None:
    if cart:
        print("\nCurrent Cart:")
        for item, cost in cart.items():
            print(f"{item}: ${cost:.2f}")
        print(f"Total: ${sum(cart.values()):.2f}")
    else:
        print("Your cart is empty.")
