#!/usr/bin/python

import os
import re
import sys
from pprint import pprint

directory = "/proc"
dirCheck = re.compile(r'^\d*$')

processList = dict()

for filename in os.listdir(directory):
    myDir = os.path.join( directory, filename )
    if os.path.isdir(myDir):
        # print "Directory :",myDir

        if dirCheck.search(filename) is not None:
            with open(directory+"/"+filename+"/stat") as proc_file:
                content = proc_file.read()
                tuples = re.split('\s', content)
                # print "Process:"+tuples[3]+" --> "+tuples[0]
                if tuples[3] not in processList:
                    processList[tuples[3]] = dict()
                    processList[tuples[3]]["childs"] = []
                    # print "\tCreated parent process "+tuples[3]
                if tuples[0] not in processList:
                    processList[tuples[0]] = dict()
                    processList[tuples[0]]["childs"] = []
                    # print "\tCreated own process "+tuples[0]
                processList[tuples[0]]["name"] = tuples[1]
                # print "\tOwn process name is "+tuples[1]
                processList[tuples[3]]["childs"].append(tuples[0])
                # print "\tAdded "+tuples[0]+" as "+tuples[3]+"'s child process"

# pprint(processList)

def showAsTree( PID, depth ):
    sys.stdout.write( "  "*depth )
    if "name" not in processList[PID]:
        processList[PID]["name"] = "init"
    print "> ["+PID+"] "+processList[PID]["name"] + "  (Childs: "+str(len(processList[PID]["childs"]))+")"
    depth += 1
    for childProcess in processList[PID]["childs"]:
        showAsTree(childProcess, depth)

showAsTree("0",1)
