from modules.houston import Houston

Houston = Houston()

if __name__ == '__main__':
    while True:
        try:
            Houston.start()
            
        except OSError:
            print('\n[ ! ] Warning: OSError, running anyways :).\n')

        except KeyboardInterrupt:
            print("\n[ ! ] Exiting\n")
            exit()