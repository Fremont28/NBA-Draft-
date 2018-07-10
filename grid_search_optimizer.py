import pandas as pd 
import numpy as np 

sprite=pd.read_csv("vorpy_sprite.csv")
sprite1=sprite.fillna(0)
sprite1.shape 
sprite1.head(4)

#predict if player will achieve a certain VORP level?
#dec tree y knn??
from sklearn.model_selection import train_test_split,StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier 

X=sprite1.iloc[:,3:32] #features 
y=sprite1.iloc[:,32] #VORP classes  

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                          test_size=0.3, random_state=17)
tree=DecisionTreeClassifier(max_depth=5,random_state=17)
knn=KNeighborsClassifier(n_neighbors=10)
tree.fit(X_train,y_train)
knn.fit(X_train,y_train)

from sklearn.metrics import accuracy_score
tree_pred=tree.predict(X_test)
acc_tree=accuracy_score(tree_pred,y_test) #0.311 

knn_pred=knn.predict(X_test)
acc_knn=accuracy_score(knn_pred,y_test) #0.378 

#i. fine-tune the decision tree 
#using grid-search for optimizing model parameter
from sklearn.model_selection import GridSearchCV,cross_val_score

tree_params={'max_depth':range(1,11),
'max_features':range(3,30)}

tree_grid=GridSearchCV(tree,tree_params,cv=5,
n_jobs=-1,verbose=True)

tree_grid.fit(X_train,y_train)

#top tree parameters 
tree_grid.best_params_ #{'max_depth': 2, 'max_features': 5}
tree_grid.best_score_ #0.55555
accuracy_score(y_test,tree_grid.predict(X_test)) #0.4189 

#fine-tune the knn algorithm 
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

knn_pipe=Pipeline([('scaler',StandardScaler()),
('knn',KNeighborsClassifier(n_jobs=-1))])

knn_params={'knn__n_neighbors':range(1,10)}

knn_grid=GridSearchCV(knn_pipe,knn_params,
cv=5,n_jobs=-1,verbose=True)

knn_grid.fit(X_train,y_train)
knn_grid.best_score_ #0.427

#random forest classifier 
from sklearn.ensemble import RandomForestClassifier

forest=RandomForestClassifier(n_estimators=100,n_jobs=-1,
random_state=17)

np.mean(cross_val_score(forest,X_train,y_train,cv=5,
n_jobs=-1,verbose=True))

forest_params={'max_depth':range(1,11),
'max_features':range(7,30)}

forest_grid=GridSearchCV(forest,forest_params,cv=5,n_jobs=-1,
verbose=True)

forest_grid.fit(X_train,y_train) 
forest_grid.best_score_ #0.561