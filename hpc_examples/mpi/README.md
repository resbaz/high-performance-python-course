## Multinode

This is a multinode example using MPI (Message Passing Interface). It works by passing messages within and between computers on a network (instead of through shared memory on a single computer), which allows it to scale to thousands of CPUs. It's a complex framework, and there's a huge literature on how to get the most out of it for particular applications. 

Here we have a simple example, with just four tasks -- one acting as the master, and three as slaves (there are many other topologies possible of course). These tasks will work together to come up with an estimate for Pi. The master task will send out instructions to the slave tasks, which will sit pending until the receive a command, do the work, send the result to the master, and then shutdown. Using our SLURM script, we're going to request the four tasks, and one CPU for each, and kick them off using the `mpiexec` command.

You can submit this job using:

`sbatch mpi.slurm`

... and check its status using:

`squeue -u your_username`


It should only take a few moments to run, but it might take some time until compute resources are available for you. You can find the results of each job in output files, which will look like `slurm-(job number).out`.


# How to Extend

Check out the multiprocessing documentation for more details (https://docs.python.org/2/library/multiprocessing.html), there are many more ways of initiating processes and communicating between them using queues, semaphores and so on.