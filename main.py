import pandas as pd
import matplotlib.pyplot as plt

#column_names = ["id", "startTime", "finishTime", "email", "Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10", "Q11", "Q12"]

df = pd.read_excel("input.xlsx")
df = df.dropna(axis=1, how='all')
#df.columns = column_names

labels = ["Trifft gar nicht zu", "Trifft wenig zu", "Neutral", "Trifft zu", "Trifft voll und ganz zu"]
# For Questions 4-10: Assign a score to the answer group

def label_function(val):
    return f'{val / 100 * len(df):.0f}\n{val:.0f}%'


for i in range(4,16):
    if i==14:
        plot = df.groupby(df.iloc[:,i]).size().reindex(labels).plot(kind='pie', figsize=(9, 5), labeldistance=None, autopct='%1.1f%%', textprops={'fontsize': 12})
    else:
        plot = df.groupby(df.iloc[:,i]).size().plot(kind='pie', figsize=(9, 5), labeldistance=None, autopct='%1.1f%%', textprops={'fontsize': 12})
    #plot.title.set_size(10)
    #plt.title(df.columns[i][:-1], wrap=True)
    result_string = f"Q{i}.png"
    plot.legend(bbox_to_anchor=(1, 1.02), loc='upper left')
    plot.get_figure().savefig(result_string)
    plt.clf()
