from ldap3 import Server,Connection,ALL,Tls
from ldap3.extend.microsoft.modifyPassword import ad_modify_password
import ssl
import base64
tls=Tls(local_private_key_file='',local_certificate_file='',validate=ssl.CERT_REQUIRED,version=ssl.PROTOCOL_TLSv1, ca_certs_file='ca_certs.b64')
host='192.168.70.107'
server=Server(host,port=636,use_ssl=True,get_info=ALL)
conn=Connection(server,user='WZ01\\administrator',password='Ibm123456.',authentication='NTLM',auto_bind=True)
conn.start_tls()
res=conn.search('DC=wz01,DC=test','(objectclass=user)',attributes=['objectclass'])
print(conn)
print(conn.entries)
print(server.schema.object_classes['user'])
newpw="Ibm564782."

ad_modify_password(conn,'CN=wz,DC=wz01,DC=test',new_password=newpw,old_password='Ibm123456.')
print(conn.result)
