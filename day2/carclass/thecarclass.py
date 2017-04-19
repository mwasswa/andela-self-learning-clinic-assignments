class Car(object):
    def __init__(self,name="General",model="GM",type='saloon'):
        self.type = type
        self.model = model
        self.name = name
        self.speed = 0
        if self.name.lower() in ['porshe','koenigsegg']:
            self.num_of_doors = 2
        else:
            self.num_of_doors =4

        if self.type.lower() == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4


    def is_saloon(self):
        if self.type.lower() == 'saloon':
            return True
        else:
            return False

    def drive(self, moving_speed):
        if moving_speed == 3:
            self.speed = 1000
        elif moving_speed == 7:
            self.speed = 77

        return self




