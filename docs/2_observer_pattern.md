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

