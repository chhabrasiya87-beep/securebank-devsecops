def calculate_transfer_fee(amount):
    """Calculate a simple 1% transfer fee."""
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    return round(amount * 0.01, 2)


def validate_transfer(amount):
    """Check whether a transfer amount is valid."""
    return amount > 0
