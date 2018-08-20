# Even Python doesn't have 'variable declarations' I like to 'declare' them for organization
# purposes

ACTIVATION_FUNCTION_TEXT = 'La salida es 0 si f(v) <= 0. La salida es 1 si f(v) > 0'
FILENAME = 'data.txt'

class Perceptron:
    input = []
    weight = []
    threshold = None
    output = None
    summation = None

    def getData(self, input_list):
        for input in input_list:
            self.input.append(input)

    def getWeight(self, weight_list):
        for weight in weight_list:
            self.weight.append(weight)

    def activationFunction(self, v):
        if v <= 0:
            self.output = 0
        else:
            self.output = 1

    def simplePerceptronAlgorithm(self, input_list, weight_list, threshold):
        self.getData(input_list)
        self.getWeight(weight_list)
        self.threshold = threshold
        xw = [x * w for x, w in zip(self.input, self.weight)]
        self.summation = sum(xw)
        v = self.summation - self.threshold
        self.activationFunction(v)


class DataAccessObject():
    weightData = []
    threshold = None
    sizeWeightList = None

    def __init__(self):
        self.getData()

    def getData(self):
        file = open (FILENAME, "r")
        for line in file:
            fields = line.split(" ")
            size = len(fields)
            self.threshold = int(fields[0])
            for data in range(1,size):
                self.weightData.append(int(fields[data]))
        self.sizeWeightList = len(self.weightData)


class UserInterface:
    inputData = list()

    def getData(self, size):
        print("Hay "+ str(size) + " pesos en el archivo. Necesitas escribir "
              + str(size) + " datos.")
        for element in range(size):
            self.inputData.append(input('Escribe el valor ' + str(element+1) + ': '))


# Algorithm
perceptron = Perceptron()
dao = DataAccessObject()
ui = UserInterface()
ui.getData(dao.sizeWeightList)
perceptron.simplePerceptronAlgorithm(ui.inputData, dao.weightData, dao.threshold)

#Result
print('Entradas: ' + str(perceptron.input))
print('Pesos: ' + str(perceptron.weight))
print('Umbral: ' + str(perceptron.threshold))
print('Sumatoria: ' + str(perceptron.summation))
print(ACTIVATION_FUNCTION_TEXT)

print(" La salida de este perceptron es " + str(perceptron.output) + ".")
