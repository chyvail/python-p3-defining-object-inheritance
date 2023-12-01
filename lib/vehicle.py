class Vehicle:
    def __init__(self, wheel_size, wheel_number): # instances of vehicle initializes wheel size and wheel number
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number
    
    def go(self): # go and fill up methods show some veheicle behavior
        return "vrrrrrrrooom!"
    
    def fill_up_tank(self):
        return "filling up!"
