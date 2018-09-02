mortality = pd.read_html(
    "https://www.ssa.gov/oact/STATS/table4c6.html",
    skiprows=[0, 1, 2, 3],
    header=None)[0]

mortality = mortality.iloc[0:120, [1, 4]]
display(mortality.head())
print(mortality.columns)
mortality.rename(
    columns=dict(
        zip(mortality.columns, ("Male prob. death", "Female prob. death"))),
    inplace=True)
print(mortality.head().to_html())


####### 
mortality.rename(columns=dict(zip(mortality.columns, 
                                  ("Male prob. death", 
                                   "Female prob. death"))), 
                 inplace=True)
mortality.columns


######

mortality.columns.rename(zip(mortality.columns, 
                                  ("Male prob. death", 
                                   "Female prob. death")), inplace=True)


mortality = pd.read_html(
    "https://www.ssa.gov/oact/STATS/table4c6.html",
    skiprows=[0, 1, 2, 3],
    header=None)[0]

mortality = mortality.iloc[0:120, [1, 4]]
display(mortality.head())
print(mortality.columns)
mortality.rename(
    columns=dict(
        zip(mortality.columns, ("Male prob. death", "Female prob. death"))),
    inplace=True)
print(mortality.head().to_html())

mortality.index=pd.to_datetime(pd.DataFrame(mortality.index.values.tolist(), columns=["Male prob. death", 
                                   "Female prob. death"]))


mortality = pd.read_html("https://www.ssa.gov/oact/STATS/table4c6.html", 
                         skiprows=4, 
                         tupleize_cols=True,
                         header=None)[0]
mortality = mortality.iloc[0:120,[1,4]]
mortality.rename(columns=dict(zip(mortality.columns, 
                                  ("Male prob. death", 
                                   "Female prob. death"))),inplace=True)
mortality.head()

