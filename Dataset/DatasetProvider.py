import inspect
import pandas as pd 

from sklearn import datasets
from sklearn.preprocessing import scale
from Support.SupportProvider import SupportProvider

class DatasetProvider(object):

    _class_name:str = None
    _support:SupportProvider = None
    _iris:any = None

    def __init__(self) -> None:  
        try:

            print("Init DatasetProvider class")
            self._class_name = __class__.__name__
            self._support = SupportProvider()
            
            _iris = datasets.load_iris()

        except Exception as ex:
            self._support.ExceptMessage(classname = self._class_name,
                                        funcname=inspect.currentframe().f_code.co_name,
                                        exception=ex)

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
            self._support.ExceptMessage(classname = self._class_name,
                                        funcname=inspect.currentframe().f_code.co_name,
                                        exception=ex)

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
            self._support.ExceptMessage(classname = self._class_name,
                                        funcname=inspect.currentframe().f_code.co_name,
                                        exception=ex)

    def getIrisFeatureNames(self) -> any:
        try:
            return self.iris.feature_names
        except Exception as ex:
            self._support.ExceptMessage(classname = self._class_name,
                                        funcname=inspect.currentframe().f_code.co_name,
                                        exception=ex)

    def getIrisTargetNames(self) -> any:
        try:
            return self.iris.target_names
        except Exception as ex:
            self._support.ExceptMessage(classname = self._class_name,
                                        funcname=inspect.currentframe().f_code.co_name,
                                        exception=ex)