import csv
import datetime as dt

def printToFile(csvFile, fieldnames, data):
    row = dict()
    for i in range(len(data)):
        row[fieldnames[i]] = data[i]
    csvFile.writerow(row)

direct = './input/'
directOut = './result/'
inventory = 'inventory.csv'
sell = 'sell.csv'
supply = 'supply.csv'
outSteal = 'steal.csv'
outDayly = 'dayly.csv'
allStat = 'allStat.csv'

fieldnames = ['date', 'apple', 'pen']

oneDay = dt.timedelta(1)

states = {"MS": ['b1', 'b2', 'm1', 'm2', 's1', 's2', 's3', 's4', 's5'], "LA": ["a1", "a2"]}

resAllStat = []

for state in states:
    shopResesMass = []
    for shop in states[state]:
        aSold = 0
        aStolen = 0
        pSold = 0
        pStolen = 0        
        shopResDict = {}
        nowPen = 0
        nowApple = 0
        EOF = False    
        pref = direct + state + '-' + shop + '-'
        prefOut = directOut + state + '-' + shop + '-'
        with open(pref + inventory) as fInv, open(pref + sell) as fSell, open(pref + supply) as fSupply, open(prefOut + outSteal, "w", newline='') as fOutSteal, open(prefOut + outDayly, "w", newline='') as fOutDayly:
            
            csvInv = csv.reader(fInv)
            csvSell = csv.reader(fSell)
            csvSupply = csv.reader(fSupply)
            csvOutSteal = csv.DictWriter(fOutSteal, delimiter = ',', fieldnames = fieldnames)
            csvOutDayly = csv.DictWriter(fOutDayly, delimiter = ',', fieldnames = fieldnames)
            
            csvOutSteal.writeheader()
            csvOutDayly.writeheader()
            
            next(csvInv), next(csvSell), next(csvSupply)
            sellRow = next(csvSell)
            
            prevYear = dt.date.fromisoformat(sellRow[0]).year
            
            #months
            while not EOF:
                date = dt.date.fromisoformat(sellRow[0])
                if prevYear != date.year:
                    shopResDict[prevYear] = [aSold, aStolen, pSold, pStolen]
                    aSold = aStolen = pSold = pStolen = 0
                    
                prevYear = date.year
                #in months
                startMonth = date.month
                while startMonth == date.month and not EOF:
                    day = date.day
                    
                    if day == 1 or day == 15:
                        sup = next(csvSupply)
                        nowApple += int(sup[1])
                        nowPen += int(sup[2])
                        
                    #in day
                    startDay = date.day
                    while startDay == date.day and not EOF:
                        product = sellRow[1].split('-')[2]
                        if product == 'ap':
                            nowApple -= 1
                            aSold += 1
                        else:
                            nowPen -= 1
                            pSold += 1
                        try:
                            sellRow = next(csvSell)
                            date = dt.date.fromisoformat(sellRow[0])
                        except:
                            EOF = True
                    
                    if (date + int(EOF) * oneDay).day == 1:
                        inv = next(csvInv)
                        trueApple = int(inv[1])
                        truePen = int(inv[2])
                        printToFile(csvOutSteal, fieldnames, [(date - int(not EOF) * oneDay).isoformat(), nowApple - trueApple, nowPen - truePen])
                        aStolen += nowApple - trueApple
                        pStolen += nowPen - truePen
                        nowPen = truePen
                        nowApple = trueApple
                        
                    printToFile(csvOutDayly, fieldnames, [(date - int(not EOF) * oneDay).isoformat(), nowApple, nowPen])
                    
            shopResDict[prevYear] = [aSold, aStolen, pSold, pStolen]
            
        shopResesMass.append(shopResDict)
    
    stateRes = (state, shopResesMass.pop())
    for i in range(len(shopResesMass)):
        someResDict = shopResesMass.pop()
        for years in someResDict:
            for j in range(4):
                stateRes[1][years][j] += someResDict[years][j]
        
    resAllStat.append(stateRes)

fieldnamesAllStat = ['year', 'state', 'apple_sold', 'apple_stolen', 'pen_sold', 'pen_stolen']
with open(directOut + allStat, "w", newline='') as fAllStat:
    csvAllStat = csv.DictWriter(fAllStat, delimiter = ',', fieldnames = fieldnamesAllStat)
    csvAllStat.writeheader()
    for stateCort in resAllStat:
        for year in stateCort[1]:
            printToFile(csvAllStat, fieldnamesAllStat, [year] + [stateCort[0]] + stateCort[1][year])