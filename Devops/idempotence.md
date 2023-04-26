## Idempotence

Idempotence is any function that can be executed several times without changing the final result beyond its first iteration. Idempotence is a technical word, used in mathematics and computer science, that classifies a function’s behavior.
As a function, it can be expressed as:

```
f(f(x)) = f(x)
```
That means that an operation can be performed on x to return y. Then, if that same function were performed on y, the result would still equal y.

A basic example of idempotence in mathematics is absolute function ```abs()```.So let suppose you value -10 if you perform abs() function on it, it will return 10 and if you again perfrom it,it will 10 only.

Now it is very helful in development also.let take a real life example.
Think about the “Pay now” button the last time you bought something online. Now, let’s say you’re ready to purchase your shopping cart items, so you press “Pay now”. What happens if you press it multiple times? Will your credit card be charged for each time you hit the button?

This is where idempotence comes in: if the function in the “Pay now” button is idempotent, the user can tap the “Pay Now” button many times—yet their card is charged only once and they only make one purchase on their cart’s contents. If, alternatively, the function of the “Pay Now” button weren’t idempotent and the user anxiously pressed the key several times, the user would end up with multiple charges on and receive several of the same items in their mailbox.

So, idempotence is an important design for many functions in technology.


 ### Idempotent HTTP functions

In the land of HTTP methods, the GET, DELETE, and PUT functions are idempotent.

The GET method retrieves information from an HTTP endpoint. Whatever information GET asks for will be the same information again and again. This behavior is illustrated by hitting refresh on an internet browser. The browser pings an IP address and gets information. If GET weren’t idempotent, perhaps it would stack more and more pages on top of each other, adding each refreshed page in the browser’s cache. DELETE has similar behavior.

PUT is also an idempotent function—but POST is not. In HTTP, PUT will define a value, and continue to define the value as whatever is stated.

POST works differently. POST can send the same value repeatedly, but it adds an element to a collection. POST could repeatedly send the same Twitter status 10 times per hour, and all the followers will receive 10 status updates all saying the same thing. The PUT function just puts the status out there once.

