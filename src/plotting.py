import pandas as pd
import numpy as np
import extraction
import matplotlib.pyplot as plt


extraction.df_all.plot(x='Experiment Date', y='Tensile stress at Break (Standard)')

plt.show()