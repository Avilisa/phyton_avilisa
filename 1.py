import pandas as pd
import matplotlib.pyplot as plt
zillow = pd.read_csv('zillow.csv', names=['Index', 'LivingSpace (sqft)', 'Beds', 'Baths', 'Zip', 'Year',
                                          'ListPrice ($)'], index_col='Index')
sort = zillow.sort_values(by='Baths').head(20)
df = pd.DataFrame(sort)
print(df)
plt.hist(df['Baths'], bins=20)
plt.savefig('Baths.png')
