from __future__ import annotations


def view_basket(basket: dict[str, float]) -> None:
    if basket:
        print("\nCurrent Basket:")
        for item, cost in basket.items():
            print(f"{item}: ${cost:.2f}")
        print(f"Total: ${sum(basket.values()):.2f}")
    else:
        print("Your basket is empty.")
