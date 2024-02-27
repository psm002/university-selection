import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, RidgeCV, LogisticRegression, LogisticRegressionCV
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import streamlit as st

def predict(df4, rank, gpa, sat):
    
    X = df4[['US News Rank','GPA','SAT']]
    y = df4['Status']    
    y = LabelEncoder().fit_transform(y)
    
    #@st.experimental_memo
    model = LogisticRegression(solver='newton-cholesky', C=10, max_iter=100)
    #model = LogisticRegressionCV(solver='newton-cholesky', Cs=10, max_iter=100, cv = 5)
    #model = RandomForestClassifier(max_depth=9, n_estimators=500)
    model.fit(X, y)

    return model.predict_proba(pd.DataFrame([[rank, gpa, sat]]))[0][1]    
