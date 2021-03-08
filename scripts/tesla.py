class Tesla:
    """ Makes the Tesla class. Model and colour need to be provided."""
    def __init__(self, model: str, color: str, autopilot: bool = False, efficiency: float = 0.3):
        self.__autopilot = autopilot
        self.__model = model
        self.__battery_charge = 99.9
        self.__is_locked = True
        self.__seats_count = 5
        self.__color = color
        self.__efficiency = efficiency

    @property
    def color(self) -> str:
        """Color allows to check the colour of the car."""
        return self.__color

    @property
    def seats_count(self) -> int:
        """Seat count check number of seats in the car."""
        return self.__seats_count

    def welcome(self) -> str:
        return f"Hello from model {self.__model}!"

    def autopilot(self, obstacle: str) -> str:
        if self.__autopilot:
            return f"Tesla model {self.__model} avoids {obstacle}"
        return "Autopilot is not available"

    def open_doors(self) -> str:
        if self.__is_locked:
            return "Car is locked!"
        return "Doors open sideways"

    def unlock(self) -> None:
        self.__is_locked = False

    @seats_count.setter
    def seats_count(self, new_seats_count: str) -> None:
        self.__seats_count = new_seats_count

    @property
    def check_battery_level(self) -> str:
        return f"Battery charge level is {self.__battery_charge}%"

    def charge_battery(self) -> None:
        self.__battery_charge = 100

    def drive(self, travel_range: float):
        battery_discharge_percent = travel_range * self.__efficiency
        if self.__battery_charge - battery_discharge_percent >= 0:
            self.__battery_charge = self.__battery_charge - battery_discharge_percent
            return self.check_battery_level
        else:
            return "Battery charge level is 0%, please charge!"
