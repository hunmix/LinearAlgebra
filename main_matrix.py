from LA.Matrix import Matrix
from LA.Vector import Vector

if __name__ == "__main__":
    matrix = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])
    print(matrix)
    print("matrix.shape = {}".format(matrix.shape()))
    print("matrix.row_num = {}".format(matrix.row_num()))
    print("matrix.col_num = {}".format(matrix.col_num()))
    print("matrix.size = {}".format(matrix.size()))
    print("matrix.length = {}".format(len(matrix)))
    print("matrix[0][0] = {}".format(matrix[0, 0]))
    print("matrix.row_vector = {}".format(matrix.row_vector(0)))
    print("matrix.col_vector = {}".format(matrix.col_vector(0)))
    print("add: {}".format(matrix + matrix2))
    print("sub: {}".format(matrix - matrix2))
    print("matrix * 3 = {}".format(matrix * 3))
    print("3 * matrix = {}".format(matrix * 3))
    print("3 * matrix = {}".format(matrix * 3))
    print("zero_2_3 = {}".format(Matrix.zero(2, 3)))
    print("matrix.dot((1, 2)) = {}".format(matrix.dot(Vector([1, 2]))))
    print("matrix1.dot(matrix2) = {}".format(matrix.dot(matrix2)))