from dataclasses import dataclass
import struct

@dataclass
class Kit():
    shirt_colors : "list[int, int, int, int, int]" # 5 shirt colours
    shorts_colors  : "list[int, int, int, int]" # 4 short colours
    socks_colors : "list[int, int, int]" # 3 socks colours
    # captain armband
    captain_colors  : "list[int, int, int]" # 3 colours
    # border color
    name_border_color : int
    # fill color
    name_color : int
    number_border_color : int
    number_color : int
    shorts_num_border_color : int
    shorts_num_color : int
    #collar is the first of 5 shirt layers, with only two values
    #the following 5 attributes specifie what type is used (same order as in PES5)
    #the colors (how much of them are used depends on selected type) can be set above
    collar : int
    
    shirt_layers : "list[int, int, int, int]"
    shorts_type : int
    socks_type : int
    captain_type : int
    name_location : int
    name_type : int
    name_shape : int
    number_type : int
    shorts_number_location : int
    logo_location : int
    unknown_1 : int
    kit_type : int
    unknown_2 : int
    model : int
    #not sure about that...
    editable : int
    unknown_3 : int

def zero_fill_right_shift(val, n):
    return (val % 0x100000000) >> n

def get_value(val, shift, mask):
    j = val << 8 | val
    j = zero_fill_right_shift(j,shift)
    j &= mask
    return j

"""
def set_value(self, offset, shift, mask, new_value):
    j = (self.data[offset]) << 8 | (self.data[(offset - 1)])
    k = 0xFFFF & (mask << shift ^ 0xFFFFFFFF)
    j &= k
    new_value &= mask
    new_value <<= shift
    new_value = j | new_value
    self.data[(offset - 1)] = (new_value & 0xFF)
    self.data[offset] = (zero_fill_right_shift(new_value,8))
"""


def main():
    total_shirt_colors = 5
    total_short_colors = 4
    total_socks_colors = 3
    total_captain_colors = 3
    total_shirt_layers = 4
    
    kit_file = open("./test/kit6.bin", "rb")

    for i, kit_name in enumerate(["GA", "PA", "GB", "PB", ]):
    
        shirt_colors = list(struct.unpack("<%dH" % total_shirt_colors, kit_file.read(total_shirt_colors*2)))
        short_colors = list(struct.unpack("<%dH" % total_short_colors, kit_file.read(total_short_colors*2)))
        socks_colors = list(struct.unpack("<%dH" % total_socks_colors, kit_file.read(total_socks_colors*2)))
        captain_colors = list(struct.unpack("<%dH" % total_captain_colors, kit_file.read(total_captain_colors*2)))
        kit_data_1 = struct.unpack("<6HB", kit_file.read(6*2 + 1))
        shirt_ayers = list(struct.unpack("<%dB" % total_shirt_layers, kit_file.read(total_shirt_layers)))
        kit_data_2 = struct.unpack("<15B", kit_file.read(15))

        kit = Kit(shirt_colors, short_colors, socks_colors, captain_colors, *kit_data_1, shirt_ayers, *kit_data_2)

        print("Radar Color/Main Shirt Color")
        print("R:", get_value(kit.shirt_colors[0], 0, 31) * 8)
        print("G:", get_value(kit.shirt_colors[0], 5, 31) * 8)
        print("B:", get_value(kit.shirt_colors[0], 10, 31) * 8)
        print("%s kit configuration" % kit_name)
        print(kit)
    kit_file.close()

if __name__ == "__main__":
    main()
