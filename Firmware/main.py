import board

from kmk.keys import KC
from kmk.extensions.RGB import RGB
from kmk.modules.layers import Layers
from kmk.modules.macros import Macros
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.rgb import AnimationModes

pieboard = KMKKeyboard()

macros = Macros()
pieboard.modules.append(macros)

encoder_handler = EncoderHandler()
pieboard.modules = [layers, holdtap, encoder_handler]


ROW1 = board.GP4
ROW2 = board.GP16
ROW3 = board.GP11
ROW4 = board.GP9
ROW5 = board.GP14
ROW6 = board.GP15
ROW7 = board.GP0
ROW8 = board.GP23
ROW9 = board.GP22
ROW10 = board.GP12
ROW11 = board.GP24
ROW12 = board.GP13
COL1 = board.GP25
COL2= board.GP19
COL3 = board.GP10
COL4 = board.GP21
COL5 = board.GP20
COL6 = board.GP18
COL7 = board.GP17
COL8 = board.GP5
COL9 = board.GP6
COL10 = board.GP7
COL11 = board.GP8

row_pins = [ROW1, ROW2, ROW3, ROW4, ROW5, ROW6, ROW7, ROW8, ROW9, ROW10, ROW11, ROW12]
col_pins = [COL1, COL2, COL3, COL4, COL5, COL6, COL7, COL8, COL9, COL10, COL11]

# I need to find my coord mapping when I have my keyboard assembled shttps://kmkfw-doc.misc.place/docs/basics/porting_to_kmk.html
coord_mapping = [

]

pieboard.keymap = [

_______ = KC.TRNS
xxxxxxx = KC.NO

# Default Layer
[
KC.ESC , KC.F1  , KC.F2  , KC.F3  , KC.F4  , xxxxxxx, KC.F5  , KC.F6  , KC.F7  , KC.F8  , KC.F9  , KC.F10  , KC.F11 , KC.F12 , KC.PSCR, KC.SLCK, KC.BRK
KC.TILD, KC.N1  , KC.N2  , KC.N3  , KC.N4  , KC.N5  , KC.N6  , KC.N7  , KC.N8  , KC.N9  , KC.N0  , KC.MINS , KC.EQL , KC.BSPC, KC.INS , KC.HOME, KC.PGUP, KC.NLCK, KC.PSLS, KC.PAST, KC.PMNS
KC.TAB , KC.Q   , KC.W   , KC.E   , KC.R   , KC.T   , KC.Y   , KC.U   , KC.I   , KC.O   , KC.P   , KC.LBRC , KC.RBRC, KC.BSLS, KC.DEL , KC.END , KC.PGDN, KC.KP_7, KC.KP_8, KC.KP_9, KC.PPLS
KC.LCAP, KC.A   , KC.S   , KC.D   , KC.F   , KC.G   , KC.H   , KC.J   , KC.K   , KC.L   , KC.SCLN, KC.QUOT , xxxxxxx, KC.ENT , xxxxxxx, xxxxxxx, xxxxxxx, KC.KP_4, KC.KP_5, KC.KP_6,
KC.LSFT, KC.Z   , KC.X   , KC.C   , KC.V   , KC.B   , KC.N   , KC.M   , KC.COMM, KC.DOT , KC.SLSH, xxxxxxx , xxxxxxx, KC.RSFT, xxxxxxx, KC.UP  , xxxxxxx, KC.KP_1, KC.KP_2, KC.KP_3, KC.PENT
KC.LCTL, KC.LGUI, KC.LALT, xxxxxxx, xxxxxxx, KC.SPC , xxxxxxx, xxxxxxx, KC.RALT, KC.RGUI, xxxxxxx, KC.MO(1), xxxxxxx, KC.RCTL, KC.LEFT, KC.DOWN, KC.RGHT, KC.KP_0, xxxxxxx, KC.PDOT,

# FN Layer
],
xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx   , xxxxxxx   , xxxxxxx   , KC.MPRV, KC.MPLY, KC.MNXT, xxxxxxx
xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx   , xxxxxxx   , xxxxxxx   , xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx
xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx   , xxxxxxx   , xxxxxxx   , xxxxxxx, xxxxxxx, xxxxxxx
xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx   , xxxxxxx   , xxxxxxx   , xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx
xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx   , KC.RGB_SAI, xxxxxxx   , xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx
xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx, KC.RGB_HUD, KC.RGB_SAD, KC.RGB_HUI, xxxxxxx, xxxxxxx, xxxxxxx
]

encoder_handler.pins = ( (board.GP29, board.GP30, board.GP26, False, 2,), )


encoder_handler.map = [
((KC.VOLD, KC.VOLU, KC.MUTE),), # Default 
((KC.RGB_VAD, KC.RGB_VAI, KC.RGB_TOG),) # FN layer
]


rgb = RGB(pixel_pin=board.GP3, num_pixels = 104)
pieboard.extensions.append(rgb)


if __name__ == '__main__':
    pieboard.go()
