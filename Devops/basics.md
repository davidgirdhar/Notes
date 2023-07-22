
###  Load Balancer
    Now firsly let's understand the term load balancing, so it basically -> efficiently distributing incoming network traffic across a group of backend servers, also known as a server farm or server pool.
    So the functions performed by load balancer is that it Distributes client requests or network load efficiently across multiple servers, Ensures high availability and reliability by sending requests only to servers that are online, Provides the flexibility to add or subtract servers as demand dictates

#### load balancing algorithm
* __Round Robin__ — Requests are distributed across the group of servers sequentially.
* **Least Connections** — A new request is sent to the server with the fewest current connections to clients. The relative computing capacity of each server is factored into determining which one has the least connections.
* **IP Hash** — The IP address of the client is used to determine which server receives the request.
