import pandas as pd
import numpy as np
import pymc3 as pm

from pyei.data import Datasets
from pyei.two_by_two import TwoByTwoEI
from pyei.goodmans_er import GoodmansER
from pyei.goodmans_er import GoodmansERBayes
from pyei.r_by_c import RowByColumnEI

from pyei.plot_utils import tomography_plot
from pyei.plot_utils import plot_precinct_scatterplot
df = pd.read_csv("tracts.csv")

# generate percentages
# check on datapoints by year

race_fractions = np.array(df[["pct_white", "pct_black", "pct_asian", "pct_latino", "pct_native"]]).T
access_fractions = np.array(df[["pct_internet","pct_none"]]).T

race_names = ["White", "Black", "Latino", "Latino", Native]
access_names = ["Broadband Access", "No Broadband Access"]

tract_pops = np.array(df["population"])
