## 4. The Factory Pattern

In python we do not use the `new` operator.
You can just instance an object (e.g. `Foo()` instead of `new Foo()`).

### Simple Factory

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

The Simple Factory uses an object (e.g. `SimplePizzaFactory`) to handle the object creation.

>A *factory method* handles object creation and encapsulates it.
>It does so by letting a subclass handle the creation.
>The code that uses the object (superclass) is called the client.
>Using a factory method, the client code is decoupled from the object creation of the subclass (client doesn't know what type of object is created!).

### The Factory Pattern

I finally got to meet the factory pattern.
It consists out of two parts: *Creator Classes* and *Product Classes*

The Creator Classes consist of an abstract Creator and concrete Creators (`PizzaStore` and `NYPizzaStore`).
Same hierarchy applies to Product Classes, so an abstract Product and concrete Product (`Pizza` and `NYStyleCheesePizza`).

The abstract Creator doesn't know anything about the objects the concrete Creators create by implementing the `factoryMethod()`.
However, the abstract Creator does have methods that perform operations on these objects (e.g. `prepare()`).

The type of concrete Creator determines the concrete Product that is created (by using the factory method).

**The Factory Method Pattern**: defines an interface for creating an object, but lets subclasses decide which class to instantiate.
Factory Method lets a class defer instantiation to subclasses.

### Guru and Student...

Factories allow you to encapsulate the part of the code that handle object creation.
This latter part varies a lot, thus, it is good to separate it from the rest of the code.

> **Design Principle**
>
> Depend upon abstractions.
> Do not depend upon concrete classes.

### Invert Your Thinking

Guidelines:

- No variable should hold a reference to a concrete class (use factories for that).
- No class should derive from a concrete class (derive from an abstraction e.g interface or abstract class).
- No method should override an implemented method of any of its base classes (if you override those, the base class wasn't an abstraction)

These are guidelines!
In principle every program out there violates these (e.g. by instantiating a string).
But with these in the back of our mind we know when we violate them and do that for a good reason.

### Abstract Factories

By creating an abstract factory, an interface was created for factory "family" to adhere to.
The concrete families, who actually create products, are decoupled from this abstract factory.
So by creating a variety of factories, we get a variety of implementations, without the client code changing.
E.g. create the Chicago specific ingredient factory. 
In this example, the `ChicagoPizzaStore` is the client.

**The Abstract Factory Pattern** provides an interface for creating families of related or dependent object without specifying their concrete classes.

Most of the time the methods of the AbstractFactory, are a factory method (e.g `createDough()`, `createCheese()`).

### Abstract Factory vs. Factory Method

Both are good at decoupling applications for specific implementations.
Abstract Factory (AF) does so by object composition and Factory Method (FM), via inheritance. 
AF provides an abstract type for creating family of products, FM makes you extend a class and provide an implementation for a factory method.
AF is useful when you have families of products you need to create and group them.
FM is good at decoupling the client code from the concrete classes you need to instantiate.

Both use factory methods, only in a different way.
AF to purely create the products.
FM also implements these in the abstract creator to use the concrete types the subclasses create.
These subclasses decide what concrete product is instantiated.

