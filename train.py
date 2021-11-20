import pandas as pd
from sklearn.ensemble import RandomForestRegressor as RF
from sklearn.model_selection import train_test_split as split
import pickle

headers = [
    'Date', 'IPO_Name', 'Profile', 'Issue_Size',
    'QIB', 'HNI', 'RII', 'Total',
    'Bid_Price', 'Listing_Open', 'Listing_Close', 'Listing_Gains', 'CMP', 'Current_Gains'
]

df = pd.read_csv(open('ipo_history.csv', 'r'))

model = RF(n_estimators=10)

data = df.drop([headers[0], headers[1], headers[2], headers[7], headers[8], headers[9], headers[10], headers[11], headers[12], headers[13]], axis=1)
target = df[headers[11]]

x_train, x_test, y_train, y_test = split(data, target, test_size=0.25)

model.fit(x_train, y_train)

print('Model Score', model.score(x_test, y_test))


with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
