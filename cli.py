import sys
import json
import click
from bot.client import BinanceClient
from bot.orders import OrderService
from bot.logging_config import setup_logger
from bot import validators

logger = setup_logger()

@click.command()
@click.option('--symbol', prompt='Trading pair symbol (e.g., BTCUSDT)', help='Trading pair symbol (e.g., BTCUSDT)')
@click.option('--side', type=click.Choice(['BUY', 'SELL'], case_sensitive=False), prompt='Order side', help='Order side (BUY or SELL)')
@click.option('--type', 'order_type', type=click.Choice(['MARKET', 'LIMIT', 'STOP_LIMIT'], case_sensitive=False), prompt='Order type', help='Order type (MARKET, LIMIT, or STOP_LIMIT)')
@click.option('--quantity', type=float, prompt='Quantity', help='Quantity to trade')
@click.option('--price', type=float, required=False, help='Price for LIMIT and STOP_LIMIT orders')
@click.option('--stop-price', type=float, required=False, help='Stop price for STOP_LIMIT orders')
@click.option('--yes', '-y', is_flag=True, help='Skip confirmation prompt')
@click.option('--verbose', '-v', is_flag=True, help='Print full raw response from Binance')
def main(symbol: str, side: str, order_type: str, quantity: float, price: float, stop_price: float, yes: bool, verbose: bool):
    """Binance Futures Testnet Trading Bot CLI."""
    
    # Intelligently prompt for conditional variables based on order choice dynamically 
    if str(order_type).upper() in ['LIMIT', 'STOP_LIMIT'] and price is None:
        price = click.prompt(f'Price for {str(order_type).upper()} order', type=float)
        
    if str(order_type).upper() == 'STOP_LIMIT' and stop_price is None:
        stop_price = click.prompt('Stop Price for STOP_LIMIT order', type=float)

    try:
        # Validate inputs using our custom validators securely mapping all logic flows
        symbol = validators.validate_symbol(symbol)
        side = validators.validate_side(side)
        order_type = validators.validate_order_type(order_type)
        quantity = validators.validate_quantity(quantity)
        price = validators.validate_price(price, order_type)
        stop_price = validators.validate_stop_price(stop_price, order_type)
        
    except ValueError as e:
        click.secho(f"\nFAILURE: Invalid Input - {e}", fg='red', bold=True)
        sys.exit(1)

    # 1. Show clean summary before execution
    click.secho("\n===== ORDER SUMMARY =====", fg='cyan', bold=True)
    click.echo(f"{'Symbol:':<15} {symbol}")
    click.echo(f"{'Side:':<15} {side}")
    click.echo(f"{'Type:':<15} {order_type}")
    click.echo(f"{'Quantity:':<15} {quantity}")
    if order_type in ['LIMIT', 'STOP_LIMIT']:
        click.echo(f"{'Price:':<15} {price}")
    if order_type == 'STOP_LIMIT':
        click.echo(f"{'Stop Price:':<15} {stop_price}")
    click.secho("=========================\n", fg='cyan', bold=True)

    # 2. Ask for confirmation (y/n) unless --yes is supplied natively circumventing lock
    if not yes:
        click.secho("WARNING: You are about to place an order.", fg='yellow')
        click.confirm("Do you want to proceed?", abort=True)
        click.echo("")

    try:
        logger.info("Initializing trading platform clients...")
        client = BinanceClient()
        order_service = OrderService(binance_client=client)

        click.secho(f"Executing {order_type} {side} order...", fg='yellow')

        if order_type == 'MARKET':
            response = order_service.place_market_order(symbol, side, quantity)
        elif order_type == 'LIMIT':
            response = order_service.place_limit_order(symbol, side, quantity, price)
        elif order_type == 'STOP_LIMIT':
            response = order_service.place_stop_limit_order(symbol, side, quantity, price, stop_price)

        click.secho("\n===== RESPONSE =====", fg='cyan', bold=True)
        click.secho("SUCCESS: Order placed successfully!", fg='green', bold=True)
        click.echo(f"{'Order ID:':<15} {response.get('orderId')}")
        click.echo(f"{'Status:':<15} {response.get('status')}")
        click.echo(f"{'Executed Qty:':<15} {response.get('executedQty')}")
        
        avg_price = response.get('avgPrice')
        if avg_price and float(avg_price) > 0:
            click.echo(f"{'Avg Price:':<15} {avg_price}")

        if verbose:
            click.secho("\n--- RAW RESPONSE ---", fg='cyan')
            click.echo(json.dumps(response.get('raw', {}), indent=2))
            
        click.secho("====================\n", fg='cyan', bold=True)

    except ValueError as e:
        logger.error(f"Order formulation error: {e}")
        click.secho(f"\n❌ Order failed: {e}", fg='red', bold=True)
        sys.exit(1)
        
    except Exception as e:
        logger.exception("An unexpected error occurred during order routing.")
        click.secho(f"\n❌ Order failed: {e}", fg='red', bold=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
