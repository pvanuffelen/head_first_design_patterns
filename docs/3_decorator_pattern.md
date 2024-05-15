## 3. The Decorator Pattern

The main example of this chapter is StarBuzz Coffee and their beverages.
Trying to let them all inherit form the `Beverage` Class led to "class explosion".
Adding the toppings to the Parent Class also didn't seem to work out great...

A new Design Principle appeared!

> __Design Principle__
>
> Classes should be open for extension, but closed for modification.

We're going to use the Decorator Pattern to construct drink orders.
Decorator objects act as "wrappers".

The decorator object has the same supertype as the object it wraps.
This way we can pass around the decorated object in place of the original (wrapped) object.
The decorator adds its own behaviour before and/or after delegating to the object it decorates to do the rest of the job.

**The Decorator Pattern** attaches additional responsibilities to an object dynamically.
Decorators provide a flexible *alternative* to subclassing for extending functionality.

In the pattern we will use inheritance for *type matching* not to get *behaviour*.

The UML class diagram will contain:

- Component (Beverage), can be used on its own or wrapped by a decorator.
- ConcreteComponent (DarkRoast), dynamically adds behavior to the Components it extends.
- Decorator (CondimentDecorator), implement the same interface or abstract class as the component they are going to decorate.
- ConcreteDecorator (Whip), ...

NOTE: The Factory and Builder Patterns show much better ways of decorating objects.
Those will be discussed later-on in the book.

A *downside* of the Decorator Patterns is that it results in a large number of small classes.
This can be overwhelming.
Example the Java I/O libraries.

