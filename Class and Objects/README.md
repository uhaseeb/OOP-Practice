# Introduction
Class and Objects are the fundamental part in Object Oriented Programming(OOP).

## Class
A class is a collection of objects. A class contains the blueprints or the
prototype from which the objects are being created.
It is a logical entity that contains some attributes and methods.
We are going to illustrate an example to illustrate the need of class,

Let's consider we have to identify a number of employees on the base of their 
different attributes like name, experience, age, designation etc. If a list
of attributes is used the first element would be name second would be experience
and so on let's suppose we are having 100 employees that have different 
attributes then how can we identify which element belongs to which employee and
if we have to add more attributes to employee, how could we do that?
That specific problem raise the need of classes in programming.

A class can have following characterstics:
- Classes are created by keyword class.
- Attributes are the variables that belong to a class.
- Attributes are always public and can be accessed using the dot (.) operator.
  Eg.: Myclass.Myattribute

### Access Modifiers
There are basically three types of access modifiers in OOP classes.
- Public: Public access modifiers are available throughout the project
  we can access then anywhere. Default value of access modifiers of variables and
  methods is public.
- Private: Private access modifiers are available only within the class
  you cannot access then outside the class. You will get an Attribute error
  if you call them outside. Private access modifiers are represented by 
  __ before the name
- Protected: Protected access modifiers are available only in the derived classes 
  of the superclass. We will discuss Inheritance concept later on
  to have a clear understanding of protected access modifiers. 

## Objects
The object is an entity that has a state and behavior associated with it.
It may be any real-world object like a mouse, keyboard, chair, table, pen, etc.
Integers, strings, floating-point numbers, even arrays, and dictionaries,
are all objects. More specifically, any single integer or any single string
is an object. The number 12 is an object, the string “Hello, world” is an object,
a list is an object that can hold other objects, and so on. 

Let's consider an example of object, with the reference to the question raised 
in class section. We can solve the problem by creating different objects
of class employee in a way that each object represents an employee with different
attributes.

An object consist of:
- State: It is represented by the attributes of an object. 
  It also reflects the properties of an object. 
  For example age, designation, experience. 
- Behavior: It is represented by the methods of an object.
  It also reflects the response of an object to other objects. For example
  display_employee_info, calculate_employee_salary etc.
- Identity: It gives a unique name to an object and enables one object 
  to interact with other objects. For example name of an employee.

### The self
The class methods have an extra argument self in the class defination.
We don't need to assign a value to it, python will do it for you.
If a method have no arguments then we still have value of self.

### __init__ method
It is a default constructor in python that will be called automatically when we
create an object of class. It is called everytime you create a new object
of class. Basically we assign the value of attributes to specific instance
in the __init__ method.