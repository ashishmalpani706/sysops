import csv
import paramiko
#key_fname should be your ssh private key
key_fname='assignmentKeyPair.pem'
#hostnames.txt is the file that contains hostnames and the ip addresses of the machine in the format hostname<SPACE>ip
with open("hostnames.txt") as f:
    for line in f:
        arr=line.split()
        uname=arr[0]
        ip=arr[1]
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=uname, key_filename=key_fname)
        stdin, stdout, stderr = ssh.exec_command('hostname')
        hostname=stdout.readlines()[0].rstrip()
        print (hostname)
        stdin, stdout, stderr = ssh.exec_command('stat --format=mtime=%y\|ctime=%z\|atime=%x ~/.ssh/authorized_keys')
        stats = stdout.readlines()[0].rstrip()
        print(stats)
        sftp = ssh.open_sftp()
        path='/home/'+uname+'/.ssh/authorized_keys'
		#newkey.pub is the replacement SSH Authorized Key File
        sftp.put('newkey.pub',path)
        stdin, stdout, stderr = ssh.exec_command('cat '+path)
        content = stdout.readlines()[0].rstrip()
		#Output is generated in output.csv file
        with open('output.csv','a') as f1:
            writer=csv.writer(f1)
            writer.writerow([hostname,ip,stats,content])