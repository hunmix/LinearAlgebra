from LA.Vector import Vector

if __name__ == "__main__":

    vec = Vector([5, 2])
    vec2 = Vector([2, 5])
    print(vec)
    print(len(vec))
    print(vec + vec2)
    print(vec - vec2)
    print("vec[0] = {}, vec[1] = {}".format(vec[0], vec[1]))
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))
    print("{} * {} = {}".format(vec, 3, vec * 3))
    print("{} * {} = {}".format(3, vec, vec * 3))
    print("+{} = {}".format(vec, +vec))
    print("-{} = {}".format(vec, -vec))

    zero2 = Vector.zero(2)
    print(zero2)

    print("norm {} is {}".format(vec, vec.norm()))
    print("normalize {} is {}".format(vec, vec.normalize()))
    try:
        print("normalize {} is {}".format(zero2, zero2.normalize()))
    except ZeroDivisionError:
        print("Cannot normalize zero vector {}".format(zero2))

    print("{} dot {} = {}".format(vec, vec2, vec.dot(vec2)))