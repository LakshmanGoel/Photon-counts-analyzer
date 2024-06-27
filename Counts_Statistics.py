import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

outer_folder_to_view = r"C:\Users\Owner\OneDrive\Desktop\Kwiat Lab\MCF Project\Quantum signal characterization"
for folder in os.listdir(outer_folder_to_view):
    folder_to_view = f'{outer_folder_to_view}/{folder}'
    if folder.split("-")[0] == "Unprimed":
        Cols=["1", "2", "3", "4"]
        if folder.split("-")[1] == "Unprimed":
            index=["4", "3", "2", "1"]
        else:
            index=["4'", "3'", "2'", "1'"]
    elif folder.split("-")[0] == "Primed":
        Cols=["1'", "2'", "3'", "4'"]
        if folder.split("-")[1] == "Unprimed":
            index=["4", "3", "2", "1"]
        else:
            index=["4'", "3'", "2'", "1'"]
    else:
        continue
    df_1 = pd.DataFrame(index=index, columns=Cols, dtype=float)
    df_2 = pd.DataFrame(index=index, columns=Cols, dtype=float)

    for file in os.listdir(folder_to_view):
        full_path = f'{folder_to_view}/{file}'
        df = pd.read_csv(full_path, sep='\t', header=None)
        # df = df.iloc[df.iloc[:,1]>0,1] (Write in the new version)
        df.drop([0, 2, 3, 4, 5, 6, 7, 8, 9], axis=1, inplace=True)
        df.drop(df[df[1]==0].index, inplace=True)
        s = pd.Series(df[1].values)
        # start, end = file.split() (Write in the new version)
        df_1.loc[file.split("-")[1], file.split("-")[0]] = s.mean()
        df_2.loc[file.split("-")[1], file.split("-")[0]] = s.std()

    svm_1 = sns.heatmap(df_1, annot=True, fmt=".0f", cmap="crest")
    svm_1.set(xlabel="Input", ylabel="Output")
    svm_1.set_title(folder + " mean plot")
    plt.savefig(folder + '-mean.png', dpi=400)
    plt.clf()
    svm_2 = sns.heatmap(df_2, annot=True, fmt=".0f", cmap="crest")
    svm_2.set(xlabel="Input", ylabel="Output")
    svm_2.set_title(folder + " std plot")
    plt.savefig(folder + '-std.png', dpi=400)
    plt.clf()

#############################################################
# index= ["4", "3", "2", "1"]
# Cols = ["1", "2", "3", "4"]
# df_1 = pd.DataFrame(index=index, columns=Cols, dtype=float)
# df_2 = pd.DataFrame(index=index, columns=Cols, dtype=float)

# folder_to_view = r"C:\Users\Owner\OneDrive\Desktop\Kwiat Lab\MCF Project\Quantum signal characterization\Unprimed-Unprimed"

# for file in os.listdir(folder_to_view):
#     full_path = f'{folder_to_view}/{file}'
#     df = pd.read_csv(full_path, sep='\t', header=None)
#     df.drop([0, 2, 3, 4, 5, 6, 7, 8, 9], axis=1, inplace=True)
#     df.drop(df[df[1]==0].index, inplace=True)
#     s = pd.Series(df[1].values)
#     df_1.loc[file.split("-")[1], file.split("-")[0]] = s.mean()
#     df_2.loc[file.split("-")[1], file.split("-")[0]] = s.std()

# os.makedirs(r"C:\Users\Owner\OneDrive\Desktop\Kwiat Lab\MCF Project", exist_ok=True)  
# df_final.to_csv(r"C:\Users\Owner\OneDrive\Desktop\Kwiat Lab\MCF Project\test.csv", index=Index, columns=Cols)
# svm_1 = sns.heatmap(df_1, annot=True, cmap="crest")
# svm_1.set(xlabel="Input", ylabel="Output")
# svm_1.set_title("Unprimed-primed mean plot")
# plt.savefig('Unprimed-primed-mean.png', dpi=400)
# plt.clf()
# svm_2 = sns.heatmap(df_2, annot=True, cmap="crest")
# svm_2.set(xlabel="Input", ylabel="Output")
# svm_2.set_title("Unprimed-primed std plot")
# plt.savefig('Unprimed-primed-std.png', dpi=400)

#######################################################

# df = pd.read_csv(r"C:\Users\Owner\OneDrive\Desktop\Kwiat Lab\MCF Project\Quantum signal characterization\Unprimed-Primed\1-1'", sep="\t", header=None)
# df.drop([0, 2, 3, 4, 5, 6, 7, 8, 9], axis=1, inplace=True)
# df.drop(df[df[1]==0].index, inplace=True)
# os.makedirs(r"C:\Users\Owner\OneDrive\Desktop\Kwiat Lab\MCF Project", exist_ok=True)  
# df.to_csv(r"C:\Users\Owner\OneDrive\Desktop\Kwiat Lab\MCF Project\test.csv", header=False, index=False)
# s = pd.Series(df[1].values)
# print(s.mean())
# print(s.std())