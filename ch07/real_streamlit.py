import streamlit as st
import pandas as pd
import plotly.express as px
def main():

    df = pd.read_csv('./data/seoul_real_estate.csv')

    # Plotly Express를 사용하여 히스토그램 그리기
    fig = px.histogram(df, x="HOUSE_TYPE")

    # Streamlit에서 Plotly 그래프를 표시하기 위해 st.plotly_chart 사용
    st.plotly_chart(fig)

    st.write("-" * 50)

    df['BUILD_YEAR'] = pd.to_numeric(df['BUILD_YEAR'], errors='coerce')
    df['DECADE_BUILT'] = (df['BUILD_YEAR']//10) * 10

    df_filtered = df[df['DECADE_BUILT'] != 0]
    fig = px.histogram(df_filtered, x="DECADE_BUILT")
    st.plotly_chart(fig)

    st.write("-" * 50)
    df['DEAL_YMD'] = pd.to_datetime(df['DEAL_YMD'], errors='coerce')

    transactions_by_date = df.groupby('DEAL_YMD').size().reset_index(name='Transaction_Count')

    # Create line chart
    fig = px.line(transactions_by_date, x='DEAL_YMD', y='Transaction_Count', title='Transaction Count Over Time')
    fig.update_xaxes(title_text='Date')
    fig.update_yaxes(title_text='Transaction Count')

    # Show the plot
    st.plotly_chart(fig)

    options = st.multiselect(
        '건물용도',
        ['단독다가구', '오피스텔', '연립다세대', '아파트'])

    result = df[df['HOUSE_TYPE'].isin(options)].reset_index(drop=True)
    st.table(result)

    st.write("-" * 50)
    st.write(df.describe())

if __name__ == "__main__":
    main()