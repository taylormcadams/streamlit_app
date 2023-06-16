import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import io


web_apps = st.sidebar.selectbox("Select Web Apps",
                                ("Exploratory Data Analysis", "Don't pick this one"))


if web_apps == "Exploratory Data Analysis": 

  uploaded_file = st.sidebar.file_uploader("Choose a file")

  if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)
    show_df = st.checkbox("Show Data Frame", key="disabled")

    if show_df:
      st.write(df)

    column_type = st.sidebar.selectbox('Select Data Type',
                                       ("Numerical", "Categorical"))

    if column_type == "Numerical":
      numerical_column = st.sidebar.selectbox(
          'Select a Column', df.select_dtypes(include=['int64', 'float64']).columns)

      # histogram
      choose_color = st.color_picker('Pick a Color', "#69b3a2")
      choose_opacity = st.slider(
          'Color Opacity', min_value=0.0, max_value=1.0, step=0.05)

      hist_bins = st.slider('Number of bins', min_value=5,
                            max_value=150, value=30)
      hist_title = st.text_input('Set Title', 'Histogram')
      hist_xtitle = st.text_input('Set x-axis Title', numerical_column)

      fig, ax = plt.subplots()
      ax.hist(df[numerical_column], bins=hist_bins,
              edgecolor="black", color=choose_color, alpha=choose_opacity)
      ax.set_title(hist_title)
      ax.set_xlabel(hist_xtitle)
      ax.set_ylabel('Count')

      st.pyplot(fig)
      filename = "plot.png"
      fig.savefig(filename,dpi = 300)

      # Display the download button
      with open("plot.png", "rb") as file:
        btn = st.download_button(
            label="Download image",
            data=file,
            file_name="flower.png",
            mime="image/png"
        )
       # categorical variable 
    if column_type == "Categorical": 
        categorical_column = st.sidebar.selectbox('Select a Column',
                                                  df.select_dtypes(include=['object']).columns) 
        st.subheader("Proportions Table")
        head_value = st.slider('Number to display', min_value=1, 
                               max_value=df[categorical_column].nunique(), value=5)
        st.table(df[categorical_column].value_counts(normalize=True).head(head_value))

        st.subheader("Barplot")
        col1, col2 = st.columns(2)
        choose_color = col1.color_picker('Pick a Color', "#69b3a2")

        fig, ax = plt.subplots()
        to_display = col2.slider('How many to display', min_value=1, 
                                 max_value=df[categorical_column].nunique(), value=5)
        bar_title = st.text_input('Set Title', 'Barplot')
        bar_xaxis = st.text_input('Set x-axis Title', categorical_column)
        test = df[categorical_column].value_counts(normalize=True)
        ax.bar(test.index[0:to_display], test.values[0:to_display],
                        edgecolor="black", color=choose_color)
        ax.set_title(bar_title)
        ax.set_xlabel(bar_xaxis)
        ax.set_ylabel('Proportion')

        st.pyplot(fig)
        filename = "plot.png"
        fig.savefig(filename,dpi = 300)

