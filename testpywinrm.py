from winrm import Session
import telnetlib
from time import sleep
host='192.168.70.109'

s=Session(host,auth=('administrator@wz.edu','Ibm12345678.'))
s.run_ps('cd')