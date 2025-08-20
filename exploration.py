import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_csv('AeroConnectData.csv')
#find non-missing values
df.info()


# find missing values
print(f"\n# of missing values:\n{df.isnull().sum()}")






# check total of freight and passengers match. account for floating point error in freights
df['Passengers_Check'] = df['Passengers_In'] + df['Passengers_Out'] - df['Passengers_Total']
df['Freight_Check'] = df['Freight_In_(tonnes)'] + df['Freight_Out_(tonnes)'] - df['Freight_Total_(tonnes)']


print(f"\nPassenger calculation check: {df['Passengers_Check'].ne(0).sum()} errors")
print(f"Freight calculation check): {(abs(df['Freight_Check']) > 0.001).sum()} errors")






# create joint routes column and get uniqueness numbers
df['Route'] = df['AustralianPort'] + ' <-> ' + df['ForeignPort'] + ' (' + df['Country'] + ')'
print(f"\nTotal routes: {df['Route'].nunique()}")
print(f"Unique Australian ports: {df['AustralianPort'].nunique()}")
print(f"Unique foreign ports: {df['ForeignPort'].nunique()}")
print(f"Unique countries: {df['Country'].nunique()}")


# top 5 busiest routes overall
top_routes = df.groupby('Route')['Passengers_Total'].sum().sort_values(ascending=False).head(5)
print(f"\nTop 5 routes with total passengers:")
print(top_routes)




# bottom 5 busiest routes overall
top_routes = df.groupby('Route')['Passengers_Total'].sum().sort_values(ascending=True).head(5)
print(f"\nBottom 5 routes with total passengers:")
print(top_routes)


# '#' of routes per year
routes_per_year = df.groupby('Year')['Route'].nunique()
print("\nNumber of unique routes per year:")
for year, count in routes_per_year.items():
   print(f"{year}: {count} routes")




# Cell: Monthly Passenger Distribution (All 5 Years)
# Calculate monthly totals for each year
monthly_totals = df.groupby(['Year', 'Month_num'])['Passengers_Total'].sum().unstack(fill_value=0)


# Calculate proportions (each month as % of that year's total)
yearly_totals = df.groupby('Year')['Passengers_Total'].sum()
monthly_proportions = monthly_totals.div(yearly_totals, axis=0) * 100


print("Monthly Passenger Proportions by Year (%):")
print(monthly_proportions.round(1))


# Cell: Visualization - Monthly Distribution Across 5 Years
plt.figure(figsize=(16, 8))


# Month names for x-axis
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


# Colors for each year
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
years = [1985, 1986, 1987, 1988, 1989]


# Plot each year as a separate line
for i, year in enumerate(years):
   year_data = monthly_proportions.loc[year]
   plt.plot(month_names, year_data.values,
            marker='o', linewidth=2, markersize=6,
            color=colors[i], label=str(year))


plt.xlabel('Month')
plt.ylabel('Percentage of Annual Passengers (%)')
plt.title('Monthly Passenger Distribution by Year (1985-1989)', fontsize=16, fontweight='bold')
plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Show summary statistics
print("\nSeasonal Insights:")
print("Peak months across all years:")
peak_months = monthly_proportions.idxmax(axis=1)
for year in years:
   peak_month = peak_months[year]
   peak_value = monthly_proportions.loc[year, peak_month]
   print(f"{year}: {month_names[peak_month-1]} ({peak_value:.1f}%)")


print("\nLowest months across all years:")
low_months = monthly_proportions.idxmin(axis=1)
for year in years:
   low_month = low_months[year]
   low_value = monthly_proportions.loc[year, low_month]
   print(f"{year}: {month_names[low_month-1]} ({low_value:.1f}%)")

