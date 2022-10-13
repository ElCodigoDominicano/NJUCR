"""
New Jersey UCR Data Graph

This program....
!! I'm not affiliated with any public or private offical, media, journalist etc. 

- Thus this program is as-is this will not work on other spreadsheet files unless
  the formatting is nearly identical to the way the ones downloaded from the website below.

- Takes roughly 7 seconds if no webrowser is open a little less if one is open.

+ It produces over several hundred graphs one for each authoritive department in each county for the state of NJ.
+ The public data provided by: https://nj.gov/njsp/ucr/current-crime-data.shtml
+ Its a small project I've put together.  though I miss home.. more importantly its meant 
  as an educational tool teaching myself more on software development(using python),
  data visualization (using plotly graph_objects) and web-application development,
  taking real-world data (in this case NJ Uniform.Crime.Reports) and producing visual results in 
  this case a graph. as well as using pandas dataframes to help represent all of that data.

++ This is open sourced for anyone to use .

WARNING: Monmouth County have duplicate iffy row data no conditional written to handle those errornous rows of data yet.

requirements: inside requirements.txt

Those of which will be installed using the terminal and entering this command: pip install -r requirements.txt 

Author: AERivas @ElCodigoDR
Date: 10/13/2022
"""
import os
import asyncio
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Not fully implemented and obviously will change.
def find_possible_file() -> list[str]:
    """ returns a list of possible spreadsheet files, mainly .xlsx.."""
    it_is_xlsx = []
    current_directory = os.listdir(os.path.curdir)
    for file_and_directory in current_directory:
        file_extention = file_and_directory.rfind(".")
        is_it_xlsx = file_and_directory[file_extention:].find('.xlsx')
        if (is_it_xlsx) and os.path.isfile(file_and_directory):
            it_is_xlsx.extend([file_and_directory[is_it_xlsx:]])
    return it_is_xlsx


# pd.set_option('display.max_rows',None) # helps with viewing dataframe ,console-wise, visually. 
def get_spreadsheet_names() -> list[str]:
        """RETURNS a list of strings, every string is a county name in NJ from the provided .xlsx spreadsheet."""
        # Excludes the first document labeled DocumentMap.
        get_spreadsheet_names.list_of_sheet_names = pd.ExcelFile("2020_Uniform_Crime_Report.xlsx").sheet_names[1:]
        return get_spreadsheet_names.list_of_sheet_names


async def get_all_sheets() -> dict[str, pd.DataFrame]:
    get_spreadsheet_names()
    get_all_sheets.all_sheets = pd.read_excel(
        "2020_Uniform_Crime_Report.xlsx", 
        sheet_name=[county for county in get_spreadsheet_names.list_of_sheet_names], 
        engine='openpyxl',
        skiprows=3)
    return get_all_sheets.all_sheets


async def make_all_dataframes() -> list[pd.DataFrame]:
    """ 
    *Coroutine
    RETURNS a list containing pandas dataframes, the rows are in groups of 5. respectively, representing each department
    in each county of the state in NJ. 
    
    each group of rows have a tag ORINumber(department number..), Department Name, the counties Population, respectivly..
    those elements are contained in a list of strings think ['orinumber', 'department_name', 'county_population']..
    """
    await asyncio.create_task(get_all_sheets())
    all_counties = get_all_sheets.all_sheets
    
    dfs = []
    make_all_dataframes.department_information = []
    for df in all_counties.values():
        df.copy()
       
      # Gather department information such as ORINumber, Department name, and Population 
        dept_data = df.iloc[1::6, [0, 1, 2]].fillna(0)
        dept_data["Population"] = dept_data["Population"].astype(np.int64) # From float64 
        make_all_dataframes.department_information.extend([str(x[0]) + " " + x[1]  + " " + str(x[2]) for x in dept_data.values.tolist()][:-1])
        
        # row and columns ( excluded columns: ORINumber and Population )     
        all_data = df.loc[
            (df["Agency"] == "Number of Offenses") |
            (df["Agency"] == "Rate Per 100,000") |
            (df["Agency"] == "Number of Clearances") |
            (df["Agency"] == "Percent Cleared") |
            (df["Agency"] == "Number of Arrests"), :].dropna(axis='columns')

        indexer = all_data.set_index(["Agency"], drop=True)
        all_dataframes = [indexer[y:y+5] for y in range(0, len(indexer), 5)]
        dfs.extend(all_dataframes)       
    return dfs


async def show_charts() -> None:
    """
    *Coroutine
    This function handles displaying a barchart using Plotly handles the, figures,
    graphing objects, graphing layout, and adding a dropdown button to each graph being created.
    
    Creates 1 single trace using graph_objects by columns then for a button supplies a dictionary containing 
    plotly.updatemenus argments and their proper values to update the graph for each department and county total
    """
    all_dfs = await asyncio.create_task(make_all_dataframes()) # 599 dataframes.. 
    fig = go.Figure()
    
    # Create ONE trace; based on column data
    for col in all_dfs[0].columns:
        fig.add_trace(go.Bar(x=all_dfs[0].index, 
                        y=all_dfs[0][col],
                        visible=True,
                        name=col))
    
    # Each dictionary inside represents each dataframe as its own graph
    # for the use of updatemenus below in reguards to the figure class method update_layout below which will be a dropdown button.
    buttons = [] 
    for x, df in enumerate(all_dfs):
        each_trace = dict(
            method='update',
            label=make_all_dataframes.department_information[x],
            visible=True,
            args=[{"type":"bar",
                    "x": [df.index],
                    "y": [df[col] for col in df.columns],},[0]])
        buttons.append(each_trace)
   
    # Layout
    fig.update_layout(showlegend=True, 
        updatemenus=[{
            "buttons": buttons, # list of dict containing all data 
            "direction": 'down',
            "showactive": True,}],
        title={"text": "The Crime Statistics in New Jersey", "font":{"size": 36}})
    fig.show()

    
if __name__ == '__main__':
    import time
    start = time.time()
    if len(find_possible_file()) == 0:
        print("Nope.")
    else:
        asyncio.run(show_charts())
    end = time.time()
    print(end - start)
