import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style

option = int(input("Enter graph type:\n1) Total\n2) Today\n3) Week\nEnter your option: "))
if option < 1 and option > 3:
    print("Entered Option is not available")
    exit()

if option == 1:
    title = "Graph based on total count"
elif option == 2:
    title = "Graph based on last 24 hours count"
else:
    title = "Graph based on last 7 days count"
df = pd.read_csv("tagsData.csv", usecols=[0, option], names=['Tag', 'Count'])

df2 = pd.DataFrame(df)
print(df2)

style.use('ggplot')

df2.sort_values(by=['Count'], ascending=False).head(10).set_index('Tag').plot(kind='bar', title=title)
plt.show()
