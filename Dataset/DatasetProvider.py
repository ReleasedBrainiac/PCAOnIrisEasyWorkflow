import pandas as pd 

from sklearn import datasets
from sklearn.preprocessing import scale

class DatasetProvider(object):

    _iris:any = None

    def __init__(self) -> None:  
        try:
            print ("Init " + __class__.__name__+ " class")
            self._iris = datasets.load_iris()

        except Exception as ex:
            raise

    def LoadIrisDataset(self, verbose:int = 0) -> any:
        try:
            features = self._iris.data
            targets = self._iris.target

            if (verbose > 0): 
                print("Load Iris Dataset\n")
                print("Feature names: " + str(self.getIrisFeatureNames()))
                print("Feature_shape: " + str(features.shape) + "\n")
                print("Target names: " + str(self.getIrisTargetNames()))
                print("Target_shape: " + str(targets.shape) + "\n")

            if (verbose > 0): 
                print("Scale Features")

            return scale(features), targets

        except Exception as ex:
            raise

    def getSpecies(self, target, verbose:int = 0) -> any:
        try:
            if (verbose > 0): 
                print("Load Iris Species")

            targets_label = []

            for i in target:
                if i == 0:
                    targets_label.append('Setosa')
                elif i == 1:
                    targets_label.append('Versicolor')
                else:
                    targets_label.append('Virginica')

            return pd.DataFrame(targets_label, columns=['Species'])
        except Exception as ex:
            raise

    def getIrisFeatureNames(self) -> any:
        try:
            return self._iris.feature_names
        except Exception as ex:
            raise

    def getIrisTargetNames(self) -> any:
        try:
            return self._iris.target_names
        except Exception as ex:
            raise