# Binance Futures Testnet Trading Bot

A robust, Python-based CLI application for automatically trading on the Binance Futures Testnet natively configured via environment variables.

## Features
- **Orders**: Directly interfaces with Market Options, Limit Options, and complex Stop Limit deployments securely.
- **CLI Framework**: Utilizes interactive prompting and strict UI logging validations built on top of `click`.
- **Structured Output Logging**: Implements centralized isolated logging schemas with native timestamp, origin map mapping cleanly to terminal streams and active `.log` debugging traces simultaneously. 

## Environment Setup
Create a `.env` file in the root codebase directly tracking the endpoints:
```env
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_api_secret
BASE_URL=https://testnet.binancefuture.com
LOG_LEVEL=INFO
```

## Running the CLI

Execute the terminal UI interface directly, prompting for parameters interactively:
```bash
python cli.py
```

Skip interactivity bypassing confirmation locks by supplying parameters via flags:
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.05 -y
```

### Sample CLI Output

**Success Case:**
```text
===== ORDER SUMMARY =====
Symbol:         BTCUSDT
Side:           BUY
Type:           MARKET
Quantity:       0.05
=========================

Executing MARKET BUY order...

===== RESPONSE =====
SUCCESS: Order placed successfully!
Order ID:       123456789
Status:         NEW
Executed Qty:   0.00
====================
```

**Error Case:**
```text
FAILURE: Invalid Input - Invalid quantity '-0.5'. Quantity must be a positive number.
```

## Error Handling Strategy
The application employs a defense-in-depth error handling architecture designed to fail gracefully:
1. **Pre-flight Validation**: All CLI inputs pass through strict, modular evaluators (`validators.py`) preventing malformed requests from ever reaching the exchange.
2. **Graceful Degradation**: The core service intercepts underlying HTTP bounds mapping `BinanceAPIException` into clean, human-readable CLI alerts. 
3. **Isolated Tracebacks**: Standard Python traceback stack traces are suppressed from cluttering the command line UI, while remaining faithfully preserved and mapped into the underlying local `trading_bot.log` files for secure backend debugging.

## Future Improvements
- **Stop-Limit Enhancements**: Extending the current configuration bounds to support algorithmic trailing stops and dynamic triggers.
- **Web UI Dashboard**: Transitioning the headless CLI configuration into a dynamic, web-based React monitoring console.
- **Automated Retries**: Establishing asynchronous handler loops to gracefully process momentary Binance API disconnects or ping spikes.
- **Rate Limit Management**: Implementing weighted queue buckets strictly mapping Binance's operational limits, actively mitigating HTTP `429` blockages before they happen.

## Running Tests

Comprehensive unit tests validate internal bounds handling, restricting erroneous orders blocking silent deployment failures.

The testing pipeline natively runs safely against isolated constraints using `pytest`. 

**1. Install PyTest locally inside your framework:**
```bash
pip install pytest
```

**2. Execute the Pytest suite natively over the whole folder array:**
```bash
pytest
```
