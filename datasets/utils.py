import json
import os


available_makes = [
    'acura',
    'alfa romeo',
    'aston martin',
    'audi',
    'bmw',
    'bugatti',
    'buick',
    'cadillac',
    'chevrolet',
    'chrysler',
    'dodge',
    'ferrari',
    'fiat',
    'ford',
    'general motors',
    'geo',
    'gmc',
    'honda',
    'hummer',
    'hyundai',
    'infiniti',
    'isuzu',
    'jaguar',
    'jeep',
    'kia',
    'koenigsegg',
    'lamborghini',
    'land rover',
    'lexus',
    'lincoln',
    'lotus',
    'maserati',
    'mazda',
    'mercedes-benz',
    'mercury',
    'mini',
    'mitsubishi',
    'nissan',
    'oldsmobile',
    'pagani',
    'plymouth',
    'pontiac',
    'porsche',
    'renault',
    'saab',
    'saturn',
    'scion',
    'smart',
    'subaru',
    'suzuki',
    'tesla',
    'toyota',
    'volkswagen',
    'volvo',
]

def modelsByYearsDict(vMake, vYearSet):

    # open corresponding make.json file
    fname = vMake.replace(' ', '_') + ".json"
    infile = open(fname, 'r')
    makesDict = json.loads(infile.read())
    infile.close()

    # Use years a keys to makesDict. Each value will
    # be a list of dictionaires. Each dict. will have
    # a 'model' and 'transmission' key. Build a dict.
    # that has makes for keys with a list of years that
    # make was manufactured as the key value.
    modelsToYear = {}
    for year in vYearSet:
        for obj in makesDict[year]:
            if obj['model'] not in modelsToYear.keys():
                modelsToYear[obj['model']] = [year]
            else:
                if year not in modelsToYear[obj['model']]:
                    modelsToYear[obj['model']].append(year)

    # Once the dict. above is built, dump it into a json file.
    outfile = open(
        vMake.replace(' ', '_') + '_models.json',
        'w'
    )

    json.dump(modelsToYear, outfile)
    outfile.close()



def makeToYears():
    makeslist = makes.available_makes
    makesDict = {}
    makesToYearsDict = {}
    for make in makeslist:
        yearlist = []
        fname = make.replace(' ', '_') + ".json"

        with open(fname, 'r') as infile:
            makesDict = json.loads(infile.read())
            for x in makesDict.keys():
                yearlist.append(x)
                
        yearlist.sort()
        makesToYearsDict[make] = yearlist

    with open('makesToYears.json', 'w') as outfile:
        json.dump(makesToYearsDict, outfile)



def sanitizeDict():
    makesList = makes.available_makes

    for make in makesList:         
        makesDict = {}
        make = make.replace(' ', '_')

        with open(make + "_makes.json", "r") as infile:
            makesDict = json.loads(infile.read())

            for model in makesDict.keys():
                sans = list(dict.fromkeys(makesDict[model]))
                makesDict[model] = sans

        with open(make + "_makes.json", "w") as outfile:
                json.dump(makesDict, outfile)



def modelsToYears(seed):
    seedFile = open(seed, 'r')
    mDict = json.loads(seedFile.read())
    seedFile.close()

    for k in mDict.keys():
        modelsByYearsDict(k, mDict[k])


def getModelsForMake(make):
    fname = make.replace(' ', '_') + '_models.json'

    with open(os.path.join(os.getcwd()) + '/datasets/' + fname, 'r') as mDict:
        makesDict = json.loads(mDict.read())
        makesList = []
        for key in makesDict.keys():
            makesList.append(key)
            makesList.sort()

        return makesList

def getYearsForModel(make, model):
    fname = make.replace(' ', '_') + '_models.json'

    with open(os.path.join(os.getcwd()) + '/datasets/' + fname, 'r') as mDict:
        makeDict = json.loads(mDict.read())
        yearList = makeDict[model]
        return yearList