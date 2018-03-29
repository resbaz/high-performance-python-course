## Multiprocessing

This is a multicore example, using the Python `multiprocessing` library. Our SLURM script requests 4 cores (CPUs), and our Python script then starts four processes to run across them.

Extending from the `easy_parallel` example, we're going to count the words across four files, and then sum them to get an overall total. This last step requires communication between processes, which is what makes this a multicore job rather than just embarassingly parallel.


 
 
You can submit this job using:

`sbatch easy_parallel.slurm`

... and check its status using:

`squeue -u your_username`


It should only take a few moments to run, but it might take some time until compute resources are available for you. You can find the results of each job in output files, which will look like `slurm-(job number)_(array index).out`.


# How to Extend

Instead of referring to input files directly using `SLURM_ARRAY_TASK_ID`, you might use this number in your script to dynamically look up a file name, or even look up a particular row in a CSV file which maps the inputs you'd like to use for the job.