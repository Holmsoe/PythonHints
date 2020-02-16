
def validate_age(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        if data > 100:
            print("fejl i data for funktion:",func.__name__)
            raise ValueError("Age too big")
        return data
    return wrapper

@validate_age
def fetch_customer_data():
    return 88
  

@validate_age
def query_orders(*criteria):
    return 82


@validate_age
def create_invoice(params):
    return 91

fetch_customer_data()
query_orders(1,2,3)
create_invoice({1:"hej",2:"ugh"})
