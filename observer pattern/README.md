### Observer is a behavioral design pattern that allows some objects to notify other objects about changes in their state.
#### Observer design pattern lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.

The object that has some interesting state is often called subject, but since it’s also going to notify other objects about the changes to its state, we’ll call it publisher. All other objects that want to track changes to the publisher’s state are called subscribers.
The Observer pattern suggests that you add a subscription mechanism to the publisher class so individual objects can subscribe to or unsubscribe from a stream of events coming from that publisher.
