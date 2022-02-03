import os
from modules.Quintero import Quintero

Quintero = Quintero()

if __name__ == '__main__':
    while True:
        try:
            Quintero.start()

        # except OSError:
        #     print("[ error ] OSError. Rebooting ...")
        #     os.system("sudo reboot")

        except KeyboardInterrupt:
            print("\n[ ! ] Exiting\n")
            exit()

        # except Exception as e:
        #     print("[ error ] Exception: " + str(e))
        #     print("[ ! ] Rebooting ...")
        #     os.system("sudo reboot")
