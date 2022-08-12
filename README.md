# Project1

This repo was the first I created for my internship at Spacebot in Chicago (2022).
I first created a Datacamp folder which is now a new repo in wgich I have some examples and the syntax for Pandas and SQLite in notebooks.
The Keylogger folder is now a repo in which I have text files containing some collected data (key typed) in different formats, in order to make it easier to clean and use with pandas and working with ArgParse selectiong the name of the .text doc you want to log the keys in.
The light sensors folder is now a repo where there are programs to get ambiant luxmeasures, using systemd (.service) and sqlite databases to get the data from both VEML and TSL sensors, then cleaning and merging them using pandas.
The Lux work folder contains programs logging lux measures into sql databases (veml and tsl) and work with Openweather API to get the current weather and store it via SQLite using datamodels and systemd (.timer file triggering .service file)
The SQL database folder contains most of the databases I created through these 3 months of internship
