# NJUCR
A small project I had in mind its merely for educational purposes (self), nothing more. free to use.

Caveat: The data; albeit open to the public, obtainable here -> [https://nj.gov/njsp/ucr/current-crime-data.shtml]
for Monmouth county sheet "inside the .xlsx files" contain duplicated rows. This program "assumes" data is formatted the same all around
might implement a fix for that over the course of time.

# Pretty simple to use

## 1) Install a recent version of python >= 3.8:
[https://www.python.org]

## 2) Download this application:
2.1) Click on the green "Code" dropdown button<br>
2.2) Click "Download Zip"<br>
2.3) Navigate to your Downloads folder<br>
2.4) Extract the contents of the zip file into the Downloads folder.<br>

## 3) **Good-Practice** Creating a python virtual environment for this or any python based application
### ..assuming the folder "nj_crime" is in your downloads.. open your shell of choice and type:
 `$> python -m venv nj_crime`

## 4) Run the venv
`$> source nj_crime/bin/activate`<br>
4.1) After running this command you will notice `(nj_crime) $>` in your console.<br>
4.2) Navigate into the nj_crime folder. <br>

## 5) Installing application requirements
`pip install -r requirements`

## 6) Run the application
`python all_nj_crime_data.py`
