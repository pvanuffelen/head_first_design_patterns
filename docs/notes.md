# Head First Design Patterns Second Edition

The document you're looking at right now holds all the notes I took while working through the book.
This can be a summary of the chapter, exercises etc.

## 0. OO Basics

Before starting the book (or actually half-way chapter 1) I learned about the Object-Oriented (OO) basics in Java.
[This](https://stackify.com/oops-concepts-in-java/) article, about OO concepts in Java, discusses the four concepts that are assumed common knowledge in the book.
These four concepts are: abstraction, encapsulation, polymorphism and inheritance.
In the section below, I describe these concepts using my own words.

### Abstraction

Abstraction (in Java) is the act of using classes, objects and methods to do all the 'heavy-lifting' for you.
You use these objects etc. in your code.
Instead of having to understand all the code, you only need to know how to use the objects.
Much like you don't need to know exactly how an engine works, in order to drive a car.

> In Java, there are two ways implementing abstraction.
> Through __abstract classes__ and through __interfaces__.

An abstract class, is a class that cannot be instanced, but only be extended on by subclasses.
The abstract class can have both __abstract methods__ as __non-abstract methods__.
An abstract method does not have a body and must be implemented by any subclass.
A non-abstract method has a body and can directly be called by the subclass.

An interface is a collection of methods, which define a behavior (e.g. flyBehavior).
A class can implement multiple interfaces and must implement all the methods of the interface.

### Encapsulation

In Java, there are three access levels:

1. __public__: everyone can see and use this
2. __private__: only the class/object itself can use
3. __protected__: class and child classes can use

### Inheritance

Classes can inherit/extend on existing classes.
Allows usability of code.

## Polymorphism

Where a subclass can inherit from multiple parent-classes and can override or overload methods from these parent-classes.


## 1. Intro to Design Patterns

In this chapter the **duck simulator** is used to introduce you to the first design pattern.
This design pattern in the Strategic Design Pattern. But why would you even want to use design patterns in the first place?

- You spend way more time maintaining the code than writing the code
- Scalability
- ...

In this chapter you are asked to implement the `fly()` method to the `Duck` class (Parent Class).
However, changing this in the Parent Class, also makes the rubber ducks fly around.
So instead of changing the Parent Class you learn the first two Design Principles.

> __Design Principle__
>
> Identify the aspects of your application that vary and separate them from what stays the same (encapsulate).

and

> __Design Principle__
>
> Program to an interface, not an implementation

So instead of implementing the `fly()` method in the Parent Class, we learn to implement behaviors (interface).
Each type of duck must implement the `FlyBehavior` interface.

> In java, you can create interfaces.
> In python this is not really a thing.
> You can make your class behave as such by using the `ABCMeta` and `@abstractclass` packages
> For an example look in the chapter 1 folder

Each duck now HAS-A `FlyBehavior` which delegates the flying of the duck.

When you put to Classes together like this, you're using **composition** instead of *inheriting*.
The ducks now get their behavior by being *composed* with the right behavior object/interface.

This is the basis of the third Design Principle

> __Design Principle__
>
> Favor Composition over inheritance

### Takeaways

- If you want to communicate (efficiently) with other designers, design patterns give you a __shared vocabulary__
- Identify the aspects of your code that (can) vary and encapsulate them
- Program to interfaces not to implementations.
- I've learned about the Strategic Pattern (implement a 'behavior')
- Favor composition over inheritance

*The Strategy Pattern* defines a family of behaviors/algorithms, encapsulates them and makes the interchangeable.
Strategy lets the algorithm vary (independently) from the client (duck) that uses it.

## 2. The Observer Pattern

The Observer Patterns defines a one-to-many relationship between objects.
In this pattern, Observers listen to a Subject, the latter published new information regularly.

In the first implementation we used the _push_ strategy.
This way, the Subject doesn't need to know anything about the Observer, just that it implements the `Observer()` interface (and thus the `update()` method).
This is an example of loose-coupling, which allows the Subject to _push_ notifications to all the Observers when values have changed.
The Subject doesn't need to know anything about the other objects (Observers).

### _push_ vs _pull_

We can also make the Observers _pull_ the information they need.
This makes it easier to add measurements to the `WeatherStation` class and the Display classes do NOT have to receive the measurements they're not interested in.
Otherwise, we would have to refactor all the `update()` methods of the Displays.

When implementing the push strategy, we use Getters to receive all the measurements.
So we created Getters in the WeatherData class.
We can remove all the input parameters/measurements from the `update()` method.
And make all the displays 'get' their own desired parameters when using `update()`
The `notify_obersevers()` method now also no longer needs any input measurements and just notifies (loops over) the Observers, so they can execute their own update method.

> __Design Principle__
>
> Strive for loosely coupled designs between objects that interact.

### Design Principle Challenge

*Identify the aspects of your application that vary and separate them from what stays the same.*

The aspects that vary in this example are the amount of Observers and the measurements of the Weather Station (Subject).
With this Design Pattern, you can vary all of these without much effort.
OG ANSWER: The Observer Pattern separates the Subject and the Observers.
This loose-coupling allows for many different types Observers to listen to the Subject, without the Subject changing.

*Program to an Interface, not an implementation*

Both the Subject and the Observers use an interface.
The Subject uses it to keep track of the objects implementing the Observer interface and the Observers use it to register and get notified.
OG ANSWER: The Observers in this pattern implement the Observer interface.
...

*Favor composition over inheritance*

The Observer Pattern uses composition to compose any number of Observers with their Subject.
These relationships aren't set up by some kind of inheritance hierarchy
OG ANSWER:The Observer Pattern favors composition over inheritance since it separates the Subject and Observers from each-other.

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

## 4. The Factory Pattern

In python we do not use the `new` operator.
You can just instance an object (e.g. `Foo()` instead of `new Foo()`).

Brain Power page 111:

- **Q:** How might you take all the parts of your application that instantiate concrete classes and separate or encapsulate them from the rest of you application?
- **A:** We put the instantiation in the main file or create a separate class where all the instantiation takes place.
This way we have all concrete classes in one place.

Think about the `if ifelse else` creation problem in the `orderPizza()` method.

A factory deals with the object creation.
Think about the creation problem (all the `if-else` statements) of the `orderPizza()` method.
The creation part was taken out of the method and moved to the `SimplePizzaFactory`.
Hereby taking what we expect to change and encapsulating it.

Brian Power page 116:

- **Q:**    We know that object composition allows us to change behavior dynamically at runtime (among other things) because we can swap in an out implementations.
            How might we be able to use that in PizzaStore?
            What factory implementations might we be able to swap in and out?
- **My A:** ...
- **A:** We don't know about you, be we think about New York, Chicago ..... --> Apparently there are different types of pizza in the US.

Simple Factory =/= The Factory Pattern.

>A *factory method* handles object creation and encapsulates it.
It does so by letting a subclass handle the creation.
The code that uses the object (superclass) is called the client.
Using a factory method, the client code is decoupled from the object creation of the subclass (client doesn't know what type of object is created!).
