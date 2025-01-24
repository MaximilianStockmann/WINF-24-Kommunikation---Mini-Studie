import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("input.xlsx")
df = df.dropna(axis=1, how='all')

labels = ["Trifft gar nicht zu", "Trifft wenig zu", "Neutral", "Trifft zu", "Trifft voll und ganz zu"]

for i in range(4,16):
    plot = df.groupby(df.iloc[:,i]).size().plot(kind='pie', figsize=(9, 5), labeldistance=None, autopct='%1.1f%%', textprops={'fontsize': 12})
    result_string = f"Q{i}.png"
    plot.legend(bbox_to_anchor=(1, 1.02), loc='upper left')
    plot.get_figure().savefig(result_string)
    plt.clf()
