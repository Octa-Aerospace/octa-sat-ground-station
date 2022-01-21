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
		try: 
			while True:
				packet = rfm9x.receive()
				rssi = rfm9x.rssi # Signal strength of last received message
				snr = rfm9x.snr # Signal to noise ratio

				if packet is None:
					print('[ - ] Listening ...')
				else:
					print('\n[ ! ] Received packet:')
					print('[ + ] Signal strength (RSSI): {0} dBm'.format(rssi))
					print('[ + ] SNR: {0} dB'.format(snr))
					print('[ + ] Data (raw bytes): {0}'.format(packet))
					
					return str(packet, 'utf-8')
		except KeyboardInterrupt:
			print('\n[ x ] Listening stopped.')
			return None
