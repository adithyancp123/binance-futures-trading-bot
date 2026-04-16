from typing import Dict, Any, Optional
from binance.exceptions import BinanceAPIException, BinanceRequestException
from bot.client import BinanceClient
from bot.logging_config import setup_logger

logger = setup_logger()
class OrderService:
    def __init__(self, binance_client: Optional[BinanceClient] = None) -> None:
        if binance_client is None:
            self.binance_client = BinanceClient()
        else:
            self.binance_client = binance_client
            
        self.client = self.binance_client.get_client()

    def _format_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice"),
            "raw": response
        }

    def place_market_order(self, symbol: str, side: str, quantity: float) -> Dict[str, Any]:
        try:
            symbol = symbol.upper()
            side = side.upper()
            quantity = float(quantity)

            if side not in ["BUY", "SELL"]:
                raise ValueError(f"Invalid side '{side}', must be 'BUY' or 'SELL'.")

            logger.info(f"Submitting MARKET request: Symbol={symbol}, Side={side}, Quantity={quantity}")

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logger.info(f"Order Successful | ID: {response.get('orderId')} | Status: {response.get('status')} | ExecQty: {response.get('executedQty')} | AvgPrice: {response.get('avgPrice')}")
            
            return self._format_response(response)

        except ValueError as e:
            logger.error(f"Validation error placing market order: {e}")
            raise
        except BinanceAPIException as e:
            logger.error(f"Binance API Error placing market order for {symbol}: {e.status_code} - {e.message}")
            raise
        except BinanceRequestException as e:
            logger.error(f"Binance Request Error placing market order for {symbol}: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error placing market order: {e}")
            raise

    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float) -> Dict[str, Any]:
        try:
            symbol = symbol.upper()
            side = side.upper()
            quantity = float(quantity)
            price = float(price)

            if side not in ["BUY", "SELL"]:
                raise ValueError(f"Invalid side '{side}', must be 'BUY' or 'SELL'.")

            logger.info(f"Submitting LIMIT request: Symbol={symbol}, Side={side}, Quantity={quantity}, Price={price}")

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=price
            )

            logger.info(f"Order Successful | ID: {response.get('orderId')} | Status: {response.get('status')} | ExecQty: {response.get('executedQty')} | AvgPrice: {response.get('avgPrice')}")

            return self._format_response(response)

        except ValueError as e:
            logger.error(f"Validation error placing limit order: {e}")
            raise
        except BinanceAPIException as e:
            logger.error(f"Binance API Error placing limit order for {symbol}: {e.status_code} - {e.message}")
            raise
        except BinanceRequestException as e:
            logger.error(f"Binance Request Error placing limit order for {symbol}: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error placing limit order: {e}")
            raise

    def place_stop_limit_order(self, symbol: str, side: str, quantity: float, price: float, stop_price: float) -> Dict[str, Any]:
        try:
            symbol = symbol.upper()
            side = side.upper()
            quantity = float(quantity)
            price = float(price)
            stop_price = float(stop_price)

            if side not in ["BUY", "SELL"]:
                raise ValueError(f"Invalid side '{side}', must be 'BUY' or 'SELL'.")

            logger.info(f"Submitting STOP_LIMIT request: Symbol={symbol}, Side={side}, Quantity={quantity}, Price={price}, StopPrice={stop_price}")

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                timeInForce="GTC",
                quantity=quantity,
                price=price,
                stopPrice=stop_price
            )

            logger.info(f"Order Successful | ID: {response.get('orderId')} | Status: {response.get('status')} | ExecQty: {response.get('executedQty')} | AvgPrice: {response.get('avgPrice')}")

            return self._format_response(response)

        except ValueError as e:
            logger.error(f"Validation error placing stop limit order: {e}")
            raise
        except BinanceAPIException as e:
            logger.error(f"Binance API Error placing stop limit order for {symbol}: {e.status_code} - {e.message}")
            raise
        except BinanceRequestException as e:
            logger.error(f"Binance Request Error placing stop limit order for {symbol}: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error placing stop limit order: {e}")
            raise
