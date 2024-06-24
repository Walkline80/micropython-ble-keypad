"""
Copyright © 2024 Walkline Wang (https://walkline.wang)
Gitee: https://gitee.com/walkline/micropython-ble-keypad
"""
import sys
sys.path.append('/blelib')

import esp
esp.osdebug(None) # 注释此行可显示详细调试信息


class Config(object):
	class SPIParams(object):
		SCK  = 6
		MOSI = 7
		MISO = 2
		PL   = 4
		CE   = 5

		BAUDRATE = 4_000_000 # 4Mhz


	class KeyPadParams(object):
		CHIP_COUNTS    = 5               # 74HC165 * 5
		GPIO_COUNTS    = CHIP_COUNTS * 8 # 可用 GPIO 数量
		KEY_COUNTS     = 40              # 按键数量，不能超过 GPIO_COUNTS 的数量
		BUFFER_COUNTS  = CHIP_COUNTS     # 通过 74HC165 采集数据的字节数量
		FILTER_TIME_US = 100             # 按键消抖过滤时间，单位：毫秒

		# 发送键盘按键数据的字节数量，不包括修饰符和占位符
		REPORT_DATA_COUNT = 13
		'''
		根据`blelib/devices/hid/keyboard_2/reportmap.py`中的定义::

		    0x19, 0x04,   # Usage Minimum (0x04)
		    0x29, 0x65,   # Usage Maximum (0x65)
		    0x15, 0x00,   # Logical Minimum (0)
		    0x25, 0x01,   # Logical Maximum (1)
		    # 0x95, 0x62, # Report Count (98)
		    0x95, 0x68,   # Report Count (104)
		    0x75, 0x01,   # Report Size (1)

		`Report Count (104)`表示可以一次性发送 104 个数据位，`104 / 8 = 13.0`，
		因此数据字节数量为 13

		但是实际的数据位应为：`0x65 - 0x04 + 1 = 98`，为了 8 位字节对齐所以选择了 104 个数据位。
		'''
