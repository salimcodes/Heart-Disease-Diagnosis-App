# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:34:10 2020

@author: OYINLOLA SALIM O
"""

mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml