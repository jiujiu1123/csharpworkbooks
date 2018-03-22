---
uti: com.xamarin.workbook
id: 31df215e-f114-43e1-90ed-749d45c270b0
title: Classes, intro to object
platforms:
- Console
---

# Classes, intro to object

Let’s go back to the type chapter, we can see that different variables have different types. However, in c# you are not limited to the types that the system provides you with, in fact, you have the ability to create your own type, which we call a class.

Before we start, let me just clarify something. An variable is in fact an object, which can have types such as string, int, bool. I will be using object a lot in this chapter, and I hope you will not be confused by it.

So what exactly is an object? Well, practically everything, but allow me to be more specific. Imagine you have a car, there are any properties of a car. For example, what’s the model of the car, how many engines it may have, or its price on the market.

In programming, we aim to model this by creating a custom type, which as I mentioned earlier, is known as a class. When we are creating a class, we are in fact essentially creating a blueprint of an object. The class defines what the data collected in this class mean but not the data themselves. For example, your car and your friends car all have properties that makeup a car. They all have a model, they all have engines, and they all have a price. (ofc this is keeping things more generic).

```csharp
class Car{
    public string Model{get; set;}
    public int EngineNumber{get; set;}
    public double Price{get; set;}
    private double _cost; 

    public Car()
    {
        _cost = 0;
    }
}
Car mycar = new Car();
mycar.Model = "Lamborghini Gallardo";
mycar.EngineNumber = 1;
mycar.Price = 198000.00;//The data is faked lol.
//mycar._cost = 29900.00; //This will not work, as _cost is private.
mycar
```

I understand what you must feel at this stage. Indeed, many new things that I should probably explain.

First, Car is the name of the class, which is essentially a blueprint. Moving down, Model, EngineNumber and Price are in fact *class* variables, they are very similar to the variables that we talked about earlier, but you need an access modifier to make it avaliable outside. Allow me to clarify, as you can see we are accessing those properties(variables) outside of the class, so that we need to make the properties public to allow access. In contrast, \_cost is a private *field*. To keep it to the most simple cases, if a variable in the class is accessible from the outside, make it a property with the {get; set;}. However, if the variable will only be used with in the class itself, you can just make it a private field without the {get;set;}. I understand that this topic can be very difficult to grapse and trust me it took a long time for me to truly understand the specific mechanics behind the operations of the code. I have added a few links that can help you better understand:

https://medium.com/omarelgabrys-blog/properties-vs-fields-in-c-6cec86c59dc9

https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/using-properties

The function inside, public Car(), may first seem extremely strange to you. In the previous chapter, we talked about how function has a return type, but this one apprantly doesn’t. This is because the return type for this function is actually not explicitly stated but implicit in the class design, as the return type is actually just the type of the class(car). When you look down to the line

Car mycar = new Car();

You can see that we are creating a new car object. The double bracket looks a lot like a function call. Indeed, this is actually calling the function public Car(), and the returned value is assigned to the mycar variable. This function is known as the constructor as it creates the object. \
\
To access and modify the properties of this mycar object simply use the dot syntax like this:

```csharp
mycar.EngineNumber
```

Using this syntax, you can both access and modify the properties of an object just like variables.

Further, a class can contain many functions that can be called from the outside. For example, in this car class, we can have a function upgrade that increase the number of engines in the car.

```csharp
class Car{
    public string Model{get; set;}
    public int EngineNumber{get; set;}
    public double Price{get; set;}
    private double _cost; 

    public Car()
    {
        _cost = 0;
    }

    public void Upgrade(int howmuch)
    {
        EngineNumber = EngineNumber + howmuch;
    }
}
Car mycar = new Car();
mycar.Upgrade(3);
mycar.EngineNumber
```

Further, you can modify the constructor function to take in more input, so that when you create the object you can use these inputs to fill in more information. Like this:

```csharp
class Car{
    public string Model{get; set;}
    public int EngineNumber{get; set;}
    public double Price{get; set;}
    private double _cost; 

    public Car(string model, double cost, double profitMargin)
    {
       Model = model;
       _cost = cost;
       Price = _cost + profitMargin;
    }

    public void Upgrade(int howmuch)
    {
        EngineNumber = EngineNumber + howmuch;
    }
}
Car mycar = new Car("Telsa S5",12312.00, 1229.01);
mycar.Price
```

With these methods making more sense, I think you are ready for static methods and variables. Let me first demonstrate using an example and I will explain.

```csharp
class Car{
    public static string Classification{get;set;} = "Motor Vehical";
    public static bool IsCorrectClassification(string classfies)
    {
        return classfies == Classification;
    }
}
Car.IsCorrectClassification("Air Transportation");
```

As you can see, for static variables and functions, you don’t need to create a new object of that class, the class itself becomes similar to an object with its own functions and variables that you can access.

These functions can be very important and useful in everyday programming. For example, a lot of functions involving math, are in fact static functions.

```csharp
Math.Abs(-92393);
```

This is treating the class Math as an object by itself and calls the static Abs function within the math class.

```csharp
Console.WriteLine("Hello World");
```

This function is a system provided function to print texts as a form of output. The Concole is a class with an writeline static function.

Static fuctions are extremely useful when the function describes an operation that applies to a whole class rather than a specific object. Back to the car object example, if the function concerns a specific car itself, then normal methods rather than static methods should be used. However, if the function concerns all of the class, such as classfications then static methods are preferable.

I should probably make a note here about the Console.WriteLine function here. What this Writeline function does is that it output the value of whatever’s inside the bracket. For example, in the above case, it was the string “Hello World”. You should be aware that you can actually put a variable inside the bracket as well and it will output the value of the variable.

```csharp
int a = 3;
Console.WriteLine(a);
//Because a has the value of 3 this is exactly the same as writing 
Console.WriteLine(3);
```

For the first few chapters of this guide, whenever I wanted to you the value of a variable, I simply placed it in the code section like this.

```csharp
a
```

And you can see that the result is almost identical to when you are using Console.WriteLine. This is because in the background, the computing are actually doing this step for you. It’s just something to be aware of when you start programming in the real world as the nice helpful Xamarin Workbook will not be avalaible.