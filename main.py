"""
Resources: 

1. https://github.com/dataprofessor/code/blob/master/python/PCA_analysis.ipynb
2. https://plotly.com/python/bar-charts/
3. https://plotly.com/python/creating-and-updating-figures/
4. https://plotly.com/python/3d-scatter-plots/
5. https://plotly.com/python-api-reference/plotly.express.html
6. https://plotly.com/python/templates/

"""
import inspect

from Visualization.Visualizer import Visualizer
from Dataset.DatasetProvider import DatasetProvider
from Support.SupportProvider import SupportProvider
from PCA.PrincipleComponentAnalysis import PrincipleComponentAnalysisProvider

class IrisPrincipleComponentAnalysis():

    _class_name:str = None
    _support:SupportProvider = None
    _pca_components:int = 3
    _pc_names:list = ['','PC1', 'PC2', 'PC3']
    _pc_col_name:str = 'PC'

    def __init__(self) -> None:  
        try:
            self._support = SupportProvider()
            self._class_name = __class__.__name__
            
            self.Execute()
        except Exception as ex:
            self._support.ExceptMessage(classname = self._class_name,
                                        funcname=inspect.currentframe().f_code.co_name,
                                        exception=ex)

    def Execute(self,
                verbose:int = 0) -> any:

        try:
            dp:DatasetProvider = DatasetProvider()
            pcap:PrincipleComponentAnalysisProvider = PrincipleComponentAnalysisProvider(pca_components=self._pca_components)
            vs:Visualizer = Visualizer()

            if (verbose > 0): 
                print("Load and preprocess iris dataset.")

            features, targets = dp.LoadIrisDataset()
            Species = dp.getSpecies(targets)
            iris_feature_names = dp.getIrisFeatureNames()

            if (verbose > 0): 
                print("Start Principle Component Analysis.")
            
            scores = pcap.PerformAnalysis(features=features, species_dataframe=Species)
            loadings = pcap.getLoadingsValues(iris_feature_names=iris_feature_names)
            explained_variance = pcap.getExplainedVarianceData()
            cumulative_variance = pcap.getExplainedCumulativeData(explained_variance=explained_variance)
            combined_variances = pcap.CombinePCAVariances(  pc_names=self._pc_names, 
                                                            pc_col_name=self._pc_col_name,
                                                            explained_variance=explained_variance, 
                                                            cumulative_variance=cumulative_variance)

            if (verbose > 0): 
                print("Start plotting Principle Component Analysis results.")

            vs.ShowExplainedVariance(explained_variance=combined_variances)

            vs.ShowCombinedVariance(combined_variances=combined_variances, 
                                    use_seperate_plot=True)

            vs.Show3DPrincipleComponents(   scores=scores, 
                                            use_tight=False)

            vs.Show3DLoadings(  loadings=loadings, 
                                use_tight=False)
            

        except Exception as ex:
            self._support.ExceptMessage(classname = self._class_name,
                                        funcname=inspect.currentframe().f_code.co_name,
                                        exception=ex)

if __name__ == "__main__":
    IrisPrincipleComponentAnalysis()