#!/usr/bin/env python3
import platform, os, random

MSSQLDBSERVER = ['127.0.0.1', 'sa', '12345678']
MYSQLDBSERVER = {'user': 'root', 'password': '12345678', 'host': '127.0.0.1'}

# windows获取home
if platform.system() == "Windows":
    HOMEDOCPATH = os.environ["HOMEDRIVE"] + os.environ["HOMEPATH"] + "\\Documents\\"
    DOCDIR = HOMEDOCPATH + "mysoft"
    while (os.path.exists(DOCDIR)):
        DOCDIR = DOCDIR + random.choice("0123456789")
    os.mkdir(DOCDIR)
    LOGDIR = DOCDIR + "\\log"
    os.mkdir(LOGDIR)
    ERRORLOG = LOGDIR + "\\err.log"
    INFOLOG = LOGDIR + "\\info.log"
    #
    f = open("CONFIG.py", "w")
    f.write("MSSQLDBSERVER = %s" % MSSQLDBSERVER + "\n")
    f.write("MYSQLDBSERVER = %s" % MYSQLDBSERVER + "\n")
    f.write(("DOCDIR = \"%s\"" % DOCDIR).replace("\\", "/") + "\n")
    f.write(("LOGDIR = \"%s\"" % LOGDIR).replace("\\", "/") + "\n")
    f.write(("ERRORLOG = \"%s\"" % ERRORLOG).replace("\\", "/") + "\n")
    f.write(("INFOLOG = \"%s\"" % INFOLOG).replace("\\", "/") + "\n")
    f.close()
# linux获取home
elif platform.system() == "Linux":
    HOMEDOCPATH = os.environ["HOME"] + "/Documents/"
    DOCDIR = HOMEDOCPATH + "mysoft"
    while (os.path.exists(DOCDIR)):
        DOCDIR = DOCDIR + random.choice("0123456789")
    os.mkdir(DOCDIR)
    LOGDIR = DOCDIR + "/log"
    os.mkdir(LOGDIR)
    ERRORLOG = LOGDIR + "/err.log"
    INFOLOG = LOGDIR + "/info.log"
    #
    f = open("CONFIG.py", "w")
    f.write("MSSQLDBSERVER = %s" % MSSQLDBSERVER + "\n")
    f.write("MYSQLDBSERVER = %s" % MYSQLDBSERVER + "\n")
    f.write("DOCDIR = \"%s\"" % DOCDIR + "\n")
    f.write("LOGDIR = \"%s\"" % LOGDIR + "\n")
    f.write("ERRORLOG = \"%s\"" % ERRORLOG + "\n")
    f.write("INFOLOG = \"%s\"" % INFOLOG + "\n")
    f.close()
else:
    pass
