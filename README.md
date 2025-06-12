<div style="display: flex; justify-content: center;">
    <img src="docs/assets/icon.png" width="300" align="center" />
</div>

# Asagg

The **Asagg** library **(Auto Setter And Getter Generator)** is a library inspired by another
library that is in the [Java](https://www.java.com) environment, which is the [Lombok](https://projectlombok.org/) library, this library
aims to automate the generation of access methods to private attributes, 
automatically generating Getters and Setters Among other things.

## Installation

To install the library use the following command, you can also use another 
dependency manager of your choice, such as [Poetry](https://python-poetry.org/) or 
[Pipenv](https://pipenv.pypa.io/en/latest/).

```shell
# for pip
> pip install asagg-lib

# for Poetry
> poetry add --group=dev asagg-lib

# for Pipenv
> pipenv install asagg-lib
```
## Usage

Following the same line of operation as Lombok, to be able to use the library, just 
use a decorator and the magic will happen. The decorators are divided into three functions 
where each one has a functionality and one has the functionality of the other two, 
being their combination.

Old way to create properties without **Asagg**:
```python
class MyClass:
    def __init__(self):
        self._my_private_attribute = "private"
    
    @property
    def my_private_attribute(self):
        return self._my_private_attribute

my_class = MyClass()
        
# method generated automaticly with Asagg
print(my_class.my_private_attribute)  # Output: "private"
```

New way to create properties with **Asagg**:
```python
from asagg_lib import Asagg

@Asagg.getter
class MyClass:
    def __init__(self):
        self._my_private_attribute = "private"

my_class = MyClass()
        
# method generated automaticly with Asagg
print(my_class.my_private_attribute)  # Output: "private"
```

### ``Asagg.getter``

This decorator is responsible for generating the getters of the class to which it is applied, 
it will scan the attributes of the class and take only the private and protected attributes, 
then a function will be applied to generate a property for each attribute collected 
and thus making the getters available

Example:
```python
from asagg_lib import Asagg

@Asagg.getter
class MyClass:
    def __init__(self):
        self._my_private_attribute = "private"
```

### ``Asagg.setter``

This decorator is responsible for generating the setters of the class to which it is applied, 
it will scan the attributes of the class and take only the private and protected attributes, 
then a function will be applied to generate a property for each attribute collected 
and thus making the setters available

Example:
```python
from asagg_lib import Asagg

@Asagg.setter
class MyClass:
    def __init__(self):
        self._my_private_attribute = "private"
```

> #### 📘 **Info**
> 
> The function used to generate the setters also uses a typing
> check to prevent a value of a different type from being assigned to the property

### ``Asagg.data``

This decorator is responsible for generating the setters and getters of the class to which 
it is applied, it will scan the attributes of the class and take only the private 
and protected attributes, then a function will be applied to generate a property 
for each attribute collected and thus making the setters and getters available

Example:
```python
from asagg_lib import Asagg

@Asagg.data
class MyClass:
    def __init__(self):
        self._my_private_attribute = "private"
```

<p style="text-align: center; margin-top: auto; font-size: 0.65rem;">
    All rights reserved &copy; pedr.augustobarbosa.aparecido@gmail.com
</p>