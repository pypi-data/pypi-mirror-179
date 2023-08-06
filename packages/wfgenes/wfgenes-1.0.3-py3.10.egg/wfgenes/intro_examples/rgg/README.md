# wfGenes Executor Tuning:

This guide help users to tune wfGenes executor for porting wfGenes python model from single machine to clusters. 

1. single machine: Using available local threads. 
2. Clusters: Submit a job to run a python model on clusters through Slurm workload manager. 

To run the examples in this directory, use run_model.py with necessary arguments to tune executors and perform computation:  

        --model_path - Path to python executable(Dask or Parsl based workflow) 
        
        --pool- Specify pool type. Possible options are [local_threads, slurm]

        --sleep(int) - Sleep duration(sec) of each task, valid only for balanced case

        --maximum_threads(int) - Maximum local thread size, siuted for single machine without slurm workload manger (only with local_threads pool type)


        --scale(int)- Specify number of nodes (only with Slurm)

        --worker_per_node(int)- Set number of workers per node (only with Slurm)

        --cpu_per_node(int)- Number of cores per worker (only with Slurm)


        
        
        
        