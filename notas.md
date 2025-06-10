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