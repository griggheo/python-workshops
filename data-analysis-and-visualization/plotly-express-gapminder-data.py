import plotly_express as px
gapminder = px.data.gapminder()
gapminder2007 = gapminder.query("year == 2007")

# life expectancy vs GPD per capita by country for 2007
fig1 = px.scatter(gapminder2007, x="gdpPercap", y="lifeExp")
fig1.show()

# break down the data by continent
fig2 = px.scatter(gapminder2007, x="gdpPercap", y="lifeExp", color="continent")
fig2.show()

# scale the points by the country population
fig3 = px.scatter(gapminder2007, x="gdpPercap", y="lifeExp", color="continent", size="pop", size_max=60)
fig3.show()

# add hovering so you can easily identify any country
fig4 = px.scatter(gapminder2007, x="gdpPercap", y="lifeExp", color="continent", size="pop", size_max=60, hover_name="country")
fig4.show()

# facet the graph by continent and make the x-axis logarithmic to see things more clearly
fig5 = px.scatter(gapminder2007, x="gdpPercap", y="lifeExp", color="continent", size="pop", size_max=60,
    hover_name="country", facet_col="continent", log_x=True)
fig5.show()

# see how this chart evolved over time by animating it
# also provide prettier labels that get applied throughout the figure
fig6 = px.scatter(gapminder, x="gdpPercap", y="lifeExp",size="pop", size_max=60, color="continent", hover_name="country",
    animation_frame="year", animation_group="country", log_x=True, range_x=[100,100000], range_y=[25,90],
    labels=dict(pop="Population", gdpPercap="GDP per Capita", lifeExp="Life Expectancy"))
fig6.show()