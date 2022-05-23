import serial
import time
from gpiozero import OutputDevice

uart0 = serial.Serial(port='/dev/ttyS0', baudrate = 9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

# nitro = b'0x01,0x03, 0x00, 0x1e, 0x00, 0x01, 0xe4, 0x0c'
# phosp = b'0x01,0x03, 0x00, 0x1f, 0x00, 0x01, 0xb5, 0xcc'
# potas = b'0x01,0x03, 0x00, 0x20, 0x00, 0x01, 0x85, 0xc0'

nitro = [0x01,0x03, 0x00, 0x1e, 0x00, 0x01, 0xe4, 0x0c]
phosp = [0x01,0x03, 0x00, 0x1f, 0x00, 0x01, 0xb5, 0xcc]
potas = [0x01,0x03, 0x00, 0x20, 0x00, 0x01, 0x85, 0xc0]

# nitro = b"\x01\x03\x00\x1e\x00\x01\xe4\x0c"
# phosp = b"\x01\x03\x00\x1f\x00\x01\xb5\xcc"
# potas = b"\x01\x03\x00\x20\x00\x01\x85\xc0"
nitro = bytearray(nitro)
phosp = bytearray(phosp)
potas = bytearray(potas)

re = OutputDevice(17)
de = OutputDevice(27)

def read(inp_):
    #Maybe try setting RE/DE to high
	re.on()
	de.on()
	time.sleep(0.1)
	if (uart0.write(inp_) == 8):
		#tx = uart0.write(inp_)
		uart0.flush()
		#print("Sent Data : " + str(tx))
		time.sleep(0.1)
		re.off()
		de.off()
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
