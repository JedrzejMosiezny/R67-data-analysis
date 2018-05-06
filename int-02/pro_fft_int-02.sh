#!/bin/bash -l
## Nazwa zlecenia
#SBATCH -J SRS_v02-int-02-fft
## Liczba węzłów
#SBATCH --nodes=1
## Ilość zadań na węzeł
#SBATCH --ntasks-per-node=1
## Ilość pamięci przypadającej na jeden rdzeń obliczeniowy (domyślnie 5GB na rdzeń)
#SBATCH --mem-per-cpu=32GB
## Maksymalny czas trwania zlecenia (format HH:MM:SS)
#SBATCH --time=72:00:00 
## Nazwa grantu do rozliczenia zużycia zasobów
#SBATCH -A acnoise2017
## Specyfikacja partycji
#SBATCH -p plgrid
## Plik ze standardowym wyjściem
#SBATCH --output="fft.out"
## Plik ze standardowym wyjściem błędów
#SBATCH --error="fft.err"


## przejscie do katalogu z ktorego wywolany zostal sbatch
cd $SLURM_SUBMIT_DIR

srun /bin/hostname

## Load python
module load tools/python-intel/3.6.2

## point to work directory
#cd $PBS_O_WORKDIR

## run calculation
python3 /net/people/plgmosieznyj/R67-data-analysis/int-02/int-02-fft.py

# ----------------------------------------------------------------- end-of-file