#!/usr/bin/python

import sys
import os
import paramiko

server = 'localhost'
username = 'chhanz'
keyfile = 'chhanz.pem'
destpath = '/tmp'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(server, username=username, key_filename=keyfile)

sftp = ssh.open_sftp()
localpath = sys.argv[1]
remotepath = destpath + "/" + os.path.basename(localpath)

sftp.put(localpath, remotepath)
# DEBUG
print("Done Fast-sftp")

sftp.close()
ssh.close()
