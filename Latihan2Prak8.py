def dataStat(x):
    average = sum(x)/len(x)
    nilaiMax = max(x)
    nilaiMin = min(x)
    return [average, nilaiMax, nilaiMin]

print(dataStat([1,2,3,4,5,6,7,8,9,10]))
