### Handling Large Datasets in Pandas (Memory Optimisation)

Well working with datasets in python, there is one answer comes to mind `Pandas`.yes it most useful python library to work with data, but it also comes with flaws which we will get to know in this blog.

So Pandas can perform very well while working with small datasets but it's not recommended to use pandas in large datasets due to preprocessing and memory usage.When the dataset is small, around 2-3 GB, Panda is a fantastic tool. However, using Pandas is not recommended when the dataset size exceeds 2-3 GB. Before performing any processing on the DataFrame, Pandas loads all of the data into memory. Therefore, you will encounter memory errors if the size of the dataset exceeds the RAM. As a result, datasets larger than what can fit in RAM cannot be handled by Pandas.

Sometimes, even when the dataset is smaller than the available RAM, we still experience memory problems. Because of the creation of a copy of the DataFrame during preprocessing and transformation by Pandas, the memory footprint is increased, leading to memory problems.

However, it is possible to use Pandas on datasets that are larger than what can fit in memory. With some techniques, Pandas may be used to manage big datasets in Python.

Let's look at some of the methods

#### Sampling

For randomly selecting N items from a list, use the .sample() method. The sample() function in the random module of Python allows for random sampling, which selects many elements at random from a list without repeating any of the elements. It gives a list of distinct items selected at random from the list, sequence, or collection. It is referred to as random sampling without replacement.


#### Chunking

If you are working with large data, we can split the data into several chunks and then can perform operation data cleaning and feature engineering on each chunk. Additionally, you have two choices based on the kind of model you want to use:

If the model of your choice allows for partial fitting, you can incrementally train a model on the data of each chunk.
For each chunk, train a model separately. Predict with each model and then pick the average or majority vote as the final prediction to determine the score for unseen data.


```python
import pandas as pd
data = pd.read_csv('file_address',chunksize=1000)
print(data)

```


#### Optimizing Data Types

We can optimize the data types to reduce memory usage. By using the memory_usage() function we can find the memory used by the data objects. It returns a series with an index of the original column names and values representing the amount of memory used by each column in bytes.