import struct
from .utils import common_functions, rgb_to_hex, hex_to_rgb, zero_fill_right_shift
from .utils.constants import *

class Kit:
    def __init__(self, data:bytearray):
        """
        Se inicializa la clase recibiendo un bytearray y se inicializan los parametros para el kit
        """
        self.data = data

    @property
    def font_curve(self):
        return FONT_CURVE[self.data[52]]

    @font_curve.setter
    def font_curve(self, new_value:int):
        """
        """
        if new_value not in FONT_CURVE:
            raise ValueError("Value not allowed")
        self.data[52] = FONT_CURVE.index(new_value)

    @property
    def short_number(self):
        """
        """
        return OFF_LEFT_RIGHT[self.data[54]]

    @short_number.setter
    def short_number(self, new_value:int):
        """
        """
        if new_value not in OFF_LEFT_RIGHT:
            raise ValueError("Value not allowed")
        self.data[54] = OFF_LEFT_RIGHT.index(new_value)

    @property
    def license(self):
        """
        Lee y carga en la variable self.license el valor correcto
        """
        license = self.data[58]
        return KIT_LICENSE[license]

    @license.setter
    def license(self, new_val:str):
        """
        Recibe un string que puede ser Yes o No y actualiza el valor,
        en los bytes del kit y en la clase
        """
        self.data[58] = new_val

    @property
    def model(self):
        """
        Carga el numero de model que tiene por default el kit
        """
        return self.data[60]

    @model.setter
    def model(self, new_value:int):
        """
        Actualiza el model en el kit
        """
        min_value = 0
        max_value = 0xFF
        if common_functions.check_value(min_value,new_value,max_value):
            self.data[60] = new_value
        else:
            raise ValueError(f"Model must be between {min_value} and {max_value}")

    @property
    def color_radar(self):
        """
        Carga el color del radar que tiene el kit por default
        """
        color_radar_r = self.get_value(0,8,31) * 8
        color_radar_g = self.get_value(1,5,31) * 8
        color_radar_b = self.get_value(1,10,31) * 8
        
        colors_radar_rgb = color_radar_r,color_radar_g,color_radar_b

        return rgb_to_hex(colors_radar_rgb)

    @color_radar.setter
    def color_radar(self, new_value):
        """
        hacer una funcion para validar los valores a pasar que esten entre 0 y 31 y que sea int
        actualizo el valor de rojo a 5
        """
        hex_rgb = hex_to_rgb(new_value)

        r = int(hex_rgb[0] / 8)
        g = int(hex_rgb[1] / 8)
        b = int(hex_rgb[2] / 8)

        self.set_value(0, 8, 31, r)
        self.set_value(1, 5, 31, g)
        self.set_value(1, 10, 31, b)
        
        #self.color_radar = new_value

    def get_value(self, offset, shift, mask):
        j = (self.data[offset]) << 8 | (self.data[(offset - 1)])
        j = zero_fill_right_shift(j,shift)
        j &= mask
        return j

    def set_value(self, offset, shift, mask, new_value):
        j = (self.data[offset]) << 8 | (self.data[(offset - 1)])
        k = 0xFFFF & (mask << shift ^ 0xFFFFFFFF)
        j &= k
        new_value &= mask
        new_value <<= shift
        new_value = j | new_value
        self.data[(offset - 1)] = (new_value & 0xFF)
        self.data[offset] = (zero_fill_right_shift(new_value,8))



