#   Tutorial gap seq

## ⚙️ Instalación 
### a) Descargar dependencias 

```bash
sudo apt install ncbi-blast+ git libglpk-dev r-base-core exonerate bedtools barrnap bc parallel curl libcurl4-openssl-dev libssl-dev libsbml5-dev bc
```
### b) Descargar versión más actual 

```bash
git clone https://github.com/jotech/gapseq && cd gapseq
```
### c) Descaragar base de datos de secuencias de referencia más actualizada  
```bash
bash ./src/update_sequences.sh
```

### d) Agregar ruta
```bash
export PATH=$PATH:$(pwd)
```

### e) Confirmar si se intaló 
```bash
./gapseq test
```
📨 Salida:
```
/gapseq test

gapseq version: 1.4.0 95c8e31d
linux-gnu
#149~20.04.1-Ubuntu SMP Wed Apr 16 08:29:56 UTC 2025 
```

Workflow

```
RC3LPC_1_NS_M1_01_25.faa

mv RC3LPC_1_NS_M1_01_25.faa bac1.faa

RC3="bac1"

                                    
gapseq find-transport -b 200 $RC3.faa 

          
gapseq draft -r $RC3-all-Reactions.tbl -t $RC3-Transporter.tbl -p $RC3-all-Pathways.tbl -u 200 -l 100 -c $RC3.faa

gapseq fill -m $RC3-draft.RDS -n LBmed.csv -c $RC3-rxnWeights.RDS -g $RC3-rxnXgenes.RDS -b 100

```
#!/bin/bash
 #SBATCH --job-name=prokka
 #SBATCH --output=%x.log
 #SBATCH --error=%x.error
 #SBATCH --time=240:00:00
 #SBATCH --cpus-per-task=8
 #SBATCH --mem=8G


 # Info del script
 # prueba de prokka
 date
 echo "===== Beginning pipeline ====="
 eval "$(conda shell.bash hook )"
 conda activate prokka

 # comand line 


'''bash
#!/bin/bash
 #SBATCH --job-name=gapseq
 #SBATCH --output=%x.log
 #SBATCH --error=%x.error
 #SBATCH --time=240:00:00
 #SBATCH --cpus-per-task=8
 #SBATCH --mem=8G

 # Info del script
 # gapsec bacteria rizo

 date
 echo "===== Beginning pipeline ====="

 eval "$(conda shell.bash hook )"
 conda activate gapseq

 # comand line


INPUT_DIR="/mnt/data/sur/users/mmontante/input"
 OUTPUT_DIR="/mnt/data/sur/users/mmontante/output"

 mkdir -p "$OUTPUT_DIR"

 for file in "$INPUT_DIR"/ST*.fna; do
     base=$(basename "$file" .fna)

    gapseq doall "$file" \
         --outdir "$OUTPUT_DIR/$base" \
         --prefix "$base" \
         --cpus 8 \
         --kingdom Bacteria
 done

 echo "===== Pipeline done ====="
 date
'''
ad