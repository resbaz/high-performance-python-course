#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --time=0-00:5:00
#SBATCH --array=1-5

module load Python/3.6.1-intel-2017.u2

python word_count.py input_${SLURM_ARRAY_TASK_ID}.txt