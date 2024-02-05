# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import scipy.stats as stats

# アプリのタイトルと説明を表示
st.title("人生の羅針盤")
st.markdown("金融情報を入力すると、最適なライフプランを提案してくれるアプリです。")

# サイドバーに金融情報の入力欄を作成
st.sidebar.header("金融情報の入力")
# 年収の入力
income = st.sidebar.number_input("年収（万円）", min_value=0, max_value=10000, value=500, step=10)