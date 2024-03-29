### Commands

**ls**  
   show list of files or directory.<br />
   ** ls -a -> show list of all files and directory(hidden also).<br />
   ** ls -lt -> show list of all the recently modified files and folders first.<br />
   ** ls -lrt -> show list of all the recently modified files and folders at last.<br />
   ** ls -lh -> show size of files and directory in human readable format.<br />
   

**scp** 
   scp (secure copy) command in Linux system is used to copy file(s) between servers in a secure way. The SCP command or secure copy allows secure transferring of files in between the local host and the remote host or between two remote hosts. It uses the same authentication and security as it is used in the Secure Shell (SSH) protocol. SCP is known for its simplicity, security and pre-installed availability. 
Here an example of it:
``` scp (directory address or file address in your local server) (destination-server: directory or file address)```

**rsync** 
   Remote Sync (Rsync) is the most commonly used command for copying and synchronizing files and directories remotely as well as locally in Linux/Unix systems.**Rsync** uses a remote-update protocol which allows transferring just the differences between two sets of files. The first time, it copies the whole content of a file or a directory from source to destination but from next time, it copies only the changed blocks and bytes to the destination.
           


**df** 
   tells you the total disk size, space used, space available, usage percentage, and what partition the disk is mounted on. I recommend pairing it with the -h flag to make the data human-readable.


**du**  
   The "disk usage" command is excellent when applied in the correct context. This command is at its best when you need to see the size of a given directory or subdirectory.

**dig**  

**yum**
   yum is a package management utility used in Linux distributions that are based on Red Hat Enterprise Linux (RHEL) or CentOS. It stands for "Yellowdog Updater, Modified." yum simplifies the process of installing, updating, and managing software packages on a system.

### systemctl
   systemctl is a command-line utility used in Linux distributions that use systemd as the init system. systemd is a system and service manager that provides advanced control and management features for processes, services, and system resources.


### sudo su -

### whoami

### Netstat
   Netstat command displays various network related information such as network connections, routing tables, interface statistics, masquerade connections, multicast memberships etc.
   example:
   ** Netsat -a** ->To show both listening and non-listening sockets.
   **Nestat -l** -> Show listening ports only.

 
