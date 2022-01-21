from modules.transceiver import LoraRF


def main():
  rf = LoraRF()
  
  print('\n\nDebug 2:')
  rf.receivePckts()

if __name__ == '__main__':
  main()
