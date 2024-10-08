def convert_area(value, from_unit, to_unit):
    conversions = {
        'square_meters': 1,
        'square_kilometers': 1e6,
        'hectares': 1e4,
        'acres': 4046.86,
        'square_feet': 0.092903,
        'square_yards': 0.836127,
        'square_miles': 2.59e6
    }
    return value * (conversions[from_unit] / conversions[to_unit])

def convert_length(value, from_unit, to_unit):
    conversions = {
        'meters': 1,
        'kilometers': 1e3,
        'miles': 1609.34,
        'feet': 0.3048,
        'inches': 0.0254,
        'yards': 0.9144,
        'centimeters': 0.01,
        'millimeters': 0.001
    }
    return value * (conversions[from_unit] / conversions[to_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32

def convert_volume(value, from_unit, to_unit):
    conversions = {
        'liters': 1,
        'milliliters': 1e-3,
        'cubic_meters': 1e3,
        'gallons': 3.78541,
        'quarts': 0.946353,
        'pints': 0.473176,
        'cups': 0.236588
    }
    return value * (conversions[from_unit] / conversions[to_unit])

def convert_mass(value, from_unit, to_unit):
    conversions = {
        'kilograms': 1,
        'grams': 1e-3,
        'pounds': 0.453592,
        'ounces': 0.0283495,
        'stones': 6.35029,
        'metric_tons': 1e3
    }
    return value * (conversions[from_unit] / conversions[to_unit])

def convert_data(value, from_unit, to_unit):
    conversions = {
        'bytes': 1,
        'kilobytes': 1e3,
        'megabytes': 1e6,
        'gigabytes': 1e9,
        'terabytes': 1e12,
        'petabytes': 1e15
    }
    return value * (conversions[from_unit] / conversions[to_unit])

def convert_speed(value, from_unit, to_unit):
    conversions = {
        'mps': 1,
        'kph': 0.277778,
        'mph': 0.44704,
        'knots': 0.514444
    }
    return value * (conversions[from_unit] / conversions[to_unit])

def convert_time(value, from_unit, to_unit):
    conversions = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400,
        'weeks': 604800,
        'months': 2.62974e6,
        'years': 3.154e7
    }
    return value * (conversions[from_unit] / conversions[to_unit])
