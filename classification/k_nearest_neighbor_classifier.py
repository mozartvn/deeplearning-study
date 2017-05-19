
# assume we have Xtr_rows, Ytr, Xte_rows, Yte as before
# recall Xtr_rows is 50,000 x 3072 matrix

Xval_rows = Xtr_rows[:1000, :] # take first 1000 for validation
Yval = Ytr[:1000]
Xtr_rows = Xtr_rows[1000:, :] # keep last 49.000 for train
Ytr = Ytr[1000:]

# find hyperparametrers taht work best on the validation set
validation_accuracies = []
for k in [1, 3, 5, 10, 20, 50, 100]:
  #use a particular value of k and evaluation on validation data
  nn = NearestNeighbor()
  nn.train(Xtr_rows, Ytr)

  #here we assume a modified NearestNeighbor class that can take a ka as input
  Yval_predict = nn.predict(Xval_rows, k = k)
  acc = np.mean(Yval_predict == Yval)
  print('accuracy: %f' % (acc,))

  #keep track of what works on the validation set
  validation_accuracies.append((k, acc))

# visualize high-dimentional data : # http://homepage.tudelft.nl/19j49/t-SNE.html