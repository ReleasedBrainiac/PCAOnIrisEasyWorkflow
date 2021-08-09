import plotly.express as px
import plotly.graph_objects as go

from plotly.subplots import make_subplots

class Visualizer():

    def __init__(self) -> None:  
        try:
            print ("Init " + __class__.__name__+ " class")
        except Exception as ex:
            raise

    def ShowExplainedVariance(self,
                              explained_variance:any,
                              verbose:int = 0) -> None:  
        try:

            if (verbose > 0):
                print("Show Explained Variance")
            
            fig = px.bar(explained_variance, 
                         x='PC', 
                         y='Explained Variance',
                         text='Explained Variance',
                         width=800)

            fig.update_traces(texttemplate='%{text:.3f}', textposition='outside')
            fig.show()
        except Exception as ex:
            raise
                                        
    def ShowCombinedVariance(   self,
                                combined_variances:any,
                                use_seperate_plot:bool = True,
                                verbose:int = 0) -> None:  
        try:

            if (verbose > 0):
                print("Shown combined (explained + cumulative) variances?")

            cmlvarscatter = go.Scatter( x=combined_variances['PC'],
                                        y=combined_variances['Cumulative Variance'],
                                        marker=dict(size=15, 
                                                    color="LightSeaGreen")
                                        )

            expvarscatter = go.Bar( x=combined_variances['PC'],
                                    y=combined_variances['Explained Variance'],
                                    marker=dict(color="RoyalBlue")
                                    )
            
            if (not use_seperate_plot):
                fig = make_subplots(rows=1, cols=2)
                fig.add_trace(cmlvarscatter, row=1, col=1)
                fig.add_trace(expvarscatter, row=1, col=1)
            else:
                fig = go.Figure()
                fig.add_trace(cmlvarscatter)
                fig.add_trace(expvarscatter)

            fig.show()
        except Exception as ex:
            raise

    def Show3DPrincipleComponents(  self,
                                    scores:any,
                                    use_tight:bool = False,
                                    verbose:int = 0) -> None:  
        try:

            if (verbose > 0):
                print("Show Principle components scatter 3D")
            
            fig = px.scatter_3d(scores, 
                                x='PC1', 
                                y='PC2', 
                                z='PC3',
                                color='Species',
                                symbol='Species',
                                opacity=0.5)

            if(use_tight):
                fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))

            fig.update_layout(template='seaborn') # "plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"

            fig.show()
        except Exception as ex:
            raise

    def Show3DLoadings( self,
                        loadings:any,
                        use_tight:bool = False,
                        verbose:int = 0) -> None:  
        try:

            if (verbose > 0):
                print("Show Loadings scatter 3D")
            
            loadings_label = loadings.index
            fig = px.scatter_3d(loadings, 
                                x='PC1', 
                                y='PC2', 
                                z='PC3',
                                text = loadings_label)

            if(use_tight):
                fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))

            fig.update_layout(template='seaborn') # "plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"

            fig.show()
        except Exception as ex:
            raise

if __name__ == "__main__":
    Visualizer()