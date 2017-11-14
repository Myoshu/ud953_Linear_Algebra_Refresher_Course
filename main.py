from vector import Vector
from math import degrees

def main():
    v1 = Vector([7.579, -7.88])
    v2 = Vector([22.737, 23.64])

    print(v1.is_parallel(v2))
    print(v1.is_orthogonal(v2))

    v3 = Vector([-2.029, 9.97, 4.172])
    v4 = Vector([-9.231, -6.639, -7.245])

    print(v3.is_parallel(v4))
    print(v3.is_orthogonal(v4))

    v5 = Vector([-2.328, -7.284, -1.214])
    v6 = Vector([-1.821, 1.072, -2.94])

    print(v5.is_parallel(v6))
    print(v5.is_orthogonal(v6))

    v7 = Vector([2.118, 4.827])
    v8 = Vector([0, 0])

    print(v7.is_parallel(v8))
    print(v7.is_orthogonal(v8))

if __name__ == "__main__":
    main()
