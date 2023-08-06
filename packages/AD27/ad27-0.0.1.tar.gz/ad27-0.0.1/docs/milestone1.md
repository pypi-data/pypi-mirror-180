## Introduction

There are many problems in modern computation that require computing gradients and derivatives of complex functions. From calculating the movement or flow of electricity, motion of an object to and fro like a pendulum, to explaining thermodynamics concepts, solving differential equations is essential for science and engineering. 

In the case of extremely complicated functions such as neural networks, the calculation and storage of these derivatives can be quite complex and cumbersome. The problem grows even worse when taking into account that the input to these functions can be extremely high-dimensional. To this end we introduce AD27, a library for Automatic Differentiation that provides users a simple and intuitive API for the automatic calculation and storage of derivatives.

## Background

**Automatic Differentiation** is a method of computing the derivative of a function using a computer program. 

Unlike symbolic differentiation - which requires manual calculations and exponential runtime - and numerical differentiation - which fails to give an accurate approximation when the error is too small or too large, automatic differentiation can **achieve machine precision** in constant time. 

To evaluate the derivative of a function using automatic differentiation, we decompose complex functional forms into a series of elementary function operations based on the order math is carried out by definition. After the decomposition, any complicated analytical formula of the original function can be represented by a computational graph. The independent variables and the outermost function will be the input and output of this graph. All intermediate variables will form a computational network in between, as is shown in the following example: 

$$f(x) = \pi x^2 + sin(3e^x + 7x) - e^x$$

![Image](./graph_example.png)

In this graphical representation, all dependent variables show up as nodes connected through elementary operations. By zooming in to a single parent-child node structure, we observe that the value of each dependent variable node can be evaluated once the value of all its parent nodes are given. 

To evaluate the derivatives of each dependent variable, we should recall the chain rule: 

$$\frac{\partial f}{\partial x} = \frac{\partial f}{\partial u}\frac{\partial u}{\partial x}$$

Therefore, the derivative of each child node variable with respect to a given direction in the independent variable space can be evaluated given the derivatives of all its parent nodes in that direction, as well as the value of the parent node variables. The series of values of dependent variables form the primal trace of the computational graph. The series of directional derivatives of the dependent variables form the tangent trace of the computational graph.

The actual evaluation of the primal and tangent trace depend on a tool structure - the dual number. A dual number z is written as $$z=a+\epsilon b$$, , where a and b are real numbers while $$\epsilon$$  is a nilpotent number satisfying $$\epsilon^2=0$$ and $$\epsilon \neq 0$$. 

Once we store the value of a dependent variable as a, the real part of the dual number, and the directional derivative of a dependent variable as the b, the dual part of the dual number, the special properties of a dual number structure enables the combined evaluation of the primal trace and the tangent trance of a given parent-child node with dual number operation. 

The forward mode autodiff part of our package is implemented by defining the dual number structure, overloading dual number operations and evaluating node-by-node in the computational graph the dependent variables and their directional derivatives. 

## How to Use AD27

The user can install our package via the preferred installer program (pip):
```bash
>>> pip install ad27
```
Forward and reverse mode automatic differentiation in the AD27 package will be implemented by the user as follows:

Import the Forward and Reverse modules of the AD27 package:
```python
>>>import AD27.Forward as Forward
>>>import AD27.Extension as Extension
```
Initiate a forward autodiff object, which takes a user-defined function object as the argument ($$f: R^m \rightarrow R^n$$):

```python
>>>test_fad = Forward(f) # for forward mode autodiff 
```
To evaluate the Jacobian at a given point. The test_fad.Jacobian method takes one argument, which is a float point number or a numpy array representing a point the 1- or m-dimensional space where the function is defined
```python
>>>test_fad.Jacobian(X) # code is the same for both forward and reverse modes
>>># return the Jacobian matrix of the function func evaluated at point X
```

Evaluate the directional derivative at a given point in a given direction. The test_fad.directional method takes two arguments, one is a float point number or a numpy array representing a point the 1- or m-dimensional space where the function is defined, the other is a vector in the m-dimensional space along which direction the derivative of the function will be evaluated:
```python
>>>test_fad.directional(X, p) # code is the same for both forward and reverse modes
>>># return a n-dimensional vector, each element of the vector is the scalar directional derivative of the corresponding element of the vector function f.
```

## Software Organization
### Directory Structure
```
main   
├── docs
|   |
│   └── milestone1.md
├── requirements.txt
├── .gitignore
├── setup.py /* CI/CD set up  */
|
├── tests
│   ├── __init__.py
│   └── ...
└── ad27
    └── __init__.py
    ├── forward.py
    |     └── DualNumber.py
    |     └── ComputationGraph.py
    |     └── Node.py
    |
    └── extension.py
    └── function_overload.py
          └── BasicOperation.py
├── pyproject.toml
├── LICENSE
├── README.md  
```
### Modules and Functionalities
- function\_overload module that defines the elementary operations and functions for dual numbers. 
- Forward module that contains classes to compute the derivates. It will return a numpy array that represents the Jacobian of the function that was passed to it.
- Extension module that uses forward module to achieve applications.

### Test
- We will use CI to perform tests and the tests will live in the test folder.

### Package distribution
We use PyPI

## Implementation

