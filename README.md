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

The Observer Patterns works similar to newspaper subscriptions.
A subscriber is called an OBSERVER and the publisher is the SUBJECT.

Some quotes form chapter 2:

- "If you understand newspaper subscriptions, you pretty much understand the Observer Pattern, only we call the publisher the SUBJECT and the subscribers the OBSERVERS.
- "__The Observer Pattern__ defines a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically."
- Loose coupling is not knowing that much about another class, which makes you less dependent on that class (minimize interdependency).
- "Design Principle: Strive for loosely coupled designs between objects that interact."
- 

### Takeaways

- Observer pattern works because all OBSERVERS implement the `Observer` interface, which makes them implement the `update()` method. 
- Loose coupling: refers to not knowing everything about another object (minimize interdependency).