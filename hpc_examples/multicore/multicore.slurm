#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --time=0-00:5:00

module load Python/3.6.1-intel-2017.u2

python multicore.py