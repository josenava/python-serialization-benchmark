# Python Serialization Benchmark

This is a simple benchmark to compare the performance of serialization libraries in Python. The benchmark compares the performance of the following libraries when serializing and deserializing a single object and a list of 2 objects multiple times (1000).

* [Django REST Framework](http://www.django-rest-framework.org/)
* [Marshmallow](https://marshmallow.readthedocs.io/en/latest/)
* [Pydantic](https://docs.pydantic.dev/latest/)


## Running the benchmark
1. Create a virtualenv and install the requirements
2. execute `python benchmark.py`

## Results
```
serialize
Library                  Many Objects 1000 times (seconds)    One Object 1000 times (seconds)    Relative
---------------------  -----------------------------------  ---------------------------------  ----------
Pydantic                                         0.0305219                          0.0151608     1
Marshmallow                                      0.135807                           0.101068      5.18523
Django REST Framework                            0.150117                           0.106956      5.62737
=============


deserialize
Library                  Many Objects 1000 times (seconds)    One Object 1000 times (seconds)    Relative
---------------------  -----------------------------------  ---------------------------------  ----------
Pydantic                                        0.00236011                          0.001086       1
Marshmallow                                     0.047121                            0.0318861     22.9265
Django REST Framework                           0.0553589                           0.0341067     25.9614

```
