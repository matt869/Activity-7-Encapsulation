import time

class Car:
    """A class to represent a vehicle with speed control functionality."""
    def __init__(self, year_model, make):
        """Initialize car with year model and make."""
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        """Increase car speed by 5 mph."""
        self.__speed += 5

    def brake(self):
        """Decrease car speed by 5 mph."""
        self.__speed -= 5

    def get_speed(self):
        """Return the current speed of the car."""
        return self.__speed

    def get_make(self):
        """Return the make of the car."""
        return self.__make

    def get_year_model(self):
        """Return the year model of the car."""
        return self.__year_model

    def is_moving(self):
        """Check if the car is currently moving."""
        return self.__speed > 0

    def stop(self):
        """Stop the car completely."""
        self.__speed = 0

    def get_max_speed(self):
        """Get the maximum speed of the car (200 mph limit)."""
        return 200

    def is_speeding(self):
        """Check if the car is exceeding speed limit (80 mph)."""
        return self.__speed > 80

# --- Test Program ---
def display_dashboard(action, speed):
    """Creates a visual speedometer bar."""
    bar = "█" * (speed // 2)
    color = '\033[92m' if action == "Accelerating" else '\033[91m'
    RESET = '\033[0m'
    print(f"[{color}{action:^12}{RESET}] Speed: {speed:3} mph |{color}{bar}{RESET}")
    time.sleep(0.4)

def main():
    print("\033[96m--- Vehicle Telemetry Initiated ---\033[0m\n")
    my_car = Car(2025, "Porsche 911 GT3 RS")
    
    for _ in range(5):
        my_car.accelerate()
        display_dashboard("Accelerating", my_car.get_speed())
        
    print("-" * 40)
    
    for _ in range(5):
        my_car.brake()
        display_dashboard("Braking", my_car.get_speed())

if __name__ == "__main__":
    main()