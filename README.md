# 🚀 Binance Futures Testnet Trading Bot

A robust, production-style **Python CLI trading bot** for placing orders on the **Binance Futures Testnet (USDT-M)**.
Designed with clean architecture, input validation, structured logging, and error handling.

---

## 📌 Overview

This project demonstrates how to build a modular trading bot that interacts with Binance Futures APIs.
It supports **MARKET** and **LIMIT** orders, includes a clean CLI interface, and logs all operations for traceability.

---

## ✨ Features

* 📈 Place **MARKET** and **LIMIT** orders
* 🔄 Supports both **BUY** and **SELL** sides
* 🖥️ Interactive and flag-based **CLI interface (Click)**
* ✅ Strong **input validation layer**
* 🧾 Structured **logging (file + console)**
* ⚠️ Robust **error handling (API + user errors)**
* 🧱 Clean modular architecture (client, orders, validators, CLI)

---

## 🛠️ Tech Stack

* **Python 3.x**
* **python-binance**
* **Click (CLI framework)**
* **python-dotenv**
* **Logging (built-in)**

---

## 📂 Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py          # Binance client wrapper
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│
├── tests/                 # Unit tests (validators)
├── cli.py                 # CLI entry point
├── requirements.txt       # Dependencies
├── README.md
├── trading_bot.log        # Generated logs
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/adithyancp123/binance-futures-trading-bot.git
cd binance-futures-trading-bot
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
BASE_URL=https://testnet.binancefuture.com
```

> ⚠️ Note: Testnet keys are recommended. Do NOT use real funds.

---

## ▶️ Usage

### 🔹 MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### 🔹 LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

---

### 🔹 Interactive Confirmation

Before placing an order:

```
WARNING: You are about to place an order.
Do you want to proceed? [y/N]:
```

---

## 📊 Sample Output

```
===== ORDER SUMMARY =====
Symbol:         BTCUSDT
Side:           BUY
Type:           MARKET
Quantity:       0.001
=========================

Executing MARKET BUY order...

❌ Order failed: API-key format invalid
```

---

## 🧾 Logging

Logs are stored in:

```
trading_bot.log
```

Includes:

* API requests
* API responses
* Error traces

Example:

```
INFO  | orders | Submitting MARKET request
ERROR | orders | Binance API Error: API-key format invalid
```

---

## 🧠 Error Handling

The application gracefully handles:

* Invalid user inputs
* Missing parameters
* Binance API errors
* Network issues

All errors are:

* Logged in detail (log file)
* Displayed cleanly to the user (CLI)

---

## ⚠️ Assumptions

* Uses **Binance Futures Testnet (no real funds)**
* API keys may be restricted (no KYC), resulting in authentication errors
* Focus is on **correct API integration, structure, and logging**

---

## 🔮 Future Improvements

* Stop-Limit / OCO order support
* Retry mechanism for API failures
* Rate limiting handling
* Web-based UI dashboard
* Strategy-based trading (signals, indicators)

---

## ✅ Status

✔ Core requirements implemented
✔ Logging and validation included
✔ CLI interface working
✔ Clean modular architecture

---

## 👨‍💻 Author

**Adithyan C P**
GitHub: https://github.com/adithyancp123

---
