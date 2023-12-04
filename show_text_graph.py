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




# 建立 Django Dash app
app = dash.Dash(__name__ )


# 建立下拉式選單的選項（名字）
name_options = [{'label': name, 'value': name} for name in df['Name'].unique()]

# 建立布局
app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='name-dropdown',
            options=name_options,
            value=name_options[0]['value'])]),
    html.Div([
        dcc.Graph(id='performance-graph')])
])

# 設定 Callback
@app.callback(
    Output('performance-graph', 'figure'),
    Input('name-dropdown', 'value'))

# 依照選擇的名字更新圖表資料
def update_performance_graph(selected_name):
    # 從 DataFrame 中篩選出選定名字的資料
    filtered_data = df[df['Name'] == selected_name]
    
    # 使用 Plotly Express 繪製互動式圖表
    fig = px.line(filtered_data, x='Year', y='Age', title=f'Performance of {selected_name}')
    return fig

if my_custom_name == '__main__':
    app.run_server(debug=False, port=3002)

