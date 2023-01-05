import threading


shared_array = [0] * 46

class Worker(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num
    
    def run(self):
        a = 0
        b = 1
        for i in range(self.num):
            c = a + b
            a = b
            output = b
            b = c
        shared_array[self.num - 1] = output


a = int(input("Enter a number: "))

if a < 1:
    print("Error!")
    exit()
elif a > 46:
    print("Too big!")
    exit()

workers = []

# create thread workers
for i in range(a):
    workers.append(Worker(i + 1))
    workers[i].start()

for i in range(a):
    workers[i].join()

# Output array result
for i in range(a):
    print(str(shared_array[i]) + ' ', end="")
