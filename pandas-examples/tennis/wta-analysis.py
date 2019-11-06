# dataset: //raw.githubusercontent.com/JeffSackmann/tennis_wta/master/wta_matches_2017.csv
# Code heavily borrowed from https://www.dataguasu.com/Tennis-Analytics/

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sys

matches = pd.read_csv("wta_matches_2017.csv")
pd.set_option("display.max_rows", 10)

#print(matches.dtypes)

### Players with most wins

most_wins = matches.groupby(['winner_name']).agg({'round':'count'}).sort_values(['round'], 
    ascending=False).head(15).copy()
#print(most_wins)
most_wins = most_wins.reset_index()
most_wins.columns = ['Player','Matches Won']
most_wins = most_wins.sort_values('Matches Won',ascending=True)
most_wins.plot('Player','Matches Won', 
    kind='barh', 
    title='Players with Most Wins', 
    legend=False,
    figsize=(20,8))

### Players with most titles

most_titles = matches.loc[matches['round']=='F'].groupby(['winner_name']).agg({'round':'count'}).sort_values(['round'], 
    ascending=False).head(15).copy()
#print(most_titles)
most_titles = most_titles.reset_index()
most_titles.columns = ['Player','Titles Won']
most_titles = most_titles.sort_values('Titles Won',ascending=True)
most_titles.plot('Player','Titles Won', 
    kind='barh', 
    title='Players with Most Titles', 
    legend=False,
    figsize=(20,8))

### Histograms on various dimensions
dimensions = [
    'winner_rank','loser_rank',
    'winner_age','loser_age',
    'winner_ht', 'loser_ht',
    'w_svpt','l_svpt']

plt.figure(figsize=(22,8))
for i in range(1,9):
    plt.subplot(2,4,i)
    matches[dimensions[i-1]].plot(kind='hist', title=dimensions[i-1])
#plt.show()

### Distribution of aces by surface type
matches_h = matches[~np.isnan(matches['w_ace']) & (matches['tourney_level'].isin(['G','M'])) ].copy()
#print(matches_h)
plt.figure(figsize=(20,8))
bplot = sns.boxplot(x="surface", y="w_ace", data=matches_h)
bplot.set(xlabel='Surface', ylabel='Aces')

#plot_file_name="aces_by_surface_type_boxplot.jpg"
#bplot.figure.savefig(plot_file_name,
#                    format='jpeg',
#                    dpi=100)

### Players with most aces

# create dataframe with details on aces by winners of each match
sw = matches.groupby(['winner_name']).agg({'w_ace':'sum'}).fillna(0).sort_values(['w_ace'], 
    ascending=False)

# create dataframe with details on aces by losers of each match
sl = matches.groupby(['loser_name']).agg({'l_ace':'sum'}).fillna(0).sort_values(['l_ace'], 
    ascending=False)

# concatenate dataframes
dfs = [sw,sl]
r = pd.concat(dfs, sort=True).reset_index().fillna(0)

# derive new column with total number of aces
r['aces'] = r['l_ace']+r['w_ace']

aces = r.groupby('index').agg({'aces':'sum'}).sort_values('aces',ascending=False).head(10)
aces = aces.reset_index()
aces.columns = ['Player','Aces']
aces = aces.sort_values('Aces',ascending=True)
aces.plot('Player','Aces', 
    kind='barh', 
    title='Players with Most Aces', 
    legend=False,
    figsize=(20,8))

### Players with most double faults

# create dataframe with details on double faults by winners of each match
sw = matches.groupby(['winner_name']).agg({'w_df':'sum'}).fillna(0).sort_values(['w_df'], 
    ascending=False)

# create dataframe with details on double faults by losers of each match
sl = matches.groupby(['loser_name']).agg({'l_df':'sum'}).fillna(0).sort_values(['l_df'], 
    ascending=False)

# concatenate dataframes
dfs = [sw,sl]
r = pd.concat(dfs, sort=True).reset_index().fillna(0)

# derive new column with total number of aces
r['dfs'] = r['l_df']+r['w_df']

dfs = r.groupby('index').agg({'dfs':'sum'}).sort_values('dfs',ascending=False).head(10)
dfs = dfs.reset_index()
dfs.columns = ['Player','Double Faults']
dfs = dfs.sort_values('Double Faults',ascending=True)
dfs.plot('Player','Double Faults', 
    kind='barh', 
    title='Players with Most Double Faults', 
    legend=False,
    figsize=(20,8))

### Top rivalries

pd.set_option("display.max_rows", 5000)

h2h_wl = matches.groupby(['winner_name','loser_name']).agg({'tourney_id':'count'}).reset_index()
h2h_wl.columns = ['player_a','player_b','total']
#print(h2h_wl)

h2h_lw = matches.groupby(['loser_name','winner_name']).agg({'tourney_id':'count'}).reset_index()
h2h_lw.columns = ['player_a','player_b','total']
#print(h2h_lw)

h2h_f = h2h_wl.merge(h2h_lw, on=['player_a', 'player_b'])
h2h_f['total'] = h2h_f['total_x'] + h2h_f['total_y']
print(h2h_f)

h2h_f['player_a'] = np.where(h2h_f['player_a'] < h2h_f['player_b'], h2h_f['player_a'], h2h_f['player_b'])
#print(h2h_f['player_a'])
h2h_f['player_b'] = np.where(h2h_f['player_a'] > h2h_f['player_b'], h2h_f['player_a'], h2h_f['player_b'])
#print(h2h_f['player_b'])
h2h_f['names'] = h2h_f['player_a'].str.split(" ").str.get(1) + "-" + h2h_f['player_b'].str.split(" ").str.get(1)
#print(h2h_f['names'])

h2h_f2 = h2h_f.groupby(['player_a','player_b','names']).agg({'total':'max'}).reset_index()
h2h_f2_sorted = h2h_f2[h2h_f2['player_a']!=h2h_f2['player_b']].sort_values(['total'], ascending=False)#.head(20)

plt.figure(figsize=(15,6))

ax1=sns.barplot(x="total", y="names", palette='Blues_d', data=h2h_f2_sorted.head(10))
ax1.set(xlabel='', ylabel='Players', title='Top 10 rivalries')

sns.despine(left=True, bottom=True)

plt.show()
