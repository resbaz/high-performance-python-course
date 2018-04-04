## Multicore

This is a multicore example, using the Python `multiprocessing` library. Our SLURM script requests 4 cores (CPUs), and our Python script then starts four processes to run across them.

Extending from the `easy_parallel` example, we're going to count the words across four files, and then sum them to get an overall total. This last step requires communication between processes, which is what makes this a multicore job rather than just embarassingly parallel.

You can submit this job using:

`sbatch multicore.slurm`

... and check its status using:

`squeue -u your_username`


It should only take a few moments to run, but it might take some time until compute resources are available for you. You can find the results of each job in output files, which will look like `slurm-(job number).out`.


# How to Extend

Check out the multiprocessing documentation for more details (https://docs.python.org/2/library/multiprocessing.html), there are many more ways of initiating processes and communicating between them using queues, semaphores and so on.