# Head First Design Patterns 2nd edition

I created this repo to help me work through the book Head First Design Patterns 2nd Edition.
I will use this README as a notebook/logbook type of thing.
For each chapter I will make a section where I list stuff that I found interesting, wanted to remember or just was funny.

## 0. OO Basics

[This](https://stackify.com/oops-concepts-in-java/) article, about OOP concepts in Java, discusses the four concepts that are assumed common knowledge in the book.
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

In this chapter, I was introduced to my first design pattern (strategic) and why you want to use design patterns.

- You spend way more time in the code after the application is live
- Scalability

The main example of this chapter is about a duck simulator.
The designer is asked to make ducks fly and implements this in the `Duck` class.
However, this also made all the rubber ducks fly around.
To combat this, he created 'Duck Behavior' interfaces (e.g. quackBehaviour).

Each duck class should implement these behaviours.
This allows for more flexibility and gives you an overview of what each class can do.
This Design Pattern in called the **Strategic Design Pattern**.

> In java, you can create interfaces.
> In python this is not really a thing.
> You can make your class behave as such by using the `ABCMeta` and `@abstractclass` packages

You can find the code of the duck simulator in the `1_intro_to_design_patterns` folder.

### Takeaways

- If you want to communicate (efficiently) with other designers, design patterns give you a __shared vocabulary__
-
- I've learned about the Strategic Pattern (implement a 'behavior')

## 2. The Observer Pattern

The Observer Patterns defines a one-to-many relationship between objects.
In this pattern, Observers listen to a Subject, the latter published new information regularly.

In the first implementation we used the _push_ strategy.
This way, the Subject doesn't need to know anything about the Observer, just that it implements the `Observer()` interface (and thus the `update()` method).
This is an example of loose-coupling, which allows the Subject to _push_ notifications to all the Observers when values have changed.
The Subject doens't need to know anything about the other objects (Observers).

### _push_ vs _pull_

We can also make the Observers _pull_ the information they need.
This makes it easier to add measurements to the `WeatherStation` class and the Display classes do NOT have to receive the measurements they're not interested in.
Otherwise we would have to refactor all the `update()` methods of the Displays.

When implementing the push strategy, we use Getters to receive all the measurements.
So we created Getters in the WeatherData class.
We can remove all the input parameters/measurements from the `update()` method.
And make all the displays 'get' their own desired parameters when using `update()`
The `notify_obersevers()` method now also no longer needs any input measurements and just notifies (loops over) the Observers, so they can execute their own update method.

### Design Principle Challenge

*Identify the aspects of your application that vary and separate them from what stays the same.*

The aspects that vary in this example are the amount of Obersers and the measurements of the Weather Station (Subject).
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
