# Introduction to Pandas

Pandas is a powerful and flexible open-source data analysis and manipulation library for Python. It provides data structures and functions needed to work on structured data seamlessly. The primary data structures in Pandas are `Series` and `DataFrame`.

Here I Will not be explaining to explain it;s usage. I am just explain how does it store data in memory:
So what pandas does is, it store data in columnar way. What columnar is for suppose you have a dataframe with columns `Employee Id`, `Name`,  `salary`. Now What pandas does is, it store all values of Employee id in one contiguous memory (like vector).

Why does it do so?

It helps in faster read queries.So for suppose you want to apply average of `Salary` column. Now What will happend it will not read other columns from memory, saving reading time and less processing.