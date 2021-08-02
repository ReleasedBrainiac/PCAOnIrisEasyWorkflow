import pandas as pd      
import numpy as np 

from sklearn import decomposition

class PrincipleComponentAnalysisProvider(object):

    _pca:any = None
    _pca_columns:list = None

    def __init__(   self,
                    pca_columns:list = ['', 'PC1', 'PC2', 'PC3'],
                    pca_components:int = 3) -> None:  
        try:

            print ("Init " + __class__.__name__+ " class")
            self._pca_columns = pca_columns
            self._pca = decomposition.PCA(n_components=pca_components)
            
        except Exception as ex:
            raise

    def PerformAnalysis(self, 
                        features:any, 
                        species_dataframe:any,
                        pca:any = None,
                        verbose:int = 0) -> any:
        try:
            if(pca == None): 
                pca = self._pca

            if (verbose > 0): 
                print("Performing Principle Component Analysis\n")
        
            print(pca.fit(features))

            scores_df = pd.DataFrame(pca.transform(features), 
                                     columns=self._pca_columns[1:])

            scores = pd.concat([scores_df, species_dataframe], axis=1)

            if (verbose > 0): 
                print("Compute and retrieve the scores values\n")
                print(scores)

            return scores
        except Exception as ex:
            raise

    def CombinePCAVariances(self, 
                            pc_names:list,
                            pc_col_name:str,
                            explained_variance:any,
                            cumulative_variance:any,
                            verbose:int = 0) -> any:
        try:
            if (pc_names == None):
                pc_names = self._pca_columns

            pc_df = pd.DataFrame(pc_names, columns=[pc_col_name])
            explained_variance_df = pd.DataFrame(explained_variance, columns=['Explained Variance'])
            cumulative_variance_df = pd.DataFrame(cumulative_variance, columns=['Cumulative Variance'])
            pca_explained_variances = pd.concat([pc_df, explained_variance_df, cumulative_variance_df], axis=1)

            if (verbose > 0): 
                print("Finished combining the variances dataframe\n")
                print(pca_explained_variances)

            return pca_explained_variances
        except Exception as ex:
            raise

    def getPCA(self) -> any:
        try:
            return self._pca
        except Exception as ex:
            raise

    def getLoadingsValues(  self,
                            iris_feature_names:any,
                            pca:any = None, 
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
            raise

    def getExplainedVarianceData(self,
                                 pca:any = None, 
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
            raise

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
            raise