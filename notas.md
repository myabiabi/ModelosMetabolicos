# 20250606

## RECONSTRUCCION DE GEM
## CarveMe
### ¿Qué hace?

1. Leer el archivo .faa con las proteínas anotadas del genoma
2. Alinear las proteínas con su propia base de datos de referencia (basada en BiGG) usando DIAMOND
3. Aplicar reglas GPR para asociar genes con proteínas con reacciones
4. Calcular puntuaciones para cada reacción (basadas en similitud)
5. 	Eliminar reacciones con puntuación baja (model carving)
6. 	Generar el modelo metabólico en formato .sbml o .json

### Instalación
 ```bash
 $pip install carveme
 ```
  ```bash
$conda install -c bioconda diamond
 ```
Solver: Gurobi (ya lo tenía instalado)

### Ejecución
 ```bash
carve genome.faa -o model.xml
```
### Más información 
[Documentación de CarveMe](https://carveme.readthedocs.io/en/latest/index.html)

## GapSeq
### Instalacion 

Descargar dependencias 
```bash
sudo apt install ncbi-blast+ git libglpk-dev r-base-core exonerate bedtools barrnap bc parallel curl libcurl4-openssl-dev libssl-dev libsbml5-dev bc
```
Descargar versión más actual 
```bash
git clone https://github.com/jotech/gapseq && cd gapseq
```
 Descaragar base de datos de secuencias de referencia más actualizada  
```bash
bash ./src/update_sequences.sh
```
Confirmar si se intaló 
```bash
./gapseq test
```
```
/gapseq test

gapseq version: 1.4.0 95c8e31d
linux-gnu
#149~20.04.1-Ubuntu SMP Wed Apr 16 08:29:56 UTC 2025 
```



### Más informaciójn
[Documentación de GaoSeq](https://gapseq.readthedocs.io/en/latest/)

# 092524

### vincular con un repositorio
```bash
git init
git add .
git remote add origin https://github.com/myabiabi/Modelos-Metab-licos-.git
```
### Guardar, comit y push
Primero guardar el scrip que tengo
después en la terminal
```bash
git add ''scrip.py''
git commit -m "mensaje de la modificiacion"
git push
```
Refesh gitbub

## GAPSEQ
Puede ser utilizado para predecir _rutas metabólicas_ y por el otro lado sirve para reconstruir _redes metabólicas_ 

En un inicio todas las predicciones pueden ser hechas con: 
## ejemplo documentación

```b
./gapseq doall toy/myb71.fna.gz

```

Para correrlo tienes que especificar la dirección de donde se descargó el programa
## no me corrió

```b
/home/abigaylmontantearenas/Documents/practicas/MODELOS/doc/gapseq/gapseq doall toy/C2RQJT_1_rerun_NS_M2_01_25_2.fna
```
o asignar un alias
### no lo probé
```b 
alias gapseq='/home/abigaylmontantearenas/Documents/practicas/MODELOS/doc/gapseq/gapseq'

```
```b
gapseq doall toy/C2RQJT_1_rerun_NS_M2_01_25_2.fna
```

C2RQJT_1_rerun_NS_M2_01_25_2.fna

### ESTA  LINEA FUE LA QUE CORRIÓ 
```b
~/Documents/practicas/MODELOS/doc/gapseq/gapseq doall ~/Documents/practicas/MODELOS/data/C2RQJT_1_rerun_NS_M2_01_25_2.fna

```

# 130625

### tutorial gapseq

[referencia](https://github.com/jotech/gapseq/blob/master/docs/tutorials/yogurt.md)
Después de instalarlo agregar path temporal a gapseq

```
export PATH=$PATH:$(pwd)
```


```bash
gapseq find -p all -b 200 -m auto -t auto $modelA.faa.gz
```
error:
```bash
Error in library(httr) : there is no package called ‘httr’
Execution halted
md5sum: 1.3.1.8.fasta: No such file or directory
cat: 1.3.1.8.fasta: No such file or directory
		Downloading unreviewed sequences for: 1.3.1.8
```
¿Qué pasó?
el paquete httr de R no está instalado

¿Cómo solucionarlo? 

```bash
R
install.packages("httr")
library(httr)
q()
```
LO vuelvo a correr

```bash
gapseq find -p all -b 200 -m auto -t auto $modelA.faa.gz
```
Error: 
```
Error in library(stringr) : there is no package called ‘stringr’
Execution halted
md5sum: 0e9279fadf0e6dab0a8e78912d5a37d4.fasta: No such file or directory
cat: 0e9279fadf0e6dab0a8e78912d5a37d4.fasta: No such file or directory
		Downloading unreviewed sequences for: 2,4-dichloro-cis,cis-muconate dehalogenase 
		(hash: 0e9279fadf0e6dab0a8e78912d5a37d4)
```
¿Qué pasó? ocupo el paquete de R "stringr"

Paquetes necesarios: 
* httr (para descargar datos vía HTTP)

* stringr (para manipulación de strings)

* jsonlite (para manejar JSON)

* data.table (para manejo eficiente de tablas)

* dplyr (para manipulación de datos)

* tidyr (para ordenar y limpiar datos)

* magrittr (para usar pipes %>%)

* curl (para conexiones HTTP)

```
sudo R -e "install.packages(c('httr','stringr','jsonlite','data.table','dplyr','tidyr','magrittr','curl'), repos='https://cloud.r-project.org')"

R

library(httr)
library(stringr)
library(jsonlite)
library(data.table)
library(dplyr)
library(tidyr)
library(magrittr)
library(curl)

q()

```
Vuelvo a correr el mismo código

```
gapseq find -p all -b 200 -m auto -t auto $modelA.faa.gz
```
Ya jaló

```
3339 s
```
pero según yo fue 1:15 (de las 3:57-5:11)

siguiendo con el tutorial
```
gapseq find -p all -b 200 -m auto -t auto $modelB.faa.gz

```
de las 18:05 a 19:01

3345 s

```
gapseq find-transport -b 200 $modelA.faa.gz 
```

Running time: 93 s.


```
/tmp/tmp.jrImsFbkeu
Protein fasta detected.
glycerol lactic acid 1.A.8.2.4 1.Channels and pores
glycerol 1.A.8.2.8 1.Channels and pores
formate FORMATE OXALATE 2.A.1.11.1 2.Electrochemical potential-driven transporters
formate FORMATE OXALATE 2.A.1.11.1 2.Electrochemical potential-driven transporters
formate FORMATE OXALATE 2.A.1.11.1 2.Electrochemical potential-driven transporters
chloride cysteine deoxyuridine sodium sulfate uridine 2.A.1.3.3 2.Electrochemical potential-driven transporters
chloride cysteine deoxyuridine sodium sulfate uridine 2.A.1.3.3 2.Electrochemical potential-driven transporters
chloride cysteine deoxyuridine sodium sulfate uridine 2.A.1.3.3 2.Electrochemical potential-driven transporters
chloride cysteine deoxyuridine sodium sulfate uridine 2.A.1.3.3 2.Electrochemical potential-driven transporters
chloride cysteine deoxyuridine sodium sulfate uridine 2.A.1.3.3 2.Electrochemical potential-driven transporters
chloride cysteine deoxyuridine sodium sulfate uridine 2.A.1.3.3 2.Electrochemical potential-driven transporters
chloride 2.A.1.3.50 2.Electrochemical potential-driven transporters
(R)-lactate (S)-lactate 2.A.14.1.3 2.Electrochemical potential-driven transporters
(R)-lactate (S)-lactate 2.A.14.1.3 2.Electrochemical potential-driven transporters
lactose 2.A.2.2.1 2.Electrochemical potential-driven transporters
raffinose 2.A.2.2.2 2.Electrochemical potential-driven transporters
D-galactose 2.A.2.2.3 2.Electrochemical potential-driven transporters
sodium 2.A.26.1.1 2.Electrochemical potential-driven transporters
L-isoleucine valine 2.A.26.1.2 2.Electrochemical potential-driven transporters
L-isoleucine valine 2.A.26.1.2 2.Electrochemical potential-driven transporters
arginine D-alanine D-serine histidine L-alanine L-methionine lysine phenylalanine putrescine tryptophan tyrosine 2.A.3.1.1 2.Electrochemical potential-driven transporters
arginine D-alanine D-serine histidine L-alanine L-methionine lysine phenylalanine putrescine tryptophan tyrosine 2.A.3.1.1 2.Electrochemical potential-driven transporters
arginine D-alanine D-serine histidine L-alanine L-methionine lysine phenylalanine putrescine tryptophan tyrosine 2.A.3.1.1 2.Electrochemical potential-driven transporters
arginine D-alanine D-serine histidine L-alanine L-methionine lysine phenylalanine putrescine tryptophan tyrosine 2.A.3.1.1 2.Electrochemical potential-driven transporters
arginine D-alanine D-serine histidine L-alanine L-methionine lysine phenylalanine putrescine tryptophan tyrosine 2.A.3.1.1 2.Electrochemical potential-driven transporters
arginine D-alanine D-serine histidine L-alanine L-methionine lysine phenylalanine putrescine tryptophan tyrosine 2.A.3.1.1 2.Electrochemical potential-driven transporters
arginine D-alanine D-serine histidine L-alanine L-methionine lysine phenylalanine putrescine tryptophan tyrosine 2.A.3.1.1 2.Electrochemical potential-driven transporters
arginine D-alanine D-serine histidine L-alanine L-methionine lysine phenylalanine putrescine tryptophan tyrosine 2.A.3.1.1 2.Electrochemical potential-driven transporters
arginine D-alanine D-serine histidine L-alanine L-methionine lysine phenylalanine putrescine tryptophan tyrosine 2.A.3.1.1 2.Electrochemical potential-driven transporters
arginine D-alanine D-serine histidine L-alanine L-methionine lysine phenylalanine putrescine tryptophan tyrosine 2.A.3.1.1 2.Electrochemical potential-driven transporters
arginine D-alanine D-serine histidine L-alanine L-methionine lysine phenylalanine putrescine tryptophan tyrosine 2.A.3.1.1 2.Electrochemical potential-driven transporters
L-methionine 2.A.3.1.10 2.Electrochemical potential-driven transporters
arginine 2.A.3.1.11 2.Electrochemical potential-driven transporters
D-alanine D-serine L-alanine 2.A.3.1.17 2.Electrochemical potential-driven transporters
D-alanine D-serine L-alanine 2.A.3.1.17 2.Electrochemical potential-driven transporters
D-alanine D-serine L-alanine 2.A.3.1.17 2.Electrochemical potential-driven transporters
Lysine 2.A.3.1.19 2.Electrochemical potential-driven transporters
asparagine D-alanine D-serine glycine L-alanine L-cysteine L-serine L-threonine lysine phenylalanine proline tryptophan tyrosine 2.A.3.1.2 2.Electrochemical potential-driven transporters
asparagine D-alanine D-serine glycine L-alanine L-cysteine L-serine L-threonine lysine phenylalanine proline tryptophan tyrosine 2.A.3.1.2 2.Electrochemical potential-driven transporters
asparagine D-alanine D-serine glycine L-alanine L-cysteine L-serine L-threonine lysine phenylalanine proline tryptophan tyrosine 2.A.3.1.2 2.Electrochemical potential-driven transporters
asparagine D-alanine D-serine glycine L-alanine L-cysteine L-serine L-threonine lysine phenylalanine proline tryptophan tyrosine 2.A.3.1.2 2.Electrochemical potential-driven transporters
asparagine D-alanine D-serine glycine L-alanine L-cysteine L-serine L-threonine lysine phenylalanine proline tryptophan tyrosine 2.A.3.1.2 2.Electrochemical potential-driven transporters
asparagine D-alanine D-serine glycine L-alanine L-cysteine L-serine L-threonine lysine phenylalanine proline tryptophan tyrosine 2.A.3.1.2 2.Electrochemical potential-driven transporters
asparagine D-alanine D-serine glycine L-alanine L-cysteine L-serine L-threonine lysine phenylalanine proline tryptophan tyrosine 2.A.3.1.2 2.Electrochemical potential-driven transporters
asparagine D-alanine D-serine glycine L-alanine L-cysteine L-serine L-threonine lysine phenylalanine proline tryptophan tyrosine 2.A.3.1.2 2.Electrochemical potential-driven transporters
asparagine D-alanine D-serine glycine L-alanine L-cysteine L-serine L-threonine lysine phenylalanine proline tryptophan tyrosine 2.A.3.1.2 2.Electrochemical potential-driven transporters
asparagine D-alanine D-serine glycine L-alanine L-cysteine L-serine L-threonine lysine phenylalanine proline tryptophan tyrosine 2.A.3.1.2 2.Electrochemical potential-driven transporters
asparagine D-alanine D-serine glycine L-alanine L-cysteine L-serine L-threonine lysine phenylalanine proline tryptophan tyrosine 2.A.3.1.2 2.Electrochemical potential-driven transporters
asparagine D-alanine D-serine glycine L-alanine L-cysteine L-serine L-threonine lysine phenylalanine proline tryptophan tyrosine 2.A.3.1.2 2.Electrochemical potential-driven transporters
asparagine D-alanine D-serine glycine L-alanine L-cysteine L-serine L-threonine lysine phenylalanine proline tryptophan tyrosine 2.A.3.1.2 2.Electrochemical potential-driven transporters
D-alanine D-serine glycine L-alanine L-serine 2.A.3.1.20 2.Electrochemical potential-driven transporters
D-alanine D-serine glycine L-alanine L-serine 2.A.3.1.20 2.Electrochemical potential-driven transporters
D-alanine D-serine glycine L-alanine L-serine 2.A.3.1.20 2.Electrochemical potential-driven transporters
D-alanine D-serine glycine L-alanine L-serine 2.A.3.1.20 2.Electrochemical potential-driven transporters
D-alanine D-serine glycine L-alanine L-serine 2.A.3.1.20 2.Electrochemical potential-driven transporters
L-cysteine L-serine L-threonine 2.A.3.1.21 2.Electrochemical potential-driven transporters
L-cysteine L-serine L-threonine 2.A.3.1.21 2.Electrochemical potential-driven transporters
L-cysteine L-serine L-threonine 2.A.3.1.21 2.Electrochemical potential-driven transporters
proline 2.A.3.1.23 2.Electrochemical potential-driven transporters
asparagine 2.A.3.1.24 2.Electrochemical potential-driven transporters
D-alanine D-serine glycine 2.A.3.1.25 2.Electrochemical potential-driven transporters
D-alanine D-serine glycine 2.A.3.1.25 2.Electrochemical potential-driven transporters
D-alanine D-serine glycine 2.A.3.1.25 2.Electrochemical potential-driven transporters
phenylalanine tryptophan tyrosine 2.A.3.1.3 2.Electrochemical potential-driven transporters
phenylalanine tryptophan tyrosine 2.A.3.1.3 2.Electrochemical potential-driven transporters
phenylalanine tryptophan tyrosine 2.A.3.1.3 2.Electrochemical potential-driven transporters
alanine gamma-aminobutyric acid proline 2.A.3.1.5 2.Electrochemical potential-driven transporters
alanine gamma-aminobutyric acid proline 2.A.3.1.5 2.Electrochemical potential-driven transporters
alanine gamma-aminobutyric acid proline 2.A.3.1.5 2.Electrochemical potential-driven transporters
proline 2.A.3.1.6 2.Electrochemical potential-driven transporters
D-alanine D-serine glycine serine 2.A.3.1.7 2.Electrochemical potential-driven transporters
D-alanine D-serine glycine serine 2.A.3.1.7 2.Electrochemical potential-driven transporters
D-alanine D-serine glycine serine 2.A.3.1.7 2.Electrochemical potential-driven transporters
D-alanine D-serine glycine serine 2.A.3.1.7 2.Electrochemical potential-driven transporters
asparagine 2.A.3.1.8 2.Electrochemical potential-driven transporters
histidine 2.A.3.1.9 2.Electrochemical potential-driven transporters
sodium 2.A.35.1.1 2.Electrochemical potential-driven transporters
lactate malate sodium 2.A.35.1.2 2.Electrochemical potential-driven transporters
lactate malate sodium 2.A.35.1.2 2.Electrochemical potential-driven transporters
lactate malate sodium 2.A.35.1.2 2.Electrochemical potential-driven transporters
lactate malate sodium 2.A.35.1.2 2.Electrochemical potential-driven transporters
tyrosine 2.A.35.1.3 2.Electrochemical potential-driven transporters
arginine ornithine 2.A.35.1.4 2.Electrochemical potential-driven transporters
arginine ornithine 2.A.35.1.4 2.Electrochemical potential-driven transporters
sodium 2.A.35.1.6 2.Electrochemical potential-driven transporters
gamma-aminobutyric acid glutamate 2.A.3.7.2 2.Electrochemical potential-driven transporters
gamma-aminobutyric acid glutamate 2.A.3.7.2 2.Electrochemical potential-driven transporters
sodium 2.A.37.2.1 2.Electrochemical potential-driven transporters
potassium sodium 2.A.37.2.2 2.Electrochemical potential-driven transporters
potassium sodium 2.A.37.2.2 2.Electrochemical potential-driven transporters
aspartate glutamate 2.A.3.7.6 2.Electrochemical potential-driven transporters
aspartate glutamate 2.A.3.7.6 2.Electrochemical potential-driven transporters
histidine L-threonine phenylalanine serine tryptophan tyrosine 2.A.3.8.12 2.Electrochemical potential-driven transporters
histidine L-threonine phenylalanine serine tryptophan tyrosine 2.A.3.8.12 2.Electrochemical potential-driven transporters
histidine L-threonine phenylalanine serine tryptophan tyrosine 2.A.3.8.12 2.Electrochemical potential-driven transporters
histidine L-threonine phenylalanine serine tryptophan tyrosine 2.A.3.8.12 2.Electrochemical potential-driven transporters
histidine L-threonine phenylalanine serine tryptophan tyrosine 2.A.3.8.12 2.Electrochemical potential-driven transporters
histidine L-threonine phenylalanine serine tryptophan tyrosine 2.A.3.8.12 2.Electrochemical potential-driven transporters
uracil 2.A.40.1.1 2.Electrochemical potential-driven transporters
uracil 2.A.40.1.2 2.Electrochemical potential-driven transporters
uracil 2.A.40.1.4 2.Electrochemical potential-driven transporters
xanthine 2.A.40.3.1 2.Electrochemical potential-driven transporters
xanthine 2.A.40.3.3 2.Electrochemical potential-driven transporters
xanthine 2.A.40.4.2 2.Electrochemical potential-driven transporters
guanosine 2.A.40.7.2 2.Electrochemical potential-driven transporters
guanosine 2.A.40.7.4 2.Electrochemical potential-driven transporters
xanthine 2.A.40.7.5 2.Electrochemical potential-driven transporters
2-oxoglutarate 2.A.47.3.1 2.Electrochemical potential-driven transporters
citrate succinate 2.A.47.3.2 2.Electrochemical potential-driven transporters
citrate succinate 2.A.47.3.2 2.Electrochemical potential-driven transporters
succinate 2.A.47.3.3 2.Electrochemical potential-driven transporters
citrate 2.A.47.3.4 2.Electrochemical potential-driven transporters
alanine 2.A.50.2.1 2.Electrochemical potential-driven transporters
potassium 2.A.72.1.2 2.Electrochemical potential-driven transporters
potassium 2.A.72.1.3 2.Electrochemical potential-driven transporters
RIBOSE 2.A.7.5.2 2.Electrochemical potential-driven transporters
iron 3.A.1.10.2 3.Primary active transporters
iron 3.A.1.10.2 3.Primary active transporters
iron 3.A.1.10.3 3.Primary active transporters
iron 3.A.1.10.3 3.Primary active transporters
iron 3.A.1.10.4 3.Primary active transporters
iron 3.A.1.10.4 3.Primary active transporters
iron 3.A.1.10.6 3.Primary active transporters
iron 3.A.1.10.6 3.Primary active transporters
arabinose D-glucosamine fructose galactose glucose maltose mannose sucrose trehalose xylose 3.A.1.1.1 3.Primary active transporters
arabinose D-glucosamine fructose galactose glucose maltose mannose sucrose trehalose xylose 3.A.1.1.1 3.Primary active transporters
arabinose D-glucosamine fructose galactose glucose maltose mannose sucrose trehalose xylose 3.A.1.1.1 3.Primary active transporters
arabinose D-glucosamine fructose galactose glucose maltose mannose sucrose trehalose xylose 3.A.1.1.1 3.Primary active transporters
arabinose D-glucosamine fructose galactose glucose maltose mannose sucrose trehalose xylose 3.A.1.1.1 3.Primary active transporters
arabinose D-glucosamine fructose galactose glucose maltose mannose sucrose trehalose xylose 3.A.1.1.1 3.Primary active transporters
arabinose D-glucosamine fructose galactose glucose maltose mannose sucrose trehalose xylose 3.A.1.1.1 3.Primary active transporters
arabinose D-glucosamine fructose galactose glucose maltose mannose sucrose trehalose xylose 3.A.1.1.1 3.Primary active transporters
arabinose D-glucosamine fructose galactose glucose maltose mannose sucrose trehalose xylose 3.A.1.1.1 3.Primary active transporters
putrescine spermidine 3.A.1.11.1 3.Primary active transporters
putrescine spermidine 3.A.1.11.1 3.Primary active transporters
putrescine Spermidine 3.A.1.11.10 3.Primary active transporters
putrescine Spermidine 3.A.1.11.10 3.Primary active transporters
putrescine 3.A.1.11.2 3.Primary active transporters
galactose glucose mannose 3.A.1.1.13 3.Primary active transporters
galactose glucose mannose 3.A.1.1.13 3.Primary active transporters
galactose glucose mannose 3.A.1.1.13 3.Primary active transporters
arabinose fructose xylose 3.A.1.1.14 3.Primary active transporters
arabinose fructose xylose 3.A.1.1.14 3.Primary active transporters
arabinose fructose xylose 3.A.1.1.14 3.Primary active transporters
trehalose 3.A.1.1.15 3.Primary active transporters
Maltodextrin 3.A.1.1.16 3.Primary active transporters
gamma-aminobutyric acid 3.A.1.11.6 3.Primary active transporters
maltose sucrose trehalose 3.A.1.1.17 3.Primary active transporters
maltose sucrose trehalose 3.A.1.1.17 3.Primary active transporters
maltose sucrose trehalose 3.A.1.1.17 3.Primary active transporters
putrescine spermidine 3.A.1.11.7 3.Primary active transporters
putrescine spermidine 3.A.1.11.7 3.Primary active transporters
spermidine 3.A.1.11.8 3.Primary active transporters
putrescine spermidine 3.A.1.11.9 3.Primary active transporters
putrescine spermidine 3.A.1.11.9 3.Primary active transporters
L-cysteine 3.A.1.122.1 3.Primary active transporters
glucose mannose 3.A.1.1.24 3.Primary active transporters
glucose mannose 3.A.1.1.24 3.Primary active transporters
maltose sucrose trehalose 3.A.1.1.25 3.Primary active transporters
maltose sucrose trehalose 3.A.1.1.25 3.Primary active transporters
maltose sucrose trehalose 3.A.1.1.25 3.Primary active transporters
maltose maltotetraose trehalose 3.A.1.1.27 3.Primary active transporters
maltose maltotetraose trehalose 3.A.1.1.27 3.Primary active transporters
maltose maltotetraose trehalose 3.A.1.1.27 3.Primary active transporters
raffinose stachyose 3.A.1.1.28 3.Primary active transporters
raffinose stachyose 3.A.1.1.28 3.Primary active transporters
betaine glycine proline 3.A.1.12.8 3.Primary active transporters
betaine glycine proline 3.A.1.12.8 3.Primary active transporters
betaine glycine proline 3.A.1.12.8 3.Primary active transporters
D-glucosamine glucose glycerol inositol phosphate trehalose 3.A.1.1.3 3.Primary active transporters
D-glucosamine glucose glycerol inositol phosphate trehalose 3.A.1.1.3 3.Primary active transporters
D-glucosamine glucose glycerol inositol phosphate trehalose 3.A.1.1.3 3.Primary active transporters
D-glucosamine glucose glycerol inositol phosphate trehalose 3.A.1.1.3 3.Primary active transporters
glucose 3.A.1.1.30 3.Primary active transporters
glycerol 3.A.1.1.32 3.Primary active transporters
chloride 3.A.1.135.7 3.Primary active transporters
inositol phosphate 3.A.1.1.38 3.Primary active transporters
iron 3.A.1.139.2 3.Primary active transporters
iron 3.A.1.139.2 3.Primary active transporters
D-mannitol fucose lactose maltodextrin maltose melibiose trehalose 3.A.1.1.4 3.Primary active transporters
D-mannitol fucose lactose maltodextrin maltose melibiose trehalose 3.A.1.1.4 3.Primary active transporters
D-mannitol fucose lactose maltodextrin maltose melibiose trehalose 3.A.1.1.4 3.Primary active transporters
D-mannitol fucose lactose maltodextrin maltose melibiose trehalose 3.A.1.1.4 3.Primary active transporters
D-mannitol fucose lactose maltodextrin maltose melibiose trehalose 3.A.1.1.4 3.Primary active transporters
D-mannitol fucose lactose maltodextrin maltose melibiose trehalose 3.A.1.1.4 3.Primary active transporters
maltose 3.A.1.1.45 3.Primary active transporters
D-mannitol 3.A.1.1.49 3.Primary active transporters
choline fructose glucose maltoheptaose maltose maltotetraose melibiose raffinose stachyose sucrose trehalose xylose 3.A.1.1.5 3.Primary active transporters
choline fructose glucose maltoheptaose maltose maltotetraose melibiose raffinose stachyose sucrose trehalose xylose 3.A.1.1.5 3.Primary active transporters
choline fructose glucose maltoheptaose maltose maltotetraose melibiose raffinose stachyose sucrose trehalose xylose 3.A.1.1.5 3.Primary active transporters
choline fructose glucose maltoheptaose maltose maltotetraose melibiose raffinose stachyose sucrose trehalose xylose 3.A.1.1.5 3.Primary active transporters
choline fructose glucose maltoheptaose maltose maltotetraose melibiose raffinose stachyose sucrose trehalose xylose 3.A.1.1.5 3.Primary active transporters
choline fructose glucose maltoheptaose maltose maltotetraose melibiose raffinose stachyose sucrose trehalose xylose 3.A.1.1.5 3.Primary active transporters
choline fructose glucose maltoheptaose maltose maltotetraose melibiose raffinose stachyose sucrose trehalose xylose 3.A.1.1.5 3.Primary active transporters
choline fructose glucose maltoheptaose maltose maltotetraose melibiose raffinose stachyose sucrose trehalose xylose 3.A.1.1.5 3.Primary active transporters
choline fructose glucose maltoheptaose maltose maltotetraose melibiose raffinose stachyose sucrose trehalose xylose 3.A.1.1.5 3.Primary active transporters
choline fructose glucose maltoheptaose maltose maltotetraose melibiose raffinose stachyose sucrose trehalose xylose 3.A.1.1.5 3.Primary active transporters
choline fructose glucose maltoheptaose maltose maltotetraose melibiose raffinose stachyose sucrose trehalose xylose 3.A.1.1.5 3.Primary active transporters
fructose glucose maltose sucrose 3.A.1.1.52 3.Primary active transporters
fructose glucose maltose sucrose 3.A.1.1.52 3.Primary active transporters
fructose glucose maltose sucrose 3.A.1.1.52 3.Primary active transporters
melibiose raffinose stachyose 3.A.1.1.53 3.Primary active transporters
melibiose raffinose stachyose 3.A.1.1.53 3.Primary active transporters
melibiose raffinose stachyose 3.A.1.1.53 3.Primary active transporters
L-arabinose maltose Trehalose 3.A.1.1.54 3.Primary active transporters
L-arabinose maltose Trehalose 3.A.1.1.54 3.Primary active transporters
L-arabinose maltose Trehalose 3.A.1.1.54 3.Primary active transporters
xylose 3.A.1.1.56 3.Primary active transporters
maltose sucrose trehalose 3.A.1.1.8 3.Primary active transporters
maltose sucrose trehalose 3.A.1.1.8 3.Primary active transporters
maltose sucrose trehalose 3.A.1.1.8 3.Primary active transporters
cobalt 3.A.1.18.2 3.Primary active transporters
cobalt 3.A.1.18.3 3.Primary active transporters
maltodextrin maltose Maltose Sulfate Trehalose 3.A.1.19.6 3.Primary active transporters
maltodextrin maltose Maltose Sulfate Trehalose 3.A.1.19.6 3.Primary active transporters
maltodextrin maltose Maltose Sulfate Trehalose 3.A.1.19.6 3.Primary active transporters
maltodextrin maltose Maltose Sulfate Trehalose 3.A.1.19.6 3.Primary active transporters
maltodextrin maltose Maltose Sulfate Trehalose 3.A.1.19.6 3.Primary active transporters
iron 3.A.1.20.1 3.Primary active transporters
iron 3.A.1.20.1 3.Primary active transporters
phosphate 3.A.1.20.2 3.Primary active transporters
iron 3.A.1.20.3 3.Primary active transporters
iron 3.A.1.20.3 3.Primary active transporters
glycerol 3.A.1.20.4 3.Primary active transporters
adenosine arabinose deoxyguanosine guanosine inosine xanthosine xylitol xylose 3.A.1.2.1 3.Primary active transporters
adenosine arabinose deoxyguanosine guanosine inosine xanthosine xylitol xylose 3.A.1.2.1 3.Primary active transporters
adenosine arabinose deoxyguanosine guanosine inosine xanthosine xylitol xylose 3.A.1.2.1 3.Primary active transporters
adenosine arabinose deoxyguanosine guanosine inosine xanthosine xylitol xylose 3.A.1.2.1 3.Primary active transporters
iron 3.A.1.210.1 3.Primary active transporters
iron 3.A.1.210.1 3.Primary active transporters
Heme 3.A.1.210.15 3.Primary active transporters
iron 3.A.1.210.8 3.Primary active transporters
iron 3.A.1.210.8 3.Primary active transporters
cobalt nickel 3.A.1.210.9 3.Primary active transporters
cobalt nickel 3.A.1.210.9 3.Primary active transporters
arabinose 3.A.1.2.14 3.Primary active transporters
arabinose 3.A.1.2.14 3.Primary active transporters
xylitol 3.A.1.2.15 3.Primary active transporters
xylose 3.A.1.2.18 3.Primary active transporters
Ribose 3.A.1.2.19 3.Primary active transporters
arabinose D-fructose glucose inositol riboflavin ribose xylose 3.A.1.2.2 3.Primary active transporters
arabinose D-fructose glucose inositol riboflavin ribose xylose 3.A.1.2.2 3.Primary active transporters
arabinose D-fructose glucose inositol riboflavin ribose xylose 3.A.1.2.2 3.Primary active transporters
arabinose D-fructose glucose inositol riboflavin ribose xylose 3.A.1.2.2 3.Primary active transporters
arabinose D-fructose glucose inositol riboflavin ribose xylose 3.A.1.2.2 3.Primary active transporters
glucose xylose 3.A.1.2.20 3.Primary active transporters
glucose xylose 3.A.1.2.20 3.Primary active transporters
D-fructose ribose xylose 3.A.1.2.23 3.Primary active transporters
D-fructose ribose xylose 3.A.1.2.23 3.Primary active transporters
xylose 3.A.1.2.26 3.Primary active transporters
arabinose galactose glucose xylose 3.A.1.2.3 3.Primary active transporters
arabinose galactose glucose xylose 3.A.1.2.3 3.Primary active transporters
arabinose galactose glucose xylose 3.A.1.2.3 3.Primary active transporters
arabinose galactose glucose xylose 3.A.1.2.3 3.Primary active transporters
arabinose galactose glucose xylose 3.A.1.2.3 3.Primary active transporters
Ribose 3.A.1.2.30 3.Primary active transporters
arabinose 3.A.1.2.32 3.Primary active transporters
arabinose 3.A.1.2.32 3.Primary active transporters
xylose 3.A.1.2.33 3.Primary active transporters
xylose 3.A.1.2.4 3.Primary active transporters
methionine 3.A.1.24.1 3.Primary active transporters
L-methionine methionine 3.A.1.24.2 3.Primary active transporters
L-methionine methionine 3.A.1.24.2 3.Primary active transporters
methionine 3.A.1.24.3 3.Primary active transporters
L-histidine 3.A.1.24.5 3.Primary active transporters
arabinose fucose galactose glucose xylose 3.A.1.2.5 3.Primary active transporters
arabinose fucose galactose glucose xylose 3.A.1.2.5 3.Primary active transporters
arabinose fucose galactose glucose xylose 3.A.1.2.5 3.Primary active transporters
arabinose fucose galactose glucose xylose 3.A.1.2.5 3.Primary active transporters
arabinose fucose galactose glucose xylose 3.A.1.2.5 3.Primary active transporters
biotin 3.A.1.25.4 3.Primary active transporters
Cobalt Folate 3.A.1.26.10 3.Primary active transporters
Cobalt Folate 3.A.1.26.10 3.Primary active transporters
thiamine 3.A.1.26.5 3.Primary active transporters
Cobalt 3.A.1.26.7 3.Primary active transporters
folate 3.A.1.28.2 3.Primary active transporters
thiamine 3.A.1.30.1 3.Primary active transporters
thiamine 3.A.1.30.2 3.Primary active transporters
arginine asparagine aspartate glutamate glutamine histidine lysine ornithine 3.A.1.3.1 3.Primary active transporters
arginine asparagine aspartate glutamate glutamine histidine lysine ornithine 3.A.1.3.1 3.Primary active transporters
arginine asparagine aspartate glutamate glutamine histidine lysine ornithine 3.A.1.3.1 3.Primary active transporters
arginine asparagine aspartate glutamate glutamine histidine lysine ornithine 3.A.1.3.1 3.Primary active transporters
arginine asparagine aspartate glutamate glutamine histidine lysine ornithine 3.A.1.3.1 3.Primary active transporters
arginine asparagine aspartate glutamate glutamine histidine lysine ornithine 3.A.1.3.1 3.Primary active transporters
arginine asparagine aspartate glutamate glutamine histidine lysine ornithine 3.A.1.3.1 3.Primary active transporters
arginine asparagine aspartate glutamate glutamine histidine lysine ornithine 3.A.1.3.1 3.Primary active transporters
arginine ornithine 3.A.1.3.11 3.Primary active transporters
arginine ornithine 3.A.1.3.11 3.Primary active transporters
arginine glutamine histidine lysine 3.A.1.3.12 3.Primary active transporters
arginine glutamine histidine lysine 3.A.1.3.12 3.Primary active transporters
arginine glutamine histidine lysine 3.A.1.3.12 3.Primary active transporters
arginine glutamine histidine lysine 3.A.1.3.12 3.Primary active transporters
cysteine Cysteine glutamine 3.A.1.3.13 3.Primary active transporters
cysteine Cysteine glutamine 3.A.1.3.13 3.Primary active transporters
cysteine Cysteine glutamine 3.A.1.3.13 3.Primary active transporters
arginine 3.A.1.3.15 3.Primary active transporters
aspartate glutamate 3.A.1.3.16 3.Primary active transporters
aspartate glutamate 3.A.1.3.16 3.Primary active transporters
arginine histidine lysine 3.A.1.3.17 3.Primary active transporters
arginine histidine lysine 3.A.1.3.17 3.Primary active transporters
arginine histidine lysine 3.A.1.3.17 3.Primary active transporters
asparagine aspartate glutamate glutamine 3.A.1.3.19 3.Primary active transporters
asparagine aspartate glutamate glutamine 3.A.1.3.19 3.Primary active transporters
asparagine aspartate glutamate glutamine 3.A.1.3.19 3.Primary active transporters
asparagine aspartate glutamate glutamine 3.A.1.3.19 3.Primary active transporters
alanine arginine asparagine glutamate glutamine histidine L-glutamic acid L-proline L-threonine lysine serine tyrosine valine 3.A.1.3.2 3.Primary active transporters
alanine arginine asparagine glutamate glutamine histidine L-glutamic acid L-proline L-threonine lysine serine tyrosine valine 3.A.1.3.2 3.Primary active transporters
alanine arginine asparagine glutamate glutamine histidine L-glutamic acid L-proline L-threonine lysine serine tyrosine valine 3.A.1.3.2 3.Primary active transporters
alanine arginine asparagine glutamate glutamine histidine L-glutamic acid L-proline L-threonine lysine serine tyrosine valine 3.A.1.3.2 3.Primary active transporters
alanine arginine asparagine glutamate glutamine histidine L-glutamic acid L-proline L-threonine lysine serine tyrosine valine 3.A.1.3.2 3.Primary active transporters
alanine arginine asparagine glutamate glutamine histidine L-glutamic acid L-proline L-threonine lysine serine tyrosine valine 3.A.1.3.2 3.Primary active transporters
alanine arginine asparagine glutamate glutamine histidine L-glutamic acid L-proline L-threonine lysine serine tyrosine valine 3.A.1.3.2 3.Primary active transporters
alanine arginine asparagine glutamate glutamine histidine L-glutamic acid L-proline L-threonine lysine serine tyrosine valine 3.A.1.3.2 3.Primary active transporters
alanine arginine asparagine glutamate glutamine histidine L-glutamic acid L-proline L-threonine lysine serine tyrosine valine 3.A.1.3.2 3.Primary active transporters
alanine arginine asparagine glutamate glutamine histidine L-glutamic acid L-proline L-threonine lysine serine tyrosine valine 3.A.1.3.2 3.Primary active transporters
alanine arginine asparagine glutamate glutamine histidine L-glutamic acid L-proline L-threonine lysine serine tyrosine valine 3.A.1.3.2 3.Primary active transporters
alanine arginine asparagine glutamate glutamine histidine L-glutamic acid L-proline L-threonine lysine serine tyrosine valine 3.A.1.3.2 3.Primary active transporters
alanine arginine asparagine glutamate glutamine histidine L-glutamic acid L-proline L-threonine lysine serine tyrosine valine 3.A.1.3.2 3.Primary active transporters
lysine 3.A.1.3.20 3.Primary active transporters
L-proline 3.A.1.3.21 3.Primary active transporters
glutamine L-glutamic acid 3.A.1.3.22 3.Primary active transporters
glutamine L-glutamic acid 3.A.1.3.22 3.Primary active transporters
alanine arginine histidine lysine valine 3.A.1.3.23 3.Primary active transporters
alanine arginine histidine lysine valine 3.A.1.3.23 3.Primary active transporters
alanine arginine histidine lysine valine 3.A.1.3.23 3.Primary active transporters
alanine arginine histidine lysine valine 3.A.1.3.23 3.Primary active transporters
alanine arginine histidine lysine valine 3.A.1.3.23 3.Primary active transporters
asparagine glutamate glutamine 3.A.1.3.25 3.Primary active transporters
asparagine glutamate glutamine 3.A.1.3.25 3.Primary active transporters
asparagine glutamate glutamine 3.A.1.3.25 3.Primary active transporters
asparagine glutamine histidine L-threonine serine tyrosine 3.A.1.3.26 3.Primary active transporters
asparagine glutamine histidine L-threonine serine tyrosine 3.A.1.3.26 3.Primary active transporters
asparagine glutamine histidine L-threonine serine tyrosine 3.A.1.3.26 3.Primary active transporters
asparagine glutamine histidine L-threonine serine tyrosine 3.A.1.3.26 3.Primary active transporters
asparagine glutamine histidine L-threonine serine tyrosine 3.A.1.3.26 3.Primary active transporters
asparagine glutamine histidine L-threonine serine tyrosine 3.A.1.3.26 3.Primary active transporters
arginine histidine lysine 3.A.1.3.29 3.Primary active transporters
arginine histidine lysine 3.A.1.3.29 3.Primary active transporters
arginine histidine lysine 3.A.1.3.29 3.Primary active transporters
arginine 3.A.1.3.3 3.Primary active transporters
Glutamine 3.A.1.3.30 3.Primary active transporters
glutamate 3.A.1.3.4 3.Primary active transporters
tryptophan 3.A.1.34.1 3.Primary active transporters
asparagine aspartate glutamate glutamine 3.A.1.3.7 3.Primary active transporters
asparagine aspartate glutamate glutamine 3.A.1.3.7 3.Primary active transporters
asparagine aspartate glutamate glutamine 3.A.1.3.7 3.Primary active transporters
asparagine aspartate glutamate glutamine 3.A.1.3.7 3.Primary active transporters
glutamate 3.A.1.3.9 3.Primary active transporters
mannose 3.A.1.5.15 3.Primary active transporters
L-alanine nickel 3.A.1.5.3 3.Primary active transporters
L-alanine nickel 3.A.1.5.3 3.Primary active transporters
L-alanine 3.A.1.5.38 3.Primary active transporters
sodium sulfate thiosulfate 3.A.1.6.1 3.Primary active transporters
sodium sulfate thiosulfate 3.A.1.6.1 3.Primary active transporters
sodium sulfate thiosulfate 3.A.1.6.1 3.Primary active transporters
sulfate 3.A.1.6.3 3.Primary active transporters
molybdate 3.A.1.6.5 3.Primary active transporters
phosphate 3.A.1.7.1 3.Primary active transporters
phosphate 3.A.1.7.2 3.Primary active transporters
phosphate 3.A.1.7.3 3.Primary active transporters
phosphate 3.A.1.7.4 3.Primary active transporters
phosphate 3.A.1.7.5 3.Primary active transporters
sodium 3.A.2.1.12 3.Primary active transporters
sodium 3.A.2.1.2 3.Primary active transporters
sodium 3.A.2.1.5 3.Primary active transporters
sodium 3.A.2.1.6 3.Primary active transporters
sodium 3.A.2.1.9 3.Primary active transporters
phosphate 3.A.23.6.1 3.Primary active transporters
zinc 3.A.29.1.4 3.Primary active transporters
zinc 3.A.29.1.5 3.Primary active transporters
potassium sodium 3.A.3.1.1 3.Primary active transporters
potassium sodium 3.A.3.1.1 3.Primary active transporters
potassium sodium 3.A.3.1.10 3.Primary active transporters
potassium sodium 3.A.3.1.10 3.Primary active transporters
potassium sodium 3.A.3.1.11 3.Primary active transporters
potassium sodium 3.A.3.1.11 3.Primary active transporters
potassium sodium 3.A.3.1.12 3.Primary active transporters
potassium sodium 3.A.3.1.12 3.Primary active transporters
potassium sodium 3.A.3.1.13 3.Primary active transporters
potassium sodium 3.A.3.1.13 3.Primary active transporters
potassium sodium 3.A.3.1.15 3.Primary active transporters
potassium sodium 3.A.3.1.15 3.Primary active transporters
potassium 3.A.3.1.2 3.Primary active transporters
potassium 3.A.3.1.4 3.Primary active transporters
potassium sodium 3.A.3.1.5 3.Primary active transporters
potassium sodium 3.A.3.1.5 3.Primary active transporters
potassium sodium 3.A.3.1.6 3.Primary active transporters
potassium sodium 3.A.3.1.6 3.Primary active transporters
potassium 3.A.3.1.7 3.Primary active transporters
potassium sodium 3.A.3.1.8 3.Primary active transporters
potassium sodium 3.A.3.1.8 3.Primary active transporters
sodium 3.A.3.1.9 3.Primary active transporters
calcium 3.A.3.2.10 3.Primary active transporters
calcium 3.A.3.2.11 3.Primary active transporters
calcium 3.A.3.2.12 3.Primary active transporters
calcium manganese 3.A.3.2.13 3.Primary active transporters
calcium manganese 3.A.3.2.13 3.Primary active transporters
calcium 3.A.3.2.14 3.Primary active transporters
calcium manganese 3.A.3.2.16 3.Primary active transporters
calcium manganese 3.A.3.2.16 3.Primary active transporters
calcium 3.A.3.2.17 3.Primary active transporters
calcium manganese 3.A.3.2.19 3.Primary active transporters
calcium manganese 3.A.3.2.19 3.Primary active transporters
calcium 3.A.3.2.20 3.Primary active transporters
calcium 3.A.3.2.21 3.Primary active transporters
calcium 3.A.3.2.22 3.Primary active transporters
calcium 3.A.3.2.23 3.Primary active transporters
calcium 3.A.3.2.24 3.Primary active transporters
calcium manganese 3.A.3.2.26 3.Primary active transporters
calcium manganese 3.A.3.2.26 3.Primary active transporters
calcium manganese 3.A.3.2.28 3.Primary active transporters
calcium manganese 3.A.3.2.28 3.Primary active transporters
calcium 3.A.3.2.29 3.Primary active transporters
cadmium calcium manganese 3.A.3.2.3 3.Primary active transporters
cadmium calcium manganese 3.A.3.2.3 3.Primary active transporters
cadmium calcium manganese 3.A.3.2.3 3.Primary active transporters
calcium 3.A.3.2.30 3.Primary active transporters
calcium 3.A.3.2.32 3.Primary active transporters
calcium 3.A.3.2.34 3.Primary active transporters
calcium 3.A.3.2.36 3.Primary active transporters
calcium 3.A.3.2.37 3.Primary active transporters
calcium 3.A.3.2.39 3.Primary active transporters
calcium magnesium potassium sodium 3.A.3.2.4 3.Primary active transporters
calcium magnesium potassium sodium 3.A.3.2.4 3.Primary active transporters
calcium magnesium potassium sodium 3.A.3.2.4 3.Primary active transporters
calcium magnesium potassium sodium 3.A.3.2.4 3.Primary active transporters
sodium 3.A.3.2.41 3.Primary active transporters
calcium 3.A.3.2.42 3.Primary active transporters
magnesium potassium 3.A.3.2.43 3.Primary active transporters
magnesium potassium 3.A.3.2.43 3.Primary active transporters
calcium 3.A.3.2.46 3.Primary active transporters
calcium 3.A.3.2.48 3.Primary active transporters
calcium manganese 3.A.3.2.5 3.Primary active transporters
calcium manganese 3.A.3.2.5 3.Primary active transporters
Cadmium 3.A.3.25.3 3.Primary active transporters
iron 3.A.3.25.4 3.Primary active transporters
iron 3.A.3.25.4 3.Primary active transporters
calcium manganese 3.A.3.2.6 3.Primary active transporters
calcium manganese 3.A.3.2.6 3.Primary active transporters
calcium 3.A.3.2.7 3.Primary active transporters
copper 3.A.3.27.4 3.Primary active transporters
copper 3.A.3.27.5 3.Primary active transporters
calcium manganese 3.A.3.2.9 3.Primary active transporters
calcium manganese 3.A.3.2.9 3.Primary active transporters
magnesium potassium 3.A.3.3.2 3.Primary active transporters
magnesium potassium 3.A.3.3.2 3.Primary active transporters
cadmium 3.A.3.32.4 3.Primary active transporters
cadmium manganese 3.A.3.3.3 3.Primary active transporters
cadmium manganese 3.A.3.3.3 3.Primary active transporters
magnesium nickel 3.A.3.4.1 3.Primary active transporters
magnesium nickel 3.A.3.4.1 3.Primary active transporters
magnesium 3.A.3.4.2 3.Primary active transporters
magnesium 3.A.3.4.5 3.Primary active transporters
cadmium copper iron lead 3.A.3.5.1 3.Primary active transporters
cadmium copper iron lead 3.A.3.5.1 3.Primary active transporters
cadmium copper iron lead 3.A.3.5.1 3.Primary active transporters
cadmium copper iron lead 3.A.3.5.1 3.Primary active transporters
cadmium copper iron lead 3.A.3.5.1 3.Primary active transporters
copper 3.A.3.5.10 3.Primary active transporters
copper 3.A.3.5.13 3.Primary active transporters
copper 3.A.3.5.15 3.Primary active transporters
copper 3.A.3.5.16 3.Primary active transporters
copper 3.A.3.5.18 3.Primary active transporters
copper iron lead 3.A.3.5.19 3.Primary active transporters
copper iron lead 3.A.3.5.19 3.Primary active transporters
copper iron lead 3.A.3.5.19 3.Primary active transporters
copper iron lead 3.A.3.5.19 3.Primary active transporters
copper 3.A.3.5.2 3.Primary active transporters
copper 3.A.3.5.21 3.Primary active transporters
copper 3.A.3.5.22 3.Primary active transporters
copper 3.A.3.5.23 3.Primary active transporters
copper 3.A.3.5.24 3.Primary active transporters
copper 3.A.3.5.25 3.Primary active transporters
copper 3.A.3.5.26 3.Primary active transporters
copper 3.A.3.5.27 3.Primary active transporters
copper 3.A.3.5.29 3.Primary active transporters
copper 3.A.3.5.30 3.Primary active transporters
copper 3.A.3.5.31 3.Primary active transporters
copper 3.A.3.5.33 3.Primary active transporters
copper 3.A.3.5.34 3.Primary active transporters
copper 3.A.3.5.38 3.Primary active transporters
cadmium copper zinc 3.A.3.5.39 3.Primary active transporters
cadmium copper zinc 3.A.3.5.39 3.Primary active transporters
cadmium copper zinc 3.A.3.5.39 3.Primary active transporters
copper 3.A.3.5.40 3.Primary active transporters
copper 3.A.3.5.41 3.Primary active transporters
copper 3.A.3.5.5 3.Primary active transporters
copper 3.A.3.5.7 3.Primary active transporters
cadmium calcium cobalt copper lead mercury nickel zinc 3.A.3.6.1 3.Primary active transporters
cadmium calcium cobalt copper lead mercury nickel zinc 3.A.3.6.1 3.Primary active transporters
cadmium calcium cobalt copper lead mercury nickel zinc 3.A.3.6.1 3.Primary active transporters
cadmium calcium cobalt copper lead mercury nickel zinc 3.A.3.6.1 3.Primary active transporters
cadmium calcium cobalt copper lead mercury nickel zinc 3.A.3.6.1 3.Primary active transporters
cadmium calcium cobalt copper lead mercury nickel zinc 3.A.3.6.1 3.Primary active transporters
cadmium calcium cobalt copper lead mercury nickel zinc 3.A.3.6.1 3.Primary active transporters
cadmium calcium cobalt copper lead mercury nickel zinc 3.A.3.6.1 3.Primary active transporters
zinc 3.A.3.6.11 3.Primary active transporters
cadmium cobalt lead mercury nickel zinc 3.A.3.6.12 3.Primary active transporters
cadmium cobalt lead mercury nickel zinc 3.A.3.6.12 3.Primary active transporters
cadmium cobalt lead mercury nickel zinc 3.A.3.6.12 3.Primary active transporters
cadmium cobalt lead mercury nickel zinc 3.A.3.6.12 3.Primary active transporters
cadmium cobalt lead mercury nickel zinc 3.A.3.6.12 3.Primary active transporters
cadmium cobalt lead mercury nickel zinc 3.A.3.6.12 3.Primary active transporters
copper zinc 3.A.3.6.15 3.Primary active transporters
copper zinc 3.A.3.6.15 3.Primary active transporters
Cadmium 3.A.3.6.16 3.Primary active transporters
cadmium cobalt copper lead mercury nickel zinc 3.A.3.6.2 3.Primary active transporters
cadmium cobalt copper lead mercury nickel zinc 3.A.3.6.2 3.Primary active transporters
cadmium cobalt copper lead mercury nickel zinc 3.A.3.6.2 3.Primary active transporters
cadmium cobalt copper lead mercury nickel zinc 3.A.3.6.2 3.Primary active transporters
cadmium cobalt copper lead mercury nickel zinc 3.A.3.6.2 3.Primary active transporters
cadmium cobalt copper lead mercury nickel zinc 3.A.3.6.2 3.Primary active transporters
cadmium cobalt copper lead mercury nickel zinc 3.A.3.6.2 3.Primary active transporters
cobalt 3.A.3.6.21 3.Primary active transporters
cobalt 3.A.3.6.22 3.Primary active transporters
cadmium cobalt zinc 3.A.3.6.25 3.Primary active transporters
cadmium cobalt zinc 3.A.3.6.25 3.Primary active transporters
cadmium cobalt zinc 3.A.3.6.25 3.Primary active transporters
cadmium cobalt zinc 3.A.3.6.27 3.Primary active transporters
cadmium cobalt zinc 3.A.3.6.27 3.Primary active transporters
cadmium cobalt zinc 3.A.3.6.27 3.Primary active transporters
cadmium cobalt zinc 3.A.3.6.3 3.Primary active transporters
cadmium cobalt zinc 3.A.3.6.3 3.Primary active transporters
cadmium cobalt zinc 3.A.3.6.3 3.Primary active transporters
cadmium copper zinc 3.A.3.6.5 3.Primary active transporters
cadmium copper zinc 3.A.3.6.5 3.Primary active transporters
cadmium copper zinc 3.A.3.6.5 3.Primary active transporters
cadmium 3.A.3.6.8 3.Primary active transporters
zinc 3.A.3.6.9 3.Primary active transporters
sodium 3.A.3.9.1 3.Primary active transporters
potassium 3.A.3.9.2 3.Primary active transporters
potassium sodium 3.A.3.9.3 3.Primary active transporters
potassium sodium 3.A.3.9.3 3.Primary active transporters
sodium 3.A.3.9.4 3.Primary active transporters
potassium sodium 3.A.3.9.5 3.Primary active transporters
potassium sodium 3.A.3.9.5 3.Primary active transporters
potassium sodium 3.A.3.9.6 3.Primary active transporters
potassium sodium 3.A.3.9.6 3.Primary active transporters
calcium 3.A.3.9.7 3.Primary active transporters
D-mannitol fructose 4.A.2.1.1 4.Group translocators
D-mannitol fructose 4.A.2.1.1 4.Group translocators
fructose 4.A.2.1.13 4.Group translocators
fructose 4.A.2.1.14 4.Group translocators
fructose 4.A.2.1.16 4.Group translocators
fructose 4.A.2.1.17 4.Group translocators
fructose 4.A.2.1.18 4.Group translocators
fructose 4.A.2.1.19 4.Group translocators
fructose 4.A.2.1.20 4.Group translocators
fructose 4.A.2.1.21 4.Group translocators
fructose 4.A.2.1.23 4.Group translocators
fructose 4.A.2.1.25 4.Group translocators
fructose 4.A.2.1.26 4.Group translocators
fructose 4.A.2.1.4 4.Group translocators
fructose xylitol 4.A.2.1.7 4.Group translocators
fructose 4.A.2.1.8 4.Group translocators
cellobiose D-glucosamine glucomannan 4.A.3.2.1 4.Group translocators
cellobiose D-glucosamine glucomannan 4.A.3.2.1 4.Group translocators
cellobiose 4.A.3.2.11 4.Group translocators
cellobiose 4.A.3.2.4 4.Group translocators
D-fructose D-gluconic acid D-glucosamine fructose glucose mannose N-acetylgalactosamine 4.A.6.1.1 4.Group translocators
D-fructose D-gluconic acid D-glucosamine fructose glucose mannose N-acetylgalactosamine 4.A.6.1.1 4.Group translocators
D-fructose D-gluconic acid D-glucosamine fructose glucose mannose N-acetylgalactosamine 4.A.6.1.1 4.Group translocators
D-fructose D-gluconic acid D-glucosamine fructose glucose mannose N-acetylgalactosamine 4.A.6.1.1 4.Group translocators
D-fructose D-gluconic acid D-glucosamine fructose glucose mannose N-acetylgalactosamine 4.A.6.1.1 4.Group translocators
D-fructose D-gluconic acid D-glucosamine fructose glucose mannose N-acetylgalactosamine 4.A.6.1.1 4.Group translocators
fructose glucose 4.A.6.1.10 4.Group translocators
fructose glucose 4.A.6.1.10 4.Group translocators
mannose 4.A.6.1.11 4.Group translocators
glucose mannose 4.A.6.1.15 4.Group translocators
glucose mannose 4.A.6.1.15 4.Group translocators
mannose 4.A.6.1.16 4.Group translocators
D-fructose D-glucosamine fructose glucosamine glucose mannose N-acetyl-D-glucosamine ribitol 4.A.6.1.2 4.Group translocators
D-fructose D-glucosamine fructose glucosamine glucose mannose N-acetyl-D-glucosamine ribitol 4.A.6.1.2 4.Group translocators
D-fructose D-glucosamine fructose glucosamine glucose mannose N-acetyl-D-glucosamine ribitol 4.A.6.1.2 4.Group translocators
D-fructose D-glucosamine fructose glucosamine glucose mannose N-acetyl-D-glucosamine ribitol 4.A.6.1.2 4.Group translocators
D-fructose D-glucosamine fructose glucosamine glucose mannose N-acetyl-D-glucosamine ribitol 4.A.6.1.2 4.Group translocators
D-fructose D-glucosamine fructose glucosamine glucose mannose N-acetyl-D-glucosamine ribitol 4.A.6.1.2 4.Group translocators
D-fructose D-glucosamine fructose glucosamine glucose mannose N-acetyl-D-glucosamine ribitol 4.A.6.1.2 4.Group translocators
D-glucosamine fructose glucosamine glucose 4.A.6.1.29 4.Group translocators
D-glucosamine fructose glucosamine glucose 4.A.6.1.29 4.Group translocators
D-glucosamine fructose glucosamine glucose 4.A.6.1.29 4.Group translocators
D-glucosamine fructose glucosamine glucose 4.A.6.1.29 4.Group translocators
glucose 4.A.6.1.6 4.Group translocators
fructose glucose mannose 4.A.6.1.7 4.Group translocators
fructose glucose mannose 4.A.6.1.7 4.Group translocators
fructose glucose mannose 4.A.6.1.7 4.Group translocators

Found transporter for substances:
2-oxoglutarate
alanine
arabinose
arginine
asparagine
aspartate
betaine
biotin
cadmium
calcium
cellobiose
chloride
choline
citrate
cobalt
copper
cysteine
D-alanine
deoxyuridine
D-fructose
D-galactose
D-glucosamine
D-mannitol
D-serine
folate
formate
fructose
galactose
gamma-aminobutyric acid
glucosamine
glucose
glutamate
glutamine
glycerol
glycine
guanosine
Heme
histidine
iron
lactate
lactose
L-alanine
L-arabinose
L-cysteine
lead
L-glutamic acid
L-histidine
L-isoleucine
L-methionine
L-proline
L-serine
L-threonine
lysine
magnesium
malate
maltodextrin
maltoheptaose
maltose
maltotetraose
manganese
mannose
melibiose
mercury
methionine
molybdate
N-acetyl-D-glucosamine
N-acetylgalactosamine
nickel
ornithine
OXALATE
phenylalanine
phosphate
potassium
proline
putrescine
raffinose
ribose
(R)-lactate
serine
(S)-lactate
sodium
spermidine
stachyose
succinate
sucrose
sulfate
thiamine
thiosulfate
trehalose
tryptophan
tyrosine
uracil
uridine
valine
xanthine
xylitol
xylose
zinc

Found transporter without reaction in DB:
acetate
adenosine
ammonia
coenzyme A
cytidine
deoxycholate
deoxyguanosine
D-gluconic acid
FAD
fucose
glucomannan
inosine
inositol
lactic acid
pantothenate
rhamnose
ribitol
riboflavin
xanthosine
xylan

Add alternative transport reactions:
adenosine
ammonia
arabitol
arsenite
CARNITINE
CoA
coenzyme A
CROTONOBETAINE
cyanate
cytidine
deoxyguanosine
D-gluconic acid
FAD
Formate
fucose
glucomannan
gluconate
inosine
lactic acid
NADP
rhamnose
ribitol
Serine
threonine
turanose
xanthosine
xylan
Total number of found substance transporter for ldel: 88
Running time: 93 s.
```

```
gapseq find-transport -b 200 $modelB.faa.gz
```
Running time: 98 s.

Hasta aqui todo bien
```
gapseq draft -r $modelA-all-Reactions.tbl -t $modelA-Transporter.tbl -p $modelA-all-Pathways.tbl -u 200 -l 100 -c $modelA.faa.gz

```
```

gapseq draft -r $modelA-all-Reactions.tbl -t $modelA-Transporte
Error in library(getopt) : there is no package called ‘getopt’
Execution halted
```


instalé desde R getopt

```
 gapseq draft -r $modelA-all-Reactions.tbl -t $modelA-Transporter.tbl -p $modelA-all-Pathways.tbl -u 200 -l 100 -c $modelA.faa.gz
Error in library(R.utils) : there is no package called ‘R.utils’
Calls: suppressMessages -> withCallingHandlers -> library
Execution halted
```

instalé desde r R.utils 
```
gapseq draft -r $modelA-all-Reactions.tbl -t $modelA-Transporter.tbl -p $modelA-all-Pathways.tbl -u 200 -l 100 -c $modelA.faa.gz
Error in library(IRanges) : there is no package called ‘IRanges’
Calls: suppressMessages -> withCallingHandlers -> library

```


```
R
 cran_pkgs <- c("data.table", "dplyr", "stringr", "readr", "optparse")
> install.packages(cran_pkgs)

```
## ejemplo
```
gapseq draft -r $modelA-all-Reactions.tbl -t $modelA-Transporter.tbl -p $modelA-all-Pathways.tbl -u 200 -l 100 -c $modelA.faa.gz
Protein fasta detected.
Predicted domain: Bacteria 
Predicted Gram-staining: pos 
Creating Gene-Reaction list... 523 unique genes
Constructing draft model: 
Error in getClass(Class, where = topenv(parent.frame())) : 
  “ModelOrg” is not a defined class
Calls: build_draft_model_from_blast_results -> new -> getClass
In addition: Warning message:
In library(package, lib.loc = lib.loc, character.only = TRUE, logical.return = TRUE,  :
  there is no package called ‘cobrar’
No traceback available 
```
# 160625

* Agregar gaoseq al path
* Correr gapseq con mis datos
1. Definir el nombre de mis modelos 

a) Descargar datos 

1. RC3LPC_1_NS_M1_01_25.faa
2. C2RQJT_1_rerun_NS_M2_01_25_2.faa

b) Renombrar datos
```
mv RC3LPC_1_NS_M1_01_25.faa bac1.faa
mv C2RQJT_1_rerun_NS_M2_01_25_2.faa bac2.faa
```
✅✅✅

```
RC3="bac1"
C2R="bac2"
```
✅✅✅

c) Construir modelo metabólico 
(1) Predicción de reacciones y vías 
```
gapseq find -p all -b 200 -m auto -t auto $RC3.faa
gapseq find -p all -b 200 -m auto -t auto $C2R.faa
```
duración: 3329 s
✅✅✅


