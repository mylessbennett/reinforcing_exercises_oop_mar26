class Location:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "{}".format(self.name)

class Trip:
    
    def __init__(self):
        self.stops = []

    def add_stop(self, stop):
        self.stops.append(stop)

    def list_locations(self):
        print('Began trip.')
        for i, stop in enumerate(self.stops):
            if i + 1== len(self.stops):
                break
            else:
                print("Travelled from {} to {}".format(stop, self.stops[i+1]))
        print('Ended trip.')


my_trip = Trip()
print(my_trip.stops)
my_trip.add_stop(Location('Toronto'))
my_trip.add_stop(Location('Ottawa'))
my_trip.add_stop(Location('Montreal'))
my_trip.add_stop(Location('Vancouver'))
my_trip.list_locations()



