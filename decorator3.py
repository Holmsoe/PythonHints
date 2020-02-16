
def log_order_event(func):
    def wrapper(*args, **kwargs):
        print("Ordering:", func.__name__)
        order = func(*args, **kwargs)
        print("Order result:", order)
        return order
    return wrapper

@log_order_event
def order_pizza(*toppings):
    ordertext="Pizza med "+" ".join(*toppings)
    return ordertext

@log_order_event
def order_hamburger(*specials):
    ordertext="Hamburger med "+" ".join(*specials)
    return ordertext

order_pizza(["asparges","tomat"])
order_hamburger(["Cheese","Bacon"])
