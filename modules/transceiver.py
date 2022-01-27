import adafruit_rfm9x
import digitalio
import board
import busio


class LoraRF:
	def __init__(self) -> None:
		self.cs = digitalio.DigitalInOut(board.CE1)
		self.reset = digitalio.DigitalInOut(board.D25)
		self.spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
		self.b_rate = 1000000

	def receivePckts(self) -> str:
		rfm9x = adafruit_rfm9x.RFM9x(
			self.spi,
			self.cs,
			self.reset,
			915.0,
			baudrate=self.b_rate,
		)

		rfm9x.tx_power = 23 # (5 - 23)dBm

		print('\n[ ok ] RFM95w Radio configured.\n')

		packet = rfm9x.receive()
		rssi = rfm9x.last_rssi # Signal strength of last received message
		snr = rfm9x.snr # Signal to noise ratio

		if packet is None:
			print('[ - ] Listening ...')

		else:
			print('\n[ ! ] Received packet:')
			print('[ + ] Signal strength (RSSI): {0} dBm'.format(rssi))
			print('[ + ] SNR: {0} dB'.format(snr))
			print('[ + ] Data (raw bytes): {0}'.format(packet))

			# print(str(packet))
			return packet

	def unpack(self, data):
		unpacked_data = None
		data = data.split(";")
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

		return unpacked_data
