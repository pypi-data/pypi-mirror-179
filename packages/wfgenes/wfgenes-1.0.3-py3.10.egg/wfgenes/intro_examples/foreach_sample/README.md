
## FOREACH
wfGenes implements the FOREACH method to support data parallelism in python models. The specification of FOREACh is set through 'func' field in the WConfig file. 

      func: [ filename(str), modulename(str) , FOREACH(str) , partitionable(str), unrolling factor(str), zip_inputs(list)] 

* filename(str): a name of python source file. 
* modulename(str): a name of module to be imported, the *filename* must be in $PYTHONPATH. 
* FOREACH(str): This enables wfGenes to generate necessary code for **FOREACH** method.
* partitionable(str): The array which **'FOREACH'** traverse in a parallel manner. 
* Partitioning factor(str): The default is **'full'** that rovides the maximum level of parallelism. Max = len(partitionable) and min = 1, any value between can be set to achieve optimum performance. 
* zip_inputs(lst): List of arguments to be partitioned  with same factor as split array passed to concurrent function instances.       

Both Dask and Parsl return tuple objects for parallel FOREACH operation. Within the wfGenes framework, flat_tuple method is used to map the computed results of function with multiple return objects to separate lists which can be used for further data processing. The flat_list method has the same functionality with much simpler implementation for functions with single return value. The wfGenes is capable to generate code and deploy proper builtin methods in **BUILTIN** file placed in  **wfGenes_exe** folder in this repository. 

```
results = []
for element in split_array:
    y = dask.delayed(f)(element)
    tuple_result.append(y)

results = dask.compute(*tuple_result)

flat_result = flat_tuple(results, retun_number)

```


![image info](./fig/dask_tuple.png)


 
