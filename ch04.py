# -*- coding:utf-8 -*-

import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly

@st.cache_data
def load_data():
    df = sns.load_dataset('tips')
    return df
def main():
    st.title("Streamlit with Matplotlib")
    tips = load_data()

    # 시각화 아무거나 하세요
    # plt.show()
    # fig, ax = plt.subplots(figsize=(10, 10))
    # ax.hist(tips['total_bill'])
    # st.pyplot(fig)

    st.write('-'*50)
    # 데이터가공
    m_tips = tips.loc[tips['sex'] == 'Male', :]
    f_tips = tips.loc[tips['sex'] == 'Female', :]
    # 시각화 차트
    fig, ax = plt.subplots(ncols=2, figsize=(10, 6), sharex=True, sharey=True)
    ax[0].scatter(x=m_tips['total_bill'], y=m_tips['tip'])
    ax[0].set_title('Male')
    ax[1].scatter(x=f_tips['total_bill'], y=f_tips['tip'])
    ax[1].set_title('Female')

    st.pyplot(fig)


    #seaborn으로 시각화 코드 아무거나 작성
    fig, ax = plt.subplots()
    sns.distplot(m_tips['total_bill'])

    st.pyplot(fig)

    #

    fig = make_subplots(rows=1,
                        cols=2,
                        subplot_titles=('Male', 'Female'),
                        shared_yaxes=True,
                        shared_xaxes=True,
                        x_title='Total Bill($)'
                        )
    fig.add_trace(go.Scatter(x=m_tips['total_bill'], y=m_tips['tip'], mode='markers'), row=1, col=1)
    fig.add_trace(go.Scatter(x=f_tips['total_bill'], y=f_tips['tip'], mode='markers'), row=1, col=2)
    fig.update_yaxes(title_text="Tip($)", row=1, col=1)
    fig.update_xaxes(range=[0, 60])
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
if __name__ == '__main__':
    main()