# NJUCR
A small coding project I've had in mind earlier this year its merely for educational purposes (me learning more on software development, data analytics, computer science), nothing more. free to use.

small-caveat: The data; albeit open to the public, obtainable here -> [https://nj.gov/njsp/ucr/current-crime-data.shtml]
for Monmouth county sheet "inside the .xlsx files" contain duplicated rows. This program "assumes" data is formatted the same all around
might implement a fix for that over the course of time.


<p> 
  The data, by the crime type (columns) and using the crime statistic(rows) to
  respresent them as barcharts per county, per recorded statistic by department + their ORINumber (whatever that is.), 
  and county population. I will continue to improve this and hopefully use it later in a bigger web development based project im currently working on
</p>


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

## 5) Install application requirements
`pip install -r requirements`

## 6) Run the application
`python all_nj_crime_data.py`

# If you ask me 'Pizza' is the king and queen of foods.
