#python program that converts temperatue between celsius and fahenheit
def convert_temperature(value,unit):
    if unit=="C":
        return (value*9/5)+32,"F"
    elif unit=="F":
        return (value-32)*5/9,"C"
    else:
        return None
value=float(input("enter the temperature :")) 
unit=input("enter unit (C/F) :").upper()
converted_value,converted_unit=convert_temperature(value,unit)
if converted_value is not None:
    print(f"{value}°{unit} is {converted_value:2f} ° {converted_unit}") 
else:
    print("invalid unit")                  