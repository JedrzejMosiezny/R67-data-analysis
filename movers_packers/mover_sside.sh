#!/bin/bash -l
## Nazwa zlecenia
#SBATCH -J SRS_v02_move_sside
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
#SBATCH --output="output-sside.out"
## Plik ze standardowym wyjściem błędów
#SBATCH --error="error-sside.err"


## przejscie do katalogu z ktorego wywolany zostal sbatch
cd $SLURM_SUBMIT_DIR
srun /bin/hostname


## run calculation
cp -r /net/scratch/people/plgmosieznyj/SRS_v02/noise-data/sside/* /net/archive/groups/plggcfdp/R67_fluent/SRS_v02/noise-data/sside/*

# ----------------------------------------------------------------- end-of-file