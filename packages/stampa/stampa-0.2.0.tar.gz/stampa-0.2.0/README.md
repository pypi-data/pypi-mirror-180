# Stampa
## datetime.now() without spaces
```
datetime.datetime(2022, 12, 7, 21, 0, 49, 482071)
```

```python
from stampa.stampa import Stamp

stamp = Stamp("stamp")
print(stamp)
```
#####  20221207210049482071
```python
stamp = Stamp("year")
print(stamp)
```
##### 2022
```python
stamp = Stamp("month")
print(stamp)
```
##### 202212
```python
stamp = Stamp("day")
print(stamp)
```
#####  20221207
```python
stamp = Stamp("hour")
print(stamp)
```
#####  2022120721
```python
stamp = Stamp("min")
print(stamp)
```
#####  202212072100
```python
stamp = Stamp("sec")
print(stamp)
```
#####  20221207210049
