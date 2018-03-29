## Embarassingly Parallel

This is the simplest approach to parallel programming, where each task can run completely independently. Say for example you have a large set of images to batch process, or you need to run a model repeatedly with many different parameters.

A common way to structure this task on a HPC system is by using a job array. In this example, a single run will create ten seperate jobs, processing ten separate files. SLURM creates a special variable `SLURM_ARRAY_TASK_ID`, which each job can use to identify itself so it may select, for example, a particular input file or set of input parameters.
 
In this example, we have ten text files, and we would like to count the number of words in each.
 
You can submit this job using:

`sbatch easy_parallel.slurm`

... and check its status using:

`squeue -u your_username`


It should only take a few moments to run, but it might take some time until compute resources are available for you. You can find the results of each job in output files, which will look like `slurm-(job number)_(array index).out`.


# How to Extend

Instead of referring to input files directly using `SLURM_ARRAY_TASK_ID`, you might use this number in your script to dynamically look up a file name, or even look up a particular row in a CSV file which maps the inputs you'd like to use for the job.