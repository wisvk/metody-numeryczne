from math import pi
import numpy as np
import linalg

def cylinder_area(r:float,h:float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    if r >0 and h > 0:
        pole = 2 * pi * r * r + 2 * pi * r * h
        return pole
    else:
        return np.NaN


def fib(n:int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    lst = [1, 1]

    if type(n)==int:
        if n <= 0:
            return None
        elif n < 2:
            return np.array([lst[0]])
        elif n == 2:
            return np.array(lst)
        else:
            for i in range(2, n):
                lst.append(lst[i-1]+lst[i-2])
            return np.reshape(np.array(lst),(1,n))

    return None

def matrix_calculations(a:float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    matrix = np.array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])
    Mdet = np.linalg.det(matrix)
    if Mdet == 0:
        Minv = np.NaN
    else:
        Minv = np.linalg.inv(matrix)
    Mt = np.transpose(matrix)

    return Minv, Mt, Mdet

def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """

    if type(m)==int and type(n) == int and m>0 and n>0:
        zero_matrix = np.zeros((m, n))
        for i in range(m):
            for j in range(n):
                if i>j:
                    zero_matrix[i,j]=i
                else:
                    zero_matrix[i,j]=j
        return zero_matrix
    else:
        return None

print(custom_matrix(4,5))


#zad 2
print(np.arange(5,20, 2.5))
print(np.arange(68.3, 70.6, 0.3))
print(np.linspace(7.9, 3.7, num=6))
print(np.linspace(1, 10, num=17))

#zad 5
M = np.array([[3, 1, -2, 4], [0, 1, 1, 5], [-2, 1, 1, 6], [4, 3, 0, 1]])
print(M)
print(M[0,0])
print(M[2,2])
print(M[2,1])
w1 = M[:,2]
w2 = M[1,:]
print(w1, w2)

#zad 7
v = np.array([1, 3, 13])
v1 = np.transpose(v)
v2 = np.array([8, 5, -2])

print(np.multiply(4, v1))  #4*v1

v3 = np.array([[2], [2], [2]])

print(-v2 + v3)  # -v2 + v3
print(np.dot(v1, v2))  #w sensie mnożenia macierzy, tzw. mnożenie macierzy w sensie Cauchy’ego
print(np.multiply(v1, v2))  #w sensie mnożenia Hadamarda (element-wise)

#zad 8
M1 = np.array([[1, -7, 3], [-12, 3, 4], [5, 13, -3]])
M3 = np.multiply(3, M1)
print(M3)
M4 = M3 + np.array([[1,1,1], [1,1,1], [1,1,1]])
print(M4)
print(np.transpose(M1))
print(np.dot(M1, v1))
print((np.dot(np.transpose(v2), M1)))




