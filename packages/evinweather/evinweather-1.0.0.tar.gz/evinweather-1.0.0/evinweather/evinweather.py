import requests


class Weather:
    """Creates a Weather object getting an apikey as input and either a city name
    or lat and lon coordinates.

    Package use example:

    # Create a weather object using a city name:
    # Get an api-key from https://openweathermap.org. Wait a couple of hours for activation.

    # >>> weather1 = Weather(apikey="-", cycle=1, city='Istanbul')

    # Using latitude and longitude coordinates
    # >>> weather2 = Weather(apikey="-", cycle=1, lat = 4.1, lon = -4.1)

    # Get complete weather data for the next specified hours:
    # >>> weather1.next_12h()

    # Simplified data for the next specified cycle of hours:
    # >>> weather1.next_12h_simplified()

    # 1 cycle --> refers to next 3 hours

    """

    def __init__(self, apikey, cycle=1, city=None, lat=None, lon=None):
        if city:
            url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        elif lat and lon:
            url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={apikey}&units=metric"
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError("Provide a city or lat and lon arguments")

        if self.data['cod'] != "200":
            raise ValueError(self.data['message'])

        self.cycle = cycle



    def next_12h(self):
        """ Returns specified cycle-hours of data as a dict
        """
        return self.data['list'][:self.cycle]

    def next_12h_simplified(self):
        """Returns date, temperature, and sky condition every cycle-hours as a tuple of tuples.
        """
        simple_data = []
        for dicty in self.data['list'][:self.cycle]:
            simple_data.append((dicty['dt_txt'], dicty['main']['temp'],dicty['weather'][0]['description']))
        return simple_data





