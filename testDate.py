from ldap3 import Server,Connection,ALL
from ldap3.extend.microsoft.modifyPassword import ad_modify_password
import base64
host='192.168.70.109'
server=Server(host,port=636,use_ssl=True,get_info=ALL)
conn=Connection(server,user='WZ\\administrator',password='Ibm12345678.',authentication='NTLM',auto_bind=True)
res=conn.search('DC=wz,DC=edu','(objectclass=user)',attributes=['objectclass'])
print(conn)
print(conn.entries)
print(server.schema.object_classes['user'])
newpw="Ibm564782"

res=conn.extend.microsoft.modify_password('CN=test000,OU=ttttttttt,DC=wz,DC=edu',new_password=newpw,old_password='Ibm123456.')
print(conn.result)
conn.unbind()
c1=Connection(server,user='WZ\\test000',password='Ibm123456.',authentication='NTLM',auto_bind=True)
print(c1.result['description'])