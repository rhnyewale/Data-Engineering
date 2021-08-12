## 1. Introduction to Time Complexity ##

test_values = [4, 3, 5, 6, 2, 1]

def maximum(values):
    answer = None
    for value in values:
        if answer == None or value > answer:
            answer = value
            
    return answer

max_value = maximum(test_values)


## 2. Measuring the Execution Time ##

import time
def maximum(values):
    answer = None
    for value in values:
        if answer == None or answer < value:
            answer = value
    return answer

start = time.time()
max_value = maximum(test_values)
end = time.time()
runtime = end - start
print(runtime)
# add your code below
# variable test_values is available for you

## 3. Generating Random Inputs ##

import time
import random

def maximum(values):
    answer = None
    for value in values:
        if answer == None or answer < value:
            answer = value
    return answer

def gen_input(length):
    return [random.randint(-1000, 1000) for _ in range(length)]

# add your code below
times = []
for length in range(1,501):
    values = gen_input(length)
    start = time.time()
    maximum(values)
    end  = time.time()
    runtime = end - start
    times.append(runtime)
    
print(times)

## 5. Modeling Execution Times ##

import time
import random
import matplotlib.pyplot as plt

def plot_times(times):
    plt.plot(times)
    plt.ylabel('runtime')
    plt.xlabel('size')
    plt.show()

def sum_values(values):
    total = 0            
    for value in values: 
        total += value   
    return total  

def gen_input(length):
    return [random.randint(-1000, 1000) for _ in range(length)]

# add your code below

times = []
for length in range(1,501):
    values = gen_input(length)
    start = time.time()
    sum_values(values)
    end = time.time()
    times.append(end-start)
    
plot_times(times)

## 6. Worst-Case Analysis ##

def count_zeros(values):
    count = 0            # c1
    for value in values: # c2
        if value == 0:   # c3
            count += 1   # c4
    return count         # c5

model1 = '(c1 + c2) * N + (c3 + c4 + c5)'
model2 = '(c2 + c3) * N + (c1 + c4 + c5)'
model3 = '(c2 + c3 + c4) * N + (c1 + c5)'

correct = model3

## 7. Quadratic Complexity ##

def sum_pairs(values):
    pair_sums = 0              # c1             
    for x in values:           # c2     
        for y in values:       # c3     
            pair_sums += x + y # c4
    return pair_sums           # c5

model1 = '(c3 + c4) * N^2 + c2 * N + (c1 + c5)'
model2 = 'c4 * N^2 + (c2 + c3) * N + (c1 + c5)'
model3 = '(c2 + c3 + c4) * N^2 + (c1 + c5)'

correct = model1

## 8. Simplifying Further ##

time1 = 'N^4 + N^2 + 1'
time2 = '7 * N^3 + 0.5 * N^2 + 100'
time3 = 'N^2 + 10000 * N + 999'

O1 = "O(N^4)"
O2 = "O(N^3)"
O3 = "O(N^2)"

## 9. A Common Misconception ##

def count_triples(values):
    count = 0
    N = len(values)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if values[i] + values[j] + values[k] == 0:
                    count += 1
    return count

coefficients = [3, 1, 1, 3] # 3N^3 + N^2 + N + 3
order = "O(N^3)"