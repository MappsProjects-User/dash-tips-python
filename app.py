import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
# plotly.graph_objsとplotly.subplotsを追加
import plotly.graph_objs as go
from plotly.subplots import make_subplots

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# ============================================
# 画像と数値を組み合わせたブロック サンプル
# ============================================
new_orders = 526
new_users = 214
reviews = 128
ave_page_views = '1K'

# ============================================
# バブルチャート サンプル
# ============================================

# バブルチャート ▶︎
# データの入力、データの表示を制御する場所
# （X軸・Y軸・バブルサイズへのデータの入力、マーカーの表示、ラベルの表示など）
# ============================================
bubble_chart_sample_data = go.Scatter(
    x=[6, 9, 4, 2, 3, 4, 6, 4, 1, 8], y=[10, 10, 6, 6, 10, 17, 13, 12, 16, 10],
    mode='markers+text',

    text=['20代男性<br>20%', '30代男性<br>30%', '40代男性<br>40%', '50代男性<br>50%', '60代男性<br>60%',
          '20代女性<br>25%', '30代女性<br>35%', '40代女性<br>45%', '50代女性<br>55%', '60代女性<br>65%', ],
    textposition=['middle center', 'middle center', 'middle center', 'middle center', 'middle center',
                  'middle center', 'middle center', 'middle center', 'middle center', 'middle center', ],
    marker=dict(
        color=['#30A8F2', '#30A8F2', '#30A8F2', '#30A8F2', '#30A8F2',
               '#F2274C', '#F2274C', '#F2274C', '#F2274C', '#F2274C'],
        opacity=[0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
        size=[40, 50, 60, 70, 80,
              45, 55, 65, 75, 85],
    )
)

# バブルチャート ▶︎
# レイアウトを決める場所（タイトル、高さ、長さ、X軸、Y軸、余白など）
# ============================================
bubble_chart_sample_layout = go.Layout(
    title=dict(
        text='バブルチャート　サンプル<br><br>・円の大きさ：ダミーデータを使用<br>'
        '→サンプル数は性年代ごとに異なる<br>'
        '・X軸/Y軸：ダミーデータを使用<br>'
        '→バブルには、それぞれラベルを記載',
        y=0.91,
        yanchor="top"
    ),
    height=650,
    width=1180,
    xaxis=dict(
        title_text="X軸",
        range=[0, 10],
        dtick=1
    ),
    yaxis=dict(
        title_text="Y軸",
        range=[0, 20]
    ),
    margin=dict(t=200, r=20, b=0)
)

# バブルチャート ▶︎
# ２つをまとめて出力する場所
# ============================================
bubble_chart_sample = go.Figure(
    data=bubble_chart_sample_data, layout=bubble_chart_sample_layout
)

# ============================================
# 複合グラフ（棒グラフ＋折れ線グラフ）サンプル
# ============================================
item = ['項目1',
        '項目2',
        '項目3',
        '項目4',
        '項目5',
        '項目6',
        '項目7',
        '項目8',
        '項目9',
        '項目10',
        '項目11',
        '項目12',
        '項目13',
        '項目14',
        '項目15',
        '項目16',
        '項目17',
        '項目18',
        '項目19']

# 複合グラフ（棒グラフ＋折れ線グラフ） ▶︎
# 空のGraph Objectsを作成
# ============================================
multiple_chart_sample = go.Figure()

# 複合グラフ（棒グラフ＋折れ線グラフ） ▶︎
# 折れ線グラフ1を作成
# ============================================
multiple_chart_sample.add_trace(
    go.Scatter(
        x=item,
        y=['20%', '42%', '49%', '16%', '69%', '16%', '65%', '70%', '19%', '37%',
           '29%', '21%', '34%', '31%', '30%', '18%', '34%', '62%', '20%'],
        name='折れ線グラフ1',
        marker=dict(
            color='#F2274C',
            size=8,
            line=dict(
                color='#b24644',
                width=1
            )
        )
    )
)

# 複合グラフ（棒グラフ＋折れ線グラフ） ▶︎
# 折れ線グラフ2を作成
# ============================================
multiple_chart_sample.add_trace(
    go.Scatter(
        x=item,
        y=['67%', '62%', '64%', '49%', '63%', '22%', '15%', '30%', '17%', '24%',
           '12%', '59%', '53%', '19%', '65%', '66%', '69%', '14%', '20%'],
        name="折れ線グラフ2",
        marker=dict(
            symbol='cross',
            color='#F2A03D',
            size=8,
            line=dict(
                color='#F2A03D',
                width=1
            )
        )
    )
)

# 複合グラフ（棒グラフ＋折れ線グラフ） ▶︎
# 折れ線グラフ3を作成
# ============================================
multiple_chart_sample.add_trace(
    go.Scatter(
        x=item,
        y=['13%', '61%', '58%', '37%', '38%', '39%', '24%', '70%', '23%', '19%',
           '43%', '10%', '34%', '27%', '27%', '31%', '26%', '27%', '30%'],
        name="折れ線グラフ3",
        marker=dict(
            color='#21BFA2',
            size=8,
            line=dict(
                color='#21BFA2',
                width=1
            )
        )
    )
)

# 複合グラフ（棒グラフ＋折れ線グラフ） ▶︎
# 棒グラフを作成
# ============================================
multiple_chart_sample.add_trace(
    go.Bar(
        x=item,
        y=['66%', '61%', '47%', '47%', '46%', '42%', '42%', '40%', '39%', '39%',
           '38%', '34%', '34%', '31%', '27%', '24%', '20%', '17%', '14%'],
        name="棒グラフ",
        text=['66%', '61%', '47%', '47%', '46%', '42%', '42%', '40%', '39%', '39%',
              '38%', '34%', '34%', '31%', '27%', '24%', '20%', '17%', '14%'],
        textposition="auto",
        marker=dict(
            color='#CEE4F2',
            line=dict(
                color='#30A8F2',
                width=1
            )
        )
    )
)

# 複合グラフ（棒グラフ＋折れ線グラフ） ▶︎
# レイアウトを更新
# ============================================
multiple_chart_sample.update_layout(height=400, width=1180, showlegend=True,
                                    autosize=False, title_text='複合グラフ（棒グラフ＋折れ線グラフ）サンプル')


# ============================================
# 複合グラフ（Subplots）サンプル
# ============================================

# 複合グラフ（Subplots） ▶︎
# 空のGraph Objectsを作成
# ============================================
subplots_chart_sample = go.Figure()

# 複合グラフ（Subplots） ▶︎
# rows, cols, subplot_titlesを入力
# ============================================
subplots_chart_sample = make_subplots(rows=1, cols=3, shared_yaxes=True,
                                      subplot_titles=("タイトル1", "タイトル2", "タイトル3"))

# 複合グラフ（Subplots） ▶︎
# 折れ線グラフを各ブロックごとに作成
# ============================================
subplots_chart_sample.add_trace(go.Scatter(x=["項目1", "項目2", "項目3", "項目4"], y=[90, 75, 35, 28], marker_color='#F2274C', name="折れ線グラフ1"),
                                row=1, col=1)

subplots_chart_sample.add_trace(go.Scatter(x=["項目1", "項目2", "項目3", "項目4"], y=[64, 59, 44, 16], marker_color='#F2A03D', name="折れ線グラフ2"),
                                row=1, col=1)

subplots_chart_sample.add_trace(go.Scatter(x=["項目1", "項目2", "項目3", "項目4"], y=[58, 40, 35, 20], marker_color='#21BFA2', name="折れ線グラフ3"),
                                row=1, col=1)


subplots_chart_sample.add_trace(go.Scatter(x=["項目5", "項目6", "項目7", "項目8"], y=[89, 47, 32, 20], marker_color='#F2274C', name="折れ線グラフ1"),
                                row=1, col=2)

subplots_chart_sample.add_trace(go.Scatter(x=["項目5", "項目6", "項目7", "項目8"], y=[88, 70, 64, 30], marker_color='#F2A03D', name="折れ線グラフ2"),
                                row=1, col=2)

subplots_chart_sample.add_trace(go.Scatter(x=["項目5", "項目6", "項目7", "項目8"], y=[68, 62, 40, 30], marker_color='#21BFA2', name="折れ線グラフ3"),
                                row=1, col=2)


subplots_chart_sample.add_trace(go.Scatter(x=["項目9", "項目10", "項目11", "項目12"], y=[79, 63, 48, 38], marker_color='#F2274C', name="折れ線グラフ1"),
                                row=1, col=3)

subplots_chart_sample.add_trace(go.Scatter(x=["項目9", "項目10", "項目11", "項目12"], y=[81, 74, 60, 32], marker_color='#F2A03D', name="折れ線グラフ2"),
                                row=1, col=3)

subplots_chart_sample.add_trace(go.Scatter(x=["項目9", "項目10", "項目11", "項目12"], y=[76, 63, 55, 40], marker_color='#21BFA2', name="折れ線グラフ3"),
                                row=1, col=3)

# 複合グラフ（Subplots） ▶︎
# 画像を添付
# ============================================
subplots_chart_sample.add_layout_image(
    dict(
        source=app.get_asset_url("subplots_chart_sample_image2.png"),
        xref="paper", yref="paper",
        x=1.07, y=1.06,
        sizex=0.2, sizey=0.2,
        xanchor="right", yanchor="bottom"
    )
)

# 複合グラフ（Subplots） ▶︎
# レイアウトを更新
# ============================================
subplots_chart_sample.update_yaxes(range=[0, 100], dtick=25)
subplots_chart_sample.update_layout(height=500, width=1180, margin=dict(b=10),
                                    title_text="複合グラフ（Subplots）サンプル", showlegend=False)


# ============================================
# 帯グラフ サンプル
# ============================================

# 帯グラフ ▶︎
# データの入力、データの表示を制御する場所
# （X軸・Y軸・データの入力、マーカーの表示、ラベルの表示など）
# ============================================
trace0 = go.Bar(
    x=['16.3%', '20%', '20.1%', '18.3%', '19.7%'],
    y=['項目5', '項目4', '項目3', '項目2', '項目1'],
    name='属性1',
    text=['16.3%', '20%', '20.1%', '18.3%', '19.7%'],
    textposition="inside",
    orientation='h',
    marker=dict(
        color='#b5d8ed',
    )
)

trace1 = go.Bar(
    x=['54.2%', '44%', '46.3%', '50.5%', '43.7%'],
    y=['項目5', '項目4', '項目3', '項目2', '項目1'],
    text=['54.2%', '44%', '46.3%', '50.5%', '43.7%'],
    name='属性2',
    orientation='h',
    textposition='auto',
    marker=dict(
        color='#a7d3eb',
    )
)

trace2 = go.Bar(
    x=['29.4%', '36%', '33.6%', '31.2%', '36.6%'],
    y=['項目5', '項目4', '項目3', '項目2', '項目1'],
    text=['29.4%', '36%', '33.6%', '31.2%', '36.6%'],
    name='属性3',
    orientation='h',
    textposition='auto',
    marker=dict(
        color='#9dcde9',
    )
)

# 帯グラフ ▶︎
# データを集約
# ============================================
band_graph_sample_data = [trace0, trace1, trace2]

# 帯グラフ ▶︎
# レイアウトを決める場所（タイトル、高さ、長さ、X軸、Y軸、余白など）
# ============================================
band_graph_sample_layout = go.Layout(
    title='帯グラフ サンプル',
    barmode='stack',
    height=350,
    width=565
)

# 帯グラフ ▶︎
# データとレイアウトをまとめる場所
# ============================================
band_graph_sample = go.Figure(
    data=band_graph_sample_data, layout=band_graph_sample_layout
)

# ============================================
# レーダーチャート サンプル
# ============================================

# レーダーチャート ▶︎
# 空のGraph Objectsを作成
# ============================================
radar_chart_sample = go.Figure()

radar_item = ['項目1', '項目2', '項目3', '項目4', '項目5', '項目6',
              '項目7', '項目8', '項目9', '項目10']

# レーダーチャート ▶︎
# レーダーチャートを作成
# ============================================
radar_chart_sample.add_trace(go.Scatterpolar(
    r=[47, 18, 23, 41, 26, 29, 35, 49, 34, 45],
    theta=radar_item,
    fill='toself',
    fillcolor='rgba(242, 160, 76, 0.4)',
    textposition='bottom center',
    marker=dict(color='#f2a03d'),
    name='品目1')
)

radar_chart_sample.add_trace(go.Scatterpolar(
    r=[31, 17, 24, 11, 33, 28, 41, 13, 45, 22],
    theta=radar_item,
    fill='toself',
    fillcolor='rgba(33, 191, 162, 0.4)',
    textposition='bottom center',
    marker=dict(color='#21bfa2'),
    name='品目2')
)

# レーダーチャート ▶︎
# レイアウトを更新
# ============================================
radar_chart_sample.update_layout(
    title='レーダーチャート サンプル',
    height=365, width=572,
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 50]
        )
    ),
    margin=dict(
        l=10
    ),
    showlegend=True
)

