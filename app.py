# Import the dependencies.
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
db_session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    """All available routes"""
    return(
        f"Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

# convert query results from precipitation analysis to adictionary
@app.route("/api/v1.0/precipitation")
def precipitation_last_year():
    prcp_last_year = db_session.query(measurement.date, measurement.prcp).filter(measurement.date >= '2016-08-24').all()
    prcp_data = []
    for date, prcp in prcp_last_year:
        prcp_last_year_dict = {}
        prcp_last_year_dict["Date"] = date
        prcp_last_year_dict["Precipitation"] = prcp
        prcp_data.append(prcp_last_year_dict)
    return jsonify(prcp_data)

# return a JSON list of stations from the dataset
@app.route("/api/v1.0/stations")
def stations_list():
    stations = db_session.query(station.station).all()
    stations_list = []
    for station in stations:
        stations_list.append(station)
    return jsonify(stations_list)

#return temp obs of most active station for previous year
@app.route("/api/v1.0/tobs")
def temp_obvs():
    station_id = 'USC00519281'
    temp_last_year = db_session.query(measurement.date,measurement.tobs).filter(measurement.date >= '2016-08-24', measurement.station==station_id).all()
    temp_data = []
    for date, tobs in temp_last_year:
        temps_last_year_dict = {}
        temps_last_year_dict["Date"] = date
        temps_last_year_dict["Temp"] = tobs
        temp_data.append(temps_last_year_dict)
    return jsonify(temp_data)


@app.route("/api/v1.0/<start>")
def start_date(start):
    start_info = db_session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs).filter(measurement.date>=start)).all()
    start_data = []
    for min, max, avg in start_info:
        start_data_dict = {}
        start_data_dict["Min Temp"] = min
        start_data_dict["Max Temp"] = max
        start_data_dict["Avg Temp"] = avg
        start_data.append(start_data_dict)
    return jsonify(start_data)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    start_info = db_session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).filter(measurement.date>=start).filter(measurement.date<=end).all()
    start_end_data = []
    for min, max, avg in start_info:
        start_end_data_dict = {}
        start_end_data_dict["Min Temp"] = min
        start_end_data_dict["Max Temp"] = max
        start_end_data_dict["Avg Temp"] = avg
        start_end.append(start_end_data_dict)
    return jsonify(start_end_data)

if __name__ == "__main__":
    app.run(debug=True)

# Close Session
db_session.close()