import os
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from bot.logging_config import setup_logger

logger = setup_logger()

class BinanceClient:
    def __init__(self) -> None:
        load_dotenv()
        
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")
        base_url = os.getenv("BASE_URL")
        
        if not api_key or not api_secret or not base_url:
            logger.error("Failed to load environment variables: API_KEY, API_SECRET, or BASE_URL is missing. Please check your .env file.")
            raise ValueError("Missing required environment variables in .env")
            
        logger.info("Successfully loaded API credentials and BASE_URL from .env file.")
            
        try:
            self.client = Client(api_key, api_secret, testnet=True)
            self.client.FUTURES_URL = "https://testnet.binancefuture.com"
            
            self.client.futures_ping()
            
            logger.info(f"Confirmed Futures URL -> {self.client.FUTURES_URL}")
            logger.info("Successfully connected to Binance Futures Testnet")
            
        except BinanceAPIException as e:
            logger.error(f"Binance API Error during connection: {e.status_code} - {e.message}")
            raise ConnectionError(f"Failed to connect to Binance API: {e.message}") from e
        except BinanceRequestException as e:
            logger.error(f"Binance Request Error during connection: {e}")
            raise ConnectionError("Failed to make request to Binance") from e
        except Exception as e:
            logger.error(f"Unexpected error during Binance Futures connection: {e}")
            raise

    def get_client(self) -> Client:
        return self.client