### Classes we need
We will implement function_overload module first to define operations for dual numbers. This module will include the BasicOperation Class which will contain methods for all basic operations on dual numbers e.g. addition, multiplication, subtraction, etc.
We will implement DualNumber class, Node class, and ComputationGraph class, then Computation class in sequence.
class DualNumber: This is the class for representing the dual numbers in our computation graph.
class Node: This is the class for representing one node, or vertex, in our computation graph (v\_i). It will contain DualNumber objects and will have functions for finding the parent nodes.
class ComputationGraph: This is the class containing each node in our computation graph. It will contain one or more nodes in a tree-like data structure and can be traversed to find the Jacobian for the functions that it represents.
### Core data structures
Within the forward module, we will use a tree structure for storing the nodes. We will use an array to store the operations. Dual numbers will be created in DualNumber class, which stores its real and dual parts as attributes and also has methods for operations.


### Methods and name attributes
- BasicOperation Class in function_overload module

The BasicOperation Class will have attributes of real and dual. The methods includes basic operations for dual numbers such as add, sub, mul, etc. It will also include elementary functions, such as sin, cos, etc.

- DualNumber Class in Forward module

The DualNumber class will have name attributes of real and dual, where the real stores the real part (i.e. function value) of a dual number, and the dual part stores the dual part (i.e., first-order derivative of a function.

- Node Class in Forward module

The Node class will have name attributes of index, parents, operator, dual which store the j index, parental nodes, operator for the parental nodes and the dual number of the node Vj. It will have methods of TrackParents, TrackOperator and ComputeDual to find the parental nodes, the operator for the parental nodes and the dual number of the node.(A variable/operator dynamic list will be used here to push/pop variable/operator when reading in the function expressions. The parents and operator will thus be able to be tracked during the pushing and popping process. Once the parents and operator are known, the dual number of the node could also be evaluated.)

- ComputationGraph Class in Forward module

The ComputationGraph will have the name attributes of graph, which is a tree representing the node connections in automatic differentiation. The ComputationGraph will have methods of add_node for adding node to the computation graph, add_edge for adding edge that connects two nodes and res for returning the dual number of the last node.

### Basic operator overloading template
We will investigate different use scenarios for using the operator method. In the case that we don't want to rule out the reverse mode, we will have two scenarios: one being the operator method takes in two dual numbers; the other being the operatoe method takes in parent nodes. For the first scenario, we will use the dunder method defined in the DualNumber class. For the second scenario, we will covert the name of the parent nodes into types of new variables, and reconstruct a dual number out of these new variables with the operator at the direction of p=[0,0,...1,0,0,...], thus the dual part of the reconstructed dual number will tell us the partial derivative required in the forward pass of the reverse mode automatic differentiation.

### Function overloading to handle cases for f: R^m - > R^n
We will define a multifunction decorator. Inside the multifunction decorator, there will first be an __init__ constructor which creates a multifunction object with a given name and an empty typemap. Secondly, there will be a dunder __call__ method which makes the multifunction object itself callable. Thirdy, there will be register() method which adds a new function to the typemap.

### How to deal with basic operators and elementary functions
#### Method - Basic Operations:
We will import numpy. The basic operations for dual numbers are implemented as follow:

Addition (commutative) (+): real=real1+real2, dual=dual1+dual2

Subtraction (-): real=real1-real2, dual=dual1-dual2

Multiplication (*) (commutative): real=real1*real2, dual=real1*dual2+dual1*real2

Division (/): real=real1/real2, dual=(dual1*real2-real1*dual2)/real2**2

Power (**): real and dual number part can be calculated by performing power(n) times multiplication operation with itself.

Negation (-): real=-real, dual=-dual

#### Method - Elementary Functions: 
Elementary functions are calculated with the formula: real=f(real1), dual=f'(real1)*dual1. For example: sin(dualnumber1)=sin(real1)+cos(real1)*dual1*ε

### Handling higher-level f:
We can implement a Jacobian class that takes a Jacobian and interpret it as a series of f.

## Licensing

Our package will be under the MIT license. We want our project to be openly available for users and we want to encourage the use, modification as well as redistribution of our package. The MIT license is simple and permissive, allowing usage of the software under commercial, educational, private circumstances. Moreover, it permits the modification and redistribution of the package without restricting the license of the derivatives. We believe by choosing the MIT license, we can maximize the impact of our project.

## Feedback
### Milestone 1
* Please follow the python naming conventions as laid down by pep8. See 1st answer - https://stackoverflow.com/questions/12007811/how-should-i-name-my-classes-and-function-and-even-strings
	- FIXED: Changed all class, module, and function names to follow PEP8 naming conventions

* Need to modify the directory structure, since the package name is AD27, there should be a folder with this name with init.py inside it
	- FIXED: Renamed "applications" folder to AD27 and added the "__init__.py" file inside

* The current setup does not contain any project metadata files for this (pyproject.toml for PEP518 compliance).
	- FIXED: Added pyproject.toml file in directory structure	

* Would be great if the function_overload module is visible in the directory structure.
	- FIXED: Added function_overload module to directory structure	

* What does Forward(f) return, is it a numpy array?
	- FIXED: Added return type of Forward into "Modules and Funtionalities section"

* Provide more clarity can be provided for Classes we need and Methods and name attributes section. For example, BasicOperation class is not mentioned in the Classes we need section, define what is a “node”, maybe create a diagram which explains how these different classes fit in the pipeline and interact with each other, etc.

	- FIXED:  Added clarifying statements to each of the classes in our 'Classes we need' section and methods and name attributes section.
