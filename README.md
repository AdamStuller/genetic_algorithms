#Genetic Algorithm

This repo contains program using genetic algorithm to find treasures on map. 

Map is represented by two dimensional arrays of characters, 'X' for ordinary field, 'S' for start
and 'P' for treasure. 

Source code is in src directory. It is divided into 7 files. 

In evolution.py, main algorithm is used. Everything, generic, that can be used in 
more problems is in that file. In treasure_finder everything related to genetic algorithm, yet
specific for this problem is located. Than there is virtual_machine.py that contains everything
related to virtual machine my program si using. From app.py whole program si run and config is config :).

# Usage
**Python3.7** is used as interpreter. To set up environment use

```
git clone git@github.com:AdamStuller/genetic_algorithms.git
cd ./src
```

Now you have repository cloned. You can create virtual environment by running:
```
python3.7 -m venv ./venv
./venv/bin/pip3.7 install -r ./requirements.txt
```

And then, after modifying, config run:
```
./venv/bin/python3.7 ./src/app.py
```
