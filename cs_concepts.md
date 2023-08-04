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
