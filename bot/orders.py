from bot.validators import validate_inputs

def create_order(client, symbol, side, order_type, quantity, price=None):
    validate_inputs(symbol, side, order_type, quantity, price)

    order = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        order["price"] = price
        order["timeInForce"] = "GTC"

    return client.place_order(**order)