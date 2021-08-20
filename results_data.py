# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# %%
#import and split data
all_results = pd.read_excel("all_student_data.xlsx", index_col="Student ID")

#print(results.columns)
results = pd.melt(all_results, id_vars=["Full Name", "programme", "cohort"], var_name="assessment", value_name="grade").reset_index(drop=True)

#split by cohort
jan_results = results[results["cohort"] == "January"].reset_index(drop=True)
sept_results = results[results["cohort"] == "September"].reset_index(drop=True)
mar_results = results[results["cohort"] == "March"].reset_index(drop=True)

#split by programme
ify_results = results[results["programme"] == "IFY"].reset_index(drop=True)
iy1_results = results[results["programme"] == "IY1"].reset_index(drop=True)
pmp_results = results[results["programme"] == "PMP"].reset_index(drop=True)

#split by programme and cohort
sept_ify_results = results[(results["programme"] == "IFY") & (results["cohort"] == "September")].reset_index(drop=True)
sept_iy1_results = results[(results["programme"] == "IY1") & (results["cohort"] == "September")].reset_index(drop=True)
jan_ify_results = results[(results["programme"] == "IFY") & (results["cohort"] == "January")].reset_index(drop=True)
jan_iy1_results = results[(results["programme"] == "IY1") & (results["cohort"] == "January")].reset_index(drop=True)
mar_pmp_results = results[(results["programme"] == "PMP") & (results["cohort"] == "March")].reset_index(drop=True)