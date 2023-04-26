## What is Pub/Sub Messaging?

Pub/sub is shorthand for publish/subscribe messaging, an asynchronous communication method in which messages are exchanged between applications without knowing the identity of the sender or recipient.

Now there are few core concepts which atleast one know 

```Topic``` An intermediary channel that maintains a list of subscribers to relay messages to that are received from publishers

```Message``` Serialized messages sent to a topic by a publisher which has no knowledge of the subscribers

```Publisher``` The application that publishes a message to a topic

```Subscriber``` An application that registers itself with the desired topic in order to receive the appropriate messages

#### Faye

Faye is an open source system based on pub/sub messaging.It is much more straightforward than standard JavaScript and it was created specifically for Node.js and Ruby servers. It’s often used for online instant messaging which is a use case for pub/sub that most people experience on a daily basis. The code below shows you how to start a server, create a client, and send messages using Faye.

```Javascript
var http = require('http'),
faye = require('faye');

var server = http.createServer(),
bayeux = new faye.NodeAdapter({mount: '/'});

bayeux.attach(server);
server.listen(8000);

var client = new Faye.Client('http://localhost:8000/');

client.subscribe('/messages', function(message) {
      alert('Got a message: ' + message.text);
});

client.publish('/messages', {
      text: 'Hello world'
});
```
