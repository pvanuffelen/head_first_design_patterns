# Chapter 5: The Singleton Pattern

Of many object, we only need one instantiation (drivers, caches, pools, etc.).
For that we can use the Singleton Pattern, since it consists of only one instance (per class).
Watch out, Singleton code is hard to get right!

Singleton is perfect for objects that hold settings and which you want your entire application to use these global settings/resourches.

Singleton objects have a *private* constructor (in Java).
You don't instance a Singleton object, you use its `getInstance()` method.

Main example is Choc-O-Holic's ChocolateBoiler.

BRAIN POWER:
How might things go wrong if more than one instance of `CholoclateBoiler` is created in an application?

A:
One might be empty, another might be full and will try of fill up a physically full tank.
The same holds for boiling etc.

> **The Singleton Pattern** ensures a class has only one instance, and provides a global point of access to it.

- We're taking a clas and letting it anage a single instance of itself.
We're also preventing any other class from creating a new instance on its own.
To get an instance, you've got to go through the class itself.
- We're also providing a global access point to the instance: whenever you need an instance, just query the class and it will hand you back the single instance.
As you've seen, we can implement this so that the Singleton is created in a lazy manner, which is especially important for resource-intensive objects.

The `getInstance()` method is static, which means it's a clas method, so you can conveniently access this method from anywhere in your code using `Singleton.getInstance()`.
That's just as easy as accessing a global variable, but we get benefits like lazy instantiation from Singleton.

A problem arises when multithreading.
Apparently you then execute the code twice, with each line being executed, which each thread taking turns.
This gives a problem when executing the `getInstance()` method.
So the method needs to be `synchronized`, which is a keyword in Java.

## Summary

Singletons are classes which ensure there is only one instance of this class at the time.
Singletons are a great way of creating global access points in your code that you want to make sure only one instance is present in the code.
Stuff like settings, caches, etc.

You can create a Singleton using the old-fashioned way (without a Java enum) by creating a private constructor, the `getInstance()` method.
However, this way you can run into problems when using multithreading.
This can also be solved in four ways:

1. Use a Java enum
2. Add the `synchronize` keyword to the class, if you do NOT use the `getInstance()` often. Since Adding this keyword adds some overhead.
3. Use eager instantiation, implement this if the creation of your Singleton class is inexpensive.
4. Double-checked locking, reduces the overhead, but can be an overkill, and you have to ensure you are running at least Java 5. 
