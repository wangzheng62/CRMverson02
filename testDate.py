from ldap3 import Server,Connection,ALL
from ldap3.extend.microsoft.modifyPassword import ad_modify_password
import base64
host='192.168.70.109'
server=Server(host,port=636,use_ssl=True,get_info=ALL)
conn=Connection(server,'administrator@wz.edu','Ibm12345678.',auto_bind=True)
res=conn.search('DC=wz,DC=edu','(objectclass=user)',attributes=['objectclass'])
print(conn.result)
print(conn.entries)
print(server.schema.object_classes['user'])
newpw="\"Ibm564782\""



ad_modify_password(conn,'CN=test005,OU=ttttttttt,DC=wz,DC=edu',newpw,old_password='12345678')
print(conn.result)