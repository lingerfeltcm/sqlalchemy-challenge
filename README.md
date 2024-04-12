# sqlalchemy-challenge
##Instructions
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

##Part 1: Analyze and Explore the Climate Data
I imported all necessary libraries from Python and started up my SQLAlchemy engine and used the automap_base() function to identify the tables and classes.

I created a session called db_session to link Python to my database.

I found the column names (keys) for each of my tables to be able to begin my analysis.

##Precipitation Analysis

I found the most recent data in the dataset by sorting the date values in descending order and finding the first date.

I found the previous 12 months of data by finding all the precipitation filtered by all dates that were greater than or equal to the date a year before the most recent date located in the previous step.

I created a dataframes and set the column names. I differed from the recommended column names because I like having capitalized column names in my dataframes to help me quickly differentiate between column names and data.
I then sorted the columns by name. I thought about dropping any na values, but I didnt want to skew the data set if the na values were meant to represent 0 precipitation that day as that data would still be valuable.
I then printed summary statistics and plotted the dataframe with title, xlabels, ylabels, and rotated the xticks to make the the plot look more appealing and more easily readable.

##Station Analysis
I designed another query to find all of the stations starting by finding the number of stations and then finding how many datapoints each station had to determine which dataset was the most active.
Afterwards, I designed another query to locate the minimum, maximum, and average temperature observations (tobs) for the most active station.
I then found all the temperature data over the past year using a similar method as I did early with the precipitation.
I then plotted all the temperature data ovoer the past year


AFterwards I closed my session.

##Part 2: Design Your Climate App
I created a homepage in app.py that listed all the routes.

###/api/v1.0/precipitation

I used the code from before and a for loop to create the key value pairs needed for the JSON dictionary to list all the precipitation over the last year.

###/api/v1.0/stations

I used another list to find all the stations to jsonify.

###/api/v1.0/tobs
I used a combination of the code from identifying the most active station and the code for calculating the min, max, and avg to gather all data from the previous year and then used a similar for loop to my precipitation for loop to create the JSON dictionary.

###/api/v1.0/<start> and /api/v1.0/<start>/<end>

Created two different sets of code that allowed the user to input the start date or the start and end date to get data.

Closed my session.
