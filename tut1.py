from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import datetime

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/regular')
def regular_wing():
    #fsfs_awards = list(db.fsfs_achievements.find().sort("year", -1))
    #return render_template('regular.html', fsfs_awards=fsfs_awards)
    return render_template('regular.html')
'''@app.route('/air')
def air():
    #fsfs_awards = list(db.fsfs_achievements.find().sort("year", -1))
    #return render_template('air.html', fsfs_awards=fsfs_awards)


# FSFS route - showing achievements
@app.route('/fsfs')
def fsfs():
    #fsfs_awards = list(db.fsfs_achievements.find().sort("year", -1))
    #return render_template('fsfs.html', fsfs_awards=fsfs_awards)'''

# Gallery route
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

if __name__ == '__main__':
    app.run(debug=True)
