
input_file = 'water_potability.csv'
  
# importing data
df = pd.read_csv(input_file, header = 0)
  
# head of the data
print(df.head())

input=[
df['ph'],
df['Hardness'],
df['Solids'],
df['Chloramines'],
df['Sulfate'],
df['Conductivity'],
df['Organic_carbon'],
df['Trihalomethanes'],
df['Turbidity']]

output=df['Potability']

# using the train test split function
x_train, x_test, y_train, y_test = train_test_split(input,output,random_state=104, test_size=0.2, shuffle=True)
  
# printing out train and test sets
  
print('x_train : ')
print(x_train.head())
print('')
print('x_test : ')
print(x_test.head())
print('')
print('y_train : ')
print(y_train.head())
print('')
print('y_test : ')
print(y_test.head())