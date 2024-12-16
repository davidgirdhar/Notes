import time
import uuid
import threading

class Message:
    def __init__(self, content, delay=0, ttl=60):
        self.id = str(uuid.uuid4())
        self.content = content
        self.timestamp = time.time() + delay
        self.ttl = ttl
        self.visible = True

class MessageQueue:
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()
    
    def enqueue(self, content, delay=0, ttl=60):
        """Add a message to the queue with optional delay and TTL."""
        with self.lock:
            message = Message(content, delay, ttl)
            self.queue.append(message)
            print(f"Message {message.id} enqueued: {message.content}")
    
    def dequeue(self, visibility_timeout=10):
        """Retrieve the first visible message and hide it temporarily."""
        with self.lock:
            current_time = time.time()
            for message in self.queue:
                if message.visible and current_time >= message.timestamp:
                    message.visible = False
                    message.timestamp = current_time + visibility_timeout
                    print(f"Message {message.id} dequeued: {message.content}")
                    return message
            print("No messages available to dequeue.")
            return None
    
    def delete(self, message_id):
        """Delete a processed message."""
        with self.lock:
            self.queue = [msg for msg in self.queue if msg.id != message_id]
            print(f"Message {message_id} deleted.")
    
    def clean_expired(self):
        """Remove expired messages based on their TTL."""
        with self.lock:
            current_time = time.time()
            self.queue = [msg for msg in self.queue if current_time - (msg.timestamp - msg.ttl) <= msg.ttl]
            print("Expired messages cleaned.")

# example
if __name__ == "__main__":
    mq = MessageQueue()

    mq.enqueue("Message 1", delay=2)
    mq.enqueue("Message 2", ttl=5)

    time.sleep(3)

    msg = mq.dequeue()
    if msg:
        mq.delete(msg.id)
    
    mq.clean_expired()
