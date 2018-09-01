from functools import partial


def f(k1, k2, k3):
    print(k1, k2, k3)


# f(1, 2, 3)
# f_alias = partial(f, 1)
f_alias = partial(f, k2=10)
f_alias(k1=2, k3=3)


