"""
def [function_name]([parameter]):
    statement
    return [result]

[variable_name] = [function_name]([argument])
"""

def usd_to_thb(amount):
    amount = amount * 34
    return amount

thb = usd_to_thb(10)
print(thb)