class Pet:
    """
    A class to represent a pet with encapsulated attributes.
    Stores pet information: name, animal type, and age.
    """
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    def set_name(self, name): 
        """Set the pet's name."""
        self.__name = name
    
    def set_animal_type(self, animal_type): 
        """Set the pet's animal type."""
        self.__animal_type = animal_type
    
    def set_age(self, age): 
        """Set the pet's age."""
        self.__age = age

    def get_name(self): 
        """Get the pet's name."""
        return self.__name
    
    def get_animal_type(self): 
        """Get the pet's animal type."""
        return self.__animal_type
    
    def get_age(self): 
        """Get the pet's age."""
        return self.__age

    def __str__(self):
        """Return a formatted string representation of the pet."""
        return f"Pet(name={self.__name}, type={self.__animal_type}, age={self.__age})"

    def display_info(self):
        """Display all pet information in a formatted way."""
        print(f"Pet Name       : {self.__name}")
        print(f"Pet Type       : {self.__animal_type}")
        print(f"Pet Age        : {self.__age} years old")

    def is_adult(self):
        """Check if the pet is an adult (age >= 2 years)."""
        return self.__age >= 2

# --- Test Program ---
    CYAN, GREEN, RESET = '\033[96m', '\033[92m', '\033[0m'
    print(f"{CYAN}=== Central Pet Registration System ==={RESET}\n")
    
    my_pet = Pet()
    
    print("Please enter the following credentials:")
    my_pet.set_name(input("  > Pet Name (e.g., Niko): "))
    my_pet.set_animal_type(input("  > Animal Type (e.g., Dog, Cat, Bird): "))
    
    try:
        my_pet.set_age(int(input("  > Age (in years): ")))
    except ValueError:
        print("\033[91m[Error] Age must be an integer. Defaulting to 0.\033[0m")
        my_pet.set_age(0)
        
    print(f"\n{GREEN}--- Registration Successful ---{RESET}")
    print(f"Registered Name: {my_pet.get_name()}")
    print(f"Species / Type : {my_pet.get_animal_type()}")
    print(f"Recorded Age   : {my_pet.get_age()} years old")
    print("=======================================\n")

if __name__ == "__main__":
    main()