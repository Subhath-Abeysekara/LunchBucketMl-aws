import pandas as pd
import numpy as np
import pickle
from statistics import stdev

#read the dataset
def check_best_offer():
    df1 = pd.read_csv('CSV/foodAppOfferIncomeMarging.csv')
    # get first 50 rows
    #C:/Users/DFT/Documents/foodAppOfferIncomeMarging.csv
    df2 = df1[["offerId", "marginal_rewenue"]]
    # make parameter object
    offerIds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    dff1 = df2[df2['offerId'].isin({offerIds[0]})]
   # print(dff1)
    minimumCv = stdev(dff1["marginal_rewenue"]) / dff1["marginal_rewenue"].mean()
    bestMean = dff1["marginal_rewenue"].mean()
    largestMean = 0
    largestMeanId = 0
    bestId = offerIds[0]
    #print(minimumCv)
    for i in offerIds:
        options = {i}
        # filter data rows acording to rating
        dff = df2[df2['offerId'].isin(options)]
        Cv = stdev(dff["marginal_rewenue"]) / dff["marginal_rewenue"].mean()
        mean = dff["marginal_rewenue"].mean()
        #print("means ", mean)
        if largestMean <= mean:
            largestMean = mean
            largestMeanId = i
        if Cv <= minimumCv:
            minimumCv = Cv
            bestId = i
            bestMean = mean
            #print(minimumCv)

    # print("MinCv ", minimumCv)
    # print("bestId = ", bestId)
    # print("bestMean ", bestMean)
    # print("LargestMean ", largestMean)
    # print("LargestMeanId ", largestMeanId)

    if bestMean<0:
        object = {largestMeanId , largestMean}
        return object

    else:
        object = {bestId , bestMean}
        return {
            "bestId" : bestId,
            "bestMean" : bestMean
        }
