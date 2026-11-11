"""
Name : Aimen Saeed
Trainee ID : TRN-2026-000352
Date : 10-11-26
"""

# Warm-up: Student ID Card
name= input("Enter your name: ")
age=int(input("Enter your age: "))
grade=input("Enter your class:")
city=input("Enter your city: ")
print(
f"""
=========== STUDENT CARD ===========
Name: {name}
Age: {age}
Class: {grade}
City: {city}
====================================
"""
)
print(f"Data type of Name is: {type(name)}")
print(f"Data type of Age is: {type(age)}")
print(f"Data type of Class is: {type(grade)}")
print(f"Data type of City is: {type(city)}")

#Build: Shop Bill
item_name=input("Enter the item name: ")
item_price=float(input("Enter the item price: "))
item_quantity=int(input("Enter the item quantity: "))
discount=(item_price*item_quantity)*0.05
tax=(item_price*item_quantity)*0.17
subtotal=item_price*item_quantity
print(
    f"""=========== SHOP BILL ===========
    Item Name: {item_name}
    Item Price: {item_price}
    Item Quantity: {item_quantity}
    Subtotal: {subtotal}
    5% Discount: {discount:.2f}
    17% Tax: {tax:.2f}
    Total:{subtotal-discount+tax:.2f}
    ===================================
    """
)

#Challenge: Unit Converter
temperature=float(input("Enter the temperature in Celsius: "))
distance=float(input("Enter the distance in kilometers: "))
fahrenheit=(temperature*9/5)+32
miles=distance*0.621371
print(
    f"""
=========== UNIT CONVERTER ===========
Temperature in Celsius: {temperature}°C
Temperature in Fahrenheit: {fahrenheit:.1f}°F
Distance in Kilometers: {distance} km
Distance in Miles: {miles:.1f} miles
=======================================
"""
)