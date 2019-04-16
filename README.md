# MLC Course Project - Kaggle Taxi Fare Prediction

#### Participants: Mingyi He, Xiaoning He, Rufei Sheng, Tiancheng Yin

### Stage 0: Database ETL
- Extract: Data download from kaggle.com
- Transform: Necessary preprocessing steps from high level (might not be useful)
- Load: Upload on AWS/Azure/Google Cloud in a queryable format

### Stage I: Problem Definition
- What question are we trying to solve? Is it easily quantifiable?
- What metrics are we trying to use?
- What types of features/data are we dealing with?

### Stage II: Data Exploration
#### 0) Data Preprocessing
- N/A values handling (fill, intropolate, median, mean, 0, etc)
- outlier removal (based on IQR or customerized based on ML models, location might be out of NYC)
- feature engineering/feature selection based on our problem definition
    + Datetime bucket slot
    + Weekday / Weekend
    + Peak Hour (Criterion based the paper from Cornell)
    + National Holidays
    + Pickup and dropoff neiborhood one hot

#### 1) Data Explanatory Analysis
- Do we see any trends? Clusters? Potential movement?
- Think about what types of data are we going to feed into our model
- And..more importantly, what types of model will work best given our data

### Stage III: Predictive Analysis Models
Based on 2.6, we should have a clear view about the models we will be using. To list a few...
- Linear/Lasso/Ridge Regression
- Decision Tree (etc...)
- Random Forest Regressor
- XgBoost Regressor (idealy this should be the best performer on large dataset)

### Stage IV: Model Optimization
- From a high level, think about what models might outperform our current one and do a quick comparison
- Run a cross validation e.g(k-fold) with our validation set to determine what model or models work the best on our current problem
- Once the model is set, try to figure out how to fine tuning our hyper parameters

### Stage V: Retrospective Analysis
- What are the limitations, challenges in this project?
- How can we improve the model, process, parameters if we have additional resources? 
