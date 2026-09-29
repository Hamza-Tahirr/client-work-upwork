from crewai_tools import tool
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from io import BytesIO
import base64

class DataVisualizationTool():
    @tool("Data Visualization")
    def data_viz_tool(data):
        """Useful to visualize data as charts/graphs"""        
        # Example data visualization
        df = pd.DataFrame(data)

        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df)
        plt.title('Climate Data Trends')
        plt.xlabel('Date')
        plt.ylabel('Value')

        # Save plot as a PDF file
        file_path = 'charts.pdf' 
        plt.savefig(file_path, format='pdf')
        plt.close()

        return file_path
