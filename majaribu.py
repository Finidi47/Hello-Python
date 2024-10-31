class Hotel:
    def __init__(self, room_no, floor, room_type):
        self.room = room_type
        self.number = room_no
        self.floor = floor
        self.type = room_type

    def available(self):
        # TO DO: introduce an if statement
            print(f"Your room number is :{self.number} go to floor :{self.floor} and your room type is :{self.type}")


guest1 = Hotel(13, "Ruwenzori-2nd", "Double")
guest1.available()


