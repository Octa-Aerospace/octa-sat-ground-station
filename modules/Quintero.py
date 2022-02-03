from data.QuinteroCSV import QuinteroCSV
from modules.transceiver import LoraRF

class Quintero:
    def __init__(self):
        self.qc = QuinteroCSV()
        self.rf = LoraRF()

    def black_box(self, file_name, data):
        self.qc.header(file_name=file_name, headers=list(data.keys()))
        self.qc.writer(file_name=file_name, data=list(data.values()))
        return '[ ok ] Successfully saved'

    def start(self):
        packed_data = self.rf.receivePckts()
        data = self.rf.unpack(packed_data)

        self.black_box(file_name="/home/pi/Desktop/OctaSat/data/QuinteroCSV.csv", data=data)

        for element in data:
            print(element.upper() + ":" + str(data[element]))