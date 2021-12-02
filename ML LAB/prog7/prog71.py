import pandas as pd
import numpy as np
import csv
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianModel
import warnings

warnings.filterwarnings("ignore")

lines=list(csv.reader(open('heart.csv','r')))
attributes=lines[0]

data=pd.read_csv("heart.csv",names=attributes)
data.replace("?",np.nan,inplace=True)
model=BayesianModel(
        [
           ("age","trestbps"),
           ("sex","trestbps"),
           ("exang","trestbps"),
           ("trestbps","heartdisease"),
           ("heartdisease","chol")
                
                ])
print("learning with maximum likelihood estimator....")
model.fit(data,estimator=MaximumLikelihoodEstimator)

print("Creating Inferences")
data_infer=VariableElimination(model)

print("The chances of heartdisease in a person of age :20 ")
q=data_infer.query(variables=["heartdisease"],evidence={"age":20})
print(q)