(2) Predicción de transportadores

```
gapseq find-transport -b 200 $RC3.faa 
gapseq find-transport -b 200 $C2R.faa
```

(3) Reconstrucción del borrador del modelo 

```
gapseq draft -r $RC3-all-Reactions.tbl -t $RC3-Transporter.tbl -p $RC3-all-Pathways.tbl -u 200 -l 100 -c $RC3.faa
gapseq draft -r $C2R-all-Reactions.tbl -t $C2R-Transporter.tbl -p $C2R-all-Pathways.tbl -u 200 -l 100 -c $C2R.faa
```


(4) Relleno de huecos
NOTA: se ocupa el medio, algunos vienen en: gapseq/dat/media
```
gapseq fill -m $RC3-draft.RDS -n LBmed.csv -c $RC3-rxnWeights.RDS -g $RC3-rxnXgenes.RDS -b 100
```

```
LP solver: glpk 
Loading model files bac1-draft.RDS 
using media file LBmed.csv 


1. Initial gapfilling: Make model grow on given media using all reactions
Utilized candidate reactions:  50
Gapfill summary:
Added reactions:       34 
Added core reactions:  6 
Final growth rate:     1.034122 


2. Biomass gapfilling using core reactions only
Gapfill summary:
Filled components:     0 (  )
Added reactions:       0 
Final growth rate:     1.034122 


2b. Anaerobic biomass gapfilling using core reactions only
Gapfill summary:
Filled components:     0 (  )
Added reactions:       0 
Final growth rate:     1.034122 

3. Energy source gapfilling with core reactions only
Gapfill summary:
Filled components:     9 ( L-Lysine-e0,D-Mannitol-e0,D-Galacturonate-e0,D-Galactonate-e0,L-Idonate-e0,4-Hydroxybenzoate-e0,CELB-e0,Xylitol-e0,Formate-e0 )
Added reactions:       19 
Final growth rate:     1.066292 


4. Checking for potential metabolic products with core reactions only
Gapfill summary:
Filled components:     3 ( L-Inositol-e0,NAD-e0,Agmatine-e0 )
Added reactions:       3 
Final growth rate:     1.066292 

Uptake at limit:
L-Glutamate:1, L-Lysine:1, L-Aspartate:1, L-Arginine:1, L-Leucine:1, L-Histidine:1, L-Proline:1, L-Threonine:1, L-Isoleucine:1, H+:0.1, Uracil:0.1, Uridine:0.1, Guanosine:0.1, L-Alanine:1, L-Cysteine:1, L-Serine:1, O2:10, Adenosine:0.1, Inosine:0.1, Thiamine phosphate:0.1 

Top 10 produced metabolites [mmol / (gDW * hr)]:
CO2:8.681, NH3:8.337, H2O:5.162, Acetate:3.319, Formate:3.012, H2S:0.895, Oxalate:0.848, Urea:0.701, Propionate:0.617, Succinate:0.225 

```
```
gapseq fill -m $C2R-draft.RDS -n LBmed.csv -c $C2R-rxnWeights.RDS -g $C2R-rxnXgenes.RDS -b 100
```
```
rxnWeights.RDS -g $C2R-rxnXgenes.RDS -b 100
LP solver: glpk 
Loading model files bac2-draft.RDS 
using media file LBmed.csv 


1. Initial gapfilling: Make model grow on given media using all reactions
Utilized candidate reactions:  53
Gapfill summary:
Added reactions:       49 
Added core reactions:  6 
Final growth rate:     0.6453282 


2. Biomass gapfilling using core reactions only
Gapfill summary:
Filled components:     2 ( TPP-c0,CoA-c0 )
Added reactions:       2 
Final growth rate:     0.6453282 


2b. Anaerobic biomass gapfilling using core reactions only
Gapfill summary:
Filled components:     0 (  )
Added reactions:       2 
Final growth rate:     0.6453282 


3. Energy source gapfilling with core reactions only
Gapfill summary:
Filled components:     17 ( Cholate-e0,L-Lysine-e0,Guanosine-e0,Glycolate-e0,GABA-e0,D-Mannitol-e0,Ribitol-e0,L-Idonate-e0,Maltotetraose-e0,Maltoheptaose-e0,Stachyose-e0,N-Acetyl-D-chondrosamine-e0,Melibiose-e0,Formate-e0,Taurocholate-e0,Taurochenodeoxycholate-e0,Oxalate-e0 )
Added reactions:       48 
Final growth rate:     0.6843105 

4. Checking for potential metabolic products with core reactions only
Gapfill summary:
Filled components:     7 ( Galactose-e0,L-Inositol-e0,Neu5Ac-e0,NAD-e0,NADP-e0,GTP-e0,Agmatine-e0 )
Added reactions:       9 
Final growth rate:     0.6843105 

Uptake at limit:
Glycine:1, L-Glutamate:1, L-Lysine:1, L-Aspartate:1, L-Arginine:1, L-Proline:1, L-Threonine:1, L-Isoleucine:1, H+:0.1, Uridine:0.1, Guanosine:0.1, L-Alanine:1, L-Methionine:1, L-Cysteine:1, L-Serine:1, Inosine:0.1, Adenosine:0.1, O2:10, Thiamine phosphate:0.1 

Top 10 produced metabolites [mmol / (gDW * hr)]:
CO2:10.896, NH3:10.583, Acetate:4.919, Formate:2.567, H2O:1.144, Propionate:1.136, H2S:0.955, MTTL:0.895, Urea:0.84, Butyrate:0.743 

```



