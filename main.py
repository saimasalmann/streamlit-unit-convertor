import streamlit as st

# Conversion functions
def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "Meters": 1, "Kilometers": 0.001,"Centimeters":100,"Millimeters":1000, "Miles": 0.000621371, "Feet": 3.28084, "Inches": 39.3701
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "Kilograms": 1, "Grams": 1000,"Milligrams":1000000,"Micrograms":1000000000, "Pounds": 2.20462, "Ounces": 35.274
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32

def convert_time(value, from_unit, to_unit):
    conversion_factors = {
        "Seconds": 1, "Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400 ,"Months":1/2629056 ,"Years":1/31557600
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def convert_speed(value, from_unit, to_unit):
    conversion_factors = {
        "m/s": 1, "km/h": 3.6, "mph": 2.23694, "knots": 1.94384
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

# Streamlit UI
st.title("🔢 Unit Converter")

category = st.selectbox("Choose a category:", ["Length", "Weight", "Temperature", "Time", "Speed"])

unit_options = {
    "Length": ["Meters", "Kilometers","Centimeters","Millimeters", "Miles", "Feet", "Inches"],
    "Weight": ["Kilograms", "Grams","Milligrams","Micrograms", "Pounds", "Ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Time": ["Seconds", "Minutes", "Hours", "Days","Months","Years"],
    "Speed": ["m/s", "km/h", "mph", "knots"]
}

from_unit = st.selectbox("From:", unit_options[category])
to_unit = st.selectbox("To:", unit_options[category])
value = st.number_input("Enter value:", min_value=0.0, step=0.1)

if st.button("Convert"):
    if category == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif category == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif category == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    elif category == "Time":
        result = convert_time(value, from_unit, to_unit)
    elif category == "Speed":
        result = convert_speed(value, from_unit, to_unit)
    
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
