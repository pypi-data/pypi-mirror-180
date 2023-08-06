
<img src="resources/aeda-logo.svg" alt="mypic" style="width:600px; height:200px"/>

![PyPi](https://img.shields.io/pypi/v/aeda?label=pypi%20package)

# Aeda API 
An Aeda service for getting detailed info for cars using registration number.

# Getting Started
## 1.	Installation process
Install from PyPi using:
```console
python -m pip install aeda
```
## 2. Usage
Run either using command line or as a python library.


### Command line
Run from command line using:
```console
python -m aeda.car.main --regnumber XXXXXXXXX
``` 
Run in a python script using:
```python
import aeda.car
aeda.car.get_car_from_reg_number("XXXXXXXXX")
``` 


## 2.	API references



- 
- version "2022.12.1"