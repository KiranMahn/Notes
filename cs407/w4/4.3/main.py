import pandas
import sys 


""" 

Columns are: 

    IP – the IP address

    Reliability- A measure of confidence in the risk (rating identified), values 1-10, 1 being lowest, 10 being highest. This comes from a range of different sources, such as hacker forums and user reports. As a general guide if 60 reports are made against an IP address which is spamming, then it would be a higher level of reliability compared to one where perhaps only 10 reports are received. [https://cybersecurity.att.com/documentation/usm-appliance/otx/about-otx.htm]

    Risk- A measure of how risky the IP is, 1-10, 1 is the lowest risk, 10 is the highest. This can be defined in terms of the impact on assets, again the detail behind this value isn’t of particular note for what we are looking at.

    Type – the type of node making the connection, e.g. spamming indicates the IP represents a spamming node

    Country – the country from which the IP address originates

    Locale – a defined area within the country

    Coords – the co-ordinates of the node

    X – This is the threat score. Again, a higher value indicates a more substantial threat. This can be used as a general indication of how much of a threat this particular IP poses. You’ll notice in the book this is not really covered much. We won’t talk much about it either, this is a function of some of the variables such as risk and reliability, but it is not well documented. Instead we’ll focus on risk, reliability and types and location.

"""

avRep = "reputation.data"
av = pandas.read_csv(avRep,sep="#")
av.columns = ["IP","Reliability","Risk","Type","Country","Locale","Coords","x"]

# print out an overview of the data
print(av)

av['Risk'].describe()

# count the instances for different values
rel_ct = pandas.value_counts(av['Reliability'],sort=True)
print(rel_ct)

country_ct = pandas.value_counts(av['Country'])
print(country_ct)

def factor_col(col):
    factor=pandas.Categorical(col)
    return pandas.value_counts(factor,sort=True).reindex(factor.categories)

print(factor_col(av['Reliability']))

country_ct[:20].plot(kind='bar',title="Summary By   Country",figsize=(8,5))
