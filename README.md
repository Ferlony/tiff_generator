# tiff_generator
## About
Generate multipage or singlepage tiff file formats from provided list of dirs with pictures.

## Preview
SinglePage tiff file preview as png screenshot
<br />
![alt text](https://github.com/Ferlony/tiff_generator/blob/main/preview/1.png?raw=true)

Multipage tiff file preview as png screenshot
<br />
![alt text](https://github.com/Ferlony/tiff_generator/blob/main/preview/2.png?raw=true)

## Installation
```
git clone https://github.com/Ferlony/tiff_generator.git &&\
cd tiff_generator &&\
python -m venv venv &&\
source venv/bin/activate &&\
pip install -r requirements.txt
```

## Usage
```
usage: main.py [-h] -d DIRS [DIRS ...] [-r [ROWS]] [-o [OUT]]

options:
  -h, --help            show this help message and exit
  -d DIRS [DIRS ...], --dirs DIRS [DIRS ...]
                        Provide relative or absolute path to dirs with images to get their union in tiff Usage: -d ./dir1 /home/user/dir2 OR --dirs=./dir1 /home/user/dir2
  -r [ROWS], --rows [ROWS]
                        Use to generate singlepage tiff file from images Usage: -r 2 OR --rows=3
  -o [OUT], --out [OUT]
                        Used to set output By default puts into out in project root Usage: -o ./dir1 OR --out=/home/user/dir2
```
## Usage examples
To create singlepage tiff file from multiply several directories with 3 rows
```
python src/main.py -d /home/user/dir1 ../dir2/ /home/user/dir3/ ../dir4 -r 3
```

To create multipage tiff file from single directory and send it to specific directory
```
python src/main.py -d /home/user/dir1/ -o /home/Downloads/
```

