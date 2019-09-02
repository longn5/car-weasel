from datasets import utils as Dutils

def getAllMakes():
    return Dutils.available_makes

def getAllModels(make):
    return Dutils.getModelsForMake(make)

def getMakeYears(make, model):
    return Dutils.getYearsForModel(make, model)