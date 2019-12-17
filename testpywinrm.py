from winrm import Session
import telnetlib
from time import sleep
host='192.168.70.107'

s=Session(host,auth=('administrator','Ibm123456.'))
s.run_cmd('cd')