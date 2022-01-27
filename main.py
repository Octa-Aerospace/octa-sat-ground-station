from modules.Quintero import Quintero

Quintero = Quintero()

if __name__ == '__main__':
    while True:
        try:
            Quintero.start()

        except KeyboardInterrupt:
            print("\n[ ! ] Exiting\n")
            exit()
