# CabrilloDecoderPython
Decode File Cabrillo to dictionary Python.

# Installation
To install this package, you have to write like this:
```python
pip install cabrillo-decoder
```
# Add an example file
Make sure that you have created a Python-extension file and write like this:
```python
from cabrillo_decoder import decoder
file = open("cq-ww-cw.cbr")

cabrillo = decoder.Cabrillo(file)

print(cabrillo.decode())
```
