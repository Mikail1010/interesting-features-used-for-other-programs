#Forward fill:
#  Useful for filling read data files having merged cells

df['column'] = pd.Series(df['column']).fillna(method='ffill')
  
