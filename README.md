# Activity 7 - Encapsulation

This project demonstrates the concept of **encapsulation** in Object-Oriented Programming (OOP) through three Python classes: `Pet`, `Fan`, and `Car`.

## Project Overview

Encapsulation is one of the four fundamental OOP concepts that bundles data (attributes) and methods (functions) into a single unit and restricts direct access to some of the object's components. This project uses **name mangling** (private attributes with `__` prefix) to implement encapsulation.

---

## Files and Classes

### 1. Pet Class (`Pet/pet.py`)

The `Pet` class represents a pet with encapsulated attributes for name, animal type, and age.

#### Attributes:
- `__name` - The name of the pet (private)
- `__animal_type` - The type of animal (private)
- `__age` - The age of the pet in years (private)

#### Methods:

**Setters:**
- `set_name(name)` - Set the pet's name
- `set_animal_type(animal_type)` - Set the pet's animal type
- `set_age(age)` - Set the pet's age

**Getters:**
- `get_name()` - Return the pet's name
- `get_animal_type()` - Return the pet's animal type
- `get_age()` - Return the pet's age

**Utility Methods:**
- `display_info()` - Display all pet information in a formatted way
- `is_adult()` - Check if the pet is an adult (age >= 2 years)
- `increment_age()` - Increment the pet's age by one year
- `validate_age(age)` - Validate if the provided age is reasonable (0-100)
- `__str__()` - Return a formatted string representation

#### Usage Example:
```python
my_pet = Pet()
my_pet.set_name("Niko")
my_pet.set_animal_type("Dog")
my_pet.set_age(3)
print(my_pet.get_name())  # Output: Niko
print(my_pet.is_adult())  # Output: True
```

---

### 2. Fan Class (`Car/car.py`)

The `Fan` class represents a cooling fan with encapsulated attributes for speed, radius, color, and power state.

#### Constants:
- `SLOW = 1`
- `MEDIUM = 2`
- `FAST = 3`

#### Attributes:
- `__speed` - The speed level of the fan (private)
- `__on` - The power state of the fan (private)
- `__radius` - The radius of the fan in inches (private)
- `__color` - The color of the fan (private)

#### Methods:

**Setters:**
- `set_speed(speed)` - Set the speed of the fan
- `set_on(on)` - Set the power state of the fan
- `set_radius(radius)` - Set the radius of the fan
- `set_color(color)` - Set the color of the fan

**Getters:**
- `get_speed()` - Get the current speed of the fan
- `get_on()` - Get the power state of the fan
- `get_radius()` - Get the radius of the fan
- `get_color()` - Get the color of the fan

**Utility Methods:**
- `is_on()` - Check if the fan is currently on
- `turn_on()` - Turn the fan on
- `turn_off()` - Turn the fan off
- `get_speed_label()` - Get the speed label (SLOW, MEDIUM, or FAST)
- `get_fan_info()` - Get a formatted string with all fan information
- `validate_speed(speed)` - Validate if speed is one of the allowed constants
- `get_air_flow()` - Calculate estimated air flow based on speed and radius
- `increase_speed()` - Increase fan speed by one level
- `decrease_speed()` - Decrease fan speed by one level
- `__str__()` - Return string representation of the fan

#### Usage Example:
```python
fan1 = Fan()
fan1.set_speed(Fan.FAST)
fan1.set_radius(10)
fan1.set_color("yellow")
fan1.turn_on()
print(fan1.get_fan_info())  # Output: Fan(color=yellow, speed=FAST, radius=10.0, power=ON)
```

---

### 3. Car Class (`Fan/fan.py`)

The `Car` class represents a vehicle with encapsulated attributes for year model, make, and speed control.

#### Attributes:
- `__year_model` - The year model of the car (private)
- `__make` - The make of the car (private)
- `__speed` - The current speed of the car in mph (private)

#### Methods:

**Getters:**
- `get_speed()` - Return the current speed of the car
- `get_make()` - Return the make of the car
- `get_year_model()` - Return the year model of the car

**Control Methods:**
- `accelerate()` - Increase car speed by 5 mph
- `brake()` - Decrease car speed by 5 mph
- `stop()` - Stop the car completely

**Utility Methods:**
- `is_moving()` - Check if the car is currently moving
- `get_max_speed()` - Get the maximum speed of the car (200 mph limit)
- `is_speeding()` - Check if the car is exceeding speed limit (80 mph)
- `get_car_info()` - Return a formatted string with car information
- `__str__()` - Return string representation of the car

#### Usage Example:
```python
my_car = Car(2025, "Porsche 911 GT3 RS")
my_car.accelerate()
my_car.accelerate()
print(my_car.get_speed())  # Output: 10
print(my_car.get_car_info())  # Output: 2025 Porsche 911 GT3 RS - Speed: 10 mph
```

---

## Key Concepts Demonstrated

### Encapsulation
- **Private Attributes**: All data fields are declared as private using the double underscore (`__`) prefix
- **Public Methods**: Data is accessed and modified through public getter and setter methods
- **Data Protection**: Direct access to private attributes is prevented, ensuring data integrity

### Name Mangling
- Python uses name mangling to make attributes "private" by prefixing them with `__`
- This prevents accidental modification from outside the class
- Example: `__speed` becomes `_ClassName__speed` internally

### Getters and Setters
- **Getters** allow controlled read access to private attributes
- **Setters** allow controlled write access to private attributes
- This pattern provides a layer of abstraction

---

## Running the Programs

Each file contains a `main()` function with test code. To run a specific test:

```bash
python Pet/pet.py
python Car/car.py
python Fan/fan.py
```

---

## Educational Purpose

This project is part of Activity 7 and serves as an educational example of implementing encapsulation principles in Python. Students can use these classes as templates for understanding:

1. How to properly encapsulate data in classes
2. How to implement getter and setter methods
3. How to validate data before storing it
4. How to provide utility methods that work with private data

---

## Author
Activity 7 - Encapsulation Exercise

## Date
June 1, 2026
