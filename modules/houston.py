from time import sleep
from modules.transceiver import LORA

class Houston:
    def __init__(self):
        # self.Buzzer = Buzzer()
        self.LORA = LORA()

    def LORA_receive(self):
        package = self.LORA.receive()
        return package

    def black_box(self, file_name, data):
        self.oc.header(file_name=file_name, headers=list(data.keys()))
        self.oc.writer(file_name=file_name, data=list(data.values()))
        return '[ ok ] Successfully saved'

    def start(self):
        data = self.LORA_receive()
        print(data)
