# 20250606

# RECONSTRUCCION DE GEM
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

# Subir scrips a github
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
# ejemplo documentación

```b
./gapseq doall toy/myb71.fna.gz

```

Para correrlo tienes que especificar la dirección de donde se descargó el programa
# no me corrió

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
de las 18:05 a 


