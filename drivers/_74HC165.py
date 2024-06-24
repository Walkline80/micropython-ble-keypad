"""
Copyright © 2024 Walkline Wang (https://walkline.wang)
Gitee: https://gitee.com/walkline/micropython-ble-keypad
"""
from time import sleep_us
from machine import SPI, Pin
from config import Config


class _74HC165(object):
	def __init__(self, filter_time_us: int = Config.KeyPadParams.FILTER_TIME_US):
		self.__filter_time  = filter_time_us

		self.__spi = SPI(1)
		self.__spi.init(
			baudrate=Config.SPIParams.BAUDRATE,
			# sck=Config.SPIParams.SCK,
			# mosi=Config.SPIParams.MOSI,
			# miso=Config.SPIParams.MISO,
			polarity=1,
			phase=0,
			bits=8,
			firstbit=SPI.LSB,
		)

		self.__key_buffer = bytearray([0xff for _ in range(Config.KeyPadParams.BUFFER_COUNTS)])

		self.__keys_pl = Pin(Config.SPIParams.PL, Pin.OUT, value=1)
		self.__keys_ce = Pin(Config.SPIParams.CE, Pin.OUT, value=0)

	def __scan_keys(self):
		self.__keys_pl.off()
		self.__keys_pl.on()

		return bytearray(self.__spi.read(Config.KeyPadParams.BUFFER_COUNTS))

	def get_keys_status(self) -> bool:
		'''检查按键状态，状态发生变化返回`True`，否则返回`False`'''
		result = False

		buffer_1 = self.__scan_keys()
		sleep_us(self.__filter_time)
		buffer_2 = self.__scan_keys()

		for count in range(Config.KeyPadParams.BUFFER_COUNTS):
			mask = buffer_1[count] ^ buffer_2[count]
			buffer_2[count] |= mask

		if self.__key_buffer != buffer_2:
			self.__key_buffer = buffer_2
			result = True

		return result

	@property
	def key_buffer(self):
		return self.__key_buffer


def run_test():
	keypad = _74HC165()

	for index in range(Config.KeyPadParams.BUFFER_COUNTS):
		title = f'row{index + 1}'
		print(f'{title:^ 10} ', end='')
	print()

	while True:
		if keypad.get_keys_status():
			print('', end='\r')
			for buffer in keypad.key_buffer:
				print(''.join(reversed(f'{buffer:08b}|')), end='| ')

		sleep_us(1_000)


if __name__ == '__main__':
	run_test()
