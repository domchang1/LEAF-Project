import serial
import time

uart0 = serial.Serial(port='/dev/ttyS0', baudrate = 9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)
#uart0.open()

# nitro = b'0x01,0x03, 0x00, 0x1e, 0x00, 0x01, 0xe4, 0x0c'
# phosp = b'0x01,0x03, 0x00, 0x1f, 0x00, 0x01, 0xb5, 0xcc'
# potas = b'0x01,0x03, 0x00, 0x20, 0x00, 0x01, 0x85, 0xc0'

# nitro = [0x1h, 0x3h, 0x0h, 0x1eh, Ox0h, 0x1h, 0xe4h, 0xch]
# phosp = [0x1h, 0x3h, 0x0h, 0x1fh, 0x0h, 0x1h, 0xb5h, 0xcch]
# potas = [0x1h,0x3h, 0x0h, 0x20h, 0x0h, 0x01h, 0x85h, 0xc0h]

nitro = b"\x01\x03\x00\x1e\x00\x01\xe4\x0c"
phosp = b"\x01\x03\x00\x1f\x00\x01\xb5\xcc"
potas = b"\x01\x03\x00\x20\x00\x01\x85\xc0"


def read(inp_):
    #Maybe try setting RE/DE to high
	uart0.setRTS(True)
	uart0.setDTR(True)
	time.sleep(1)
	if (uart0.write(inp_)):
		tx = uart0.write(inp_)
		#print(inp_)
		print("Sent Data : " + str(tx))
		uart0.setRTS(False)
		uart0.setDTR(False)
		rx = uart0.read(8)
		print("Received data : " + str(rx))
		val = int.from_bytes(rx, byteorder='big')
		#val = ((int.from_bytes(rx[3], 'big')) << 8) + (int.from_bytes(rx[4], 'big'))
		return val
	else:
		print("Data Didn't Transmit")

while True:
	N = read(nitro)
	P = read(phosp)
	K = read(potas)
	print("Nitrogen: " + str(N) + " mg/kg")
	time.sleep(1)
	print("Phosphorus: " + str(P) + " mg/kg")
	time.sleep(1)
	print("Potassium: " + str(K) + " mg/kg")
	time.sleep(1)
