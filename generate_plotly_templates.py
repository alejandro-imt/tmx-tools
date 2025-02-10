import plotly.graph_objects as go

# Generar light template
def light_template():
    # Setting a custom TMX template (bold title)
    tmx_template_light = go.layout.Template()

    # Setting the layout of the template
    tmx_template_light.layout.title.font.family = "Nexa"
    tmx_template_light.layout.title.font.size = 26
    tmx_template_light.layout.title.font.color = "#000000"
    tmx_template_light.layout.title.font.weight = "bold"
    tmx_template_light.layout.font.family = "Nexa"
    tmx_template_light.layout.font.size = 18
    tmx_template_light.layout.font.color = "#000000"

    # Set the marker size
    mrkr_size = 8

    # Change the scatter markers
    tmx_template_light.data.scatter = [
        go.Scatter(marker=dict(symbol="circle", size=mrkr_size)),
        go.Scatter(marker=dict(symbol="square", size=mrkr_size)),
        go.Scatter(marker=dict(symbol="diamond", size=mrkr_size)),
        go.Scatter(marker=dict(symbol="cross", size=mrkr_size)),
        go.Scatter(marker=dict(symbol="pentagon", size=mrkr_size)),
        go.Scatter(marker=dict(symbol="star", size=mrkr_size)),
    ]

    # Paper background color
    # tmx_template_light.layout.paper_bgcolor = "#FF00FF"

    tmx_template_light.layout.colorway = [
        # "#1DBECF", descartado por parecerse mucho a #57C1A6
        "#00BDF2",
        "#57C1A6",
        "#4F8D85",
        "#32626E",
        # "#2C3A3B", demasiado oscuro, usar mejor en texto, bordes y fondos
    ]

    return tmx_template_light
