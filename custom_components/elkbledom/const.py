from enum import Enum

DOMAIN = "starrysky"
CONF_RESET = "reset"
CONF_DELAY = "delay"

class EFFECTS (Enum):
    seven_color_fade = 0x00
    rgb_fade = 0x01
    seven_color_breath = 0x02
    rgb_breath = 0x03
    red_green_fade = 0x04
    red_blue_fade = 0x05
    green_blue_fade = 0x06
    seven_color_jump = 0x07
    rgb_jump = 0x08
    seven_color_flash = 0x09
    rgb_flash = 0x0a
    red_flash = 0x0b
    green_flash = 0x0c
    blue_flash = 0x0d
    yellow_flash = 0x0e
    purple_flash = 0x0f
    cyan_flash = 0x10
    white_flash = 0x11
    yellow_purple_flash = 0x12
    purple_cyan_flash = 0x13

EFFECTS_list = ['seven_color_fade',
    'rgb_fade',
    'seven_color_breath',
    'rgb_breath',
    'red_green_fade',
    'red_blue_fade',
    'green_blue_fade',
    'seven_color_jump',
    'rgb_jump',
    'seven_color_flash',
    'rgb_flash',
    'red_flash',
    'green_flash',
    'blue_flash',
    'yellow_flash',
    'purple_flash',
    'cyan_flash',
    'white_flash',
    'yellow_purple_flash',
    'purple_cyan_flash',
    ]
