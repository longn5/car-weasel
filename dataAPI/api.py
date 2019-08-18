from datasets import utils as Dutils
from datasets import aggregate as MakesList

def getAllMakes():
    return MakesList.available_makes

def getAllModels(make):
    return Dutils.getModelsForMake(make)

def getMakeYears(make, model):
    return Dutils.getYearsForModel(make, model)