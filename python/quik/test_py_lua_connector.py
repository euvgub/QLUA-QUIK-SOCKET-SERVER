#from src.python.quik import *
from connector import *

def main():
    quik = QuikConnector()
    quik.subscribe(callback = message_received)
    quik.connect()
    quik.send(QLInstrumentParamsSubscriptionRequest("SIH9"))
    quik.send(QLCandlesRequest("SIH9", "1DAY"))

    input("Press Enter to continue...")

def message_received(message):
    if message['message_type'] == "InstrumentParams":
        ip = QLInstrumentParams(message)
        print (message)
    if message['message_type'] == "CandlesResponse":
        candles = QLCandlesResponse(message)
        print(message)


if __name__ == "__main__":
    main()
