import inspect
import pandas as pd      
import numpy as np 

from sklearn import decomposition
from Support.SupportProvider import SupportProvider

class PrincipleComponentAnalysisProvider(object):

    _class_name:str = None
    _support:SupportProvider = None
    _pca:any = None

    def __init__(self,
                 pca_components:int = 3) -> None:  
        try:

            print("Init PrincipleComponentAnalysis class")
            self._class_name = __class__.__name__
            self._support = SupportProvider()
            self._pca = decomposition.PCA(n_components=pca_components)
            
        except Exception as ex:
            self._support.ExceptMessage(classname = self._class_name,
                                        funcname=inspect.currentframe().f_code.co_name,
                                        exception=ex)

    def PerformAnalysis(self, 
                        features:any, 
                        pca:any = None,
                        verbose:int = 0) -> any:
        try:
            if(pca == None): 
                pca = self._pca

            if (verbose > 0): 
                print("Performing Principle Component Analysis\n")
        
            print(pca.fit(features))

            scores = pca.transform(features)
            scores_df = pd.DataFrame(scores, columns=['PC1', 'PC2', 'PC3'])

            if (verbose > 0): 
                print("Compute and retrieve the scores values\n")
                print(scores_df)

            return scores_df
        except Exception as ex:
            self._support.ExceptMessage(classname = self._class_name,
                                        funcname=inspect.currentframe().f_code.co_name,
                                        exception=ex)

    def CombinePCAVariances(self, 
                            pc_names:list,
                            pc_col_name:str,
                            explained_variance:any,
                            cumulative_variance:any,
                            verbose:int = 0) -> any:
        try:

            pc_df = pd.DataFrame(pc_names, columns=[pc_col_name])
            explained_variance_df = pd.DataFrame(explained_variance, columns=['Explained Variance'])
            cumulative_variance_df = pd.DataFrame(cumulative_variance, columns=['Cumulative Variance'])
            pca_explained_variances = pd.concat([pc_df, explained_variance_df, cumulative_variance_df], axis=1)

            if (verbose > 0): 
                print("Finished combining the variances dataframe\n")
                print(pca_explained_variances)

            return pca_explained_variances
        except Exception as ex:
            self._support.ExceptMessage(classname = self._class_name,
                                        funcname=inspect.currentframe().f_code.co_name,
                                        exception=ex)

    def getPCA(self) -> any:
        try:
            return self._pca
        except Exception as ex:
            self._support.ExceptMessage(classname = self._class_name,
                                        funcname=inspect.currentframe().f_code.co_name,
                                        exception=ex)

    def getLoadingsValues(self,
                         pca:any, 
                         iris_feature_names:any,
                         verbose:int = 0) -> any:
        try:

            if(pca == None): 
                pca = self._pca

            loadings = pca.components_.T
            df_loadings = pd.DataFrame(loadings, columns=['PC1', 'PC2','PC3'], index=iris_feature_names)

            if (verbose > 0): 
                print("Retrieve the loadings values\n")
                print(df_loadings)

            return df_loadings
        except Exception as ex:
            self._support.ExceptMessage(classname = self._class_name,
                                        funcname=inspect.currentframe().f_code.co_name,
                                        exception=ex)

    def getExplainedVarianceData(self,
                                 pca:any, 
                                 verbose:int = 0) -> any:
        try:

            if(pca == None): 
                pca = self._pca

            explained_variance = pca.explained_variance_ratio_

            if (verbose > 0): 
                print("Prepared the explained variance data\n")            
                print(explained_variance)

            return  np.insert(explained_variance, 0, 0)

        except Exception as ex:
            self._support.ExceptMessage(classname = self._class_name,
                                        funcname=inspect.currentframe().f_code.co_name,
                                        exception=ex)

    def getExplainedCumulativeData(self,
                                 explained_variance:any, 
                                 verbose:int = 0) -> any:
        try:

            cumulative_variance = np.cumsum(np.round(explained_variance, decimals=3))

            if (verbose > 0): 
                print("Prepared the cumulative variance data\n")            
                print(cumulative_variance)

            return cumulative_variance

        except Exception as ex:
            self._support.ExceptMessage(classname = self._class_name,
                                        funcname=inspect.currentframe().f_code.co_name,
                                        exception=ex)