import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

outer_folder_to_view = r"C:\Users\Owner\OneDrive\Desktop\Kwiat Lab\MCF Project\Quantum signal characterization\Data"
for folder in os.listdir(outer_folder_to_view):
    folder_to_view = f'{outer_folder_to_view}/{folder}'
    first, second = folder.split("-")
    if first == "Unprimed":
        index=["1", "2", "3", "4"]
        if second == "Unprimed":
            Cols=["1", "2", "3", "4"]
        else:
            Cols=["1'", "2'", "3'", "4'"]
    elif first == "Primed":
        index=["1'", "2'", "3'", "4'"]
        if second == "Unprimed":
            Cols=["1", "2", "3", "4"]
        else:
            Cols=["1'", "2'", "3'", "4'"]
    else:
        continue
    df_1 = pd.DataFrame(index=index, columns=Cols, dtype=float)
    df_2 = pd.DataFrame(index=index, columns=Cols, dtype=float)

    for file in os.listdir(folder_to_view):
        full_path = f'{folder_to_view}/{file}'
        df = pd.read_csv(full_path, sep='\t', header=None)
        df = df[df.iloc[:, 1] != 0].iloc[:, 1:2]
        s = pd.Series(df[1].values)
        start, end = file.split("-")
        df_1.loc[start, end] = s.mean()
        df_2.loc[start, end] = s.std()

    svm_1 = sns.heatmap(df_1, annot=True, fmt=".0f", cmap="crest")
    svm_1.set(xlabel="Output", ylabel="Input")
    svm_1.set_title(folder + " mean plot")
    plt.savefig(folder + '-mean.png', dpi=400)
    plt.clf()
    svm_2 = sns.heatmap(df_2, annot=True, fmt=".0f", cmap="crest")
    svm_2.set(xlabel="Output", ylabel="Input")
    svm_2.set_title(folder + " std plot")
    plt.savefig(folder + '-std.png', dpi=400)
    plt.clf()