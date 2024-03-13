from weather_data import WeatherData
from current_conditions_display import CurrentConditionsDisplay
from statistics_display import StatisticsDisplay


class WeatherStation:
    weather_data = WeatherData()
    current_conditions_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    # forecast_display = ForecastDisplay(weather_data)

    # simulate the weather measurements
    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)
