#key_fname should be your ssh private key (See 1)
#newkey.pub is the replacement SSH Authorized Key File (See 3)

1. Change the filename on line 2 to the name of the key file you want to use to connect to machines. I used Amazon EC2 for Linux machines and therefore, to connect to the machines, the code connects to the remote machines using the IP address and this key file.
2. In hostnames.txt, enter the username and hostname of the machines separated by a space. It should be "username IP". Entry for each new machine should be on a new line.
3. Replace "newkey.pub" on line 19 to the filename of the key you want to use to replace on all machines.
4.Output is generated in output.csv file