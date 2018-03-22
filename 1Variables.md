---
uti: com.xamarin.workbook
id: 86b43db3-9e64-4205-a9a1-a28c72b9c1e7
title: Variables
platforms:
- Console
---

# Variables

So you’ve decided to learn programming.  You should first understand an important concepts known as a **_variable_**. A variable is basically a place for computer to store a value. For example, imagine your friend told you a magic number, a variable is the sticky notes where you write the number down.

```csharp
int magicNumber = 1000;
```

As you can see here, we are creating a new variable, with a name that we’ve assigned to it called “MagicNumber”. The equal sign here is actually known as an assignment sign as we assign the value of 1000 to this **_variable_**. This is practically the same as writing the number 1000 on a sticky notes named magicNumber.

A few things that I should explain at this stage. The “int” in front of the variable named magicNumber is actually the type of the variable. In this case, int refers to Intergers, or whole numbers. I will explain this concept a bit further in the next chapter.

You may also notice the simi-colon on the end of this line. This basically signals the computer that a line has stoped so they can read the next line.

You may start to wonder why is it called an variable? If you’ve studied high school science before, you probably know that variable is a value that’s can be changed.

For example:

```csharp
magicNumber = 99;
```

As you can see here, we’ve changed the value of the variable magicNumber to 99. As we’ve already created this variable, we don’t need to state the type of the variable again as the computer already knows. This means that you don’t need the int before the name of the variable anymore.

We can use the value of this variable in different programming senario. For example, we could create a new variables that it 100 times the value of the magicNumber;

```csharp
int newVariable = magicNumber * 100;
```

Click run and the program will show you the new value of this new variable. So far so simple. Now we move on to types.