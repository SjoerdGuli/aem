# Repository Group 4 Applied Experimental Methods

## Introduction
In this repository, our code for the course Applied Experimental Methods for the TU Delft is presented. For testing, we used the Feelpen and we gathered data on comfort when using the pen with different temperature settings. We did this using a Likert scale, this data can be found in data.csv.

## Clone repository
To clone the repository, run the following code:
```sh
git clone https://github.com/SjoerdGuli/aem.git
pip install -r requirements.txt
```

## Code
### random_sequence.py
This code gives twenty random sequences from 1-5. We used this to generate twenty random sequences for twenty different participants. The numbers 1-5 were linked to different temperature settings: 1 = 20 degrees, 2 = 25 degrees, 3 = 30 degrees, 4 = 35 degrees and 5 = 40 degrees.

To run this script, go to the aem directory and run the following:

```sh
python random_sequence.py
```

### new_violin.py
This plot gives a violin plot of the raw data. The raw data is also visible in the violin plots, given with white dots in the violin plot.

To run this script, go to the aem directory and run the following:

```sh
python new_violin.py
```

### likert_chart.py
The script gives a likert chart for all five temperature settings. Percentages are gives to how many times a comfort rating (1-9) is given.

To run this script, go to the aem directory and run the following:

```sh
python likers_chart.py
```

### spearman.py
The spearman test is used to do statistical analysis, telling us if the results are significant or not.

To run this script, go to the aem directory and run the following:

```sh
python spearman.py
```
