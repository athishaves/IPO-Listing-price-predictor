import pickle

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Issue_Size, QIB, HNI, RII, Bid_Price
# 18915.90   2.79   0.24   1.66     2150.0

size, qib, hni, rii = float(input('Issue Size ')), float(input('QIB ')), float(input('HNI ')), float(input('RII '))

data = [
    size, qib, hni, rii
]

pred = model.predict([data])
print(pred[0])
