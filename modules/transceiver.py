import adafruit_rfm9x
import digitalio
import board
import busio


class LoraRF:
	def __init__(self):
		self.cs = digitalio.DigitalInOut(board.D17)
		self.reset = digitalio.DigitalInOut(board.D18)
		self.spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
		self.b_rate = 1000000

	def receivePckts(self):
		rfm9x = adafruit_rfm9x.RFM9x(
			self.spi,
			self.cs,
			self.reset,
			915.0,
			baudrate=self.b_rate,
		)

		rfm9x.tx_power = 23 # (5 - 23)dBm

		# print('\n[ ok ] RFM95w Radio configured.\n')

		packet = rfm9x.receive()
		rssi = rfm9x.last_rssi # Signal strength of last received message
		snr = rfm9x.snr # Signal to noise ratio

		if packet is None:
			print('[ - ] Listening ...')

		else:
			# print('\n[ ! ] Received packet:')
			# print('[ + ] Signal strength (RSSI): {0} dBm'.format(rssi))
			# print('[ + ] SNR: {0} dB'.format(snr))
			# print('[ + ] Data (raw bytes): {0}'.format(packet))

			# print(str(packet))
			return packet

	def decode(self):
		pass

	def unpack(self, data):
		unpacked_data = None
		if data != None:
			data = data.decode()
			data = data.split(";")
			# print(data)

			if len(data) == 6:
				unpacked_data = {
					"hdc_temperature": data[0],
					"bmp_temperature": data[1],
					"humidity": data[2],
					"pressure": data[3],
					"mpu_altitude": data[4],
					"time": data[5],
				}

			elif len(data) == 8:
				unpacked_data = {
					"latitude": data[0],
					"longitude": data[1],
					"hdc_temperature": data[2],
					"bmp_temperature": data[3],
					"humidity": data[4],
					"pressure": data[5],
					"mpu_altitude": data[6],
					"time": data[7],
				}
			elif len(data) == 10:
				unpacked_data = {
					"latitude": data[0],
					"longitude": data[1],
					"neo_altitude": data[2],
					"num_satellites": data[3],
					"hdc_temperature": data[4],
					"bmp_temperature": data[5],
					"humidity": data[6],
					"pressure": data[7],
					"mpu_altitude": data[8],
					"time": data[9],
				}
		# else:
		# 	no_data = "no-packets"
		# 	unpacked_data = {
		# 		"latitude": no_data,
		# 		"longitude": no_data,
		# 		"hdc_temperature": no_data,
		# 		"bmp_temperature": no_data,
		# 		"humidity": no_data,
		# 		"pressure": no_data,
		# 		"mpu_altitude": no_data,
		# 		"time": no_data,
		# 	}

		return unpacked_data
