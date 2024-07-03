### Object Pooling
    Object pooling is a software design pattern used to optimize the performance and resource usage of an application, particularly in scenarios where creating and destroying objects frequently can be resource-intensive and lead to inefficiencies.
    In object-oriented programming, objects are instances of classes, and creating objects involves allocating memory and performing initialization. Destroying objects involves releasing memory and performing cleanup. However, this process can be time-consuming and may lead to memory fragmentation and increased overhead, especially in scenarios where objects are frequently created and destroyed.
    Object pooling addresses these challenges by reusing and recycling objects instead of constantly creating and destroying them.
  
    1. Object Creation and Initialization: Instead of creating objects on-demand, a pool of pre-allocated objects is created during application initialization. These objects are typically in a "ready" or "idle" state, waiting to be used.
    2. Object Usage: When an object is needed, the application requests an object from the pool. If an idle object is available, it is retrieved from the pool. If no idle objects are available, the pool can create additional objects up to a certain limit (the pool size).
    3. Object Recycling: Once an object is no longer needed, it is returned to the pool. The object's state is reset, and it is marked as "idle" so that it can be reused in the future.

### Block Storage
    Block level storage, or block storage, is storage used for structured data and is commonly deployed in Storage Area Network (SAN) systems. It uses Internet Small Computer Systems Interface (iSCSI) and Fibre Channel (FC) protocols.
    Block storage breaks up data into blocks and then stores those blocks as separate pieces, each with a unique identifier. The SAN places those blocks of data wherever it is most efficient. That means it can store those blocks across different systems and each block can be configured (or partitioned) to work with different operating systems.
    Block storage also decouples data from user environments, allowing that data to be spread across multiple environments. This creates multiple paths to the data and allows the user to retrieve it quickly. When a user or application requests data from a block storage system, the underlying storage system reassembles the data blocks and presents the data to the user or application.

### File storage
    File storage, which is also referred to as file-level or file-based storage, is normally associated with Network Attached Storage (NAS) technology. 

### Network File Systme (NFS)
    NFS allows a system to share directories and files with others over a network. By using NFS, users and programs can access files on remote systems almost as if they were local files.

#### System call
    1. File related
    2. Device Related
    3. Information -> information(metadata) of process
    4. Process Control
    5. Communication -> Where two process communicate

#### Fork system call
    To create a child process. it return value 0 , -1 and 1. 0 -> child process and 1 -> parent process.
    Total process - > 2^n
    Total child process - > 2^n - 1  


In multi process context switching is slower and in multi thread it is faster but blocking a multi thread will block entire process(i.e. other threads)

kernel level thread -> managed by OS system

User level thread ->  managed by user level


### Scheduling Algorithm
    Pre-Emptive -> If one process is being excuted by a processor then it can taken out and put into ready queue in between and can execute another process.
     1. Shortest Remaining Time First
     2. Longest Remaining Time First
     3. Round Robin
     4. Priority Based
    Non Pre-Emptive -> x
        1. Highest Response Ratio 
        2. First Come First serve

### Burst Time
    Time required by process to execute by CPU


#### Round Robin Scheduling Algo

    Processor will execute process for upto a time which is time quantum. IN round robin there is ready queue and running queue

#### Process Synchronization
    there are two types of process->1. Cooperative and independent process
    In Cooperative processes they share (variable,memory, code) and they may affect each other

#### Race Condition
    

#### Critical Section
    It is a part of the program where shared resources are accessed by various processes/

### Condition to make process synchronization
    1. Mutual Exclusion -> only one process can access shared code(critical section) at a time.
    2. Progress
    3. Bound Wait -> all process should be able to use critical section.    
    4. No assumption related to H/w speed

#### Lock Variable
    1. Execute in User Mode
    2. Multiprocess Solution
    3. No Mutual Exclusion is guarantee
    
#### Turn Variable
    process synchronization is only for two processes and it works at user mode only.
    ME is satisfied but progess is not.

#### Semaphore
    is an int variable which is used in mutual exclusive manner various concurrent cooperative process in order to achieve synchronization
    
### necessity condition for dealock
    1. mutual exclusion
    2. No pre-emption
    3. Hold & wait
    4. Circular wait

### Methods to handle Deadlock
    1. Deadlock ignorance
    2. Deadlock prevention
    3.Deadlock Avoidance
    4. Deadlock detection & recovery

### Memory management techniques
    1. Contiguous -> processes are kept in continuous address in RAM. In contiguous, spanning is not allowed
        a. Fixed partition(static) -> Number of partitions are fixed, Size of each partition may or may not be same.
            cons-> internal fragmentation, limit in process size, limitation of degree of multi-tasking, external fragementation
        b. Varied partition(Dynamic)-> cons: external fragmentation. allocation/deallocation complex
    2. Non-Contiguous
        a. Paging
        b. Multi level paging
        c. Inverted paging
        d. Segmentation
        e. Segmentation Paging


Subnet defines your local area network
Gateway is ip address of Router
Router is the device through which lan can connect with outer network/internet
#### NAT
    Network address translation is a method of remapping an IP address while they are in transit across a traffic routing device

Firewall is a set of passive rules to protect network from unauthorised access
DMZ -> zone created within LAN, it is subnetowrk that contains and exposes a device to an untrusteed network such as internet

Port Forwarding redirects a communication request from one address and port number combination to another


