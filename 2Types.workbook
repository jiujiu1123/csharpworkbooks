---
uti: com.xamarin.workbook
id: b61b25ed-adad-4b18-9b20-b72b40bc73b1
title: Types
platforms:
- Console
---

# Types

### Int(Interger)

Now that’s reviewed the example from the last chapter.

```csharp
int magicNumber = 100;
```

I’ve explained earlier that “int”(Interger) is actually the type of the variable magicNumber. But what does this really mean?

You can think about type as the classification of the value of a variable. To be a specific type, the value must conform to a specific guideline. For example, an interger, by definition, can’t have non-zero decimal places.

```csharp
//magicNumber = 99.99;
```

Ops, when you run this example, you can see that it doesn’t work as the computer knows that 99.99 is not an interger. To fix it, try to input an interger. (You must edit the line above)

Note: There is an restriction on very big or very small numbers by C#’s interger type, between –2,147,483,648 and 2,147,483,647. Normally, these restrictions are not very concerning.

### Double

You might wonder, if an interger type variable can’t store decimal values, how can I store it in an variable?

```csharp
double magicDecimal = 99.99;
```

As you can see, this runs flawlessly without any annoying errors from the computer as we’ve changed the type to double. This basically means that it’s able to store decimals, however, including those with 0 decimal places. For example, this will run without an issue.

```csharp
magicDecimal = 0;
```

There is another type that can be used to store decimals called a float.

```csharp
float anotherMagicDecimal = 3.4f;
```

The f on the end before the semicolon distinuish the value from a double. Right now the differences are somewhat advanced to understand but I will explain them later.

### String(Text, essentially)

Imagine you are texting with your mates, and you want to store whatever you said on an variable. Obviously you can’t store that as a number, it simply doesn’t allow texts to be inputed as the value.

This is why a new type is used to represemt Texts, which is actually just a bunch of characters stuck together in a particular order. However, we nerds want to sound fancy so rather than just calling this a text, we call it a string. Like this:

```csharp
string coolText = "Can you pick me up at like 6?";
```

As you can see, to create a string variable, we must put our texts inside quotation marks, but the quotation marks themselves are not exactly part of the string. (Exactly like your English Essay, painful memory I know)

A single character, is actually known as a char. And you use single quotation marks for it.

```csharp
char character = 'c';
```

To select a particular character from a string, just use the indexer as shown through the example below.

```csharp
string str = "I Hate Life";
char character = str[0];
```

Firstly, the syntax \[] is bascially used for indexing, accessing a specific element from a collection of elements. In this case a string is a collection of characters. The number inside the \[] specify which element to select. But remember in C# and programming at large, the 0th element is the first., the 1st is in fact 2nd, a bit confusing but it should be okay.

There are many other operations of string that can be very interesting. The most common way of manipulating a string is through basic addition.

When you need to combine two strings, you can actually just add them together, although the computer will not treat this as a mathamatical operation but a string operation.

```csharp
string str1 = "I hate";
string str2 = " life";
string str3 = str1+" "+str2;
```

### Bool(ean), just true or false

We’ve all seen it before. A bunch of 0s and 1s flowing through the computer screens. And by now you are probably feeling fortunate as you don’t have to code this way, not anymore anyways. But those 0s and 1s essentially indicate false and truth, respectively. Don’t worry if this is confusing, an example should clear things out a lot.

```csharp
bool truth = true;
```

As you can see, this variable just stores the value true or false, and in the underlying computer memory, it’s stored as a 1(or a 0 if it’s false, cause 1 is better than 0 :) ). The purpose of boolean type variables will be more clear in the next chapter - Decisions, and ifs.