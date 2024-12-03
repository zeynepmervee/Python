class Employees():
    def __init__(self):
        self.FirstName=""
        self.LastName=""
        self.Address=""
class DataScience(Employees):
    def __init__(self):
        self.Programming=""
datascientist=DataScience()
datascientist.Address #miraslama yoluyla adresi Employee'den aldik
class Marketing(Employees):
    def __init__(self):
        self.StoryTelling=""


