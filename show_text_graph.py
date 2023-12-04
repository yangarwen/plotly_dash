import pandas as pd
import plotly.express as px
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go


#build a example dataframe
data = {'Name': ['John', 'Anna', 'Peter', 'Linda', 'James',
                 'John', 'Anna', 'Peter', 'Linda', 'James',
                 'John', 'Anna', 'Peter', 'Linda', 'James',
                 'John', 'Anna', 'Peter', 'Linda', 'James'],
        'Year': [2017, 2017, 2017, 2017, 2017, 2018, 2018, 2018, 2018, 2018, 
                 2019, 2019, 2019, 2019, 2019, 2020, 2020, 2020, 2020, 2020],
        'Age': [25, 30, 35, 28, 24, 26, 32, 36, 29, 25, 
                27, 33, 37, 30, 26, 28, 35, 39, 32, 28],
        'Height': [175, 160, 180, 165, 170, 178, 163, 175, 167, 168, 
                   176, 165, 180, 162, 170, 175, 165, 177, 170, 163],
        'Weight': [70, 55, 80, 60, 68, 72, 58, 75, 62, 65, 
                   75, 58, 85, 53, 68, 71, 56, 78, 66, 61]}
df = pd.DataFrame(data)


#Build Dash app
app = Dash(__name__)

#Create dropdown options
name_options = [{'label': name, 'value': name} for name in df['Name'].unique()]

#Set layout
app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='name-dropdown',
            options=name_options,
            value=[name_options[0]['value']],  # Default value for multiple selection
            multi=True  # Enable multi-select
        )
    ]),
    html.Div([
        dcc.Graph(id='performance-graph')
    ])
])

#Callback to update the graph based on dropdown value
@app.callback(
    Output('performance-graph', 'figure'),
    Input('name-dropdown', 'value')
)
def update_performance_graph(selected_names):
    filtered_data = df[df['Name'].isin(selected_names)]  # Filter data for selected names
    
    fig = go.Figure()
    for name in selected_names:
        data_subset = filtered_data[filtered_data['Name'] == name]
        fig.add_trace(go.Scatter(x=data_subset['Year'], 
                                 y=data_subset['Age'], 
                                 mode='lines+markers',
                                 name=f'Performance of {name}'))
    
    fig.update_layout(title=f'Performance of {", ".join(selected_names)}',
                      xaxis_title='Year',
                      yaxis_title='Age')
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

