# Adifpy

## Table of Contents
- [Introduction](#Introduction)
- [Background](#Background)
- [How to Use](#How-to-Use)
- [Software Organization](#Software-Organization)
  - [Directory Structure](#Directory-Structure)
  - [Test Suite](Test-Suite)
  - [Distribution](#Distribution)
- [Implementation](#Implementation)
  - [Libraries](#Libraries)
  - [Modules and Classes](#Modules-and-Classes)
  - [Overloading](#Overloading)
  - [Order of Implementation](#Order-of-Implementation)
  - [Higher Dimensions](#Higher-Dimensions)
- [Feedback](#Feedback)
  - [Milestone1](#Milestone1)
- [Licensing](#Licensing)


## Introduction
This software is aimed at allowing users to evaluate and differentiate their function. This is a powerful tool that will allow users to find solutions to complex derivations and visualize their results. It serves as an efficient way to take derivatives when compared to other solutions such as symbolic differentiation.

Applications are widespread, ranging from graphing simple functions to taking the derivative of complex, high dimension functions that can have widespread uses such as in optimization problems, machine learning, and data analysis.

## Background

Traditional methods for differentiation include symbolic differentiation and numerical differentiation. Each of these techniques brings its own challenges when used for computational science - symbolic differentiation requires converting complex computer programs into simple components and often results in complex and cryptic expressions, while numerical differentiation is susceptible to floating point and rounding errors.

Automatic differentiation (AD) solves these problems: any mathematical function (for which a derivative is needed) can be broken down into a series of constituent elementary (binary and unary) operations, executed in a specific order on a predetermined set of inputs. A technique for visualizing the sequence of operations corresponding to the function is the computational graph, with nodes representing intermediate variables and lines leaving from nodes representing operations used on intermediate variables. AD combines the known derivatives of the constituent elementary operations (e.g. arithmetic and transcendental functions) via the chain rule to find the derivative of the overall composition.

For example, for the hypothetical function ![equation](https://latex.codecogs.com/gif.image?%5Cbg_white%5Cinline%20%5Cdpi%7B110%7Dy%20=%20f(g(h(x)))), where ![equation](https://latex.codecogs.com/gif.image?%5Cbg_white%5Cinline%20%5Cdpi%7B110%7Df,%20g,%20h)
 all represent elementary operations, we can pose ![equation](https://latex.codecogs.com/gif.image?%5Cbg_white%5Cinline%20%5Cdpi%7B110%7Dv_0%20=%20x,%5Cquad%20v_1%20=%20h(v_0),%5Cquad%20v_2%20=%20g(v_1),%5Cquad%20y%20=%20v_3%20=%20h(v_2)). The desired output is ![equation](https://latex.codecogs.com/gif.image?%5Cbg_white%5Cinline%20%5Cdpi%7B110%7D%5Cfrac%7Bdy%7D%7Bdx%7D), and by the chain rule and simple derivatives, we obtain:
 
 <p align="center">
<img src="https://latex.codecogs.com/gif.image?%5Cbg_white%20%5Cdpi%7B110%7D%5Cfrac%7Bdy%7D%7Bdx%7D%20=%20%5Cfrac%7Bdv_3%7D%7Bdv_2%7D%20%5Ccdot%20%5Cfrac%7Bdv_2%7D%7Bdv_1%7D%20%5Ccdot%20%5Cfrac%7Bdv_1%7D%7Bdv_0%7D">
</p>

Our implementation of AD uses dual numbers to calculate derivatives of individual components. Dual numbers have real and dual components, taking the form ![equation](https://latex.codecogs.com/gif.image?%5Cbg_white%5Cinline%20%5Cdpi%7B110%7Da%20&plus;%20b%5Cepsilon$%20with%20$%5Cepsilon%5E2%20=%200) and ![equation](https://latex.codecogs.com/gif.image?%5Cbg_white%5Cinline%20%5Cdpi%7B110%7D%5Cepsilon%20%5Cneq%200) and where `a` and `b` are real. By the Taylor series expansion of a function around a point, notice that evaluating a function at ![equation](https://latex.codecogs.com/gif.image?%5Cbg_white%5Cinline%20%5Cdpi%7B110%7Da%20&plus;%20%5Cepsilon) yields:

<p align="center">
<img src="https://latex.codecogs.com/gif.image?%5Cbg_white%20%5Cdpi%7B110%7Df(a%20&plus;%20%5Cepsilon)%20=%20f(a)%20&plus;%20%5Cfrac%7Bf'(a)%7D%7B1!%7D%20%5Cepsilon%20&plus;%20%5Cfrac%7Bf''(a)%7D%7B2!%7D%20%5Cepsilon%5E2%20&plus;%20...%20=%20f(a)%20&plus;%20f'(a)%20%5Cepsilon">
</p>

Hence, by evaluating the function at the desired point ![equation](https://latex.codecogs.com/gif.image?%5Cbg_white%5Cinline%20%5Cdpi%7B110%7Da%20&plus;%20%5Cepsilon), the outputted real and dual components are the function evaluated at `a` and derivative of the function evaluated at `a` respectively. This is an efficient way of calculating requisite derivatives. 

## How to Use
To use the package, the user will be able to call the entire package directly (since the functionality for construction and differentiation will be in the `__main__.py` file).

A user will need to provide:
1. The function `fn` in an acceptable format (these format options will be outlined by the documentation in the package `README.md`).
2. The point `eval_pt` at which to evaluate the derivative.
3. The seed vector `p` upon which to perform the differentiation.

With these arguments, the user will be able to make a call which looks like the following:
```
import adifpy as ad
...
derivative = ad.run(fn, eval_pt, p)
```

Note that `eval_pt` and `p` will need to be of the same dimension as the input to `f`.

The user may wish to also generate a computational graph when computing the derivative. In this case, they can call the package with
```
derivative = ad.run(fn, eval_pt, p, viz_file=[FILENAME])
```
which will return the derivative and save an image at the desired `FILENAME`. Note that this runs the same function but passes an optional argument to indicate that the package should use the computational graph to construct an image and save it as well.

## Software Organization
The following section outlines our plans for organizing the package directory, sub-packages, modules, classes, and deployment.

### Directory Structure
<pre>
adifpy/
├── docs
│   └── milestone1
├── LICENSE
├── README.md
├── requirements.txt
├── <a href="#mainpy">main.py</a>
├── src
│   ├── construct
│   │   └── <a href="#function_treepy">function_tree.py</a>  
│   │   └── <a href="#nodepy">node.py</a>  
│   ├── differentiate
│   │   └── <a href="#dual_numberpy">dual_number.py</a>  
│   │   └── <a href="#forward_passpy">forward_pass.py</a>  
│   │   └── <a href="#reverse_passpy">reverse_pass.py</a>  
│   └── visualize
│       └── <a href="#graph_treepy">graph_tree.py</a>  
└── test
    └── run_tests.sh
    └── test_1.py
    └── test_2.py
    └── …
 </pre>

sub-packages: The package will contain 4 sub-packages: construct, differentiate, visualize, test. Construct will allow for the creation of a computational graph from an inputted function. Differentiate will allow a user to perform either forward or reverse automatic differentiation (AD). Visualize will allow the user to to create visualizations for either their computational graph or their AD. Test will provide a suite of tests to ensure the package is working as intended.

### Test Suite

The test suite will be contained in the test sub-package, as shown above in the [Directory Structure](#Directory-Structure).

### Distribution

Distributing Our Package: We will use PyPI to distribute our software package under the name `adifpy` (which does not currently exist).

## Implementation

Major data structures, including descriptions on how dual numbers are implemented, are described in the [Modules and Classes](#Modules-and-Classes) section below.


### Libraries
All sub-packages will require the `NumPy` package. Additionally, the `visualization` sub-package will require `MatPlotLib`. Additional libraries may be required later for additional ease of computation or visualization.


### Modules and Classes
#### `main.py`
This module will be the main communication with the user. Users will have the ability to provide functions in different formats (other than as a callable Python object). For example, this module may contain functionality for passing a function as a string representing a Latex function. Specific implementation will be decided depending on future usage and tests.

First, input will be processed and the function's computational graph will be generated: this process is described below. Next, this module will decide whether to call forward or reverse mode, depending on which will be more efficient (or, if the user explicity requests one or the other). The corresponding AD will be performed and the results returned to the user. Note that the computational graph will be generated fully before the AD is performed, so no inefficiency in constructing the graph during AD will be realized. Methods in this module will likely include `latex_to_fn`, `compute_deriv`, etc.



#### `function_tree.py`
The `FunctionTree` class, stored in this module, is a representation of a computational graph in the form of a tree, where intermediate variables are stored as nodes. The parent-child relationship between these nodes represents the elementary operations for these intermediate variables. This class contains optimizations like ensuring duplicate nodes are avoided. Methods included in this class will execute modifications to the function tree.

#### `node.py`
The `Node` class, stored in this module, mimics input to the user’s function. All of its relevant mathematical operators are overloaded so that when a function performs an operation on the node, this elementary operation can be “registered” with the relevant `FunctionTree` instance. `Node` will also have to mimic vector input, so any relevant list-like operator (like `__getitem__` will be overloaded as well). Methods in this class will conduct the various elementary operations needed to build the function tree, like add, multiply, and trigonometric functions, for example.

#### `dual_number.py`
the `DualNumber` class, stored in this module, contains the functionality for dual numbers for automatic differentiation. Its operators are overloaded so that elementary operations in forward and reverse passes work. Methods in this class will compute the various elementary operations used with dual numbers, like addition and multiplication.

#### `forward_pass.py`
the functionality for the forward pass in AD is implemented in this module. Methods in this class will execute the forward pass.

#### `reverse_pass.py`
the functionality for the reverse pass in AD is implemented in this module. Methods in this class will execute the reverse pass.

#### `graph_tree.py`
this module will contain functionality for displaying a presentable representation of a computation graph in an image. Using a function_tree instance, the resulting image will be a tree-like structure with nodes and connections representing intermediate variables and elementary operations. Methods in this class will display the tree in a computation graph in an image.


### Overloading
Some of the classes above use overloaded operators (the `Node` and `DualNumber` classes). For the major mathematical operators, they will be overloaded simply using the Python built-in dunder methods (`__add__` and `__mul__`, etc).

For elementary functions like `sin`, `cos`, `sqrt`, and `exp`, we can still overload these operators in the needed classes. For the purpose of convenience in reverse mode, each of the classes will store a boolean representing whether these functions are to be evaluated for the derivative instead of the value. This will essentially provide the "storage" for common derivatives: the derivative of the "sin" function will be encoded in the overloaded `sin` method, and will take effect when the class attribute representing whether the derivative is needed is `true` (which will occur in reverse mode).


### Order of Implementation
We will build the modules in the following order:

black box tests (if applicable) → `node.py` → `__main__.py` → `function_tree.py` → `dual_number.py` → `forward_pass.py` → `reverse_pass.py` → `graph_tree.py` → additional tests.

### Higher Dimensions
In order to handle cases with higher dimensions, `Node` will also have to mimic vector input. By overloading list-like operators like `__getitem__`, when the function accesses the `n`th input, the `Node` class can simply register these additional inputs with the relevant `FunctionTree` instance.


## Feedback
### Milestone1
1. *Thinking about how users interact with reverse mode and computational graphs:*

Users will not directly communicate the reverse mode or forward mode. By communicating with `main.py`, the user will provide a function and our library will automatically call forward or reverse mode, depending on which will be faster. This can be easily calculated from the dimensionality of the input and output of the function. This is described further in issue 3 below and in [`main.py`](#mainpy) above.

2. *Adding a `src` directory and `requirements.txt` file:*

We have updated the [directory structure](#Directory-Structure) above to reflect adding these components, and have updated the repository.

3. *Being clear about forward and reverse modes:*

We have updated the [`main.py`](#mainpy) description above to reflect how the package will call forward and reverse modes.

## Licensing
The licensing will contain the MIT License. We chose this license for two reasons: 
1. We wanted the simplest licensing. 
2. Since our project is mainly meant as a utility, to allow people to do whatever they would like with our project, in hopes of maximizing how useful our project is. 

While we use the `NumPy` and `MatPlotLib` libraries, we do not need to attribute/reference the library because we are not actually redistributing any of the source code. 
