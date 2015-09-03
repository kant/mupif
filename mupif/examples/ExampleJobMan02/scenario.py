from __future__ import print_function
import clientConfig as cConf
from mupif import *
import logging
logger = logging.getLogger()

import time as timeTime
start = timeTime.time()
logger.info('Timer started')

#locate nameserver
ns = PyroUtil.connectNameServer(nshost=cConf.nshost, nsport=cConf.nsport, hkey=cConf.hkey)

#localize JobManager running on (remote) server and create a tunnel to it
#allocate the first application app1
try:
    appRec = PyroUtil.allocateApplicationWithJobManager( ns, cConf.demoJobManRec, cConf.jobNatPorts.pop(0), cConf.sshClient, cConf.options, cConf.sshHost )
    app1 = appRec.getApplication()
except Exception as e:
    logger.exception(e)
else:
    if app1 is not None:
        appsig=app1.getApplicationSignature()
        logger.info("Working application 1 on server " + appsig)

        app1.solveStep(None)
        remoteFile = appRec.getJobManager().getPyroFile (appRec.getJobID(), 'test.txt')
        print(remoteFile)
        PyroUtil.uploadPyroFile ("localtest.txt", remoteFile)

        file = open ("localtest.txt", "r")
        answer = file.readlines()
        print(answer);
        
        if (answer[0]=="Hello MMP!"):
            print ("Test OK")
        else:
            print ("Test FAILED")
       

finally:
    if appRec: appRec.terminateAll()


