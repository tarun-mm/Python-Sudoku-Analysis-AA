import numpy as np
import time
import sudoku_back
import sudoku_MRV
import sudoku_PNP

N = 5000


def read_data():
    qizs = np.zeros((1000000, 81), np.int32)
    sols = np.zeros((1000000, 81), np.int32)

    print("Starting to Read Data")

    for i, line in enumerate(open('sudoku.csv', 'r').read().splitlines()[1:]):
        quiz, solution = line.split(",")
        for j, q_s in enumerate(zip(quiz, solution)):
            q, s = q_s
            qizs[i, j] = q
            sols[i, j] = s

    qizs = qizs.reshape((-1, 9, 9))
    sols = sols.reshape((-1, 9, 9))
    return qizs, sols


def test_back(qizs, sols):
    print("Testing Sudoku by backtracking")

    start_test = time.time()
    c = 0
    for i in qizs[:N]:
        if c%100 == 0:
            print(c)
        if sudoku_back.sudoku_solver(i):
            c += 1
    end_test = time.time()

    print("Percentage of sudokus solved: ", (float(c)*100/N), "%", sep="")
    print("Time taken to test using Backtracking:", (end_test-start_test))


def test_MRV(qizs, sols):
    print("Testing Sudoku by MRV")

    start_test = time.time()
    c = 0
    for i in qizs[:N]:
        if c%100 == 0:
            print(c)
        if sudoku_MRV.sudoku_solver(i):
            c += 1
    end_test = time.time()

    print("Percentage of sudokus solved: ", (float(c)*100/N), "%", sep="")
    print("Time taken to test using MRV:", (end_test-start_test))

def test_PNP(qizs, sols):
    print("Testing Sudoku by PNP")

    start_test = time.time()
    c = 0
    for i in qizs[:N]:
        if c%100 == 0:
            print(c)
        print(sudoku_PNP.sudoku_solver(i))
        print(sudoku_PNP.sudoku_solver(i) == sols[0])
        c += 1
    end_test = time.time()

    print("Percentage of sudokus solved: ", (float(c)*100/(N-1)), "%", sep="")
    print("Time taken to test using PNP:", (end_test-start_test))


def main():
    start_data = time.time()
    (quizzes, solutions) = read_data()
    end_data = time.time()

    print("Time taken to read data:", (end_data-start_data))

    test_back(quizzes, solutions)


if __name__ == '__main__':
    main()