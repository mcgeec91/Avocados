import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, MetaData
from sqlalchemy.pool import StaticPool

from flask import Flask, jsonify

import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)

# Reminder:
# cd to this directory before running this code in vscode.

#################################################
# Database Setup
#################################################
# Web sites use threads, but sqlite is not thread-safe.
# These parameters will let us get around it.
# However, it is recommended you create a new Engine, Base, and Session
#   for each thread (each route call gets its own thread)
engine = create_engine("sqlite:///schema.sql",
    connect_args={'check_same_thread':False},
    poolclass=StaticPool)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Avocado = Base.classes.avocado
Census = Base.classes.census

# Create our connection object
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        "Available Routes:<br/>" +
        "/api/v1.0/regions<br/>"+
        "/api/v1.0/avocados<br/>"+
        "/api/v1.0/censusregions<br/>"+
        "/api/v1.0/census<br/>"
    )


@app.route("/api/v1.0/regions")
def regions():
    """Return a list of all region names"""
    # Query all regions
    results = session.query(Avocado.region).all()

    # Convert list of tuples into normal list
    all_regions = list(np.ravel(results))

    return jsonify(all_regions)

@app.route("/api/v1.0/avocados")
def avocados():
    """Return a list of avocado data including the region, average_price, and total_volume"""
    # Query all avocado
    results = session.query(Avocado).all()

    # Create a dictionary from the row data and append to a list of all_avocado
    all_avocado = []
    for avocado in results:
        avocado_dict = {}
        avocado_dict["region"] = avocado.region
        avocado_dict["average_price"] = avocado.average_price
        avocado_dict["total_region"] = avocado.total_region
        all_avocado.append(avocado_dict)

    return jsonify(all_avocado)

@app.route("/api/v1.0/censusregions")
def censusregions():
    """Return a list of all census region names"""
    # Query all regions
    results = session.query(Census.region).all()

    # Convert list of tuples into normal list
    all_regions = list(np.ravel(results))

    return jsonify(all_regions)

@app.route("/api/v1.0/census")
def census():
    """Return a list of census data including the region, city_median_income, and city_median_age"""
    # Query all census
    results = session.query(Census).all()

    # Create a dictionary from the row data and append to a list of all_census
    all_census = []
    for census in results:
        census_dict = {}
        census_dict["region"] = census.region
        census_dict["city_median_income"] = census.city_median_income
        census_dict["city_median_age"] = census.city_median_age
        all_census.append(census_dict)

    return jsonify(all_census)

if __name__ == '__main__':
    app.run(debug=True)
