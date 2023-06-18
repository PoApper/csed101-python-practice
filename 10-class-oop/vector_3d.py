"""
Implement a `Vector3D` class, which represents a 3D vector.

You have to implement these for this class:
- `__init__` magic function, which receives `x`, `y`, `z` and sets `self.x`,
  `self.y`, `self.z` accordingly.

>>> v = Vector3D(1, 2, 3)
>>> v.x
1
>>> v.y
2
>>> v.z
3

- `to_tuple()` method, which converts the vector to a tuple in `(x, y, z)`
  format.

>>> v.to_tuple()
(1, 2, 3)

- `norm()` method, which calculates the norm (length) of the vector. The norm
  can be calculated using sqrt(x^2 + y^2 + z^2).

>>> v.norm() ** 2
14.0

- Addition between instances of `Vector3D`. The addition follows usual
  component-wise addition rule.

>>> w = Vector3D(4, 5, 6)
>>> u = v + w
>>> u.to_tuple()
(5, 7, 9)

- Substraction between instances of `Vector3D`. The Substraction also follows
  usual component-wise substraction rule.

>>> s = v - w
>>> s.to_tuple()
(-3, -3, -3)

- Scalar multiplication of vector. `s * v`, where `s` is a number and `v` is an
  instance of `Vector3D` gives an instance of `Vector3D` where its `x`, `y`, `z`
  components are multiplied by `s`.

>>> t = 3 * v
>>> t.to_tuple()
(3, 6, 9)
"""
import math


class Vector3D:
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
