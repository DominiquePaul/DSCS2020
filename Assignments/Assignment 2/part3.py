# building a ml model with sklearn

import numpy as np
import pandas as pd

"""
1. Load your data from part 2

Create two lists. One should contain the name of the features (i.e. the input
variables) you want to use to train your model, the other should contain the
column name of the labels
"""
# your code


"""
2. Divide your column into a training and testing set like we did in class. The
fraction of the training size should be somewhere between 70 and 80 percent.

Before you split the dataframe, make sure to shuffle the row order.
"""
# your code


"""
3. The sklearn actually has a function for this called 'train_test_split'. Redo
the split by using the function. Note that it will require you to feed in model
variables and labels separately.
"""
# your code


"""
4. Using the Create a multiple linear regression model using sklearn package.
Create predictions for your test set that you generated in the previous step

Linear regression model:
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
"""
# your code


"""
5. In class we simply used the accuracy as a measure of quality for our model. In
this case this won't work as we are not making categorical predictions, but
numerical ones instead.

Therefore we want to calculate the so-called mean squared error (MSE). We do
this as follows:

mse = average of all rows for ((model_predictions - labels)^2)

Calculate the mean squared error for our model predictions. In a second step,
compare this with a "model" that would have just predicted all rows to be the
average of the 'quality' column in the training data. Which MSE error is lower?
(a lower value is generally better)

Detailed formula in case the one above isn't clear:
https://www.statisticshowto.com/mean-squared-error/

Short explanation of why we use the MSE can be found here:
https://peltarion.com/knowledge-center/documentation/modeling-view/build-an-ai-model/loss-functions/mean-squared-error

Longer explanation:
https://stats.stackexchange.com/questions/127598/square-things-in-statistics-generalized-rationale/128619
"""
# your code


"""
6. Sometimes, when we've created a model we want to save it as a file so that we
can just load it into another file at another point.

Save your regression model to your local folder. Test whether it worked
by re-loading the model as a new instance and make some predictions (e.g. again
on the test dataset)

Hint: have a look at this link
https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/
"""
# your code






#
