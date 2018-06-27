import numpy as np 
import sklearn 
from sklearn.model_selection import GridSearchCV
from keras.models import Sequential 
from keras.layers import Dense 
from keras.wrappers.scikit_learn import KerasClassifier
from scipy import stats 
from sklearn.model_selection import train_test_split
import seasborn as sns 
from sklearn import svm
from sklearn.svm import SVC 

nba_draft=pd.read_csv("NBA draft class.csv")
nba_draft['BPM'].describe() 
nba_draft1=nba_draft.values 


draft_data=nba_draft[["Yrs","G","MP.1","PTS.1","TRB",
"FG%","3P%","FT%","TRB.1","AST.1","WS/48>.15"]]
draft_data.describe() #4.5 years in the league on average 
nba_draft.info() 

#remove outliers
def outlier_remove(draft):
    low=0.05
    high=0.95
    quantiles=draft_data_x.quantile([low,high])
    for name in list(draft_data_x[name]):
        draft_data_x1=draft_data_x[(draft_data_x[name]> quantiles.loc[low,high]) & (draft_data_x[(draft_data_x[name]<
        quantiles.loc[high,name])]
    return draft_data_x1 

#i. standard deviation modeling 
#calc. summary stats
draft_data_x1=draft_data_x.values 
data_mean,data_std=mean(draft_data_x1[:,3],std(draft_data_x1[:,3]))

#ii. IQR range method
import numpy as np 
q25,q75=percentile(draft_data_x1,25),percentile(draft_data_x1,75)

draft_data_x=nba_draft.dropna() 
draft_data_x.info() 
draft_data_x.College.unique() #uniuqe colleges in the dataset 

south_schools=draft_data_x[(draft_data_x.College=="University of Florida") |
(draft_data_x.College=="University of Tennessee")| (draft_data_x.College=="University of Alabama")|
(draft_data_x.College=="Mississippi State University")|(draft_data_x.College=="University, Georgia")|
(draft_data_x.College=="University of South Carolina")|(draft_data_x.College=="Texas A&amp")]
south_schools[["WS","BPM","WS/48"]].describe() #WS/48=0.099 

west_schools=draft_data_x[(draft_data_x.College=="California State University Long Beach")|
(draft_data_x.College=="University of California Santa Barbara")|
(draft_data_x.College=="University of California")|(draft_data_x.College=="University of Washington")|
(draft_data_x.College=="University of Utah")]
west_schools[["WS","BPM","WS/48"]].describe() #WS/48=0.098

draft_data_x["WS/48"].mean() #0.063 WS/48

#south schools 
sns.distplot(south_schools["WS/48"])
plt.xlabel("Win Shares per 48 Minutes")
plt.title("Valuing SEC Draft Picks")
plt.show() 

#west schools 
sns.distplot(west_schools["WS/48"])
plt.xlabel("Win Shares per 48 Minutes")
plt.title("Valuing West Coast Draft Picks")
plt.show() 

#win shares distribution
sns.distplot(draft_data_x['WS'])
plt.xlabel('Win Shares')
plt.show() 

#elite outliers (BPM) 
q=nba_draft['BPM'].quantile(0.95) #2.2 
elite=nba_draft[nba_draft["BPM"]>2.2]["Player"]
elite.count() 

q1=nba_draft['BPM'].quantile(0.10) #-6.4
below_value=nba_draft[nba_draft["BPM"]< -6.4]["Player"]
below_value #alando tucker? 

## z-scores function 
def outlier_scores(value):
    threshold=3
    mean=np.mean(value)
    sd=np.std(value)
    z_score=[(x-mean)/sd for x in value]
    return np.where(np.abs(z_score)>threshold)

nba_draft.columns.get_loc("BPM")

#drop nan 
import math
nba_draft_bpm=[value for value in nba_draft1[:,33] if not math.isnan(value)]

outlier_players=outlier_scores(nba_draft1[:,33])
outlier_players 

#hyper-parameters (grid search optimization) 
draft_data2=draft_data.fillna(0)
draft_data3=draft_data2.values 
draft_data3.shape 

X_nba=draft_data3[:,0:11]
y_nba=draft_data3[:,10]

X_train,X_test,y_train,y_test=train_test_split(X_nba,y_nba,test_size=0.3)

#SVM 
model_svm=svm.SVC(kernel="linear",C=1,gamma=1)
model_svm.fit(X_train,y_train)
predict=model_svm.predict(X_test) 
score=model_svm.score(predict,y_test)


