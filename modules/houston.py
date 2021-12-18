from time import sleep
# from modules.mainModule import Buzzer
from modules.transceiver import LORA
from data.OctaCSV import OctaCSV as oc

class Houston:
    def __init__(self):
        # self.Buzzer = Buzzer()
        self.LORA = LORA()
        self.oc = oc()

    # def Buzzer_beep(self):
    #     self.Buzzer.beep_on()
    #     sleep(0.5) #! if we put this sleep, that will affect the module's reads
    #     self.Buzzer.beep_off() 
    #     sleep(2) #! same the above
    #     return '[ ok ] Successfully beeped'

    def LORA_receive(self):
        package = self.LORA.receive()
        return package

    def black_box(self, file_name, data):
        self.oc.header(file_name=file_name, headers=list(data.keys()))
        self.oc.writer(file_name=file_name, data=list(data.values()))
        return '[ ok ] Successfully saved'

    def start(self):
        # self.Buzzer_beep() #* just beep
        
        data = self.LORA_receive()
        print(data)

        # self.black_box(file_name='../data/Houston.csv', data=data)