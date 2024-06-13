"""
Copyright © 2024 Walkline Wang (https://walkline.wang)
Gitee: https://gitee.com/walkline/micropython-ble-keypad
"""
from micropython import const


class KeyCode(object):
	NONE = const(0x00)

	# region Letters and Numbers
	A = const(0x04)
	B = const(0x05)
	C = const(0x06)
	D = const(0x07)
	E = const(0x08)
	F = const(0x09)
	G = const(0x0A)
	H = const(0x0B)
	I = const(0x0C)
	J = const(0x0D)
	K = const(0x0E)
	L = const(0x0F)
	M = const(0x10)
	N = const(0x11)
	O = const(0x12)
	P = const(0x13)
	Q = const(0x14)
	R = const(0x15)
	S = const(0x16)
	T = const(0x17)
	U = const(0x18)
	V = const(0x19)
	W = const(0x1A)
	X = const(0x1B)
	Y = const(0x1C)
	Z = const(0x1D)

	NUM_1 = const(0x1E) # 1!
	NUM_2 = const(0x1F) # 2@
	NUM_3 = const(0x20) # 3#
	NUM_4 = const(0x21) # 4$
	NUM_5 = const(0x22) # 5%
	NUM_6 = const(0x23) # 6^
	NUM_7 = const(0x24) # 7&
	NUM_8 = const(0x25) # 8*
	NUM_9 = const(0x26) # 9(
	NUM_0 = const(0x27) # 0)
	# endregion

	# region F Keys
	F1  = const(0x3A)
	F2  = const(0x3B)
	F3  = const(0x3C)
	F4  = const(0x3D)
	F5  = const(0x3E)
	F6  = const(0x3F)
	F7  = const(0x40)
	F8  = const(0x41)
	F9  = const(0x42)
	F10 = const(0x43)
	F11 = const(0x44)
	F12 = const(0x45)
	# F13 = const(0x68)
	# F14 = const(0x69)
	# F15 = const(0x6A)
	# F16 = const(0x6B)
	# F17 = const(0x6C)
	# F18 = const(0x6D)
	# F19 = const(0x6E)
	# F20 = const(0x6F)
	# F21 = const(0x70)
	# F22 = const(0x71)
	# F23 = const(0x72)
	# F24 = const(0x73)
	# endregion

	# region Punctuation
	ENTER           = const(0x28)
	ESCAPE          = const(0x29)
	BACKSPACE       = const(0x2A)
	TAB             = const(0x2B)
	SPACE           = const(0x2C)
	MINUS           = const(0x2D) # -_
	EQUAL           = const(0x2E) # =+
	LEFT_BRACKET    = const(0x2F) # [{
	RIGHT_BRACKET   = const(0x30) # ]}
	BACKSLASH       = const(0x31) # \|
	NONUS_HASH      = const(0x32) # Non-US #~
	SEMICOLON       = const(0x33) # ;:
	QUOTE           = const(0x34) # '"
	GRAVE_ACCENT    = const(0x35) # `~
	COMMA           = const(0x36) # ,<
	DOT             = const(0x37) # .>
	SLASH           = const(0x38) # /?
	NONUS_BACKSLASH = const(0x64) # Non-US \|
	# endregion

	# region Lock Keys
	CAPS_LOCK    = CAPS = const(0x39)
	SCROLL_LOCK  = SCRL = const(0x47)
	NUM_LOCK     = NUM  = const(0x53)
	# endregion

	# region Modifiers
	LEFT_CTRL   = LCTL = const(0xE0)
	LEFT_SHIFT  = LSFT = const(0xE1)
	LEFT_ALT    = LALT = const(0xE2)
	LEFT_GUI    = LGUI = const(0xE3) # GUI (Windows/Command/Meta key)
	RIGHT_CTRL  = RCTL = const(0xE4)
	RIGHT_SHIFT = RSFT = const(0xE5)
	RIGHT_ALT   = RALT = const(0xE6)
	RIGHT_GUI   = RGUI = const(0xE7)
	# endregion

	# region Commands
	PRINT_SCREEN = PSCR = const(0x46)
	PAUSE        = const(0x48)
	INSERT       = INS  = const(0x49)
	HOME         = const(0x4A)
	PAGE_UP      = PGUP = const(0x4B)
	DELETE       = DEL  = const(0x4C)
	END          = const(0x4D)
	PAGE_DOWN    = PGDN = const(0x4E)
	APPLICATION  = APP  = const(0x65) # Application (Windows Menu Key)
	# endregion

	# region Directions
	RIGHT = const(0x4F)
	LEFT  = const(0x50)
	DOWN  = const(0x51)
	UP    = const(0x52)
	# endregion

	# region Number Pad
	PAD_SLASH    = const(0x54) # /
	PAD_ASTERISK = const(0x55) # *
	PAD_MINUS    = const(0x56) # -
	PAD_PLUS     = const(0x57) # +
	PAD_ENTER    = const(0x58)
	PAD_NUM_1    = P1 = const(0x59) # 1 and End
	PAD_NUM_2    = P2 = const(0x5A) # 2 and Down Arrow
	PAD_NUM_3    = P3 = const(0x5B) # 3 and Page Down
	PAD_NUM_4    = P4 = const(0x5C) # 4 and Left Arrow
	PAD_NUM_5    = P5 = const(0x5D) # 5
	PAD_NUM_6    = P6 = const(0x5E) # 6 and Right Arrow
	PAD_NUM_7    = P7 = const(0x5F) # 7 and Home
	PAD_NUM_8    = P8 = const(0x60) # 8 and Up Arrow
	PAD_NUM_9    = P9 = const(0x61) # 9 and Page Up
	PAD_NUM_0    = P0 = const(0x62) # 0 and Insert
	PAD_DOT      = const(0x63) # . and Delete
	# endregion
