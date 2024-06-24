"""
Copyright © 2024 Walkline Wang (https://walkline.wang)
Gitee: https://gitee.com/walkline/micropython-ble-keypad
"""
from config import Config
from keypad.keycode import KeyCode as KC
from drivers._74HC165 import _74HC165
from blelib.devices.hid.keyboard_2.keyboard import BLEKeyboard104


class KeyPad(_74HC165):
	MODIFIERS = {
        KC.LCTL: 0,
        KC.LSFT: 1,
        KC.LALT: 2,
        KC.LGUI: 3,
        KC.RCTL: 4,
        KC.RSFT: 5,
        KC.RALT: 6,
        KC.RGUI: 7,
    }

	KEY_MAP = [
		[
			# 键位定义层
			 0,  1,  2,  3,  4,  5,  6,  7, # row1
			 8,  9, 10, 11, 12, 13, 14, 15, # row2
			16, 17, 18, 19, 20, 21, 22, 23, # row3
			24, 25, 26, 27, 28, 29, 30, 31, # row4
			32, 33, 34, 35, 36, 37, 38, 39, # row5
		],
		[
			# 配列层1
			KC.ESCAPE, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U,
			KC.A, KC.S, KC.D, KC.F, KC.G, KC.I, KC.O, KC.P,
			KC.Z, KC.X, KC.C, KC.V, KC.B, KC.H, KC.J, KC.K,
			KC.LCTL, KC.LALT, KC.LSFT, KC.NONE, KC.NONE, KC.L, KC.N, KC.M,
			KC.NONE, KC.NONE, KC.SPACE, KC.LGUI, KC.NONE, KC.NONE, KC.NONE, KC.ENTER,
		],
	]

	def __init__(self, led_status_cb: function = None):
		_74HC165.__init__(self, filter_time_us=Config.KeyPadParams.FILTER_TIME_US)

		self.__ble_keyboard = BLEKeyboard104(
			device_name='MP_KB40',
			led_status_cb=led_status_cb
		)

		self.__kb_modifier    = 0b00000000
		self.__kb_data_buffer = bytearray([0x00 for _ in range(Config.KeyPadParams.REPORT_DATA_COUNT)])

	def __update_kb_data(self):
		'''根据采样数据更新要发送的键盘数据'''
		for index in range(Config.KeyPadParams.KEY_COUNTS):
			try:
				key_code = self.KEY_MAP[1][self.KEY_MAP[0].index(index)]

				if key_code == KC.NONE:
					continue

				key_status = self.__get_key_status(index)
				self.__set_kb_data(key_code, key_status)
			except ValueError as ve:
				print('Key index error:', ve)

	def __get_key_status(self, index):
		'''获取键位定义层中指定按键的状态'''
		if index < 0 or index >= Config.KeyPadParams.KEY_COUNTS:
			raise ValueError(f"Index {index} out of range")

		status = self.__bitRead(self.__key_buffer[index // 8], index % 8)

		return status ^ 1 if Config.KeyPadParams.PRESSED_LOW else status

	def __set_kb_data(self, key_code: int, status: int):
		if key_code in self.MODIFIERS:
			bit_index = self.MODIFIERS[key_code]

			self.__kb_modifier = self.__bitSet(
				self.__kb_modifier, bit_index, status)
		else:
			byte_index = (key_code - KC.A) // 8
			bit_index  = (key_code - KC.A) % 8

			self.__kb_data_buffer[byte_index] = self.__bitSet(
				self.__kb_data_buffer[byte_index], bit_index, status)

	def __bitRead(self, data: int, bit: int):
		return (data >> bit) & 0x01

	def __bitSet(self, data: int, bit: int, status: int):
		if status:
			data |= (1 << bit)  # set
		else:
			data &= ~(1 << bit) # clear

		return data

	def update_battery_level(self, value: int = None):
		self.__ble_keyboard.update_battery_level(value)

	def send_kb_data(self):
		self.__update_kb_data()
		self.__ble_keyboard.send_kb_key(
			bytearray([self.__kb_modifier, 0x00]) + self.__kb_data_buffer)


def run_test():
	ready = False

	def led_status_cb(num_lock, caps_lock, scroll_lock):
		nonlocal ready
		print(f'{num_lock=}, {caps_lock=}, {scroll_lock=}')
		ready = True

	keypad = KeyPad(led_status_cb=led_status_cb)
	keypad.update_battery_level()

	while ready:
		pass

	while True:
		if keypad.get_keys_status():
			keypad.send_kb_data()


if __name__ == '__main__':
	run_test()
