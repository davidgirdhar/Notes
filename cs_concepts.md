### Object Pooling
Object pooling is a software design pattern used to optimize the performance and resource usage of an application, particularly in scenarios where creating and destroying objects frequently can be resource-intensive and lead to inefficiencies.
In object-oriented programming, objects are instances of classes, and creating objects involves allocating memory and performing initialization. Destroying objects involves releasing memory and performing cleanup. However, this process can be time-consuming and may lead to memory fragmentation and increased overhead, especially in scenarios where objects are frequently created and destroyed.
Object pooling addresses these challenges by reusing and recycling objects instead of constantly creating and destroying them.

1. Object Creation and Initialization: Instead of creating objects on-demand, a pool of pre-allocated objects is created during application initialization. These objects are typically in a "ready" or "idle" state, waiting to be used.
2. Object Usage: When an object is needed, the application requests an object from the pool. If an idle object is available, it is retrieved from the pool. If no idle objects are available, the pool can create additional objects up to a certain limit (the pool size).
3. Object Recycling: Once an object is no longer needed, it is returned to the pool. The object's state is reset, and it is marked as "idle" so that it can be reused in the future.
