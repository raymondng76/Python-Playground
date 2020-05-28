# Beginner OOP concepts

class Vehicle:
    '''Parent class'''

    num_of_vehicles = 0 # This is a class attribute, can be accessed directly from class or from each class instances

    def __init__(self, name, brand):
        '''Contructor for parent class'''
        self.set_name(name) # Need to add self. to indicate which instance to process
        self.set_brand(brand)
        Vehicle.increment_vehicle_count() # For class method you need to use the class name to dot access the class methods
    
    def set_name(self, name): # This is regular instance methods
        self.name = name
    def get_name(self): 
        return self.name

    def set_brand(self, brand):
        self.brand = brand
    def get_brand(self):
        return self.brand
    
    def drive(self):
        print(f'{self.name} is driving.')

    @classmethod # This is the header type for class methods, class methods are tied to the class instead of class instances
    def increment_vehicle_count(cls): # Class method use cls as first argument instead of self
        '''Increase total vehicle count by one'''
        cls.num_of_vehicles += 1
    
    @staticmethod # This is the header type for static methods, static methods can be access directly from the class definition
    def print_types_of_vehicles(): # Static method does not requires cls or self indicator
        '''Static method to store lists of possible vehicle'''
        veh_types = ['Car', 'Bus', 'Truck']
        print(veh_types)


class Car(Vehicle): # Car class definition have vehicle class as input argument to indicate vehicle class is the parent class
    '''Car class subclass of vehicle'''

    num_of_cars = 0 # Class attribute to count number of cars
    
    def __init__(self, name, brand, drivetype): # Car constructor takes in 3 argument instead of 2, but 2 of the argument is for the parent class
        super().__init__(name, brand) # super() method call invoke the parent class, .__init__ invoke the parent class contructor
        self.set_drivetype(drivetype)
        Car.increment_car_count() # For class method you need to use the class name to dot access the class methods

    def set_drivetype(self, drivetype):
        possible_type = ['4WD', 'RWD', 'FWD']
        if drivetype in possible_type:  # Benefit of setter function, able to validate input before set attributes
            self.drivetype = drivetype
        else:
            raise ValueError('Invalid Drive Type')
    
    def get_drivetype(self):
        return self.drivetype

    def print_stats(self):
        print(f'Car: Name={self.name}, Brand={self.brand}, DriveType={self.drivetype}')

    @classmethod
    def increment_car_count(cls):
        '''Increase car count by one'''
        cls.num_of_cars += 1


class Bus(Vehicle):
    '''Bus class subclass of vehicle'''

    num_of_bus = 0 # Bus attribute to count number of buses

    def __init__(self, name, brand, num_door): # Bus constructor differs from Car constructor as they have different class behaviors
        super().__init__(name, brand)
        self.set_num_door(num_door)
        Bus.increment_bus_count() # For class method you need to use the class name to dot access the class methods

    def set_num_door(self, num_door):
        if num_door < 1:
            raise ValueError('Num door cannot be less than 1!')
        self.num_door = num_door
    
    def get_num_door(self):
        return self.num_door

    def print_stats(self):
        print(f'Bus: Name={self.name}, Brand={self.brand}, Num_Of_Door={self.num_door}')
    
    @classmethod
    def increment_bus_count(cls):
        '''Increase bus count by one'''
        cls.num_of_bus += 1


if __name__ == "__main__":
    
    c1 = Car(name='Car1', brand='Brand1', drivetype='4WD')
    c2 = Car(name='Car2', brand='Brand2', drivetype='RWD')
    b1 = Bus(name='Bus1', brand='Brand1', num_door=2)
    b2 = Bus(name='Bus2', brand='Brand3', num_door=1)
    v1 = Vehicle(name='Vehicle1', brand='BrandX')

    c1.print_stats()
    c2.print_stats()
    print(f'Total num of cars: {c1.num_of_cars}')
    print(f'Total num of bus: {Bus.num_of_bus}')
    print(f'Total num of vehicle: {Car.num_of_vehicles}') # Parent class attributes can be access by subclass instance or class definition

    print(f'Car1 DriveType: {c1.drivetype}')