from multiprocessing import Process, Array


# Create an Array being shared between different processes
shared_array = Array('i', [0]*46)


def count_fib(number, arr):
    if number < 1:
        return "error"
    a = 0
    b = 1
    for i in range(number):
        c = a + b
        a = b
        output = b
        b = c
    arr[number - 1] = output

a = int(input("Enter a number: "))

if a < 1:
    print("Error!")
    exit()

if a > 46:
    print("Too Big!")
    exit()

proc = []

for i in range(a):
    p = Process(target=count_fib, args=(i+1, shared_array))
    proc.append(p)
    proc[i].start()


for i in range(len(proc)):
    proc[i].join()


for i in range(a):
    print(str(shared_array[i]) + ' ', end="")
