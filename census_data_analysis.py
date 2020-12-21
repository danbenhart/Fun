import pandas

census_csv = r'sub-est2019_all.csv'
# census_csv = r'Book1.csv'

census_df = pandas.read_csv(census_csv, encoding='ANSI')

towns_only = census_df.loc[census_df['PLACE'] != 0]
towns_only['pop_numeric'] = pandas.to_numeric(towns_only.loc[:, ('CENSUS2010POP')], errors='coerce')
# numeric_populations = pandas.to_numeric(towns_only['CENSUS2010POP'], errors='coerce')
# towns_only['pop_numeric'] = numeric_populations
# towns_only = census_df[census_df['test1'] != 0]
# towns_only['converted'] = pandas.to_numeric(towns_only['test1'], errors='coerce')

# print(numeric_populations.mean())

print(towns_only['pop_numeric'].mean())
# print(towns_only['pop_numeric'].median())
