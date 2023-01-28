## What is a message broker? 

A message broker is a piece of software, which enables services and applications to communicate with each other using messages. The message structure is formally defined and independent from the services that send them.
This allows applications to share information with one another, even if they’re written in different programming languages!

Now Let get to know some of the basic concepts of Message Broker


```Producer``` 
the application responsible for sending messages. It’s connected with the message broker. In publish/subscribe pattern (we’ll move on to that) they are called publishers. 

```Consumer```
the endpoint that consumes messages waiting in the message broker. In publish/subscribe pattern they are called subscribers. 

```Queue/topic```
a folder in a filesystem. Message broker uses them to store messages.

### Two of the most common distribution patterns:

```Point-to-point messaging```
In this pattern, there is one-to-one relation set between the sender and the receiver of the message. Each message is sent and consumed only once. We can use this pattern for example, when some action needs to be performed only once.

Now you probably think: “Ok, so what’s the difference between this and some REST API?”. The answer is simple. The message broker guarantees that message will not be lost in case of failure of the consumer. It’s stored safely in the message broker queue. 

```Publish/subscribe```

This pattern is slightly different from the previous one. Here, the sender of the message doesn’t know anything about receivers. The message is being sent to the topic. After that, it’s distributed among all endpoints subscribed to that topic. It can be useful e.g. for implementing notifications mechanism or distributing independent tasks. This solution can also lead to implementing an event-driven architecture-based system, where applications have fewer dependencies between each other.

In this pattern, the components are loosely coupled and transmit events to one another. These events would be messages sent to the message broker.
