import socket
import json

sock = socket.socket()
sock.connect(('localhost', 1248))
mes = json.dumps({
	'id': 1,
	'message_type': '"InstrumentParamsSubscriptionRequest',
})
sock.send(("message:" + mes).encode("windows-1251"))
while True:
	data = sock.recv(1024)
	data = data.decode("utf-8")
	if data is "":
		break
	print(data)