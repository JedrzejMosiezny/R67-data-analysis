#!/bin/bash -l
## Nazwa zlecenia
#SBATCH -J SRS_v02_pack_int-05
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
#SBATCH --output="output-int-05.out"
## Plik ze standardowym wyjściem błędów
#SBATCH --error="error-int-05.err"
## Ilość pamięci przypadającej na jeden rdzeń obliczeniowy (domyślnie 5GB na rdzeń)
#SBATCH --mem-per-cpu=32GB

## przejscie do katalogu z ktorego wywolany zostal sbatch
cd $SLURM_SUBMIT_DIR
srun /bin/hostname

## run calculation
tar -cf - /net/archive/groups/plggcfdp/R67_fluent/SRS_v02/flow-data/int-05/ | xz -9 -c - > SRS_v02_int-05.tar.xz

# ----------------------------------------------------------------- end-of-file