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

## 🥐 Prepara los datos

### a) Descargar datos
Gapseq trabaja con archivos .faa

_ejemplo_: 
```
RC3LPC_1_NS_M1_01_25.faa
```
```
C2RQJT_1_rerun_NS_M2_01_25_2.faa
```
### b) Renombrar datos
Renomabrar el archivo .faa ayuda a que sea más fácil utilizarlo en los siguientes pasos.
Hazlo con el comando "mv"


_ejemplo_: 
```
mv RC3LPC_1_NS_M1_01_25.faa bac1.faa
```
```
mv C2RQJT_1_rerun_NS_M2_01_25_2.faa bac2.faa
```

### c) Nombra los modelos
Asigna nombres a los modelos que serán usados en todo el código.
```
RC3="bac1"
```
```
C2R="bac2"
```

## 🐝
 Análisis 

### a) Construir modelo metabólico 
Predicción de reacciones y vías 
```
gapseq find -p all -b 200 -m auto -t auto $RC3.faa
```
```
gapseq find -p all -b 200 -m auto -t auto $C2R.faa
```

duración: 3329 s

**gapseq find** busca reacciones y vías metabólicas en el archivo de proteínas faa.gz (archivo comprimido con secuencias de aminoácidos).

**-p all** busca todas las posibles rutas.

**-b 200** establece un umbral o parámetro para la búsqueda (p.ej., mínimo bitscore).

**-m auto -t auto** indica que la selección del método y del hilo (threads) se haga automáticamente.

### b) Predicción de transportadores

```
gapseq find-transport -b 200 $RC3.faa 
```
```
gapseq find-transport -b 200 $C2R.faa
```
**gapseq find-transport** busca proteínas transportadoras (que mueven moléculas a través de membranas).

**-b 200** sigue siendo el umbral para la búsqueda.

### c)  Reconstrucción del borrador del modelo 

```
gapseq draft -r $RC3-all-Reactions.tbl -t $RC3-Transporter.tbl -p $RC3-all-Pathways.tbl -u 200 -l 100 -c $RC3.faa
```

```
gapseq draft -r $C2R-all-Reactions.tbl -t $C2R-Transporter.tbl -p $C2R-all-Pathways.tbl -u 200 -l 100 -c $C2R.faa
```

### d) Relleno de huecos
**¿para que?**
El _gap filling_ es una técnica computacional utilizada para mejorar la precisión y la integridad de los modelos metabólicos o ensamblajes genómicos mediante la identificación y resolución de información faltante o incompleta.
Se usa para:

* Detección de lagunas en el modelo donde se requiere una reacción para completar una vía o permitir una función metabólica específica.

* Sugerencia de añadir reacciones de bases de datos u otras fuentes para subsanar estas lagunas.

* Identificación de los genes responsables de las nuevas reacciones.
```
gapseq fill -m $RC3-draft.RDS -n LBmed.csv -c $RC3-rxnWeights.RDS -g $RC3-rxnXgenes.RDS -b 100
```
**¿Dónde encontrar otros medios medios?**
ALgunos medios vienen por default en la instalción de gap seq, los encuentras en: gapseq/dat/media

## 🙅🏾 Posibles errores
a) falta instalar librerias en R

```bash
Error in library(httr) : there is no package called ‘httr’
Execution halted
md5sum: 1.3.1.8.fasta: No such file or directory
cat: 1.3.1.8.fasta: No such file or directory
		Downloading unreviewed sequences for: 1.3.1.8
```

LIbrerias necesarias:
* httr (para descargar datos vía HTTP)

* stringr (para manipulación de strings)

* jsonlite (para manejar JSON)

* data.table (para manejo eficiente de tablas)

* dplyr (para manipulación de datos)

* tidyr (para ordenar y limpiar datos)

* magrittr (para usar pipes %>%)

* curl (para conexiones HTTP)

```R
R
sudo R -e "install.packages(c('httr','stringr','jsonlite','data.table','dplyr','tidyr','magrittr','curl'), repos='https://cloud.r-project.org')"

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
