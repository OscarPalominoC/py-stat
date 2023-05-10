def average(data: list) -> float:
    """
It receives a numerical list and returns a float value as output. This output is the average or the mean of the numerical list.

Args:
    data (list): Numerical list.

Output:
    result (float): Average or aritmetical mean.
    """
    
    for x in data:
        if type(x) != int:
            if type(x) != float:
                raise TypeError('Data must be numerical type.')
    adding = lambda x: sum(x)
    result = adding(data)/len(data)
    return result

print(average([4, 4, 9, 4.9, 4]))
