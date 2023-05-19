# Mult-Band AGN-SFG Classifier (MBASC)

## What is MBASC

TODO

## Installation

Python 3 is required to run the algorithm. In addition the following dependecies must be installed:

- pandas
- lightgbm
- sklearn
- numpy

## Usage

To run with default parameters:

::

	python MBASC.py [path/to/file.csv]
  
The following features can be used in the model, it is important that the **exact** name (except for capitalisation) is used in the csv file as header. If a certain feature is not available, it can simply be left out.

| Feature name      | Description                                               |
|-------------------|-----------------------------------------------------------|
| redshift          | Redshift of source                                        |
| u                 | u-band flux density (μJy)                                 |
| g                 | g-band flux density (μJy)                                 |
| r                 | r-band flux density (μJy)                                 |
| i                 | i-band flux density (μJy)                                 |
| z                 | z-band flux density (μJy)                                 |
| y                 | y-band flux density (μJy)                                 |
| J                 | J-band flux density (μJy)                                 |
| H                 | H-band flux density (μJy)                                 |
| K                 | K-band flux density (μJy)                                 |
| ch1-ch4           | IRAC channel 1 flux density at 3.6 μm respectively (μJy)  |
| ch2               | IRAC channel 2 flux density at 4.5 μm respectively (μJy)  |
| ch3               | IRAC channel 3 flux density at 5.7 μm respectively (μJy)  |
| ch4               | IRAC channel 4 flux density at 7.9 μm respectively (μJy)  |
| MIPS24            | Multiband Imaging Photometer for SIRTF 24 μm (μJy)        |
| PACS100           | Photodetector Array Camera and Spectrometer 100 μm (μJy)  |
| PACS160           | Photodetector Array Camera and Spectrometer 160 μm (μJy)  |
| SPIRE250          | Spectral and Photometric Imaging REceiver 250 μm (μJy)    |
| SPIRE350          | Spectral and Photometric Imaging REceiver 350 μm (μJy)    |
| SPIRE500          | Spectral and Photometric Imaging REceiver 500 μm (μJy)    |
| radiototal        | Total 150 MHz radio flux (μJy)                            |
| radiopeak         | Peak 150 MHz radio flux (μJy)                             |
  
## Troubleshooting



## Issues, Questions and Suggestions 

In case you have issues, questions or suggestions for the algorithm or anything related to it, please create an issue in this repository. Alternatively you can also send me an email at the email displayed on my profile.

## Citation

TODO
