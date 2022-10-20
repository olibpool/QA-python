import timeit


def timestables():
    for i in range(1,11):
        for j in range(1,11):
            print(f"{str(i)}*{str(j)}={i*j}")
            
    print('\n Time taken: ')
                    
loop = 100


result = timeit.timeit('timestables()', globals=globals(), number=loop)
print(result / loop)