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

