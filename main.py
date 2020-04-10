import csv
import re


def getTheIngredientsDetails():
    with open('data.csv', 'r') as data, open('step1Data.csv', 'w') as newData:
        reader = csv.reader(data)
        writter = csv.writer(newData)
        for row in reader:
            example = re.search('主料：.+教', row[4], re.M | re.I)
            if (example):
                pattern = example.group(0)
                row[4] = row[4].replace(str(pattern), '')
                pattern = pattern.replace('主料：', '')
                pattern = pattern.replace('教', '')
                row.append(pattern)
            else:
                row.append('')

            writter.writerow(row)


def getTheTaste():
    with open('step1Data.csv', 'r') as data, open('step2Data.csv', 'w') as newData:
        reader = csv.reader(data)
        writter = csv.writer(newData)
        for row in reader:
            if (re.search('口味：.味', row[4], re.M | re.I)):
                example = re.search('口味：.味', row[4], re.M | re.I)
                pattern = example.group(0)
                row[4] = row[4].replace(str(pattern), '')
                pattern = pattern.replace('口味：', '')
                pattern = pattern.replace('味', '')
                row.append(pattern)
            elif (re.search('口味：..味', row[4], re.M | re.I)):
                example = re.search('口味：..味', row[4], re.M | re.I)
                pattern = example.group(0)
                row[4] = row[4].replace(str(pattern), '')
                pattern = pattern.replace('口味：', '')
                pattern = pattern.replace('味', '')
                row.append(pattern)
            elif (re.search('口味：...味', row[4], re.M | re.I)):
                example = re.search('口味：...味', row[4], re.M | re.I)
                pattern = example.group(0)
                row[4] = row[4].replace(str(pattern), '')
                pattern = pattern.replace('口味：', '')
                pattern = pattern.replace('味', '')
                row.append(pattern)
            elif (re.search('口味：..工', row[4], re.M | re.I)):
                example = re.search('口味：..工', row[4], re.M | re.I)
                pattern = example.group(0)
                row[4] = row[4].replace(str(pattern), '')
                pattern = pattern.replace('口味：', '')
                pattern = pattern.replace('工', '')
                row.append(pattern)
            elif (re.search('口味：....工', row[4], re.M | re.I)):
                example = re.search('口味：....工', row[4], re.M | re.I)
                pattern = example.group(0)
                row[4] = row[4].replace(str(pattern), '')
                pattern = pattern.replace('口味：', '')
                pattern = pattern.replace('工', '')
                row.append(pattern)
            else:
                row.append('')

            writter.writerow(row)


def getTheCondiment():
    with open('step2Data.csv', 'r') as data, open('step3Data.csv', 'w') as newData:
        reader = csv.reader(data)
        writter = csv.writer(newData)
        for row in reader:
            example = re.search('調料：.+', row[6], re.M | re.I)
            if (example):
                pattern = example.group(0)
                row[6] = row[6].replace(str(pattern), '')
                pattern = pattern.replace('調料：', '')
                row.append(pattern)
            else:
                row.append('')
            row[6] = row[6].replace('輔料：', ',')

            writter.writerow(row)


def getTheRecipe():
    with open('step3Data.csv', 'r') as data, open('step4Data.csv', 'w') as newData:
        reader = csv.reader(data)
        writter = csv.writer(newData)
        for row in reader:
            example = re.search('才好吃.+', row[4], re.M | re.I)
            if (example):
                pattern = example.group(0)
                row[4] = row[4].replace(str(pattern), '')
                pattern = pattern.replace('才好吃', '')
                row.append(pattern)
            else:
                row.append('')
            row[4] = row[4].replace('才好吃', ',')

            writter.writerow(row)


def getTheSpecial():
    with open('step4Data.csv', 'r') as data, open('step5Data.csv', 'w') as newData:
        reader = csv.reader(data)
        writter = csv.writer(newData)
        for row in reader:
            if (row[7] == ''):
                example = re.search('的特色：.+', row[6], re.M | re.I)
                if (example):
                    pattern = example.group(0)
                    row[6] = row[6].replace(str(pattern), '')
                    pattern = pattern.replace('的特色：', '')
                    row.append(pattern)
                else:
                    row.append('')
                row[6] = row[6].replace(addDotByDishName(row[2]) + '的特色：', ',')
            else:
                example = re.search('的特色：.+', row[7], re.M | re.I)
                if (example):
                    pattern = example.group(0)
                    row[7] = row[7].replace(str(pattern), '')
                    pattern = pattern.replace('的特色：', '')
                    row.append(pattern)
                else:
                    row.append('')
                row[7] = row[7].replace(addDotByDishName(row[2]) + '的特色：', ',')

            writter.writerow(row)


def copyIngredientsDetails():
    with open('step5Data.csv', 'r') as data, open('step6Data.csv', 'w') as newData:
        reader = csv.reader(data)
        writter = csv.writer(newData)
        for row in reader:
            row.append(row[6])
            writter.writerow(row)


def getTheIngredients():
    with open('step6Data.csv', 'r') as data, open('step7Data.csv', 'w') as newData:
        reader = csv.reader(data)
        writter = csv.writer(newData)
        count = 0
        for row in reader:
            res1 = re.sub(
                r'[0-9|/|.]+[克|個|只|茶匙|杯|斤|湯匙許|兩]+|（.+）|[(.+)]|少許|少|許|[:|：]|[0-9]+|[ |　]+', '', row[-1])
            res2 = re.sub(r',| |。|，', ',', res1)
            row[-1] = res2
            print(row[-1])
            writter.writerow(row)


def addDotByDishName(name):
    dot = ''
    for i in range(len(name)):
        dot += '.'
    return dot


# Do the basic cleansing
# getTheIngredientsDetails()
# getTheTaste()


# Need to move the Ingredients column to the rear.
# getTheCondiment()

# getTheRecipe()

# getTheSpecial()

# copyIngredientsDetails()

getTheIngredients()

# Finally, manually modify a little bit.
