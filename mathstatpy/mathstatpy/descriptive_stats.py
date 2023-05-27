import matplotlib.pyplot as plt
import numpy as np

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
    
    def draw_histogram(self, xlabel: str, ylabel: str, title: str, bins = None, labels: list = None):
        if bins == None:
            bins = int(len(self.data)**(1/2)).__floor__()
        
        frecuencias, bordes, _ = plt.hist(self.data, bins=bins, label=labels, rwidth=0.9)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        if labels != None:
            plt.legend()
        
        for i, frecuencia in enumerate(frecuencias):
            plt.annotate(str(int(frecuencia)), xy=(bordes[i] + 0.5, frecuencia), ha='center', va='bottom')
        
        plt.show()
    
    def draw_boxplot(self, xlabel: str, ylabel: str, title: str):
        fig, ax = plt.subplots()
        boxplot = ax.boxplot([datos], positions=[0], widths=0.6, patch_artist=True)

        median = self.median()
        top_limit = np.percentile(self.data, 75)
        lower_limit = np.percentile(self.data, 25)
        
        ax.text(0.5, median, f'Median: {median:.2f}', color='r', fontsize=8, ha='center')
        ax.text(0.5, lower_limit, f'Lower limit: {lower_limit:.2f}', color='g', fontsize=8, ha='center')
        ax.text(0.5, top_limit, f'Top limit: {top_limit:.2f}', color='b', fontsize=8, ha='center')

# Etiquetas y título
        ax.set_xticklabels([xlabel])
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        
        plt.show()
        
    
    def scatter_plot(self):
        sorted_data = sorted(self.data)
        data = {}
        for x in sorted_data:
            if x in data:
                data[x] = data[x] + 1
            else:
                data[x] = 1
        
        
        plt.scatter(data.keys(), data.values())
        plt.show()
    
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
    


datos = np.random.randint(0,100,100)
print(type(datos))
print(type(datos[0]))
# _verify_numerical_type(datos)
#dat = Descriptive(datos)
#dat.scatter_plot()

