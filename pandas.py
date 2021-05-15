#Forward fill:
#  Useful for filling read data files having merged cells

df['column'] = pd.Series(df['column']).fillna(method='ffill')

#One value of column which applies for multiple values of other column - converting that into a dict mapped with values
dict = {}
for i in df['Column1'].unique():
  dcit[i] = list(df[df['Column1'] == i]['Column2'].values)
  
