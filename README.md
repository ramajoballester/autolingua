# Linguistic-codification (v0.2)
Automated linguistic codification python package


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
python codification2.py -fases_filename filename -input_filename filename 
```

To check program settings, run:

```
python codification2.py -h
```
