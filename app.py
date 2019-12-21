import dash
import dash_bootstrap_components as dbc

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    'https://use.fontawesome.com/releases/v5.9.0/css/all.css',
    "/css/custom-style.css",
]

meta_tags = [
    {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1",
    }
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)
app.title = "UFC Predictor"
server = app.server


@app.server.route("/css/<path>")
def static_css(path):
    static_folder = os.path.join(os.getcwd(), "css")
    return send_from_directory(static_folder, path)

@app.server.route("/img/<path>")
def static_img(path):
    static_folder = os.path.join(os.getcwd(), "img")
    return send_from_directory(static_folder, path)
