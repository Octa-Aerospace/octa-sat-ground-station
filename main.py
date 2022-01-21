from modules.transceiver import LoraRF


def main():
  rf = LoraRF()
  
  print('Debug 1:')
  print(rf.receivePckts())

  print('\n\nDebug 2:')
  rf.receivePckts()

if __name__ == '__main__':
  main()
    