import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("laptop_price - dataset.csv")


st.title('Data Visualization Using Streamlit')
st.markdown('`by Group 10 - BM7')


st.markdown("""    
The purpose of this is to convert our previous Data Visualization lesson in [Google Colab Notebook](https://colab.research.google.com/drive/151edx-zGRNvrjmuqXahFZ61FhGAxkGGC?usp=sharing) into a Streamlit Web Application.  
  
[GitHub Repository](https://github.com/princeVillamil/Group10-CSS145) for the source code
""")

# Follow this code #
# def bar_chart():
#   Code

# st.header("Bar Chart Demo") - Name of chart
# st.markdown("""

  # Ideal for comparing categorical data or displaying frequencies, bar charts offer a clear visual representation of values.  
    
  # **Observations:**  
  # 1. Notes
  # **Conclusion:**  
  # 1. Notes
# """)

# bar_chart()

def scatter_price_vs_weight():
  plt.subplots(figsize=(10, 6))
  plt.scatter(df['Weight (kg)'], df['Price (Euro)'], color='blue', alpha=0.6, edgecolor='white',s=65)
  plt.title('Price Vs. Weight',fontsize=16, fontweight='bold')
  plt.xlabel('Weight (kg)')
  plt.ylabel('Price (Euro)')
  plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.9)
  plt.show()


scatter_price_vs_weight()
st.header("Price Vs. Weight Scatter Plot")
st.markdown("""    
  **Observations:**  
  1. This scatter plot will illustrate the correlation between a laptop's price and weight. From this graph, it can be observed that weight plays a significant role in its price. As you can see, as the weight of laptops increases, it will lead to higher prices. I can assume that heavier laptops contain additional features such as larger screens, larger batteries, and overall better hardware, which can significantly change the price.
  **Conclusion:**  
  1. In conclusion, being able to understand this correlation is crucial for consumers in order to find the best laptop in the market for their budget. On the other hand, if you were the manufacturer, it would also be possible to use this as an advantage for your laptops. For example, making larger laptops for a cheaper price may attract consumers.
""")



def gpu_distribution():
  plt.figure(figsize=(10, 9))
  plt.pie(df['GPU_Company'].value_counts().values, labels=df['GPU_Company'].value_counts().index, autopct='%0.2f%%', startangle=45, colors=['#00C7FD', '#76b900', '#ED1C24', '#0091BD'] , explode=[0.05, 0.05, 0.05, 0.05], wedgeprops={'edgecolor':'black', 'linewidth' : 0.5, 'antialiased' : True}, shadow=True)
  plt.axis('equal')
  plt.title('GPU Distribution', fontsize=16, fontweight='bold')
  plt.show()


gpu_distribution()
st.header("GPU Distribution Pie Chart")
st.markdown("""    
  **Observations:**  
  1. This pie chart reveals which GPU brands are more prevalent from the date set provided to us, highlighting which brands hold a larger market share. As seen from the graph, Intel by far has a considerable amount of percentage of the market share compared to its competitors, with ARM being less than one percent.
  **Conclusion:**  
  1. This GPU distribution pie chart provides highlights into the market dynamics, showcasing which brands are currently leading in terms of GPUs, within the given dataset. This info can be vital for manufacturers and consumers because when making decision about product development or purchases it is possible to find the best GPU based on this chart.
""")



