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
Pydantic                                         0.0302958                          0.0150661     1
Marshmallow                                      0.0565639                          0.0281031     1.86647
Django REST Framework                            0.146527                           0.107131      5.59186
=============


deserialize
Library                  Many Objects 1000 times (seconds)    One Object 1000 times (seconds)    Relative
---------------------  -----------------------------------  ---------------------------------  ----------
Pydantic                                         0.002321                          0.00109506      1
Marshmallow                                      0.0241871                         0.0120111      10.5965
Django REST Framework                            0.0665438                         0.033778       29.3677

```
