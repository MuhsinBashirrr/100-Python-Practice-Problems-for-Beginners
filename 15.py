def determine_weather(temperature, humidity):
    if temperature >= 30 and humidity >= 90:
        return "Hot and Humid"
    elif temperature >= 30 and humidity < 90:
        return "Hot"
    elif temperature < 30 and humidity >= 90:
        return "Cool and Humid"
    else:
        return "Cool"

temperature = float(input("Enter the temperature in Celsius: "))
humidity = float(input("Enter the humidity in percentage: "))

weather = determine_weather(temperature, humidity)
print("Weather:", weather)
