import adafruit_rfm9x
import digitalio
import board
import busio

class LORA:        
    def send(self, Payload):
        if len(Payload) > 252:
            return "You can only send a message up to 252 bytes in length at a time!"

        BAUDRATE = 1000000
        RADIO_FREQ_MHZ = 915.0
        CS = digitalio.DigitalInOut(board.CE1) 
        RESET = digitalio.DigitalInOut(board.D25) # The pin used in the raspberry pi is D25; Number 
        spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    
        rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ, baudrate=BAUDRATE)
        rfm9x.tx_power = 23 # min 5dB; max 23dB
        #rfm9x.enable_crc = True
        #rfm9x.ack_delay = .1
        #rfm9x.node = 1
        #rfm9x.destination = 2

        rfm9x.send(bytes(Payload, "UTF-8"))

        return "[ ok ] Sending packages"

    def receive(self):
        BAUDRATE = 1000000
        RADIO_FREQ_MHZ = 915.0

        pinout = { # Pinout from the LoRaWAN RFM9x module to the Raspberry Pi
            "3.3v": 1,
            "GND": 6,
            "DI00": 7,
            "RESET": 11,
            "NSS": 22,
            "MOSI": 19,
            "MISO": 21,
            "SCK": 23,
        }

        CS = digitalio.DigitalInOut(board.D22)
        RESET = digitalio.DigitalInOut(board.D25)
        spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

        # Create the RFM9x device
        rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ, baudrate=BAUDRATE)
        
        # Create a unique ID for the device
        uid = adafruit_rfm9x.base_id
        
        # Print out the details of the RFM9x device we just created
        print("\nRFM9x Device ID: {}".format(uid))
        print("Antenna: {:.0f}°".format(rfm9x.tx_power))
        print("\nWaiting for packets...")
    
        rfm9x.tx_power = 23

        packet = rfm9x.receive()
        if packet is not None:
            return str(packet, "utf-8")
        else:
            return "[ ok ] No packages received"

    def prepare_payload(self, data):
        payload = ""
        for i in data:
            payload += str(data[i])
            if data[i] != data[list(data.keys())[-1]]:
                payload += ";"
                
        return payload


# LORA = LORA()
# LORA.send("Hello World!")
# LORA.receive()

