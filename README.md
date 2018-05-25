# NBA-Draft-
Methods to Evaluate NBA Draft picks

A simple multi-class Keras neural network algorithm was used for predicting a NBA player’s future value above replacement (VORP) over his first three seasons in the league. 

The draft picks were assigned a 1,2,or 3 categorical value depending on their VORP, which acts as the response variable in the model. This categorical variable was one-hot encoded.

The features used in the model include the draft pick’s college statistics (i.e. points per game, rebounds per game) and physical attributes (i.e. wingspan, weight). 

The multi-class Keras model was built with 28 features using a Softmax activation function (which essentially measures the probability that any of the classes are true). A dropout layer was also added to avoid overfitting the neural network. 

Read Here for a brief comparison between power and non-power conference draft selections: https://beyondtheaverage.wordpress.com/2018/05/25/non-power-conference-players-can-dominate-in-the-nba/

Source: https://keras.io/getting-started/sequential-model-guide/
