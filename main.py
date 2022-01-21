from modules.transceiver import LoraRF


def main():
  rf = LoraRF()
  rf.receivePckts()

if __name__ == '__main__':
  main()
