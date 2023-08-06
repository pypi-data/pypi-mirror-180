from .model_class import model
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
from sklearn.metrics import r2_score, mean_squared_error #metrics

#Define a linear_model class
class linear_model(model):
    """ 
    linear_model class for implementing linear_model and visualizing predictions.
    
    Attributes:
    X (pandas dataframe) representing the design matrix 
    y (pandas dataframe) representing the response variable
    """
    
    def __init__(self,X=pd.DataFrame() ,y=pd.DataFrame() ): 
        model.__init__(self,X,y)

        
    def calculate_linear_model_weights(self):
        """Method to calculate regression linear_model weights using linear algebra and numpy scientific computation.
                
        Args:
            None
        
        Returns:
            weights (numpy array): estimated weights for linear_model using the train set
        
        """        
        X_train=self.X_train
        y_train=self.y_train
        weights=np.linalg.inv(X_train.transpose().dot(X_train)).dot(X_train.transpose()).dot(y_train)
        
        return weights
    
    def predictions(self):
        """Method to calculate predictions in train and test sets respectively using the weights estimated previously
        and numpy scientific computation.
                
        Args:
            None
        
        Returns:
            weights (numpy array): estimated weights for linear_model using the train set
        
        """        
        X_train=self.X_train
        X_test=self.X_test
        weights=self.calculate_linear_model_weights()
        
        predictions_train=X_train.dot(weights)
        predictions_test=X_test.dot(weights)

        
        return predictions_train, predictions_test
    
    
    def plotting_predictions(self):
        """Method to plot predictions and compaired them with the true values of      response in train and test sets respectively.
                
        Args:
            None
        
        Returns:        
               scatterplot of fitted vs. true values of response with the main predictive measures of model validation

        
        """        

        ###Reproduce the scatterplot of prediction on the test set versus the real ones of the response column
        y_train_preds=self.predictions()[0]
        y_test_preds=self.predictions()[1]
        df_pred=pd.DataFrame(list(zip(self.y_test,y_test_preds)),columns=['True_Response_TestSet','Predicted__Response_TestSet'])
        sns.lmplot(data=df_pred, x='True_Response_TestSet', y='Predicted__Response_TestSet',line_kws={'color': 'fuchsia'})
        plt.ylabel("True_Response_TestSet",fontsize=24)
        plt.xlabel("Predicted__Response_TestSet",fontsize=24)
        plt.title("Predicted vs. True Response TestSet",loc='left',fontsize=24)
        plt.xticks( ha="right",fontsize=24)
        plt.yticks(fontsize=24)
        plt.title('R2_train: ' + str(round(r2_score(self.y_train, y_train_preds),2))+' vs. ' + 'R2_test: ' + str(round(r2_score(self.y_test, y_test_preds),2))+', '+'MSE_train: ' + str(round(mean_squared_error(self.y_train, y_train_preds),2))+' vs. ' + 'MSE_test: ' + str(round(mean_squared_error(self.y_test, y_test_preds),2)),loc="left",fontsize=20) 
     