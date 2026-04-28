import pandas as pd
import matplotlib.pyplot as plt
db=pd.read_csv("data/Amazon Sale Report.csv")
# print(db)
# print(db.describe())
# print(db.info())
# print(db.isnull().sum())

db=db.drop("Unnamed: 22",axis=1)

db=db[(db["Amount"]>0)]

db["Courier Status"]=db["Courier Status"].fillna("Unknown")
db["ship-city"]=db["ship-city"].fillna("Unknown")
db["ship-state"]=db["ship-state"].fillna("Unknown")
db["ship-postal-code"]=db["ship-postal-code"].fillna("Unknown")
db["ship-country"]=db["ship-country"].fillna("Unknown")
db["promotion-ids"]=db["promotion-ids"].fillna("Unknown")
db["fulfilled-by"]=db["fulfilled-by"].fillna("Unknown")

db["Date"]=pd.to_datetime(db["Date"])
# print(db["Date"].dt.month)

db["Qty"]=pd.to_numeric(db["Qty"])
db["Amount"]=pd.to_numeric(db['Amount'])

db=db.drop_duplicates()

db["Revenue"]=db["Amount"]*db["Qty"]
db["Custome_Price"]=db["Revenue"]*1.15

highest_revenue_category=(db.groupby("Category")["Revenue"].sum().sort_values(ascending=False))
#Category generate highest revenue
print(highest_revenue_category.iloc[:1])

#Top 5 category by revenue
print(highest_revenue_category.iloc[:5])

#Top 5 Size by revenue
highest_sell_size=(db.groupby("Size")["Revenue"].sum().sort_values(ascending=False))
print(highest_sell_size.iloc[:5])

average_order_value=db["Revenue"].sum()/db["Revenue"].count()
print(f"Average order value = {average_order_value}")

#Monthly sales trend
print(db.groupby(db["Date"].dt.month)["Revenue"].sum())

print(db)
print(db.isnull().sum())

bar=db.groupby("Category")["Revenue"].sum().reset_index()
labels=bar["Category"]
values=bar["Revenue"]
plt.figure(figsize=(10,4))
plt.title("Revenue of all Chategory")
plt.xlabel("Category")
plt.ylabel("Revenue")
bars=plt.bar(labels,values)
# plt.savefig("charts/bar_chart.png")
plt.show()



line_chart=db.groupby(db["Date"].dt.month)["Revenue"].sum()
line_chart.plot(kind="line")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
# plt.savefig("charts/line_chart.png")
plt.show()


plt.style.use('default')
set1=db.loc[db.Category=='Set']['Revenue']
kurta=db.loc[db.Category=='Kurta']['Revenue']
Western=db.loc[db.Category=='Western Dress']['Revenue']
top=db.loc[db.Category=='Top']['Revenue']
labels=['set','kurta','Western','top']
plt.title("Revenue of some Categoty")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.ylim(0,2000)
plt.boxplot([set1,kurta,Western,top],labels=labels)
# plt.savefig("charts/box_chart.png")
plt.show()

highest_revenue_category_pie=(db.groupby("Category")["Revenue"].sum().sort_values(ascending=False))
big_category=highest_revenue_category_pie[highest_revenue_category_pie>(highest_revenue_category_pie.sum()*0.02)]
value=big_category.values
m_labels=big_category.index
plt.figure(figsize=(8,6))
plt.pie(value,autopct='%1.1f%%',pctdistance=1.2,labeldistance=0.8)
plt.legend(m_labels,loc="upper right",bbox_to_anchor=(1.2,1))
plt.title("Category contribution in Revenue")
# plt.savefig("charts/pie_chart.png")
plt.show()