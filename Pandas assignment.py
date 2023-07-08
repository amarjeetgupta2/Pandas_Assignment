PandasAssignment

Q1. How do you load a CSV file into a Pandas DataFrame?
A1. df=pd.read_csv('data.csv')

Q2. How do you check the data type of a column in a Pandas DataFrame?
A2. Use the “dtype” attribute. i.e. df.dtypes

Q3. How do you select rows from a Pandas DataFrame based on a condition?
A3. df.head()-for top 5 rows (Enter value in bracket which is no. of rows, by defaukt it takes 5 rows)
    df.tail()-for bottom 5 rows (Enter value in bracket which is no. of rows, by defaukt it takes 5 rows)
e.g. df[8:13] - if we want to see rows from 8 to 12
e.g. df[8:13:2] - if we want to see rows from 8 to 12 with gap of 2rows.

Q4. How do you rename columns in a Pandas DataFrame?
A4. By using the rename() function.

Q5. How do you drop columns in a Pandas DataFrame?
A5. By specifying the column axis ( axis='columns' ), the drop() method removes the specified column. 
    df.drop('Column_name',axis=1, inplace=True)

Q6. How do you find the unique values in a column of a Pandas DataFrame?
A6. DataFrame().unique() method is used. 
    e.g. df.Column_name.unique()

Q7. How do you find the number of missing values in each column of a Pandas DataFrame?
A7. By using  isnull().values.any() method

Q8. How do you fill missing values in a Pandas DataFrame with a specific value?
A8. By using this syntax: DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None, **kwargs)

Q9. How do you concatenate two Pandas DataFrames?
A9. By using pd.concat() method:
    e.g. # concatenating df1 and df2 along rows
         vertical_concat = pd.concat([df1, df2], axis=0)

Q10. How do you merge two Pandas DataFrames on a specific column?
A10. We can merge two Pandas DataFrames on certain columns using the merge function by simply specifying the certain columns for merge. 

Syntax: DataFrame.merge(right, how=’inner’, on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, copy=True, indicator=False, validate=None)

Q11. How do you group data in a Pandas DataFrame by a specific column and apply an aggregation function?
A11. 

Q12. How do you pivot a Pandas DataFrame?
A12. The pivot() function is used to reshaped a given DataFrame organized by given index / column values.
     Syntax: DataFrame.pivot(*, index=None, columns=None, values=None)


Q13. How do you change the data type of a column in a Pandas DataFrame?
A13. To change column type into string object, use DataFrame.astype() 
	Change column type in pandas using dictionary and DataFrame.astype()
	Change column type in pandas using DataFrame.apply()
	Change column type in pandas using DataFrame.infer_objects()
	Change column type in pandas using convert_dtypes()

Q14. How do you sort a Pandas DataFrame by a specific column?
A14. df.sort_values()

Q15. How do you create a copy of a Pandas DataFrame?
A15. By using copy() Method---The copy() method returns a copy of the DataFrame.

Q16. How do you filter rows of a Pandas DataFrame by multiple conditions?
A16. By using df.loc[(dfcondition1) & (dfcondition2)]

Q17. How do you calculate the mean of a column in a Pandas DataFrame?
A17. To get column average or mean from pandas DataFrame use either mean() and describe() method.
     The DataFrame. mean() method is used to return the mean of the values for the requested axis.

Q18. How do you calculate the standard deviation of a column in a Pandas DataFrame?
A18. In Pandas,the std() function is used to find the standard Deviation of the series. 

Q19. How do you calculate the correlation between two columns in a Pandas DataFrame?
A19. In pandas, by using corr() function we can get the correlation between two columns in the dataframe.

Q20. How do you select specific columns in a DataFrame using their labels?
A20. To select a single column, use square brackets [] with the column name of the column of interest.

Q21. How do you select specific rows in a DataFrame using their indexes?
A21. You can use pandas. DataFrame. iloc[] with the syntax [start:stop:step] ; 
     where start indicates the index of the first row to start, stop indicates the index of the last row to stop, and 
     step indicates the number of indices to advance after each extraction.

Q22. How do you sort a DataFrame by a specific column?
A22. To sort the DataFrame based on the values in a single column, use df.sort_values().

Q23. How do you create a new column in a DataFrame based on the values of another column?
A23. Using apply() method

Q24. How do you remove duplicates from a DataFrame?
A24.The drop_duplicates() method removes duplicate rows.

Q25. What is the difference between .loc and .iloc in Pandas?
A25. loc gets DataFrame rows & columns by labels/names and iloc[] gets by integer Index/position. For loc[], if the label is not present it gives a key error. 
     For iloc[], if the position is not present it gives an index error.