import discord

color = 0x000099
key_features = {
    'temp' : "Temperature",
    'feels_like': "Feels Like",
    'temp_min': 'Minimum Temperature',
    'temp_max': "Maximum Temperature",
    'deg': "Wind Direction",
    'speed': "Wind Speed",
    'gust': "Wind Gust",
    "sea_level": "Sea Level",
    "grnd_level": "Ground Level"
}

def parse_data(data):
    data2 = data['main']
    data2.update(data['wind'])
    del data2['humidity']
    del data2['pressure']
    print(data2)
    return data2

def weather_message(data,location):
    location = location.title()
    print(location)
    message = discord.Embed(
        title = f"{location} Weather",
        discription = f"Here is the weather data for {location}.",
        color = color
    )
    for key in data:
        message.add_field(
            name=key_features[key],
            value=str(data[key]),
            inline =  False
        )
    return message

def error_message(location):
    location = location.title()
    return discord.Embed(
        title = 'Error',
        description = f"There was an error retrieving weather data for {location}",
        color = color
    )
