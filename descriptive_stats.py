def _verify_numerical_type(data: list):
    for x in data:
        if type(x) != int:
            if type(x) != float:
                raise TypeError('Data must be numerical type.')

def _decimal_places(number: float) -> int:
    return abs(len(str(number).split('.')[1]))
    

class Descriptive:
    
    def __init__(self, data: list):
        _verify_numerical_type(data)
        self.data = data

    def mean(self) -> float:
        """
    It receives a numerical list and returns a float value as output. This output is the average or the mean of the numerical list.
        """
        adding = lambda x: sum(x)
        result = adding(self.data)/len(self.data)
        return result
    
    def median(self) -> float:
        """
    It receives a numerical list and returns a float value as output. This output is the median value of the numerical list.
        """
        sorted_data = sorted(self.data)
        lenght = len(sorted_data)
        if lenght % 2 == 0:
            return (sorted_data[int(lenght/2 - 1)] + sorted_data[int(lenght/2)])/2
        else:
            return sorted_data[int((lenght-1)/2)]
        
    def mode(self):
        """
        It receives a numerical list and returns a numerical value as output. This output is the mode of the numerical list.
        
        Possible outputs:
            * 'AMODAL' (str): String type, in case there is no mode in the numerical list.
            * MODE (list): List type, in case it is a multimodal numerical list.
            * Numerical (int or float): Numerical type, integer or float depending on the numerical list.
        """
        sorted_data = sorted(self.data)
        data = {}
        for x in sorted_data:
            if x in data:
                data[x] = data[x] + 1
            else:
                data[x] = 1
        
        counter = 0
        frequency = 0
        possible_mode = 0
        
        for key, value in data.items():
                
            if value > frequency:
                frequency = value
                possible_mode = key
                counter = 1
                continue
            if value == frequency:
                counter += 1
                
        if frequency == 1:
            return 'AMODAL'
        if counter == 1:
            return possible_mode
        
        multimodal = []
        for key, value in data.items():
            if value == frequency:
                multimodal.append(key)
        
        return multimodal
    
    def range(self):
        """
        It returns the difference between the larger number and the smaller number.

        Returns:
            Numerical (int or float): Numerical type, integer or float depending on the numerical list.
        """
        max = float('-inf')
        min = float('inf')
        for number in self.data:
            if min > number:
                min = number
            if max < number:
                max = number
        
        n1 = 0
        n2 = 0
        if type(max) == float:
            n1 = _decimal_places(max)
        if type(min) == float:
            n2 = _decimal_places(min)
        
        if n1 == 0 and n2 == 0:
            return max - min
        elif n1 > n2:
            return round(max - min, n1)
        else:
            return round(max - min, n2)
    
    def variance(self) -> float:
        """
        Returns
        
        float: Returns the variance of the numerical list.
        """
        mean = self.mean()
        sum_square = [(x - mean)**2 for x in self.data]
        sum_square = sum(sum_square)
        variance = sum_square/(len(self.data) - 1)
        return variance
        
    def standard_dev(self) -> float:
        """
        Returns
        
        float: Returns the standard deviation of the numerical list
        """
        variance = self.variance()
        return variance ** (1/2)
    
    def draw_histogram(self):
        pass
    
    def draw_box_diagram(self):
        pass
    
    def scatter_plot(self):
        pass
    
    def pearson(self):
        pass
    
    def spearman(self):
        pass
    
    def normal_distribution(self):
        pass
    
    def binomial_distribution(self):
        pass
    
    def poisson_distribution(self):
        pass
    

test_data = [1,10, 10.1,600,3,10,3,4,50, 600]
test_data2 = [5,6,17,8,9]
dat = Descriptive(test_data2)
print(dat.standard_dev())
