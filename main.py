from vector import Vector

def main():
    v1 = Vector([8.218, -9.341])
    v2 = Vector([-1.129, 2.111])

    print(v1.plus(v2))

    v3 = Vector([7.119, 8.215])
    v4 = Vector([-8.223, 0.878])

    print(v3.minus(v4))

    v5 = Vector([1.671, -1.012, -0.318])
    multiplier = 7.41

    print(v5.scalar(multiplier))

if __name__ == "__main__":
    main()
