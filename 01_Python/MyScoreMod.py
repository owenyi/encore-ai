
def getSum(data):
    total = 0
    for x in data:
        total += x 
    return total

def getMean(data):
    return getSum(data) / len(data)

def getMax(data):
    _max = data[0]
    for x in data[1:]:
        if x > _max: _max = x
    return _max

def getMin(data):
    _min = data[0]
    for x in data[1:]:
        if x < _min: _min = x
    return _min

def getTwoSum(num2, num1): # 두 수 사이의 합
    total = 0
    if num1 > num2: num1, num2 = num2, num1
    for i in range(num1, num2 + 1):
        total += i
    return total
