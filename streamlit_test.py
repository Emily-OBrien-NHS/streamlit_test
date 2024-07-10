import streamlit as st
import numpy as np
import time
from concurrent.futures import ProcessPoolExecutor, as_completed


def func(x):
    return(x**2)

st.set_page_config(page_title="Test",
                   layout="wide",
                   initial_sidebar_state="expanded",
                   menu_items={'About': "Streamlit Test"})
st.title('Test')


if st.button('Run code'):
    st.subheader('Code in progress:')
    with st.empty():
        t0 = time.time()

        np_lst = []
        for i in range(10000):
            np_lst.append(func(i))
        t1 = time.time()

        par_lst = Parallel(n_jobs=-1)(delayed(func)(i) for i in range(10000))
        t2 = time.time()

        pp_lst = []
        with ProcessPoolExecutor() as executor:
            futures = [executor.submit(func, i) for i in range(10000)]
            for future in as_completed(futures):
                pp_lst.append(future.result())
        t3 = time.time()

    st.success('Done!')

    st.subheader(f'No parallel mean: {np.mean(np_lst)}')
    st.subheader(f'No parallel time: {t1-t0}')
    st.subheader(f'Parallel mean: {np.mean(par_lst)}')
    st.subheader(f'Parallel time: {t2-t1}')
    st.subheader(f'Process Pool mean: {np.mean(pp_lst)}')
    st.subheader(f'Process Pool time: {t3-t2}')

