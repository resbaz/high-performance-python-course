#!/bin/bash
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=4
#SBATCH --time=0-00:5:00

module load Python/3.6.1-intel-2017.u2

mpiexec -np 4 python mpi_example.py