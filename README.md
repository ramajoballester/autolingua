# Linguistic-codification (v0.2)
Automated linguistic codification python package used in [[1]](https://revistas-filologicas.unam.mx/anuario-letras/index.php/al/article/view/1685)


## Installation

To install the package, clone this repository:

```
git clone https://github.com/ramajoballester/linguistic-codification.git
```

and run the following commands:

```
cd linguistic-codification
pip install -r requirements.txt
```

## Execution

Place the codification spreadsheet file in the linguistic-codification directory and run the ```codification.py``` script. For greater flexibility, it includes the following parameters:

- color: color the automated cells.
- file_name: spreadsheet filename.
- input_cell: first cell to automate.

E.g:

```
python codification.py -init_cell D446 -file_name PRESEEA_1995_Nivel_bajo.xlsx -color
```

## Word replacement

Place the repo inside the folder with excel files and run:

```
python replacement.py -fases_filename filename -input_filename filename 
```

For sequential fase data loading:

```
python replacement.py -fases_filename filename -input_filename filename -fase2_from_file filename -fase3_from_file filename
```

To check program settings, run:

```
python replacement.py -h
```


## References

[1] Ávila, A. M., Segura, A. (2022). Estudio de las variables predictoras de la expresión del sujeto pronominal en el corpus PRESEEA. Málaga. Nivel de instrucción bajo, Anuario de Letras. Lingüística y Filología, vol. 10, no. 2, pp.57–93. doi:10.19130/iifl.adel.2022.10.2.X00S25872

