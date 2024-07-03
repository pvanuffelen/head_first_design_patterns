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

In the main example of this chapter, vendor can program to the `Command` interface, inorder to assign actions to a button.
The remote only knows to use the `execute()` method, which is enough (so it is decoupled from the actual implementation).

## Queuing Requests

The Command Pattern can be used to handle queuing requests.
Units of work/computation are packaged as commands.
These are added to the queue and executed by (a) thread(s). 
This way, the job queue class is totally decoupled from the class doing the computations.

BRAIN POWER: 
How might a web server make use of such a queue? 
What other applications can you think of?

A: 
A web server might use such a queue to handle all the queries/requests.
The other application that I can think of is a database.
It uses a queue to handle queries.

## Logging Requests

In order for the Command Pattern to support this, we need two more methods: `store()` and `load()`.

As we execute commands, we store a history of them on  disk.
When a crash occurs, we reload the command objects and invoke their `execute()` methods in batch and in order.

This type of logging doesn't make sense for remote control, but for applications that perform actions on large data structures.
E.g. spreadsheets application.
We do not want to store a copy of the data everytime a change occurs.

In advanced applications, these techniques are applied to sets of operations in a transactional manner, so that all of the operations complete or none of them do.

