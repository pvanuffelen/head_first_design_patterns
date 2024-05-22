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