# ============================================
# app.layout
# ============================================
app.layout = html.Div(
    [
        # 画像と数値を組み合わせたブロック
        html.Div(
            [
                #  例:新規注文数ブロック
                html.Div(
                    [
                        html.Span(
                            ['例:新規注文数', html.Br()]
                        ),
                        html.Br(),
                        html.Img(
                            title="例:新規注文数",
                            src=app.get_asset_url(
                                "cart_icon.png"),
                            id="",
                            style={
                                "height": "80px",
                                "width": "80px",
                                "margin-bottom": "0px",
                            },
                        ),
                        html.Br(),
                        html.Span(
                            new_orders, style={'font-size': 'xxx-large',
                                               'font-weight': 'bold'}
                        ),
                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px', 'width': '200px',
                              'margin': '10px 10px 0px 10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                              }
                ),
                #  例:新規会員登録数ブロック
                html.Div(
                    [
                        html.Span(
                            ['例:新規会員登録数', html.Br()]
                        ),
                        html.Br(),
                        html.Img(
                            title="例:新規会員登録数",
                            src=app.get_asset_url(
                                "user_icon.png"),
                            id="",
                            style={
                                "height": "80px",
                                "width": "80px",
                                "margin-bottom": "0px",
                            },
                        ),
                        html.Br(),
                        html.Span(
                            new_users, style={'font-size': 'xxx-large',
                                              'font-weight': 'bold'}
                        ),
                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px', 'width': '200px',
                              'margin': '10px 10px 0px 10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                              }
                ),
                #  例:商品レビュー数ブロック
                html.Div(
                    [
                        html.Span(
                            ['例:商品レビュー数', html.Br()]
                        ),
                        html.Br(),
                        html.Img(
                            title="例:商品レビュー数",
                            src=app.get_asset_url(
                                "comments_icon.png"),
                            id="",
                            style={
                                "height": "80px",
                                "width": "80px",
                                "margin-bottom": "0px",
                            },
                        ),
                        html.Br(),
                        html.Span(
                            reviews, style={'font-size': 'xxx-large',
                                            'font-weight': 'bold'}
                        ),
                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px', 'width': '200px',
                              'margin': '10px 10px 0px 10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                              }
                ),
                #  例:平均ページビュー数ブロック
                html.Div(
                    [
                        html.Span(
                            ['例:平均ページビュー数', html.Br()]
                        ),
                        html.Br(),
                        html.Img(
                            title="例:平均ページビュー数",
                            src=app.get_asset_url(
                                "page_view_icon.png"),
                            id="",
                            style={
                                "height": "80px",
                                "width": "80px",
                                "margin-bottom": "0px",
                            },
                        ),
                        html.Br(),
                        html.Span(
                            ave_page_views, style={'font-size': 'xxx-large',
                                                   'font-weight': 'bold'}
                        ),
                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px', 'width': '200px',
                              'margin': '10px 10px 0px 10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey'
                              }
                ),
            ], style={'display': 'flex', 'margin': '0px 0px 30px 0px'},
        ),
        # バブルチャート サンプル
        html.Div(
            [
                dcc.Graph(
                    id='',
                    figure=bubble_chart_sample
                ),
                # スタイルシートを適用
            ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px 0px 0px 5px', 'height': '700px', 'width': '1185px',
                      'margin': '0px 0px 30px 10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey',
                      }
        ),
        # 複合グラフ（棒グラフ＋折れ線グラフ）サンプル
        html.Div(
            [
                dcc.Graph(
                    id='',
                    figure=multiple_chart_sample
                ),
                # スタイルシートを適用
            ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px 0px 0px 5px', 'height': '400px', 'width': '1185px',
                      'margin': '0px 0px 30px 10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey',
                      }
        ),
        # 複合グラフ（Subplots）サンプル
        html.Div(
            [
                dcc.Graph(
                    id='',
                    figure=subplots_chart_sample
                ),
                # スタイルシートを適用
            ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px 0px 0px 5px', 'height': '500px', 'width': '1185px',
                      'margin': '0px 0px 30px 10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey',
                      }
        ),
        html.Div(
            [
                # 帯グラフ サンプル
                html.Div(
                    [
                        dcc.Graph(
                            id='',
                            figure=band_graph_sample
                        ),
                        # スタイルシートを適用
                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px 0px 0px 5px', 'height': '350px', 'width': '572px',
                              'margin': '0px 0px 30px 10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey',
                              }


                ),
                # レーダーチャート サンプル
                html.Div(
                    [
                        dcc.Graph(
                            id='',
                            figure=radar_chart_sample
                        ),
                        # スタイルシートを適用
                    ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px 0px 0px 5px', 'height': '350px', 'width': '572px',
                              'margin': '0px 0px 30px 10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey',
                              }
                ),
            ], style={'display': 'flex'}
        ),

    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
