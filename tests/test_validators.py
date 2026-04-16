import pytest
from bot import validators

def test_validate_symbol():
    # Valid
    assert validators.validate_symbol("BTCUSDT") == "BTCUSDT"
    assert validators.validate_symbol(" ethusdt ") == "ETHUSDT"
    
    # Invalid
    with pytest.raises(ValueError, match="cannot be empty"):
        validators.validate_symbol("")
    with pytest.raises(ValueError, match="alphanumeric"):
        validators.validate_symbol("BTC-USDT")

def test_validate_side():
    # Valid
    assert validators.validate_side("BUY") == "BUY"
    assert validators.validate_side("sell") == "SELL"
    
    # Invalid
    with pytest.raises(ValueError, match="cannot be empty"):
        validators.validate_side("")
    with pytest.raises(ValueError, match="Must be 'BUY' or 'SELL'"):
        validators.validate_side("SHORT")

def test_validate_order_type():
    # Valid
    assert validators.validate_order_type("MARKET") == "MARKET"
    assert validators.validate_order_type("limit") == "LIMIT"
    assert validators.validate_order_type("STOP_LIMIT") == "STOP_LIMIT"
    
    # Invalid
    with pytest.raises(ValueError, match="cannot be empty"):
        validators.validate_order_type("")
    with pytest.raises(ValueError, match="MARKET"):
        validators.validate_order_type("STOP_MARKET")

def test_validate_quantity():
    # Valid
    assert validators.validate_quantity("1.5") == 1.5
    assert validators.validate_quantity(2) == 2.0
    
    # Invalid
    with pytest.raises(ValueError, match="positive number"):
        validators.validate_quantity("abc")
    with pytest.raises(ValueError, match="greater than 0"):
        validators.validate_quantity(0)
    with pytest.raises(ValueError, match="greater than 0"):
        validators.validate_quantity(-1.5)

def test_validate_price():
    # Valid
    assert validators.validate_price(None, "MARKET") is None
    assert validators.validate_price(100.5, "MARKET") is None
    assert validators.validate_price("50000", "LIMIT") == 50000.0
    
    # Invalid LIMIT
    with pytest.raises(ValueError, match="required"):
         validators.validate_price(None, "LIMIT")
    with pytest.raises(ValueError, match="positive numeric value"):
         validators.validate_price("abc", "LIMIT")
    with pytest.raises(ValueError, match="greater than 0"):
         validators.validate_price(0, "LIMIT")

def test_validate_stop_price():
    # Valid
    assert validators.validate_stop_price(None, "MARKET") is None
    assert validators.validate_stop_price("49000", "STOP_LIMIT") == 49000.0
    
    # Invalid STOP_LIMIT
    with pytest.raises(ValueError, match="required"):
         validators.validate_stop_price(None, "STOP_LIMIT")
    with pytest.raises(ValueError, match="positive numeric value"):
         validators.validate_stop_price("xyz", "STOP_LIMIT")
    with pytest.raises(ValueError, match="greater than 0"):
         validators.validate_stop_price(-50, "STOP_LIMIT")