* Usar R desde bash

# 061725




# 061825

Modelo consenso

Workflow para construirlo
1. cargar ''options''
2. Convertir el borrador de los modelos (draft model) a un modelo MNXref
3. renombrar todos los reaciiones de intercambio y biomasa de los modelos
4. agregar metabolitos
5. fusionar modelos
6. agregar biomasa universal

 [Referencia](https://zenodo.org/records/10289699)

 Este protocolo es de MATLAB, voy a pasarlo a Python

 1. load options

este archivo es del tipo ".m" lo primero que voy a hacer es pasarlo a ".py"
comando de ML que PYTHON no reconoce:

"cd" para cambiar de directorio

remplazarlo con:

```bash 
   #options

#Options for COMMIT

#~~~~~~~~~~~~~ General settings ~~~~~~~~~~~~~%

#handling of warnings
#warning('off', 'all')

#number of parallel workers
ncpu = 20;

#habitat
habitat = {'coral','seawater'};

#experiments to be analyzed
experiments = {'coral_proj'};

#path to COMMIT top directory
topDir = '~/COMMIT';

#medium file
mediumFile = 'data/media/M9-medium.mat';
LB_mediumFile = 'data/media/LB-medium.mat';

#directory for auxotrophy media (files must be of form 'model id'.tsv)
#optional: Remove the following line or set mediaDir='' if you do not want
#to use auxotrophic media to fill gaps in the first model of each
#iteration. The minimal medium given above will be used instead.
#directory for auxotrophy media (files must be of form 'model id'.tsv)
mediaDir = '';

#top directory for OTU abundance (subdirectories must be habitat >
#experiment > otutab.txt
#optional: remove the following line or set otuDir='' if you do not want
#to use OTU abundances to select at subset of models found the experiment
# and just use all models
otuDir = 'data/otu-abundances/';

#threshold for the biomass reaction
epsilon = 1E-3;

#number of iterations for the iterative approach
iterations = 100;

#print level
verbose = true;

#provide an order for iterative gap filling (optional)
order = [];

#whether or not sink reactions should be included in the gap-filling
# objective
include_sink = false;

# change to working directory
###cambiar cd porque en python no lo reconoce por 
###cd(topDir) (original)
import os 
# Get the current working directory (optional, for verification)
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

#########ya para moverme y remplazar el comando de MT
os.chdir(topDir)
    print(f"Changed working directory to: {os.getcwd()}")
except FileNotFoundError:
    print(f"Error: Directory not found - {topDir}")
except Exception as e:
    print(f"An error occurred: {e}")
# add all matlab scripts to path
#addpath(genpath('code/matlab')) segun yo no es necesario pq estoy en python

#%~~~~~~~~~~~~~ Model workspace and output directory ~~~~~~~~~~~~~%

# location where draft models are stored
modelDir = 'data/models/';

tmp_spec = '_all';

#%~~~~~~~~~~~~~ Gap-filling resources ~~~~~~~~~~~~~%

#file for the database
dbFile = 'data/gap-filling/database/Universal-model-MNXref-balanced.mat';

# path to sequence similarity workspace
seq_sim_workspace = '';


#~~~~~~~~~~~~~ Reaction-type-specific weights ~~~~~~~~~~~~~%

# reactions with sequence evidence (E <= 1E-6) 
weights.sequence = 25;
#% transport reactions
weights.transport = 100;
#% transport reactions operating on highly-permeable metabolites
weights.permeable = 50;
#% general weight for metabolic reactions
weights.metabolic = 50;
#weight for making a reaction reversible
weights.reverse = 25;
# weight for exchange reactions from the database
weights.exchange = 100000;
# weight for allowed exchange / uptake reactions (from previous solutions)
weights.uptake = 1;
# weight for sink reactions if they should be determined in the gap-filling program
weights.sink = 0;
# weights for reactions already contained in the model
weights.model = 0;

#~~~~~~~~~~~~~ metabolite classification resources ~~~~~~~~~~~~~%

# ChEBI ontology DAG workspace
chebiOntologyWS = 'data/metabolite-classification/ontologyGraph.mat';

# tab-separated ontology file
ontologyFile = 'data/metabolite-classification/chebi_ontology.csv';

# brite Hierarchy file
briteFile = 'data/metabolite-classification/briteHierarchy_ext.csv';
```
# 062025

las siguientes comando no existen en Python ya que vienen de MAtLAb, tengo que encontrar como hacer la función equivalente

1. translateIDs
2. translateModel
3. removeDuplicateMets
4. load_universal_model
5. removeDuplica

### instalar octave 

```bash 
sudo apt install octave
octave
```
para usarlo desde la terminal:

```bash 
octave
```

Para usarlo con una interfaz
```bash
octave --gui
```

###traducir de mathlab a python

# 062425

¿Cómo construir un modelo metabólico a escala genómica en **kbase**

referencia

1. El genoma debe estar anotado o re-anotado con RAST, esto antes de crear un borrador del modelo metabólico de un organismo, es necesario porque las anotaciones funcionales SEED generadas por RAST están vinculadas directamente a las reacciones bioquímicas en la base de datos de bioquímica ModelSEED, utilizada por KBase para el modelado metabólico. 
2. Construye un borrador de tu modelo metabolico con la app de: MS2 - Build Prokaryotic Metabolic Models
3. Carga tu medio 
4. Construye el modelo y rellena huecos en el medio mínimo

En kbase descagué el archivo que tiene para el medio LB y dividí los valores por 10 para hacer medio lb al 10%, lo cargué como objeto .tsv y lo subí como (import as) ''media'', no ha cargado la reconstrucción del modelo pero si cargó como medio 

si me generó el modelo que ocupo, mañana correr en gapseq a primera hora pa no tardarme tanto

[referencia](https://kbase.us/n/18302/109/)


[objetos kbase](https://docs.kbase.us/data/upload-download-guide/data-types)
# 062525
```
gapseq fill -m $RC3-draft.RDS -n LBmed.csv -c $RC3-rxnWeights.RDS -g $RC3-rxnXgenes.RDS -b 100
```

```bash
gapseq fill -m $bac1-draft.RDS -n LBmed_10percent.csv -c $bac1-rxnWeights.RDS -g $bac1-rxnXgenes.RDS -b 100
```
```bash
gapseq draft -r $RC30-all-Reactions.tbl -t $RC30-Transporter.tbl -p $RC30-all-Pathways.tbl -u 200 -l 100 -c $RC30.faa


gapseq fill -m $RC30-draft.RDS -n LBmed_10percent.csv -c $RC30-rxnWeights.RDS -g $RC30-rxnXgenes.RDS -b 100


gapseq draft -r $C20R-all-Reactions.tbl -t $C20R-Transporter.tbl -p $C20R-all-Pathways.tbl -u 200 -l 100 -c $C20R.faa


gapseq fill -m $C20R-draft.RDS -n LBmed_10percent.csv -c $C20R-rxnWeights.RDS -g $C20R-rxnXgenes.RDS -b 100


```

Ya corrió con medios LB al 10%, el docuemnto del medio debe estar en la carpeta principal de gapseq para que lo lea o poner la ruta para que lea la dirección completa de gapseaq/data/media/lb

# 062725

# 063025
¿cómo ver la lista de metabolitos de mi gem??
from cobra import io

```bash
ruta_RC3 = '/home/abigaylmontantearenas/Documents/practicas/MODELOS/data/GEM/cvm_RC3.xml'
model = cobra.io.read_sbml_model(ruta_RC3) 

for metabolite in model.metabolites:
    print(f"{metabolite.id}\t{metabolite.name}\t{metabolite.compartment}")
```
con estos nutrientes si corrió
```bash 
test_tube.set_specific_metabolite("h2o_e", 100)
test_tube.set_specific_metabolite("o2_e", 10)
test_tube.set_specific_metabolite("pi_e", 10)
test_tube.set_specific_metabolite("glu__L_e", 0.1)
test_tube.set_specific_metabolite("gly_e", 0.1)
test_tube.set_specific_metabolite("zn2_e", 10)
test_tube.set_specific_metabolite("ala__L_e", 0.1)
test_tube.set_specific_metabolite("lys_L_e", 0.1)
test_tube.set_specific_metabolite("asp_L_e", 0.1)
```

```bash
# Add glucose to the media 
test_tube.set_specific_metabolite("h2o_e", 100)
test_tube.set_specific_metabolite("o2_e", 10)
###
test_tube.set_specific_metabolite("pi_e", 10)
test_tube.set_specific_metabolite("prbamp_c", 10)
test_tube.set_specific_metabolite("glu__L_e", 0.1)
test_tube.set_specific_metabolite("mg2_e", 0.1)
test_tube.set_specific_metabolite("gly_e", 0.1)
test_tube.set_specific_metabolite("zn2_e", 10)
test_tube.set_specific_metabolite("ala__L_e", 0.1)
test_tube.set_specific_metabolite("lys_L_e", 0.1)
test_tube.set_specific_metabolite("asp_L_e", 0.1)
test_tube.set_specific_metabolite("so4_e", 0.1)
test_tube.set_specific_metabolite("arg__L_e", 0.1)
test_tube.set_specific_metabolite("ser__L_e", 0.1)
test_tube.set_specific_metabolite("cu2_e", 0.1)
test_tube.set_specific_metabolite("met__L_e", 0.1)
test_tube.set_specific_metabolite("trp__L_e", 0.1)
test_tube.set_specific_metabolite("phe__L_e", 0.1)
test_tube.set_specific_metabolite("h_e ", 0.1)
test_tube.set_specific_metabolite("tyr__L_e", 0.1)
test_tube.set_specific_metabolite("cys__L_e", 0.1)
test_tube.set_specific_metabolite("ura_e ", 0.1)
test_tube.set_specific_metabolite("cl_e", 0.1)
###
test_tube.set_specific_metabolite("leu__L_e", 0.1) 
test_tube.set_specific_metabolite("his__L_e", 0.1)
test_tube.set_specific_metabolite("pro__L_e", 0.1)
test_tube.set_specific_metabolite("cobalt2_e", 10)
test_tube.set_specific_metabolite("val__L_e", 0.1)
test_tube.set_specific_metabolite("thr__L_e", 0.1)
test_tube.set_specific_metabolite("adn_e", 0.01)
test_tube.set_specific_metabolite("thymd_e", 0.01)
test_tube.set_specific_metabolite("k_e", 10)
test_tube.set_specific_metabolite("h2s_e", 0.01)
test_tube.set_specific_metabolite("ins_e", 0.01)
test_tube.set_specific_metabolite("uri_e", 0.01)
test_tube.set_specific_metabolite("mg2_e", 10)
test_tube.set_specific_metabolite("gsn_c", 0.01)
test_tube.set_specific_metabolite("ile__L_e", 0.1)
test_tube.set_specific_metabolite("cys__L_e", 0.1)
test_tube.set_specific_metabolite("skm_c", 0.01)
test_tube.set_specific_metabolite("fol_e", 0.01)
test_tube.set_specific_metabolite("dadn_e", 0.01)
test_tube.set_specific_metabolite("lipoate_e", 0.01)
test_tube.set_specific_metabolite("na1_e", 10)
test_tube.set_specific_metabolite("cd2_e", 10)
test_tube.set_specific_metabolite("aso4_e", 10)
test_tube.set_specific_metabolite("fe2_e", 10)
test_tube.set_specific_metabolite("fe3_e", 10)
test_tube.set_specific_metabolite("cro4_p", 10)
test_tube.set_specific_metabolite("nh3_c", 10)
```

en algunos metabolistos, marca este error: 

_Warning_ : The added metabolite (cro4_p) is not able to be taken up by any of the current models

```bash

# add the models to the test tube
test_tube.add_model(C2R)
test_tube.add_model(RC3)

# 
test_tube.set_specific_metabolite("h2o_e", 100)
test_tube.set_specific_metabolite("o2_e", 10)
###
test_tube.set_specific_metabolite("pi_e", 10)
#test_tube.set_specific_metabolite("prbamp_e", 10)
#Warning: The added metabolite (prbamp_e) is not able to be taken up by any of the current models
test_tube.set_specific_metabolite("glu__L_e", 0.1)
test_tube.set_specific_metabolite("mg2_e", 0.1)
test_tube.set_specific_metabolite("gly_e", 0.1)
test_tube.set_specific_metabolite("zn2_e", 10)
test_tube.set_specific_metabolite("ala__L_e", 0.1)
#test_tube.set_specific_metabolite("lys_L_e", 0.1)
#Warning: The added metabolite (lys_L_e) is not able to be taken up by any of the current models
#test_tube.set_specific_metabolite("asp_L_e", 0.1)
#Warning: The added metabolite (asp_L_e) is not able to be taken up by any of the current models
test_tube.set_specific_metabolite("so4_e", 0.1)
test_tube.set_specific_metabolite("arg__L_e", 0.1)
test_tube.set_specific_metabolite("ser__L_e", 0.1)
test_tube.set_specific_metabolite("cu2_e", 0.1)
test_tube.set_specific_metabolite("met__L_e", 0.1)
test_tube.set_specific_metabolite("trp__L_e", 0.1)
test_tube.set_specific_metabolite("phe__L_e", 0.1)
test_tube.set_specific_metabolite("h_e", 0.1)
test_tube.set_specific_metabolite("tyr__L_e", 0.1)
test_tube.set_specific_metabolite("cys__L_e", 0.1)
test_tube.set_specific_metabolite("ura_e", 0.1)
test_tube.set_specific_metabolite("cl_e", 0.1)
###
test_tube.set_specific_metabolite("leu__L_e", 0.1) 
test_tube.set_specific_metabolite("his__L_e", 0.1)
test_tube.set_specific_metabolite("pro__L_e", 0.1)
test_tube.set_specific_metabolite("cobalt2_e", 10)
test_tube.set_specific_metabolite("val__L_e", 0.1)
test_tube.set_specific_metabolite("thr__L_e", 0.1)
#test_tube.set_specific_metabolite("adn_e", 0.01)
#Warning: The added metabolite (adn_p) is not able to be taken up by any of the current models
test_tube.set_specific_metabolite("thymd_e", 0.01)
test_tube.set_specific_metabolite("k_e", 10)
test_tube.set_specific_metabolite("h2s_e", 0.01)
test_tube.set_specific_metabolite("ins_e", 0.01)
test_tube.set_specific_metabolite("uri_e", 0.01)
test_tube.set_specific_metabolite("mg2_e", 10)
#test_tube.set_specific_metabolite("gsn_c", 0.01)
#Warning: The added metabolite (gsn_c) is not able to be taken up by any of the current models
test_tube.set_specific_metabolite("ile__L_e", 0.1)
test_tube.set_specific_metabolite("cys__L_e", 0.1)
#test_tube.set_specific_metabolite("skm_c", 0.01)
#Warning: The added metabolite (skm_c) is not able to be taken up by any of the current models
test_tube.set_specific_metabolite("fol_e", 0.01)
#test_tube.set_specific_metabolite("dadn_e", 0.01)
#Warning: The added metabolite (dadn_e) is not able to be taken up by any of the current models
test_tube.set_specific_metabolite("lipoate_e", 0.01)
test_tube.set_specific_metabolite("na1_e", 10)
test_tube.set_specific_metabolite("cd2_e", 10)
test_tube.set_specific_metabolite("aso4_e", 10)
test_tube.set_specific_metabolite("fe2_e", 10)
test_tube.set_specific_metabolite("fe3_e", 10)
#test_tube.set_specific_metabolite("cro4_e", 10)
#Warning: The added metabolite (cro4_p) is not able to be taken up by any of the current models
#test_tube.set_specific_metabolite("nh3_c", 10)
#Warning: The added metabolite (cro4_p) is not able to be taken up by any of the current models
```

para asignar los recursos son las dos siguientes lineas de código: 
```bash
# Add glucose to the media 
test_tube.set_specific_metabolite('glc__D_e', 0.01)

# Add typical trace metabolites and oxygen coli as static
trace_metabolites = ['ca2_e', 'cl_e', 'cobalt2_e', 'cu2_e', 'fe2_e', 'fe3_e', 'h_e', 'k_e', 'h2o_e', 'mg2_e',
                     'mn2_e', 'mobd_e', 'na1_e', 'ni2_e', 'nh4_e', 'o2_e', 'pi_e', 'so4_e', 'zn2_e']

for i in trace_metabolites:
    test_tube.set_specific_metabolite(i, 1000)
    test_tube.set_specific_static(i, 1000)

```
¿Para que son cada una?? 
1er bloque: # Add glucose to the media 
test_tube.set_specific_metabolite('glc__D_e', 0.01)

* solo se está añadiendo glucosa (glc__D_e).
* 0.01 (un valor bajo, típico en simulaciones de consumo
* set_specific_metabolite implica que se puede consumir y su concentración se actualiza dinámicamente durante la simulación.
* dinámico, como un nutriente limitado que se agota

2do bloque: trace_metabolites = ['ca2_e', 'cl_e', 'cobalt2_e', 'cu2_e', 'fe2_e', 'fe3_e', 'h_e', 'k_e', 'h2o_e', 'mg2_e',
                     'mn2_e', 'mobd_e', 'na1_e', 'ni2_e', 'nh4_e', 'o2_e', 'pi_e', 'so4_e', 'zn2_e']

for i in trace_metabolites:
    test_tube.set_specific_metabolite(i, 1000)
    test_tube.set_specific_static(i, 1000)

* elementos traza esenciales (sales, iones, oxígeno, agua...).
* 1000 para que no limiten el crecimiento
* set_specific_metabolite(i, 1000): como en la línea 1, los pone en el medio.
* set_specific_static(i, 1000): los deja con concentración fija — no se agotan, no cambian.
* estáticos, permanecen constantes durante la simulación, como si fueran ilimitados.

ver otros parametros

# 070125

Modelo consenso
Pasos generales:
1. Convertir y traducir los borrados de los modelos a namespace MNXref
MetaNetX/MNXref es un namespace para merabolitos y reaciones bioquímicas diseñado para estandarizar información entre diferentes bases de datos y modelos metabolicos a escala genómica (GEM). UNe y unifica la información de varias fuentes para facilitar la comparación y análisis de los modelos metabólicos. 
* Un namespace es solo una forma de agrupar cosas con nombres únicos, evitando choques de nombres y organizando mejor el código.

MNXref es un diccionario multi lenguaje para reacciones y metabolitos, los une a los datos públicos de fuentes relacionadas al metabolismo 

1. Remover todos las reacciones de intercambio y biomasa de los modelos 
2. añadir fórmulas de metabolitos
3. unir modelos de diferentes métodos
4. agrega la biomada universal de procariotas a todos los modelos
5. Rellenas huecos (gap filling (COMMIT)


# 
ver reacciones de mis modelos GEM

# 070225
```bash
carve RC3LPC_1_NS_M1_01_25.faa
 -o cm_RC3.xml

carve C2RQJT_1_rerun_NS_M2_01_25_2.faa
- o cm_C2R
```
13:00 - 13:12
13:13

```bash
export PATH=$PATH:$(pwd)
./gapseq test
```

# 071025

SMETANA; https://github.com/cdanielmachado/smetana?tab=readme-ov-file
COMPARASION DE LOS GEM: https://sysbiochalmers.github.io/Human-GEM-guide/gem_comparison/

# 080525

```bash 
gapseq find -p all -b 200 -m auto -t auto $bac60.fna
```

Carve me no puedo hacer medio LB al 10% solo identifica presencia y ausencia 

# 081825

El ambiente del modelo, que experimentalmente es el medio de cultivo, representa todos los metbolitos y co factores disponible en el organismo de sus modelos metabólicos re construidos 
los flujos se mide en:
mmol/ gr Dw h
concentración por peso seco hora, por ejemplo: 1 mol de glucosa cada 24 h a 1 gr de bacteria, su flujo es:
1 mol / (1 g Dw)(24 h)

la importación de metabolitos y co factores no garantiza que pueda ser consumido

EL medio mínimo es el medio de cultivo más pequeño que puede mantener la tasa de crecimiento específica
SI queremos que la bacteria crezca al menos 0.1 g aun que no sea el crecimento máximo posible

```bash 
minimal_medium(ST109, 0.1, minimize_components=True)
```
ST09 es el modelo
0.1 la biomasa mínima que quiero forzar 
minimize_components=True medio con el menor número de nutrientes

Por el contrario, puede encontrar el medio mínimo para la mayor biomasa posible

```bash 
max_growth = ST109.slim_optimize()
print("Crecimiento máximo:", max_growth)

min_med = minimal_medium(ST109, max_growth)
print("\nMedio mínimo para crecimiento máximo:")
print(min_med)
```