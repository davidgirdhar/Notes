
Linux Filesystem is defined by Filesystem Hierarchy Standard 

### /bin
    contains binaries or executables that are essential to the entire operating system. E.g. -> curl, grep, gzip, ls etc.

### /sbin
    contains system binaries that should  only accessed by root user. e.g deluser

### /lib
    Now these binaries shared common libraries which is stores in this directory

### /usr
    It's user directory which it's own bin and lib directory.Now in this bin directory contains executables which are non-essential to operating system.

#### /local
    It contains binaries that you complied manually to provide a safe place that won't conflit with any software installed by system package manager

### /etc
    It stands for Editable Text Config. This directory contains mostly ediable text config file which can be edited.

### /home
    In this directory you'll find all directories named after each user

### /boot
    It contains files that needed to boot the system like the kernel itself

### /dev
    It stands for device files, here you can interface with hardware or drivers as if they were regular files. You can create disk partitions here or interface with floppy drive.

### /opt
    It contains optional or add-on software.

### /var
    It contains variable files that will change as operating system is being used, like logs and cache files.

### /temp
    temp is for temporary files and which no longer will be present if you reboot the system

### /proc
    It's an illusionary file system that doesn't actually exist on disk but is created in memory.

 




