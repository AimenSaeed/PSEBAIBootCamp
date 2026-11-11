"""
Name : Aimen Saeed
Trainee ID : TRN-2026-000352
Date : 10-11-26
"""

# Warm-up: Predict, then run
a = [1, 2, 3]
b = a
b.append(4)
print(a) # prediction: a = [1,2,3,4]
c = a.copy()
c.append(5)
print(a, c) # prediction: a = [1,2,3,4], c = [1,2,3,4,5]
print(a is b, a is c, a == a[:])

# Build: Fix the cart bug
def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(add_item("apple"))
print(add_item("banana"))
print(add_item("orange")) 

# Challenge: Safe class copy
import copy
classes= {"A": ["Ali", "Aimen", "Iqra"], "B": ["Ahmed", "Ayesha", "Zainab"]}
shallow_copy=classes.copy()
deep_copy=copy.deepcopy(classes)
shallow_copy["A"].append("Hassan")
deep_copy["B"].append("Hina")
print(classes)