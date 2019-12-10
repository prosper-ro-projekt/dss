from flask import Flask, render_template

import folium

import os

app = Flask(__name__)




@app.route('/map')
def map():
    start_coords = (46.9540700, 142.7360300)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    folium_map.add_child(folium.ClickForMarker(popup='Potential Location'))
    map_path = 'templates/map_raw.html'
    folium_map.save(map_path)
    return render_template("map.html")


@app.route('/help')
def help():
    return render_template("help.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/user')
def user():
    return render_template("user.html")

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)