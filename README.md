# NJUCR
A small project I had in mind its merely for educational purposes (self), nothing more. free to use.

Caveat: The data; albeit open to the public, obtainable here -> [https://nj.gov/njsp/ucr/current-crime-data.shtml]
for Monmouth county sheet "inside the .xlsx files" contain duplicated rows. This program "assumes" data is formatted the same all around
might implement a fix for that over the course of time.

# Pretty simple to use

Install a recent version of python >= 3.8:
1) https://www.python.org

Download this application:
2) Click on the green "Code" dropdown button
2.1) Click "Download Zip"
2.2) Navigate to your Downloads folder
2.3) Extract the contents of the zip file into the Downloads folder.

[Good-Practice] creating a python virtual environment for this or any python based application
..assuming the folder "nj_crime" is in your downloads.. open your shell of choice and type:
3) python -m venv nj_crime

running the venv
4) source nj_crime/bin/activate
4.1) After running this command you will notice (nj_crime) in your console.
4.2) Navigate into the nj_crime folder...

installing application requirements
5) pip install -r requirements 

running application
6) python all_nj_crime_data.py
