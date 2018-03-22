---
uti: com.xamarin.workbook
id: acf0776d-6464-4c47-a494-c3e733cf08a8
title: Functions, Very functional indeed
platforms:
- Console
---

# Functions, Very functional indeed

So we’ve learned about variables, types, and elementry decision makings, I think you are now ready for functions!!! yay!. For most, this shouldn’t be too strange as this concept is indeed similar in those in math. But let me just jog back some memories.

Say you need to calculate something like this

3\*(4^4-4\*7) - 8/(7^7-7\*7) = ?

It’s really messy to right and although you think there’s definatly similarities in side the brackets, it’s like impossible to keep track. But you can also do this.

let f(x) = x^x - 7x

and rewrite the above expression as

3f(4) - 8/f(7)

much simply.

Computer functions are essentially very similar. In math, a function defines a set of operations whereby an inputted value, is transformed into an output values. Imagine you have some code that you need to run a lot, say to calculate the area of an triangle. No one is stopping you from merely writing the code out everytime but it’s certainly easier to write it out as a seperate function.

Allow me to demonstrate to you with an example. Since we are dealing with decimals from calculating the area of the triangle, we are using double as our type of choice this time.

```csharp
double FindAreaOfTriangle(double baselength, double height){
    double area = baselength*height/2;
    return area;
    // FYI, this is the same as (return baselength*height/2;) 
}
```

Let me briefly explain what the syntax is and what’s happening in the function above. The first “double” refers to the type of output the function produces. So in this case, the area of a triangle would of a double(decimal) type. Next, “FindAreaOfTriangle” is just the name of the function, so that we use the function later, we can refer to it by its name. Inside the bracket, are the inputs, seperated by decimals. In this function, we have two inputs, baselenght and height, and they are of double values as well. These variables are created when we use the functions, and inside the function we can use the name baselength and height to refer to them similar to how in f(x) = 3x, where x is replaced by what ever is inputed. Inside the code block denoted by the curly brackets, you can run operations pertinant to your function. Notice how there is a return keyword. The variable, or the result of the expression after the return keyword, is, unsurprisingly, returned back as the output. In this case, it’s baselengt times height and divide by 2.

To use this function, it’s actually quite similar to those in math as well.

```csharp
double FindAreaOfTriangle(double baselength, double height){
    return baselength*height/2;
}
FindAreaOfTriangle(3.06, 5.06);
```

As you can see, you simply input the values in, and the operations return a new output based on your input and operations. Your inputs can also be other variables. And those variables’ name does not have to be the same of those defined in your function, but they just have to be of the same type.

```csharp
double FindAreaOfTriangle(double baselength, double height){
    return baselength*height/2;
}
double blength = 3.06;
double hlength = 5.06;
FindAreaOfTriangle(blength, hlength);
```

See exactly the same.

Of course, a function need not to be a purely mathamatical operation, it can be of any other types such as strings or boolean;

```csharp
bool DoIHateLife(int averageIncome, int lifeExpectency, int educationIndicator){
    double qualityOfLife = averageIncome*0.70 + lifeExpectency*0.25 + educationIndicator*0.05;
    return qualityOfLife<50;
}
DoIHateLife(10,50,70);
```

Alternatively, an example pertaining to a string.

```csharp
string Abberviate(string str1, string str2){
    return str1[0] + "." + str2[0]; //remember the indexer, we are bascially just slicing the first character from each string and combining them.
}
Abberviate("Peter","Zhong");
```

Further sometimes a function could define a set of operations that doesn’t nessceary return a value. For example, imagine you have a robot that have a funtion to open a wine bottle, after this operation is compeleted you don’t neccessarly need a returned value. In this case, we use void as the return type.

```csharp
void openWineBottle(string wine)
{
    //Let the robot do its job, this example is only used to illustrate void.
}
```

