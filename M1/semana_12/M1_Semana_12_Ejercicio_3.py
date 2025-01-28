"""Multiple inheritance allows a class to inherit attributes and/or methods from more than one base class.
   This is useful when two or more classes of objects have both common and unique attributes.
   In the next example is show how smartphones a tables as electronic devices have common features like Connectivity and Storage,
   but can also have specific ones."""

class Connectivity:
    def __init__(self, wifi, bluetooth):
        self.wifi = wifi
        self.bluetooth = bluetooth

    def show_connectivity(self):
        print(f'Wifi: {self.wifi}, Bluetooth: {self.bluetooth}')


class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
    
    def show_capacity(self):
        print(f'Storage: {self.capacity}GB')


class Smartphone(Connectivity, Storage):
    def __init__(self, wifi, bluetooth, capacity, camera):
        Connectivity.__init__(self, wifi, bluetooth)
        Storage.__init__(self, capacity)
        self.camera = camera
    
    def show_info(self):
        self.show_connectivity()
        self.show_capacity()
        print(f'Camera: {self.camera}MP')


class Tablet(Connectivity, Storage):
    def __init__(self, wifi, bluetooth, capacity, screen_size):
        Connectivity.__init__(self, wifi, bluetooth)
        Storage.__init__(self, capacity)
        self.screen_size = screen_size
    
    def show_info(self):
        self.show_connectivity()
        self.show_capacity()
        print(f'Screen size: {self.screen_size} inches')


smartphone = Smartphone(wifi=True, bluetooth=True, capacity=256, camera=20)
tablet = Tablet(wifi=True, bluetooth=True, capacity=512, screen_size=12)

print(f'\nSmartphone Info:')
smartphone.show_info()

print(f'\nTablet Info:')
tablet.show_info()