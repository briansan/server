from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/')
def root():
    return 'hello'

route_map = {
    'knicks': 'https://www.espn.com/nba/team/_/name/ny/new-york-knicks',
    'chevy': 'https://www.chevrolet.com/?cmp=OLA_DISPLAY_33145653_413137889_606392551_226395378&gclid=EAIaIQobChMIu_ylgbOjiwMVpa6DCB0ckRFMEAEYASAAEgIdhfD_BwE',
}

@app.route('/l', methods=["GET"])
def get_redirect():
    return route_map

@app.route('/l', methods=["POST"])
def create_redirect():
    data = request.get_json()
    route_map[data["short"]] = data["long"]
    return data

@app.route('/l/<link>')
def redirect_link(link):
    new_link = route_map[link]
    return redirect(new_link)

app.run(port=2000, debug=True)
