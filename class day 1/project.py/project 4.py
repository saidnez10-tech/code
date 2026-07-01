def what_to_wear(temperature_celsius):
    # Temperature threshold logic for light, soft clothing
    if temperature_celsius > 30:
        print("It's very warm! Wear lightweight, breathable fabrics like linen or cotton.")
    elif 22 <= temperature_celsius <= 30:
        print("Perfect for soft, light clothes! Keep a light layer just in case.")
    elif 15 <= temperature_celsius < 22:
        print("A bit chilly for just light clothes. Add a cardigan or a pullover.")
    else:
        print("Too cold for light clothes. Wear a jacket to stay warm!")

# Rohan can replace this value with the current local temperature
current_temp = 28
what_to_wear(current_temp)