import requests
from meya import Component
 
 
API_URL = (
"http://api.openweathermap.org/data/2.5/weather"
    "?q={city},{country}&APPID={api_key}"
)
API_KEY = '0d3efb33fc57a68d3d90224751ee224d'
 
 
def farenheit(celsius):
    return 9.0/5.0 * celsius + 32
 
 
class Weather(Component):
    def start(self):
        city = "Houston"
        country = "US"
        url = API_URL.format(city=city, country=country, api_key=API_KEY)
        data = requests.get(url).json()
        temp = int(data['main']['temp'] - 273.15)
        description = data['weather'][0]['description']
 
        if country == "US":
            units = "F"
            temp = farenheit(temp)
        else:
            units = "C"
        additional_text = "Look. My nest at Rice is always warm. You should live with me! If you are not a Rice resident, you should be! All Rice residents are as hospitable as the weather here, I promise. I am an honest owl. Hoo-hoo."
        text = (
            "It is currently {temp}{units} with {description} in {city}! Hoo-hoo..." + additional_text
        ).format(
            temp=temp,
            units=units,
            description=description,
            city=city,
            country=country
        )
        message = self.create_message(text=text)
        return self.respond(message=message, action="next")
 