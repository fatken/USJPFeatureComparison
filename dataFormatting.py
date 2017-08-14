import pandas

#read in, index_col is the first col by default
us = pandas.DataFrame.from_csv('features-full-us-2017-06-13.csv', sep = ";", index_col = None)#,,   header is for skipping prior rows, index_col set to none to automatically generate integer index

#sort values based on multiple columns, feature and choice, inplace means changes happen to the dataframe itself
us.sort_values(["Feature", "Choice"], inplace=True)

#Reset index generated from when importing the data frame, so the index is newly calculated
us.reset_index(inplace=True)#level removes selected index rows, by default remove all index rows

#remove the column index generated from import
del us["index"]

jp = pandas.DataFrame.from_csv('features-full-jp-2017-06-13.csv', sep = ";", index_col=None)#, , index_col = None, header is for skipping prior rows
jp.sort_values(["Feature", "Choice"], inplace=True)
jp.reset_index(inplace=True)#level removes selected index rows, by default remove all index rows
del jp["index"]

sameCount = 0;
for i in range(len(us)):
    if(us["Feature"][i] == jp["Feature"][i] and us["Choice"][i] == jp["Choice"][i]):
        sameCount +=1;
    else:
        print(i);

us=us.rename(columns = {'Average effect':'USEffect', "Top 100 popularity": "top100Popularity", "Top 100 popularity trend": "top100PopularityTrend", "Popularity outside top 100":"popularityOutside","Popularity outside top 100 trend":"popularityTrendOutside", "Difference in popularity": "differenceInPopularity", "Feature category":"featureCategory"})

#append JP average effect to US DF as JPEffect column
us["JPEffect"] = jp["Average effect"]

#output file
file_name = "USJP.csv"
us.to_csv(file_name)