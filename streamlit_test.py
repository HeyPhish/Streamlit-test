#%%
import pandas as pd
import numpy as np
import streamlit as st
import os
import json
from zipfile import ZipFile
import altair as at
#%%

import kaggle
#%%

# %%
kaggle.api.authenticate()
# %%

!kaggle datasets download -d yamqwe/provisional-covid-19-death-counts-by-sex-age-ande

# %%
@st.cache
data_load_state = st.text('Loading data...')
df = pd.read_csv("provisional-covid-19-death-counts-by-sex-age-ande.zip")
data_load_state.text('Loading data...done!')
# %%
df.head()
# %%
