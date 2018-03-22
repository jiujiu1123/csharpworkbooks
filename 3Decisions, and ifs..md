---
uti: com.xamarin.workbook
id: efe31287-8e93-4268-8ede-b5829c6a5b2d
title: Decisions, and ifs.
platforms:
- Console
---

# Decisions, and ifs.

Once you learn the very basics of programming, you can now really start learning about the essence of introductory coding, the ability to make decisions.

Let me start you with some theoritical usage of decision making. Just getting you familiar with the syntax. Quick reminder, the bool(ean)  type has values that are essentially true or false;

```csharp
bool result = true;
string outcome = "";//This basically means that the text described by the string is just empty, and by the way this is an comment, the // means that what ever after this in the same line will not be run
if(result)
{
    outcome = "success";
}else{
    outcome = "failure";
}
outcome
```

Play around with the code, bascially what ever is inside the if statement, like inside the bracket, must be of boolean value. The curly bracket encapsulate codes so that the computers can essentially identity “blocks” of code inside the if statements or outside it. So this would work fine:

```csharp
int magicNumber = 100;
string outcome = "";//This basically means that the text described by the string is just empty, and by the way this is an comment, the // means that what ever after this in the same line will not be run
if(magicNumber == 100)
{
    outcome = "success";
}else{
    outcome = "failure";
}
outcome
```

You see, you don’t always have to create a new variable to make your decisions, the above code is exactly\* the same as the following.

```csharp
int magicNumber = 100;
bool result = magicNumber == 100;
string outcome = "";
if(result)
{
    outcome = "success";
}else{
    outcome = "failure";
}
outcome
```

Just note that when you are making comparison between variables to see if they equal to each other, you use not just one equal sign as the computer can mistake that for an\* assignment \*instead but rather two equal signs.

Further, you can make even more complex decisions with ifs. Say if you will only have a party when Lisa and Marie comes, you can represent this logic using the code below.  Notices that AND is actually in the form of the && symbol.

```csharp
bool lisaComing = true;
bool marieComing = false;
bool havingaParty;//by not assigning a value, we can decide on its value later.
if(lisaComing &&marieComing)
{
    havingaParty = true;
}else{
    havingaParty = false;
}
//Some of you may notice that the above expressions is actually exactly the same as 
havingaParty = lisaComing && marieComing;
//This is becuase that what ever's inside the if statement actually is a bool(ean) which is the same type as havingaParty
havingaParty
```

But if you want to represent the logic of having a party when either Rob OR Indigo came, just use the OR operator, which has the symbol ||.

```csharp
bool lisaComing = true;
bool marieComing = false;
bool havingaParty;//by not assigning a value, we can decide on its value later.
if(lisaComing || marieComing)
{
    havingaParty = true;
}else{
    havingaParty = false;
}
//Some of you may notice that the above expressions is actually exactly the same as 
havingaParty = lisaComing || marieComing;
//This is becuase that what ever's inside the if statement actually is a bool(ean) which is the same type as havingaParty
havingaParty
```

Of course, these examples are very simple and once you started to learn more about functions and custom classess, you can do much more with just assigning the value of variables. But I think it’s important for you to understand like some of the basic structure of programming first before you are able to design slightly more complex softwares.