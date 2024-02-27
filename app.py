import streamlit as st

import pandas as pd
from database import get_data
from database import get_merged
from database import get_student_info
from plotting import plot_df
from predicting import predict


def show_map():    
    st.session_state.df = get_data(st.session_state.rank, st.session_state.loc, st.session_state.size)

def show_proba():
    st.session_state.df4 = get_merged()
    st.session_state.s = get_student_info(st.session_state.rank, st.session_state.loc, st.session_state.size, \
                         st.session_state.gpa, st.session_state.sat)
        
def side_show():
    # min_adm = st.sidebar.number_input('Min Admission Rate', 0., 1.0, value=1.00, format='%0.2f', step=0.01)
    st.sidebar.multiselect('Ranking', ('1-30', '31-50', '51-100'), key='rank')
    st.sidebar.multiselect('Location Setting', ('Urban', 'Suburban', 'Rural'), key='loc')
    st.sidebar.multiselect('University Size', ('Large', 'Medium', 'Small'), key='size')
    st.sidebar.button(label='Search for universities', on_click=show_map)
    
    st.sidebar.markdown("---")

    st.sidebar.number_input('Your GPA', 0., 4.0, value=3.50, format='%0.2f', step=0.01, key='gpa')
    st.sidebar.number_input('Your SAT', 0, 1600, value=1450, step=10, key='sat')
    st.sidebar.button(label='Display admission probabilities', on_click=show_proba)


def app():
    st.set_page_config(layout="wide", initial_sidebar_state="expanded")
    side_show()
    st.title('University Selection')
    st.write('Explore US universities! The streamlit app filters the universities that match \
    with your preferences and uses machine learning algorithms to predict your admission probability for those universities.')
    
    st.markdown("---")

    st.write('Set your preferences for universities to get started.')
    st.write('(You can then input your GPA and SAT to further explore admission probability for your preferred universities.)')

    
    try:
        c1, c2=st.columns([1.75,1])
        
        c1.write(plot_df(st.session_state.df))
        u_list=[]
        prob_list=[]
        for i in range(len(st.session_state.s)):
            university = st.session_state.s.iloc[i][0]
            probability = predict(st.session_state.df4, st.session_state.s.iloc[i][1], \
                                  st.session_state.s.iloc[i][2], st.session_state.s.iloc[i][3])
            u_list.append(university)
            prob_list.append(str(format(probability,'0.2f')))
       
        c2.write('Your admission probability for filtered universities')
        c2.dataframe(pd.DataFrame({'Probability': prob_list}, index=u_list))

    except:
        pass
    
if __name__ == '__main__':
    app()