import struct

class Shop:
    POINTS_OFFSET_1 = 52
    POINTS_OFFSET_2 = 0

    def __init__(self,option_file):
        self.of = option_file
        self.get_points()

    def get_points(self):
        self.points = struct.unpack("<I", self.of.data[self.POINTS_OFFSET_1 : self.POINTS_OFFSET_1 + 4])[0]

    def set_points(self,new_points):
        if 0 > new_points > 99999:
            raise ValueError("Points value must be between 0 and 99999")
        self.of.data[self.POINTS_OFFSET_1 : self.POINTS_OFFSET_1 + 4] = struct.pack("<I", new_points)
        self.of.data[self.POINTS_OFFSET_2 : self.POINTS_OFFSET_2 + 4] = struct.pack("<I", new_points)
        self.get_points()

    def lock_shop(self):
        for i in range(5144,5170):
            self.of.data[i] = 0
        self.of.data[56] = 1
        return "Shop locked!"

    def unlock_shop(self):
        for i in range(20):
            self.of.data[5144 + i] = 255
        self.of.data[5164] = 254
        self.of.data[5165] = 255
        self.of.data[5166] = 255
        self.of.data[5167] = 127
        self.of.data[5168] = 15
        self.of.data[5169] = 63
        self.of.data[56] = 98
        return "Shop unlocked!"
