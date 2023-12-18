
###  Load Balancer
    Now firsly let's understand the term load balancing, so it basically -> efficiently distributing incoming network traffic across a group of backend servers, also known as a server farm or server pool.
    So the functions performed by load balancer is that it Distributes client requests or network load efficiently across multiple servers, Ensures high availability and reliability by sending requests only to servers that are online, Provides the flexibility to add or subtract servers as demand dictates

#### load balancing algorithm
* __Round Robin__ — Requests are distributed across the group of servers sequentially.
* **Least Connections** — A new request is sent to the server with the fewest current connections to clients. The relative computing capacity of each server is factored into determining which one has the least connections.
* **IP Hash** — The IP address of the client is used to determine which server receives the request.



### Network File System
    NFS is not the actual file system but the protocol used between the clients and the servers with the data.The Network File System (NFS) protocol was designed to allow several client machines to transparently access a file system on a single server.
    NAS means network-attached st  orage and has become synonymous with remote file system storage (read more about NAS here). NFS is one of the protocols to access a NAS storage system over the network and the most common one in the Linux/Unix world. In the Windows world, SMB/CIFS is the primary protocol to access NAS storage.

#### NFS v/s SMB
    The two protocols roughly serve the same purpose: making a remote file system accessible to clients via a computer network. Sun Microsystems developed NFS as an open standard targeted at Unix environments (Sun developed Solaris, which was a Unix system). On the other hand, SMB/CIFS was developed by Microsoft for their Windows operating system. So, your client’s operating system dictates which protocol you use: Unix/Linux=NFS and Windows=SMB/CIFS. There are drivers to mount NFS on Windows and SMB on Linux. However, they are more of a last resort

