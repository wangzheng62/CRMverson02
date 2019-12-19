from ldap3 import Server,Connection,ALL,Tls
from ldap3.extend.microsoft.modifyPassword import ad_modify_password
import ssl

def testpw(server,user,password):
    try:
        Connection(server,user=user,password=password,auto_bind=True)
        return True
    except Exception as e:
        print(e)
        return False

host='192.168.70.109'
server=Server(host,port=636,use_ssl=True,get_info=ALL)

if __name__=='__main__':
    #tls=Tls(local_private_key_file='',local_certificate_file='',validate=ssl.CERT_REQUIRED,version=ssl.PROTOCOL_TLSv1, ca_certs_file='ca_certs.b64')
    host='ldaps://192.168.70.109'
    server=Server(host,port=636,use_ssl=True,get_info=ALL)
    conn=Connection(server,user='WZ\\administrator',password='Ibm12345678.',authentication='NTLM',auto_bind=True)

    res=conn.search('DC=wz,DC=edu','(&(objectclass=user)(name=test005))',attributes=['objectclass','name','pwdlastset'])
    print(conn)

    newpw="Ez8456!@#."

    if testpw(server,user='CN=test005,OU=ttttttttt,DC=wz,DC=edu',password='123456'):
        print('密码正确')

    ad_modify_password(conn,'CN=test005,OU=ttttttttt,DC=wz,DC=edu',new_password=newpw,old_password='123456')
    print(conn.result)
