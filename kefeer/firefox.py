import telnetlib
import json


def is_fullscreen():
	try:
		T=telnetlib.Telnet()
		T.open('localhost',32000)
		T.write('window.fullScreen')
		r=T.read_until('}')
		T.close()
		return r=='{"result":true}'

	except:
		return False
