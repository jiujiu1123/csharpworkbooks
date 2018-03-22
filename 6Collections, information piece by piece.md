---
uti: com.xamarin.workbook
id: fc7b64cc-44b3-4a4f-9d3f-a26ce45887c8
title: 6Collections
platforms:
- Console
---

# Collections, information piece by piece

After learning about the absolute basics of the C# langauge, I think you are ready to learn about one of the most commonly used aspect of  C#,  its support for collections. I actually believe that C#’s implementation of various collections is actually what I love the most.

To start, let’s again picture a practical situation. Say you are writing a program for Sushi bay. They will send you a bunch of numbers that represent the bill($) for each order. They want you to not only store that on the computer but also able to retrieve it based on the order number. For the purpose of this excise, we don’t deal with the complex user interface and we don’t deal with how we are collecting our data.

For example, Sushi bay has sent over their data to us of the last hour so we can use it as a guide for us :)

10, 78.3, 86.1, 9.09, 37.2, 28,

When the 2nd customer gets the bill, you will need to retrieve the 2nd item, so $78.3. And similarly when the 5th customer gets the bill, you will need to retrieve the 5th item, so $37.2.

Before I get into the details of collections, I want you to think about how you can do this using the knowledge you learned in the previous 5 chapters.

\
Below is probably what you are thinking.

```csharp
double first = 10; // BTW remember the previous chapters, we are using double because there are some decimals
double second = 78.3;
double third = 86.1;
double fouth = 9.09;
double fifth = 37.2;
double sixth = 28;
```

And when Sushi Bay want  the third item, we will simply output the sixth item.

```csharp
third
```

Allow me to reiterate that the above statement, for the purpose of this guide is the same as

```csharp
Console.WriteLine(third)
```

Now I am sure you can at least glimpse at the problem with this. It’s quite hard to write all those items out individually and we don’t even know if tomorrow it will have six orders, maybe it will only have five or have eight. And I want to show you a much more elegent way to do this.

```csharp
double[] orders = {10.33, 112.24, 35.87, 91.98,13.33,45.98};
//This is what is called an Array. As the name suggest, an Array is a collection of items(objects). So in this case a collection of all the prices for the orders. Going from left to right, you can probably recongize the double, but the squre bracket is completely new. Don't worry, this simply represent that the type of the variable orders will be an array of type double. Similarly string[] means the type array of string. Now the curly brackets indicate a collection. Those who are familar with Math should recall that this is indeed representing a set of objects. However, rather than a set in terms of Math, in this case, the objects inside the brackets are ordered. Meaning that the 1st item of orders will always be 10.33. 
//To access a specific item, you need to know its index. However note that the first item has an index of 0, the second item has an index of 1, the third item has an index of 2, etc. This is shown below
orders[0]
//As you can see to access specific item of the array, just write its variable name follwing the squre bracket with the index you want inside.
```

```csharp
//Another example: to access to 5th item, use the index 4
orders[4]
```

As you can see. This simplifies the process so much and there are more neat treat that C# offers to make it even better!!