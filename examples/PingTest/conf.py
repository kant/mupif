# List of job applications - server details
# Do not use a dictionary - items are in arbitrary order
# The format is (name, serverName, username, localNATPort, serverPort,sshClient)
apps=[('ctu-server','ksm.fsv.cvut.cz', 'mmp', 5554, 44382, 'ssh',''),
      #('celsian','jaja.fsv.cvut.cz', 'bp', 5555, 44381,'ssh',''),
      ('micress','acsrvappmic1.access.rwth-aachen.de', 'mmp', 5558, 44382,'ssh','')]

#jobname - do not change 
jobname = 'PingTest'
#nathost - do not change
nathost='localhost'
#nameserver - do not change
nshost = 'ksm.fsv.cvut.cz'
#name server port - do not change
nsport  = 9090

#do-not-change below this line, indexes in apps list
appIndx_Name = 0
appIndx_ServerName = 1
appIndx_UserName = 2
appIndx_NATPort = 3
appIndx_RemotePort = 4
appIndx_SshClient = 5
appIndx_Options = 6

import logging
#put logging before Pyro4 module
logging.basicConfig(filename='mupif.pyro.log',filemode='w',datefmt="%Y-%m-%d %H:%M:%S",level=logging.DEBUG)
logging.getLogger('Pyro4').setLevel(logging.INFO)
logger = logging.getLogger('test.py')
logger.setLevel(logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler()) #display logging also on screen

import Pyro4
Pyro4.config.SERIALIZER="pickle"
Pyro4.config.PICKLE_PROTOCOL_VERSION=2 #to work with python 2.x and 3.x
Pyro4.config.SERIALIZERS_ACCEPTED={'pickle'}
