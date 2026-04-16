from typing import Optional, Union

def validate_symbol(symbol: str) -> str:
    if not symbol or not str(symbol).strip():
        raise ValueError("Symbol cannot be empty.")
    
    symbol_upper = str(symbol).strip().upper()
    if not symbol_upper.isalnum():
        raise ValueError(f"Invalid symbol '{symbol_upper}'. Symbol must be alphanumeric (e.g., BTCUSDT).")
        
    return symbol_upper

def validate_side(side: str) -> str:
    if not side or not str(side).strip():
        raise ValueError("Side cannot be empty.")
        
    side_upper = str(side).strip().upper()
    if side_upper not in ["BUY", "SELL"]:
        raise ValueError(f"Invalid side '{side}'. Must be 'BUY' or 'SELL'.")
        
    return side_upper

def validate_order_type(order_type: str) -> str:
    if not order_type or not str(order_type).strip():
        raise ValueError("Order type cannot be empty.")
        
    ot_upper = str(order_type).strip().upper()
    if ot_upper not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError(f"Invalid order type '{order_type}'. Must be 'MARKET', 'LIMIT', or 'STOP_LIMIT'.")
        
    return ot_upper

def validate_quantity(quantity: Union[int, float, str]) -> float:
    try:
        q_float = float(quantity)
    except (TypeError, ValueError):
        raise ValueError(f"Invalid quantity '{quantity}'. Quantity must be a positive number.")
        
    if q_float <= 0:
        raise ValueError(f"Quantity must be greater than 0, got {q_float}.")
        
    return q_float

def validate_price(price: Optional[Union[int, float, str]], order_type: str) -> Optional[float]:
    ot_upper = validate_order_type(order_type)
    
    if ot_upper in ["LIMIT", "STOP_LIMIT"]:
        if price is None or str(price).strip() == "":
            raise ValueError(f"Price is required for {ot_upper} orders.")
            
        try:
            p_float = float(price)
        except (TypeError, ValueError):
            raise ValueError(f"Invalid price '{price}'. Price must be a positive numeric value.")
            
        if p_float <= 0:
            raise ValueError(f"Price must be greater than 0, got {p_float}.")
            
        return p_float
        
    return None

def validate_stop_price(stop_price: Optional[Union[int, float, str]], order_type: str) -> Optional[float]:
    ot_upper = validate_order_type(order_type)
    
    if ot_upper == "STOP_LIMIT":
        if stop_price is None or str(stop_price).strip() == "":
            raise ValueError("Stop price is required for STOP_LIMIT orders.")
            
        try:
            sp_float = float(stop_price)
        except (TypeError, ValueError):
            raise ValueError(f"Invalid stop price '{stop_price}'. Stop price must be a positive numeric value.")
            
        if sp_float <= 0:
            raise ValueError(f"Stop price must be greater than 0, got {sp_float}.")
            
        return sp_float
        
    return None
