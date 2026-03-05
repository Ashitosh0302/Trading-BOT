# Binance Futures Testnet Trading Bot (Python)

## Overview
This project is a **Python-based trading bot** built for **Binance Futures Testnet (USDT-M)**.  
The application runs on **localhost as a web application** using Flask and allows users to place **Market and Limit orders** with proper validation, logging, and error handling.

This project was developed as part of a **Python Developer assignment**.

---

## Features
- Place **Market** and **Limit** orders
- Supports **BUY** and **SELL**
- Runs on **Binance Futures Testnet**
- Web-based UI on **localhost**
- Input validation
- Structured and reusable code
- API request and response logging
- Exception handling

---

## Tech Stack
- Python 3.x
- Flask
- python-binance

---

## Project Structure
```bash
Trading-BOT/
│
├── bot/
│   ├── __init__.py                 # Package initializer
│   ├── client.py                    # Binance client setup
│   ├── orders.py                     # Order placement logic
│   ├── validators.py                  # Input validation
│   └── logging_config.py               # Logging configuration
│
├── web/
│   └── app.py                         # Flask web application
│
├── logs/                               # Log files directory
│   ├── market_order.log
│   └── limit_order.log
│
├── .env                                # Environment variables (API keys)
├── requirements.txt                    # Project dependencies
└── README.md                           # Project documentation
```

## Example Usage

### Market Order
- Symbol: BTCUSDT
- Side: BUY
- Order Type: MARKET
- Quantity: 0.001

### Limit Order
- Symbol: BTCUSDT
- Side: SELL
- Order Type: LIMIT
- Quantity: 0.001
- Price: 30000

---

## Logging
Logs are generated automatically in the `logs/` directory:
- market_order.log
- limit_order.log

Each log includes:
- Order request
- API response
- Error details (if any)

---

## Error Handling
The application handles:
- Invalid user input
- Missing parameters
- Binance API errors
- Runtime exceptions

Errors are displayed on the UI and logged to files.

---

## Assumptions
- Only USDT-M Futures are used
- Orders are placed on Binance Futures Testnet
- User has sufficient testnet balance

---

## Deployment Readiness
- Environment variables used for API credentials
- Flask application is WSGI compatible
- Ready for deployment using Gunicorn and Nginx
- Docker deployment possible

---

## Conclusion
The project fully satisfies all requirements of the provided assignment document and has been tested successfully on localhost.

---

## Author
Ashitosh Shirsath
