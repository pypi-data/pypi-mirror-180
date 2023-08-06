#Import linear algebra and data manipulation packages
import pandas as pd


#Import machine learning packages
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split #split


#Define a general model class
class model():
    """ 
    general model class for implementing modelling.
    
    Attributes:
    X (pandas dataframe) representing the design matrix 
    y (pandas dataframe) representing the response variable
    """
    
    def __init__(self,X=pd.DataFrame() ,y=pd.DataFrame() ): 
        
        self.X=X
        self.y=y
        self.y
        self.X_train=pd.DataFrame()
        self.X_test=pd.DataFrame()
        self.y_train=pd.DataFrame()
        self.y_test=pd.DataFrame()
        
    def load_dataset(self,file_name,response):
        """Method to import data from a csv file (in the same directory). The data object is just a dictionary containing all the available information
        and then converted to pandas dataframe respectively assigned to design matrix X and response y.
                
        Args:
            None
        
        Returns:
            None
        
        """
        #import csv dataset
        df = pd.read_csv(file_name)
        #update design matrix X in the main corpus of model class
        self.X=df.drop(columns =response)
        #update response y in the main corpus of model class
        self.y=df[response]        
        
    def split_method(self):
        """Method to split the response and design matrix X and response y to train and test sets respectively, thus
        X_train, X_test, y_train, y_test using the train_test_split() method from sklearn.
                
        Args:
            None
        
        Returns:
            None
        
        """
        
        #Split train/test set and update the dataframes self.X_train, self.X_test, self.y_train and self.y_test respectively
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size = 0.3, random_state=2022)          