import inspect
import plotly.express as px

from Support.SupportProvider import SupportProvider

class Visualizer():

    _class_name:str = None
    _support:SupportProvider = None

    def __init__(self) -> None:  
        try:
            self._support = SupportProvider()
            self._class_name = __class__.__name__
            
            self.Execute()
        except Exception as ex:
            self._support.ExceptMessage(classname = self._class_name,
                                        funcname=inspect.currentframe().f_code.co_name,
                                        exception=ex)

    def ShowExplainedVariance(self,
                              explained_variance:any,
                              verbose:int = 0) -> None:  
        try:

            if (verbose > 0):
                print("Show Explained Variance")
            
            fig = px.bar(explained_variance, 
                        x='PC', y='Explained Variance',
                        text='Explained Variance',
                        width=800)

            fig.update_traces(texttemplate='%{text:.3f}', textposition='outside')
            fig.show()
        except Exception as ex:
            self._support.ExceptMessage(classname = self._class_name,
                                        funcname=inspect.currentframe().f_code.co_name,
                                        exception=ex)
                                        

if __name__ == "__main__":
    Visualizer()