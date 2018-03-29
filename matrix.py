# Author: Shams Golap
# Date: Created on 26 January 2018
# Description: This program is mainly for a personal use. 
# I'm a math student and I want to learn more about processing math algos in programming.
# !!! This is a WIP !!!


class Matrix:
    def __init__(self, nbRows = 0, nbColumns = 0, coefficients = []):
        self.matrix = []
        self.nbRows = nbRows
        self.nbColumns = nbColumns

        while True:
            if self.nbRows <= 0:
                self.nbRows = int(input("Enter the number of rows in the matrix: "))
            else:
                break

        while True:
            if self.nbColumns <= 0:
                self.nbColumns = int(input("Enter the number of columns in the matrix: "))
            else:
                break

        if len(coefficients) != nbRows * nbColumns:
            print("The given coefficients cannot be used, please redefine them: ")
            print("\tTo cancel, enter *")

            for l in range(self.nbRows):
                self.matrix.append([])

                for c in range(self.nbColumns):
                    coef = input("Coefficient x{}{} : ".format(l + 1, c + 1))
                    if coef == '*':
                        print("Process canceled")
                        exit()
                    else:
                        coef = int(coef)
                    self.matrix[l].append(coef)

        else:
            self.coefficients = coefficients
            indexCoefficients = 0
            for l in range(self.nbRows):
                self.matrix.append([])

                for c in range(self.nbColumns):
                    self.matrix[l].append(coefficients[indexCoefficients])
                    indexCoefficients += 1


    def multiplyByScalar(self, scalar):
        for l in range(self.nbRows):
            for c in range(self.nbColumns):
                self.matrix[l][c] *= scalar

        return self.matrix


    def diviseByScalar(self, scalar):
        for l in range(self.nbRows):
            for c in range(self.nbColumns):
                self.matrix[l][c] //= scalar

        return self.matrix


    def transposeMatrix(self):
        newCoefficients = []
        for c in range(self.nbColumns):
            for l in range(self.nbRows):
                newCoefficients.append(self.matrix[l][c])

        return Matrix(self.nbColumns, self.nbRows, newCoefficients)


    def __add__(self, other):
        if self.nbRows != other.nbRows or self.nbColumns != other.nbColumns:
            print("Impossible to add matrices of different sizes")
        else:
            coefficientsNewMatrix = []

            for l in range(self.nbRows):
                for c in range(self.nbColumns):
                    coefficientsNewMatrix.append(self.matrix[l][c] + other.matrix[l][c])

        return Matrix(self.nbRows, self.nbColumns, coefficientsNewMatrix)


    def __mul__(self, other):
        if self.nbColumns == other.nbRows:
            nbRowsResultingMatrix = self.nbRows
            nbColumnsResultingMatrix = other.nbColumns
            coefficientsResultingMatrix = []

            for ii in range(nbRowsResultingMatrix):
                for jj in range(nbColumnsResultingMatrix):
                    coefficientsResultingMatrix.append(sum(self.matrix[ii][x] * other.matrix[x][jj] for x in range(self.nbColumns)))

            return Matrix(nbRowsResultingMatrix, nbColumnsResultingMatrix, coefficientsResultingMatrix)
        else:
            print("Operation impossible. Multiply only matrices \"Mm,n\" by \"Mn,p\"")


    def __str__(self):
        finalString = "(\n"
        for l in range(self.nbRows):
            line = "["

            for c in range(self.nbColumns):
                if c == self.nbColumns - 1:
                    line += "{}".format(self.matrix[l][c])
                else:
                    line += "{} ".format(self.matrix[l][c])

            line += "]\n"
            finalString += (line)

        finalString += ")\n"

        return finalString


    def calculateDeterminant(self):
        """
            Calculate Matrix determinant using Gauss algorithm:

        """
        # Pour une matrice 3x3:
        return(
            + self.matrix[0][0] * self.matrix[1][1] * self.matrix[2][2]
            - self.matrix[0][0] * self.matrix[1][2] * self.matrix[2][1]
            + self.matrix[0][1] * self.matrix[1][2] * self.matrix[2][0]
            - self.matrix[0][1] * self.matrix[1][0] * self.matrix[2][2]
            + self.matrix[0][2] * self.matrix[1][0] * self.matrix[2][1]
            - self.matrix[0][2] * self.matrix[1][1] * self.matrix[2][0]
        )



    def getComatrix(self):
        """
            Get comatrice using Gauss algorithm:

        """
        pass


    def reverseMatrix(self):
        """
            Get the reverse of the matrix using 
        """
        if self.isReversible():
            pass
        else:
            if self.calculateDeterminant() == 0:
                print("The matrix is not reversible because its determinant is equal to 0")
            else:
                print("The matrix is not a square matrix")

    def isReversible(self):
        """
            Returns True if the matrix is reversible.
            Else returns False.
        """
        if self.calculateDeterminant() == 0:
            return False
        else:
            return True


if __name__ == '__main__':
    I3 = Matrix(3, 3, [1, 0, 0, 0, 1, 0, 0, 0, 1])

    # print(I3)

    coefs = [1,2,-3,2,5,2,3,-1,-4]

    A = Matrix(3, 3, coefs)
    B = Matrix(3, 3, coefs[::-1])

    print(A)
    print("Det(A) = {}".format(A.calculateDeterminant()))
    if not A.isReversible():
        print("La matrice A n'est pas inversible")

    # print(A)
    # print(B)

    # print(A * I3)
    # print(B * I3)

    # print(A * B)
    # print(B * A)

    # C = Matrix(4, 4, [1, 2, 2, 1, 3, 1, 3, 3, 2, 1, -2, 4, 4, -1, -1, 2])
    # D = Matrix(3, 3, [-1, 2, 5, 1, 2, 3, -2, 8, 10])
    # ComD = Matrix(D.nbRows, D.nbColumns, [D for i in range(9)])

    # print(ComD)    

    # print(D)
