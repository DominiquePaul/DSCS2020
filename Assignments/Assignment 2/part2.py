# Working with pandas and datasets

import pandas as pd

"""
1. Read in the red wine dataset (saved in the data folder) and make sure that
    the data was imported correctly, i.e. it is in a normal tabular format
    without going into too much detail here. Use the .info() command to inspect
    the data
"""
# your code


"""
2. Print the average, the mode and the standard deviation of each column

What is the minimum value that the "quality" column contains? What is the
maximum and the average?
"""
# your code


"""
3. Print out the ratio of rows to columns in the dataframe
"""
# your code


"""
4. The 'free sulfur dioxide' column has most likely not been loaded as a numeric
    column. One way of noticing this is that multiplying the column by a scalar
    results in a string-like behaviour. Transform the column into numeric
    values by using the pandas function .to_numeric(). Make sure that any
    non-compatible formats are forced into a numeric format (hint: look at the
    documentation onhow to do this)

    Check that the column in your adjusted dataframe is indeed filled with
    numeric values before you continue
"""
# your code


"""
5. There wa s a measurement error during the measurements. The machine that
measured the citric acid had a failure and recorded the citric acid to be 0 for
many data points. Replace the cells of the column "citric acid" that currently
have the value 0, by the mean value of the column.

You should be able to check that the code worked by recalculating the mean
after applying the changes and seeing that the values has actually changed
"""
# your code


"""
6. Print out all columns of the dataframe (use google to find the command to
    get the names). Select three features for further analysis and create a
    subset dataframe out of these. Also include the "quality" column
"""
# your code


"""
7. Check how many missing values there are in each column and in a second step
drop all the rows with *any* missing values. Hint: there's a function built
into pandas that you can use to check for missing values (NA values). Print the
number of rows before and after dropping the rows with na values.
"""
# your code


"""
8. Often in data science we can find interesting relations by studying the
    interaction between two variables. Create two new columns in your subset
    dataframe by multiplying two other columns where you think that their
    combined presence might be more predictive of the wines quality than
    looking at the individual numbers alone. If you, like you can also come up
    with another creative ratio of your features
"""
# your code


"""
9. Save your newly created subset as a csv on your computer
"""
# your code





#
