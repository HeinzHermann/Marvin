# Sagecode Mathe2_Blatt3

# Marvin Glaser :       Jan Koeppen
# 4424114       :       6765802
# Gruppe 1

testmatrix = [[1, 2], [3, 4]]                                                                             
testvector = vector([1,2,3,4])
print(testvector)

def normx(v):
        return v.norm()
#done: normx

def normmatrix(n, matrix):
        r_norm = 0 

        for y in range(0, len(matrix)):
                for x in range(0, len(matrix[0])):
                        r_norm += abs(matrix[y][x]) ** n
                #endloop
        #endloop
        return r_norm ** (1/n)
#done: normatrix

print("matrix", "= ", normmatrix(2, testmatrix))
print("vector", "= ", normx(testvector))
