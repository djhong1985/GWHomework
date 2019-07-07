import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    
    result1 = session.query(Measurement.date, Measurement.prcp).all()

    all_date = []

    for date, prcp in result1:
        date_dict = {}
        date_dict["date"] = date
        date_dict["prcp"] = prcp
        all_date.append(date_dict)

    return jsonify(all_date) 


@app.route("/api/v1.0/station")
def station():
    
    result2 = session.query(Station.station).all()
    
    all_station=[]

    for station in result2:
        station_dict = {}
        station_dict["station"] = station
        all_station.append(station_dict)

    return jsonify(all_station) 


@app.route("/api/v1.0/tobs")
def tobs():
    result3 = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= '2016-08-23').all()

    all_tobs=[]

    for date,tobs in result3:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        all_tobs.append(tobs_dict)

    return jsonify(all_tobs) 

#Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
#When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
#When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive

#@app.route("/api/v1.0/start/<start_date>")
#def calc_temps(start_date):
#    results4 = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).all()
#.filter(Measurement.date <= end_date).all()

#    canonicalized = start_date
#    for start_date in results4:
#        search_term = start_date

#        if search_term == canonicalized:
#            return jsonify(results4)

 #   return jsonify({"error": f"Character with real_name {real_name} not found."}), 404

if __name__ == "__main__":
    app.run(debug=True)