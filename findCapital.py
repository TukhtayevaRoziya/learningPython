# finding the capital by country name


from countryinfo import CountryInfo

#country
country = input('Choose a country: ')
#capital
capital = CountryInfo(country).capital()
#print
print(capital)
