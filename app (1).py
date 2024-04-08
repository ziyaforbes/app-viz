import streamlit as st
st.write('# Chocolate Ratings')
st.write('## Run Streamlit on Colab')

import streamlit as st
st.image("Chocolate .jpeg", width=100)

st.sidebar.header("Dashboard")
st.sidebar.markdown("---")

import pandas as pd
import numpy as np
df = pd.read_csv('chocolate.csv')
df.head()

st.caption("Review Date & Rating Relationship")
import streamlit as st
import pandas as pd
import numpy as np
df = pd.read_csv('chocolate.csv')
st.line_chart(data=df,x="review_date",y="rating")

st.caption("Cocao Percent & Rating Relationship")
import streamlit as st
import pandas as pd
import numpy as np
df = pd.read_csv('chocolate.csv')
st.bar_chart(data=df,x="cocoa_percent",y="rating")

tab1, tab2 = st.tabs(["Review Date & Rating Relationship", "Coacao Percent & Rating Relationship"])

tab1.subheader("Review Date & Rating Relationship")
# Display a line chart for the selected variables
tab1.line_chart(data=filtered_df, x=symbols[0], y=symbols[1], width=0, height=0, use_container_width=True)

tab2.subheader("Coacao Percent & Rating Relationship")
# Display a bar chart for the selected variables
tab2.bar_chart(data=filtered_df, x=symbols[0], y=symbols[1], use_container_width=True)

t.dataframe(df.describe())

if st.button("Show Describe Code"):
        code = '''df.describe()'''
        st.code(code, language='python')

if st.button("Generate Report"):
  import streamlit as st
  import streamlit.components.v1 as components

  st.title('Chocolate Report in Streamlit')

  # Display the Chocolate report
  report_path = 'report.html'
  HtmlFile = open(report_path, 'r', encoding='utf-8')
  source_code = HtmlFile.read()
  components.html(source_code, height=1000,width=1000)


list_variables = df.columns

# Display a header for the Visualization section
st.markdown("## Visualization")
symbols = st.multiselect("Select two variables", list_variables, ["review_date", "rating"])


review_date_min, review_date_max = st.sidebar.slider('Select review_date Range', min_value=int(df['review_date'].min()), max_value=int(df['review_date'].max()), value=(int(df['review_date'].min()), int(df['review_date'].max())))
rating_min, rating_max = st.sidebar.slider('Select rating Range', min_value=float(df['rating'].min()), max_value=float(df['rating'].max()), value=(float(df['rating'].min()), float(df['rating'].max())))

# Filtering the dataframe based on the slider values
filtered_df = df[(df['review_date'] >= quality_min) & (df['rating'] <= review_date_max) & (df['rating'] >= rating_min) & (df['raing'] <= rating_max)]

