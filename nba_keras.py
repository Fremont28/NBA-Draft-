#Classifying NBA draft Picks using Keras 

#libraries 
from keras.models import Sequential 
from keras.layers import Dense,Flatten,Dropout 
from keras.wrappers.scikit_learn import KerasClassifier 
from keras.utils import np_utils 
from sklearn.model_selection import cross_val_score 
from sklearn.model_selection import KFold 
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline 

#dataset 
vorp=pd.read_csv("Vorpy Syrup.csv")
vorp.shape #245 players

# wingspan index assign 0,1 
vorp['Wingspan'].mean() #6.97 ft
vorp['Wingspan'].describe() 
vorp['VORP'].describe() 

def wingspan(w): 
    if w>=7.10:
        return 1
    elif w<7.10 and w>6.8:
        return 2
    else:
        return 3 

#define three-levels of VORP
def vorpy(v):
    if v>=2.40:
        return 1
    elif v<2.40 and v>=0.50:
        return 2
    else:
        return 3 

vorp.Wingspan=vorp.Wingspan.apply(wingspan)
vorp.VORP=vorp.VORP.apply(vorpy) 

#split the data into X (features) and y (response) variables 
vorp1=vorp.values 
vorp_x=vorp1[:,3:32]
X=vorp1[:,3:31] #31 predictors??
y=vorp1[:,31]

#conference names
vorp.Conf.unique() 
vorp=vorp.drop('Conf',1)
vorp=vorp.drop('School',1)
vorp.shape 
vorp.to_csv("vorpy_sprite.csv")

#assign conference names to numeric 
conf_names={"Conf": {"Pac-12":1,"CUSA":2,"ACC":3,
"Big Ten":4,"SEC":5,"Big 12":6,"Pac-10":7,
"A-10":8,"Total":9,"Big East":10,"Southern":11,
"Horizon":12,"AAC":13,"WAC":14,"Missouri Valley":15,
"OVC":16,"Mountain West":17,"Patriot":18,
"Mid-Eastern Athletic":19,"Ohio Valey":20,
"WCC":21,"Big Sky":22,"Big West":23,
"Ohio Valley":24,"X":25,"Summit":26,
"Sun Belt":27,"Big 10":28,"SWAC":29}}

vorp['Conf']=vorp.Conf.replace(conf_names,inplace=True)

#convert y_train to categorical-one hot vectors 
encoder=LabelEncoder() 
encoder.fit(y)
encoded_y= encoder.transform(y)
dummy_y = np_utils.to_categorical(encoded_y) # convert integers to dummy variables (i.e. one hot encoded)

#test and train sets
X_train,X_test,y_train,y_test=train_test_split(X,dummy_y,test_size=0.35)

#build keras multi-class neural network 
model=Sequential() 
model.add(Dense(15,activation='softmax',input_dim=28)) #match input dim (x-predictors)
model.add(Dense(3)) 
model.add(Dropout(0.5))
model.add(Dense(3,activation='softmax')) 
model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy'])
#train the model
model.fit(X_train,y_train,nb_epoch=5,batch_size=22)
score=model.evaluate(X_test,y_test,batch_size=5)








