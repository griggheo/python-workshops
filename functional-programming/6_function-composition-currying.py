# currying means transforming a function with multiple parameters into a chain of functions with one parameter.


"""
https://www.python-course.eu/currying_in_python.php
"""

currencies =  {'CHF': 1.0821202355817312, 
               'CAD': 1.488609845538393, 
               'GBP': 0.8916546282920325, 
               'JPY': 114.38826536281809, 
               'EUR': 1.0, 
               'USD': 1.11123458162018}


def exchange(from_currency, to_currency, amount):
    result = amount * currencies[to_currency] 
    result /= currencies[from_currency]
    return result

print(exchange("CHF", "CAD", 100))

# define curried functions from the function exchange:

def exchange_from_CHF(to_currency, amount):
    return exchange("CHF", to_currency, amount)

def CHF2EUR(amount):
    return exchange_from_CHF("EUR", amount)

print(exchange_from_CHF("EUR", 90))
    
print(CHF2EUR(90))

# rewrite the function exchange in a curryable version:

def curry_exchange(from_currency=None, 
                   to_currency=None, 
                   amount=None):
    if from_currency:
        if to_currency:
            if amount:
                def f():
                    return exchange(from_currency, to_currency, amount)
            else:
                def f(amount):
                    return exchange(from_currency, to_currency, amount)
        else:
            if amount:
                def f(to_currency):
                    return exchange(from_currency, to_currency, amount)
            else:
                def f(to_currency=None, amount=None):
                    if amount:
                        if to_currency:
                            def h():
                                return exchange(from_currency, to_currency, amount)
                        else:
                            def h(to_currency):
                                if to_currency:
                                    return exchange(from_currency, to_currency, amount)
                    else:
                        if to_currency:
                            def h(amount):
                                return exchange(from_currency, to_currency, amount)
                        else:
                            def h(to_currency, amount):
                                return exchange(from_currency, to_currency, amount) 
                    return h
    else:
        def f(from_currency, to_currency, amount):
                return exchange(from_currency, to_currency, amount)
    return f

# redefine exchange_from_CHF and CHF2EUR in a properly curried way:

exchange_from_CHF = curry_exchange("CHF")

print(exchange_from_CHF("EUR", 90))

CHF2EUR = curry_exchange("CHF", "EUR")

print(CHF2EUR(90))

# various calls to curry_exchange

print(curry_exchange("CHF")( "EUR", 100))
print(curry_exchange("CHF", "EUR")(100))
f = curry_exchange("CHF")
print(f("EUR", 100))
g = f("EUR")
print(g(100))

CHF2EUR= curry_exchange("CHF", "EUR")
print(CHF2EUR(100))

k = curry_exchange("CHF", "EUR", 100)
print(k())

print(curry_exchange("CHF", "EUR", 100))
f = curry_exchange("CHF")(amount=100)
print(f("EUR"))

f = curry_exchange("CHF")
print(f("EUR", 100))

f = curry_exchange("CHF")
g = f("EUR")
print(g(100))

g2 = f(amount=120)

for currency in currencies:
    print(currency, g2(currency))

