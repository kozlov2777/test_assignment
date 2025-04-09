import re
from decimal import Decimal, InvalidOperation


def extract_price_as_decimal(text: str) -> Decimal:
    """
    Extracts price from text and converts it to Decimal.

    Args:
        text: Text containing a price (e.g., '$29.99', 'Item total: $29.99', or '29.99')

    Returns:
        Decimal: Price as a Decimal object

    Raises:
        ValueError: If price cannot be extracted or converted
    """
    # First, look for $XX.XX format
    price_match = re.search(r"\$(\d+\.\d+)", text)
    if price_match:
        price_str = price_match.group(1)
    else:
        # If not found, look for just XX.XX
        price_match = re.search(r"(\d+\.\d+)", text)
        if price_match:
            price_str = price_match.group(1)
        else:
            # If nothing found, remove all symbols except digits and dot
            price_str = re.sub(r"[^\d.]", "", text)
            if not price_str:
                raise ValueError(f"Could not extract price from text: '{text}'")

    try:
        return Decimal(price_str)
    except InvalidOperation as e:
        raise ValueError(f"Could not convert '{price_str}' to Decimal: {str(e)}")
