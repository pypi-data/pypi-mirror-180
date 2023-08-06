# Adifpy

## Table of Contents
- [Introduction](#Introduction)
- [Background](#Background)
- [How to Use](#How-to-Use)
- [Software Organization](#Software-Organization)
  - [Directory Structure](#Directory-Structure)
  - [Subpackages](#Subpackages)
- [Implementation](#Implementation)
  - [Libraries](#Libraries)
  - [Modules and Classes](#Modules-and-Classes)
  - [Elementary Funcions](#Elementary-Functions)
- [Extention](#Future-Features)
  - [Reverse Mode](#Reverse-Mode)
  - [Visualization](#Visualization)
- [Impact](#Impact)
- [Future](#Future)


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
First, ensure that you are using Python 3.10 or newer. All future steps can/should be completed in a virtual environment so as not to pollute your base Python installation. To create and activate a new virtual environment, use the following:
```
python3 -m venv [desired/path/to/venv]
source [desired/path/to/venv]/bin/activate
```

Next, clone the package from this GitHub repository and install the needed dependencies and the package:

```
git clone https://code.harvard.edu/CS107/team33.git
python3 -m pip install -r requirements.txt
python3 -m pip install .
```

Now, you're ready to use the package. Continue to the [Example](#Example) to test our the package!

### Example

First, import the package in your python code:
```
import Adifpy
```

and create an `Evaluator` object, which takes a callable function as an argument:
```
evaluator = Adifpy.Evaluator(lambda x : x**2)
```

Next, we want to find the value and derivative of the function at a point (currently, only scalar functions with 1 input and 1 output are supported). We can use the `Evaluator`'s `eval` function, passing in the point at which you want to evaluate (and optionally, a scalar seed vector):
```
output = evaluator.eval(3)
```

This function returns a tuple, in the form `(value, derivative)`, where the value is the evaluation of the function at that point (in this case, 9) and the derivative is the derivative of the function at that point (in this case, 6).

Additionally a seed vector (for now, only scalars such as type `int` or `float` are supported) can be passed to take the derivative with respect to a different seed vector. For example, if you want to take the derivative with respect to a seed vector of `2` you could call the following:
```
output2 = evaluator.eval(3, seed_vector=2)
```
which would return `(9,12)` (since the directional derivative is in the same direction, with twice the magnitude).

## Software Organization
The following section outlines our plans for organizing the package directory, sub-packages, modules, classes, and deployment.

### Directory Structure
<pre>
adifpy/
├── docs
│   └── milestone1
│   └── milestone2
│   └── milestone2_progress
│   └── documentation
├── LICENSE
├── README.md
├── requirements.txt
├── pyproject.toml
├── Adifpy
│    ├── differentiate
│    │   └── <a href="#dual_numberpy">dual_number.py</a>
│    │   └── <a href="#evaluatorpy">evaluator.py</a>  
│    │   └── <a href="#forward_modepy">forward_mode.py</a>
│    │   └── <a href="#function_treepy">function_tree.py</a>  
│    │   └── <a href="#reverse_modepy">reverse_mode.py</a>
│    ├── visualize
│    │   └── <a href="#graph_functionpy">graph_function.py</a>  
│    ├── test 
│    │   └── README.md
│    │   └── run_tests.sh
│    │   └── test_dual_number.py
│    │   └── ... (unit and integration tests)
│    ├── __init__.py
│    └── config.py
└── .github
    └── workflows
      └── coverage.yaml
      └── test.yaml
 </pre>

### Subpackages

The `Adifpy` directory contains the source code of our package, which contains 3 subpackages: `differentiate`, `visualize`, and `test`, described below.

#### Differentiate

The differentiate subpackage currently contains modules required to perform forward mode AD on functions from R to R. Contained in this subpackage are the modules `dual_number.py`, `elementary_functions.py`, `evaluator.py`, `forward_mode.py`, `function_tree.py`, and `reverse_mode.py`. For more information on each module, see [Modules and Classes](#Modules-and-Classes).

#### Visualize

This subpackage has not been implemented yet. Check out our implementation plan [below](#Visualization).

#### Test

The test suite is contained in the test sub-package, as shown above in the [Directory Structure](#Directory-Structure). The test directory contains a `run_tests.sh`, which installs the package and runs the relevant `pytest` commands to display data on the testing suite (similar to the CI workflows).

The individual test files, each of which are named in the `test_*.py` format, test a different aspect of the package. Within each file, each function (also named `test_*`) tests a smaller detail of that aspect. For example, the `test_dual_number.py` test module tests the implementation of the `DualNumber` class. Each function in that module tests one of the overloaded operators. Thus, error messaging will be comprehensive, should one of these operators be changed and fail to work.

The easiest way to run the test suite is to go to the `test` directory and run `./run_tests.sh`.

## Implementation

Major data structures, including descriptions on how dual numbers are implemented, are described in the [Modules and Classes](#Modules-and-Classes) section below.


### Libraries
The `differentiate` sub-package requires the `NumPy` library. Additionally, the `visualization` sub-package will require `MatPlotLib` for displaying graphs. Additional libraries may be required later for additional ease of computation or visualization.

These requirements are specified in the `requirements.txt` for easy installation.


### Modules and Classes

#### `dual_number.py`
the `DualNumber` class, stored in this module, contains the functionality for dual numbers for automatic differentiation. When a forward pass (in forward mode) is performed on a user function, a `DualNumber` object is passed to mimic the function's numeric or vector input. All of `DualNumber`'s major mathematical dunder methods are overloaded so that the `DualNumber` is updated for each of the function's elementary operations.

Each of the binary dunder methods (addition, division, etc.) work with both other numeric types (integers and floats) as well as other `DualNumber`s.

#### `evaluator.py`
The `Evaluator` class, stored in this module, is the user's main communication with the package. An `Evaluator` object is defined by its function, which is provided by the user on creation. A derivative can be calculated at any point, with any seed vector, by calling an `Evaluator`'s `eval` function. The `Evaluator` class ensures that a user's function is valid, decides whether to use forward or reverse mode (based on performance), and returns the derivative on `eval` calls.

*When reverse mode is implemented, the `Evaluator` class may also contain optimizations for making future `eval` calls faster by storing a computational graph.*

#### `forward_mode.py`
This module contains only the `forward_mode` method, which takes a user function, evaluation point, and seed vector. Its implementation is incredibly simple: a `DualNumber` is created with the real part as the evaluation point and the dual part as the seed vector. This `DualNumber` is then passed through the user's function, and the resulting real and dual components of the output `DualNumber` are the function output and derivative.

#### `function_tree.py`
The `FunctionTree` class, stored in this module, is a representation of a computational graph in the form of a tree, where intermediate variables are stored as nodes. The parent-child relationship between these nodes represents the elementary operations for these intermediate variables. This class contains optimizations like ensuring duplicate nodes are avoided.

*This module is currently unused (and un-implemented). When reverse mode is implemented, a given `Evaluator` object will build up and store a `FunctionTree` for optimization.*

#### `reverse_mode.py`
This module contains only the `reverse_mode` method, which takes the same arguments as `forward_pass`. This function is not yet implemented.

#### `graph_tree.py`
This module will contain functionality for displaying a presentable representation of a computation graph in an image. Using a `FunctionTree` object, the resulting image will be a tree-like structure with nodes and connections representing intermediate variables and elementary operations. This functionality is not yet implemented.

#### `graph_function.py`
This module will contain functionality for graphing a function and its derivative. It will create an `Evaluator` object and make the necessary `eval` calls to fill a graph for display. This functionality is not yet implemented.


### Elementary Functions
Many elementary functions like trigonometric, inverse trigonometric and exponential cannot be overloaded by Python's dunder methods (like addition and subtraction can). However, a user must still be able to use these operators in their functions, but cannot use the standard `math` or `np` versions, since a `DualNumber` object is passed to the function for forward passes.

Thus, we define a module `elementary_functions.py` that contains methods which take a `DualNumber`, and return a `DualNumber`, with the real part equal to the elementary operation applied to the real part, and the derivative of the operation applied to the dual part. Thus, these functions are essentially our package's **storage** for the common derivatives (cosine is the derivative of sine, etc.), where the storage of the derivative is the assignment of the dual part of the output of these elementary operations.

These operations will be automatically imported in the package's `__init__.py` so that users can simply call `Adifpy.sin()` or `Adifpy.cos()` (for this milestone our implementation requires users to call `ef.sin()` and `ef.cos()`, not `Adifpy.sin()` or `Adifpy.cos()`), as they would with `np.sin()` and `np.cos()`.

## Extension
Now that our forward mode implementation is complete, we will move on to implement additional features and conveniences for the user.

### Reverse Mode
We will implement reverse mode AD in the differentiate subpackage. Given that we have already been quizzed on the background math, encoding this process should not be too onerous. One of the biggest challenges that we foresee is determining when it is best to use Reverse Mode and when it is best to use Forward Mode. Obviously, it is better to use forward mode when there are far more outputs than inputs and vice-versa for reverse mode, but in the cases where number of inputs and outputs are similar it is not so simple. To address this we will do a series of practical tests on functions of different dimensions, and manually encode the most efficient results into `evaluator.py`.

### Visualization
We are planning on creating a visualization tool with `MatPlotLib` that can plot the computational graph (calculated in Reverse Mode) of simple functions that are being differentiated. Obviously, the computational graph of very complex functions with many different inputs and outputs can be impractical to represent on a screen, so one of the biggest challenges that we will face is to have our program able determine when it can produce a visual tool that can be easily rendered, and when it cannot. 

## Impact


## Future
