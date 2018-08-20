# Even Python doesn't have 'variable declarations' I like to 'declare' them for organization purposes
class Perceptron:
    data = []
    weight = []
    threshold = None #umbral
    output = None

    def __init__(self):
        self.clearVariables()

    def getData(self):
        self.data.push(10,30,20)

    def clearVariables(self):
        empty(self.data)
        self.weight = list()
        self.threshold = None  # umbral
        self.output = None

perceptron = Perceptron()
print(perceptron.data)
