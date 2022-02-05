import pandas as pd

def addYear(largeDataFrame):

    largeDataFrame['Release Year'] = int(str((largeDataFrame['Title'])).split('(')[1].split(')')[0])

    return largeDataFrame

