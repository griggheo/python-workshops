import plotly.express as px

print(dir(px.data))

for dataset in ['carshare', 'election', 'gapminder', 'iris', 'tips', 'wind']:
    print(f'\nDetails for dataset "{dataset}":')
    print(getattr(px.data, dataset).__doc__)
    print(getattr(px.data, dataset)().head())

#print(px.data.carshare.__doc__)
#px.data.carshare().head()

#print(px.data.election.__doc__)
#px.data.election().head()

#print(px.data.gapminder.__doc__)
#px.data.gapminder().head()

#print(px.data.iris.__doc__)
#px.data.iris().head()

#print(px.data.tips.__doc__)
#px.data.tips().head()

#print(px.data.wind.__doc__)
#px.data.wind().head()