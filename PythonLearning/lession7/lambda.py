
def test_func(compute):
    result = compute(1, 2)
    return result 

print(test_func(lambda x, y: x + y))
