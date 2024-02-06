from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

import sqlite3
import pandas as pd
import plotly.express as px
import random

app = Dash()

server = app.server

def furniture_store():
    conn = sqlite3.connect('furniture_store+.db')
    conn

    cursor = conn.cursor()

    sql_request = """
    SELECT 
    orders.reg_number, 
    products.brand_name, 
    products.price, 
    categories.category_number, 
    categories.category_name, 
    orders.customer_number,  
    orders.date_of_order, 
    orders.delivery 
    FROM orders
    LEFT JOIN products ON orders.reg_number = products.reg_number
    LEFT JOIN categories ON products.category_number = categories.category_number;
    """

    
    cursor.execute(sql_request)
    


    fs_df = pd.DataFrame(cursor.fetchall(), columns = ['reg_number', 
                                                      'brand_name',
                                                      'price',
                                                      'category_number', 
                                                      'category_name', 
                                                      'customer_number',  
                                                      'date_of_order', 
                                                      'delivery'                                                       
                                                      ])
        
    
    fs_df['date_of_order'] = pd.to_datetime(fs_df['date_of_order'])    
    fs_df['date_of_order'] = fs_df['date_of_order'].dt.to_period('M')

    
    conn.close()

    return fs_df


fs_df = furniture_store()


period_months = sorted(fs_df['date_of_order'].unique())[2::3]
initial_slider = sorted(random.sample(range(len(period_months)),k=2))
slider_commentary = [period_months[initial_slider[0]],period_months[initial_slider[1]]]


app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

info_content = ['Данный дэшборд визуализирует часть информации из созданной ранее базы данных',
                html.Br(),
                html.Br(),
                'Первый график показывает распределение продаж по категориям мебели',
                html.Br(),
                'Второй график показывает распределение продаж по брендам и категориям мебели',
                html.Br(),
                'Третий график показывает ежеквартальную выручку',
                html.Br(),
                html.Br(),
                'Ссылка на проект, в котором происходит формирование базы, находится ниже',
               html.Br(), html.Br(),
               html.A('Ссылка на проект', href = 'https://github.com/Goosolio/Portfolio/tree/main/Project%206', target = '_blank'),
               html.Br(), html.Br()]

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([html.H1('Показатели мебельного магазина'), html.P(info_content)], width=12)]), html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Checklist(options = fs_df['category_name'].unique(), 
                          value = fs_df['category_name'].unique(), 
                          id = 'input_furniture')], width = 3)]),
    dbc.Row([
        dbc.Col([dcc.Graph(figure = px.histogram(fs_df['category_name'], 
                                                       text_auto=True,
                                                       template='plotly_dark',
                                                       color = fs_df['category_name'], 
                                                       title = 'Популярность товаров по категориям', 
                                                       labels = {'value':'категория', 
                                                                 'color':'цветовая категория'}).update_layout(yaxis_title='количество покупок', showlegend=False),
                                 id = 'output_text', style = {'width':'1000px', 'height':'600px'})])]), 
    dbc.Row([
        dbc.Col([dcc.Graph(figure = px.sunburst(fs_df,
                                                      path=['brand_name', 'category_name'], 
                                                      values='price', 
                                                      color='price',
                                                      template='plotly_dark',
                                                      color_continuous_scale='deep', 
                                                      title = 'Продажи по брендам и категориям', 
                                                      labels = {'price':'средняя стоимость товара', 
                                                                'price_sum':'выручка', 
                                                                'parent':'бренд', 
                                                                'labels':'метка'}), 
                                 id = 'output_text_2', style = {'width':'800px', 'height':'600px'})])]),
    dbc.Row([
        dbc.Col([dcc.Graph(figure = px.bar(fs_df.groupby(['date_of_order'])['price'].sum().reset_index(), 
                                                 y = 'price', 
                                                 color = 'price',
                                                 title = 'Выручка по кварталам',
                                                 template='plotly_dark',
                                                 text_auto=True, 
                                                 labels = {'price':'размер выручки'}).update_layout(uniformtext_minsize=8, 
                                                                                                    xaxis_title='квартал',xaxis=dict(tickmode='linear',
                                                                                                               dtick=1,
                                                                                                               showticklabels=False)), 
                                 id = 'output_text_3')])]),
    dbc.Row([
        dbc.Col([dcc.RangeSlider(min = 0, max = len(period_months) - 1, step = 1,
                                       value = initial_slider,
                                       marks = {i:{'label':str(period), 'style':{'font-size':'12px'}} for i,period in zip(range(len(period_months)),period_months)},
                                      id = 'slider')])]), html.Br(),
    dbc.Row([
        dbc.Col([html.H4('Параметры рэйнджслайдера'), html.P('диапазон с {} по {}'.format(*slider_commentary),
                                                                  id = 'info')])])
])


    
@app.callback(Output('output_text', 'figure'), Input('input_furniture', 'value'))
def update_figure(input_text):
#     print(input_text)
    edited_data = fs_df.loc[fs_df['category_name'].isin(input_text),'category_name']
    figure = px.histogram(edited_data, 
                          color = edited_data, 
                          text_auto=True,
                          template='plotly_dark', 
                          title = 'Популярность товаров по категориям', 
                          labels = {'value':'категория',
                                    'color':'цветовая категория'}).update_layout(yaxis_title='количество покупок', showlegend=False)
    return figure

@app.callback(Output('output_text_3', 'figure'), Output('info', 'children'), Input('slider', 'value'))
def update_slider(slider_data):
    global slider_commentary
    figure = px.bar(fs_df.groupby(['date_of_order'])['price'].sum().reset_index()[slider_data[0]:slider_data[1]], 
                                                 y = 'price', 
                                                 color = 'price',
                                                 title = 'Выручка по кварталам',
                                                 template='plotly_dark',
                                                 text_auto=True, 
                                                 labels = {'price':'размер выручки'}).update_layout(uniformtext_minsize=8,
                                                                                                    xaxis_title='квартал',
                                                                                                    xaxis=dict(tickmode='linear',
                                                                                                               dtick=1,
                                                                                                               showticklabels=False))
    slider_commentary = [period_months[slider_data[0]],period_months[slider_data[1]]]
    return (figure, 'диапазон с {} по {}'.format(*slider_commentary))





if __name__=='__main__':
    app.run_server(port=8041)