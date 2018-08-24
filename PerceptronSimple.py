# Even Python doesn't have 'variable declarations' I like to 'declare' them for organization purposes

ACTIVATION_FUNCTION_TEXT = 'La salida es 0 si f(v) <= 0. La salida es 1 si f(v) > 0'
FILENAME = 'data.txt'


class Perceptron:
    input = []
    weight = []
    threshold = None
    output = None
    summation = None

    def get_data(self, input_list):
        for input_value in input_list:
            self.input.append(input_value)

    def get_weight(self, weight_list):
        for weight in weight_list:
            self.weight.append(weight)

    def activation_function(self, v):
        if v <= 0:
            self.output = 0
        else:
            self.output = 1

    def simple_perceptron_algorithm(self, input_list, weight_list, threshold):
        self.get_data(input_list)
        self.get_weight(weight_list)
        self.threshold = threshold
        xw = [x * w for x, w in zip(self.input, self.weight)]
        self.summation = sum(xw)
        v = self.summation - self.threshold
        self.activation_function(v)


class DataAccessObject:
    weightData = []
    threshold = None
    sizeWeightList = None

    def __init__(self):
        self.get_data()

    def get_data(self):
        file = open(FILENAME, "r")
        for line in file:
            fields = line.split(" ")
            size = len(fields)
            self.threshold = int(fields[0])
            for data in range(1, size):
                self.weightData.append(int(fields[data]))
        self.sizeWeightList = len(self.weightData)


class UserInterface:
    inputData = list()

    def get_data(self, size):
        print("Hay " + str(size) + " pesos en el archivo. Necesitas escribir "
              + str(size) + " datos.")
        for element in range(size):
            self.inputData.append(int(input('Escribe el valor ' + str(element+1) + ': ')))


# Algorithm
perceptron = Perceptron()
dao = DataAccessObject()
ui = UserInterface()
ui.get_data(dao.sizeWeightList)
perceptron.simple_perceptron_algorithm(ui.inputData, dao.weightData, dao.threshold)

# Result
print('Entradas: ' + str(perceptron.input))
print('Pesos: ' + str(perceptron.weight))
print('Umbral: ' + str(perceptron.threshold))
print('Sumatoria: ' + str(perceptron.summation))
print(ACTIVATION_FUNCTION_TEXT)

print(" La salida de este perceptron es " + str(perceptron.output) + ".")
