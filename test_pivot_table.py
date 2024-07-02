import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

lst = []

outer_folder_to_view = r"C:\Users\Owner\OneDrive\Desktop\Kwiat Lab\MCF Project\Quantum signal characterization\Data"
for folder in os.listdir(outer_folder_to_view):
    folder_to_view = f'{outer_folder_to_view}/{folder}'
    for file in os.listdir(folder_to_view):
        full_path = f'{folder_to_view}/{file}'
        df = pd.read_csv(full_path, sep='\t', header=None)
        df = df[df.iloc[:, 1] != 0].iloc[:, 1:2]
        s = pd.Series(df[1].values)
        mean = s.mean()
        standard_deviation = s.std()
        start, end = file.split("-")
        list = [start, end, mean, standard_deviation]
        lst.append(list)

column_names=["from", "to", "mean", "standard_deviation"]
df = pd.DataFrame(lst, columns=column_names)
all_data_mean = df.pivot_table(index="from", columns="to", values="mean")
data_needed_mean = all_data_mean.loc[["1","2","3", "2'", "3'"], ["1'", "2", "4", "3'", "4'"]]
all_data_std = df.pivot_table(index="from", columns="to", values="standard_deviation")
data_needed_std = all_data_std.loc[["1","2","3", "2'", "3'"], ["1'", "2", "4", "3'", "4'"]]

svm_1 = sns.heatmap(data_needed_mean, annot=True, fmt=".0f", cmap="crest")
svm_1.set(xlabel="Output", ylabel="Input")
svm_1.set_title(folder + " mean plot")
plt.savefig(folder + '-mean.png', dpi=400)
plt.clf()
svm_2 = sns.heatmap(data_needed_std, annot=True, fmt=".0f", cmap="crest")
svm_2.set(xlabel="Output", ylabel="Input")
svm_2.set_title(folder + " std plot")
plt.savefig(folder + '-std.png', dpi=400)
plt.clf()