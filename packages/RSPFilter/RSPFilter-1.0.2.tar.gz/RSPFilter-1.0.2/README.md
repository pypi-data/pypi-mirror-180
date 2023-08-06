# RSPFiler
Homogeneous filtering of Relion Star Particles File.

# Installation
for now, only PIP is availble. Install RMSPFilter with the command
`pip install RMPFiler`

# Dependancies
- python>=3.8
- numpy
- pandas
- plotly
- scipy
- starfile
- panel


# Usage 
RSPFilter create a WebApplication for interactive filtering and visualization.  
However it can still be used in batch mode with the argument `-g N`

```bash
usage: RSPFilter.py [-h] [-f FILE] [-r RESOLUTION] [-d THRESHOLD] [-o OUTPUT] [-g GUI]

Homogeneous particle filtering of STAR file

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  StarFile
  -r RESOLUTION, --resolution RESOLUTION
                        Grid density (default:5)
  -d THRESHOLD, --threshold THRESHOLD
                        density threshold (default:100)
  -o OUTPUT, --output OUTPUT
                        outputfile
  -g GUI, --gui GUI     start a webserver interactive GUI (Y/n)
```

# Example
## Basic command line
`RSPFilter -f particles.star`

## WebApp Example



