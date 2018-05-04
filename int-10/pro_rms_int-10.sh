#!/bin/bash -l
## Nazwa zlecenia
#SBATCH -J SRS_v02-int-10-rms
## Liczba węzłów
#SBATCH --nodes=1
## Ilość zadań na węzeł
#SBATCH --ntasks-per-node=1
## Maksymalny czas trwania zlecenia (format HH:MM:SS)
#SBATCH --time=72:00:00 
## Nazwa grantu do rozliczenia zużycia zasobów
#SBATCH -A acnoise2017
## Specyfikacja partycji
#SBATCH -p plgrid
## Plik ze standardowym wyjściem
#SBATCH --output="rms.out"
## Plik ze standardowym wyjściem błędów
#SBATCH --error="rms.err"


## przejscie do katalogu z ktorego wywolany zostal sbatch
cd $SLURM_SUBMIT_DIR

srun /bin/hostname

## Load python
module load tools/python-intel/3.6.2

## point to work directory
#cd $PBS_O_WORKDIR

## run calculation
python3 /net/people/plgmosieznyj/R67-data-analysis/int-10/int-10-rms.py

# ----------------------------------------------------------------- end-of-file