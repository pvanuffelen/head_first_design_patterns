# The Command Pattern

Encapsulating (method) Invocation

Main example Home Automation or Bust, Inc.

Also, we visit the Objectvile Diner again to get an introduction to the Command Pattern.
Order Slips who have an `orderUp()` method.
The Waitress, only knows about the `orderUp()` method, the Short-Order Cook has the knowledge to prepare the meals.
The Waitress and the Cook are now decoupled.

Loading the invoker can be described by three steps:

1. The client creates a command object
2. The client does `setCommand()` to store the command object in the invoker
3.  (Later...) the client asks the invoker to execute the command (which results in the action being invoked on the Receiver)

> **The Command Pattern** encapsulates a request as an object, thereby letting you parameterize other object with different requests, queue or log requests and support undoable operations.

In order to *encapsulate a request*, the command pattern packages the actions and the receiver into an object, that is exposed to only one method, `execute()`.

BRAIN POWER: How does the design of the Command Pattern support decoupling of the invoker of a request and the receiver of the request?

A: By using the ConcreteCommand as a middle-man.

