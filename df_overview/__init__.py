'''
Title: df_overview
Purpose: A quick overview of your dataset with just one line!
Github link: https://github.com/sidjain1412/df_overview
Author: Siddharth Jain (github.com/sidjain1412)
'''
import warnings
import seaborn as sns
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
sns.set(style='white', color_codes=True)


def overview(df):
    basicview(df)
    correlation(df)
    head(df)


def basicview(df):
    shape = df.shape
    print("Rows:\t\t ", shape[0])
    print("Columns:\t ", shape[1])
    print()
    print("Null values in each column:")
    for col in df.columns:
        print('{:>28}'.format(col), ":", df[col].isna().sum())


def correlation(df):
    print()
    print("Correlation plot: ")
    corr = df.corr()
    plt.figure(figsize=(10, 10))
    sns.heatmap(corr, cbar=True, square=True, fmt='.2f',
                annot=True, annot_kws={'size': 9}, cmap='Greens')


def head(df):
    print()
    print("Head: ")
    print(df.head())
