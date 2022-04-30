# Example of using mlflow logged model to score 

import mlflow
# First select one of the runs
logged_model = 'runs:/6eb6df92b60e422c8fbc6b89f4425a66/model'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
import pandas as pd

model1 = mlflow.sklearn.load_model(logged_model)

data = pd.read_csv('winequality-red.csv', sep=";")

# Selecting a random row from the data to score
score_x = data.drop(["quality"], axis=1).sample()

from tabulate import tabulate
print('vector ->')
print(tabulate(score_x, headers='keys', tablefmt='psql'))    

res = loaded_model.predict(pd.DataFrame(score_x))
print('score -> ', res[0])
