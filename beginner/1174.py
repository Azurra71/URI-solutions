import array as arr

numbers_array = arr.array('f')

for i in range(100):
    number = float(input())
    numbers_array.append(number)

for index in range(len(numbers_array)):
    if(numbers_array[index] <= 10):        
        print("A[{}] = {:.1f}".format(index,numbers_array[index]))