import pandas as pd
import plotly.express as px
import json

# link com o arquivo json usado
# https://raw.githubusercontent.com/Markosalves12/geojson_estados-_brasil/main/brasil_estados.json
caminho_geo_json = r"C:\Dashboardcovid19\geojson\brasil_estados.json"
caminho_geo_json = caminho_geo_json.replace("\\", "/")


# link com o arquivo csv usado
# https://github.com/Markosalves12/csv_arquivos/blob/main/estadosxdespesas.csv
caminho_df = r"C:\Dashboardcovid19\Frames\estadosxdespesas.csv"
caminho_df = caminho_df.replace("\\", "/")

df = pd.read_csv(caminho_df, encoding="latin-1", delimiter=",")
geojson = json.load(open(caminho_geo_json))

fig = px.choropleth(df, geojson=geojson, locations='uf', color='valor',  # color_continuous_scale='blues',
                    scope='south america', projection='natural earth', width=700, height=700,
                    color_discrete_map={'color': 'red'},
                    template='plotly_dark')
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.update_layout(activeshape_opacity=0.4)
fig.update_layout(
    title={
        'text': "Espectro de volume de contratos por estado",
        'y': 0.98,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

# descomente a linha a baixo para visualisar a figura
# fig.show()
