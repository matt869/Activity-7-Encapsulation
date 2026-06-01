class Fan:
    """A class to represent a cooling fan with speed and color properties."""
    # Constants for fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        """Initialize a fan with speed, radius, color, and power state."""
        # Private data fields (Encapsulation via name mangling)
        self.__speed = speed
        self.__on = on
        self.__radius = float(radius)
        self.__color = color

    # Accessors (Getters)
    def get_speed(self): 
        """Get the current speed of the fan."""
        return self.__speed
    
    def get_on(self): 
        """Get the power state of the fan."""
        return self.__on
    
    def get_radius(self): 
        """Get the radius of the fan."""
        return self.__radius
    
    def get_color(self): 
        """Get the color of the fan."""
        return self.__color

    # Mutators (Setters)
    def set_speed(self, speed): 
        """Set the speed of the fan."""
        self.__speed = speed
    
    def set_on(self, on): 
        """Set the power state of the fan."""
        self.__on = on
    
    def set_radius(self, radius): 
        """Set the radius of the fan."""
        self.__radius = float(radius)
    
    def set_color(self, color): 
        """Set the color of the fan."""
        self.__color = color

    def is_on(self):
        """Check if the fan is currently on."""
        return self.__on

    def turn_on(self):
        """Turn the fan on."""
        self.__on = True

    def turn_off(self):
        """Turn the fan off."""
        self.__on = False

    def get_speed_label(self):
        """Get the speed label (SLOW, MEDIUM, or FAST)."""
        if self.__speed == self.SLOW:
            return "SLOW"
        elif self.__speed == self.MEDIUM:
            return "MEDIUM"
        elif self.__speed == self.FAST:
            return "FAST"
        else:
            return "UNKNOWN"

    def get_fan_info(self):
        """Get a formatted string with all fan information."""
        status = "ON" if self.__on else "OFF"
        return f"Fan(color={self.__color}, speed={self.get_speed_label()}, radius={self.__radius}, power={status})"

    def __str__(self):
        """Return string representation of the fan."""
        return self.get_fan_info()

    def validate_speed(self, speed):
        """Validate if speed is one of the allowed constants."""
        return speed in [self.SLOW, self.MEDIUM, self.FAST]

    def get_air_flow(self):
        """Calculate estimated air flow based on speed and radius."""
        return self.__speed * self.__radius if self.__on else 0

    def increase_speed(self):
        """Increase fan speed by one level."""
        if self.__speed < self.FAST:
            self.__speed += 1

    def decrease_speed(self):
        """Decrease fan speed by one level."""
        if self.__speed > self.SLOW:
            self.__speed -= 1

# --- Test Program ---
def main():
    """Main program to test Fan class functionality."""
    CYAN, GREEN, YELLOW, RESET = '\033[96m', '\033[92m', '\033[93m', '\033[0m'
    print(f"{CYAN}--- Cooling System Diagnostics ---{RESET}")

    # Create first fan object with custom settings
    fan1 = Fan()
    fan1.set_speed(Fan.FAST)
    fan1.set_radius(10)
    fan1.set_color("yellow")
    fan1.set_on(True)

    # Create second fan object with different settings
    fan2 = Fan()
    fan2.set_speed(Fan.MEDIUM)
    fan2.set_radius(5)
    fan2.set_color("blue")
    fan2.set_on(False)

    # Display fan 1 status information
    print(f"\n{YELLOW}[FAN 1 STATUS]{RESET}")
    print(f"Speed:  {fan1.get_speed()} (FAST)\nRadius: {fan1.get_radius()}\nColor:  {fan1.get_color()}\nPower:  {'ON' if fan1.get_on() else 'OFF'}")

    # Display fan 2 status information
    print(f"\n{GREEN}[FAN 2 STATUS]{RESET}")
    print(f"Speed:  {fan2.get_speed()} (MEDIUM)\nRadius: {fan2.get_radius()}\nColor:  {fan2.get_color()}\nPower:  {'ON' if fan2.get_on() else 'OFF'}\n")

if __name__ == "__main__":
    main()