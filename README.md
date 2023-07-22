# Mult-Band AGN-SFG Classifier (MBASC)

## What is MBASC

Mult-Band AGN-SFG Classifier (MBASC) is a machine learning (ML) based algorithm aimed to classify sources as Active Galactic Nuclei (AGNs) and Star Forming Galaxies (SFGs) in a quick, reliable and reproducable way. This algorithm is based on the light gradient-boosting machine ML technique. This model can use a wide range of multi-wavelength data and redshifts to predict a classification for sources. For details on the model and the data on which it is trained, the citation at the bottom can be consulted.

## Installation

Python 3 is required to run the algorithm. In addition the following dependecies must be installed:

- pandas
- lightgbm
- sklearn
- numpy

## Usage

To run with default parameters:

	python MBASC.py [path/to/file.csv]
  
The following features can be used in the model, it is important that the **exact** name (except for capitalisation) is used in the csv file as header. If a certain feature is not available, it can simply be left out. All units (except redshift) must be converted to μJy. An example file is included in this repository (example.csv) on which you can run the algorithm (python MBASC.py example.csv).

| Feature name      | Description                                                                   |
|-------------------|-------------------------------------------------------------------------------|
| id (optional)     | ID used to save the sources as, if not given a simple numerical value is used.|
| redshift          | Redshift of source                                                            |
| u                 | u-band flux density                                                           |
| g                 | g-band flux density                                                           |
| r                 | r-band flux density                                                           |
| i                 | i-band flux density                                                           |
| z                 | z-band flux density                                                           |
| y                 | y-band flux density                                                           |
| J                 | J-band flux density                                                           |
| H                 | H-band flux density                                                           |
| K                 | K-band flux density                                                           |
| ch1               | IRAC channel 1 flux density at 3.6 μm respectively                            |
| ch2               | IRAC channel 2 flux density at 4.5 μm respectively                            |
| ch3               | IRAC channel 3 flux density at 5.7 μm respectively                            |
| ch4               | IRAC channel 4 flux density at 7.9 μm respectively                            |
| MIPS24            | Multiband Imaging Photometer for SIRTF 24 μm                                  |
| PACS100           | Photodetector Array Camera and Spectrometer 100 μm                            |
| PACS160           | Photodetector Array Camera and Spectrometer 160 μm                            |
| SPIRE250          | Spectral and Photometric Imaging REceiver 250 μm                              |
| SPIRE350          | Spectral and Photometric Imaging REceiver 350 μm                              |
| SPIRE500          | Spectral and Photometric Imaging REceiver 500 μm                              |
| radiototal        | Total 150 MHz radio flux                                                      |
| radiopeak         | Peak 150 MHz radio flux                                                       |

Output of the model will be in output/results.csv. 

## Interpreting the output file

The results.csv file has 3 columns: id, output, and AGN. The ID column is the given ID, or if not given a simple numeric value. The results.csv is in the same order as the input file. The output file is the raw output the LightGBM algorithm gives. This value is a fraction, and thus not a binary classification. This value is between 0 and 1 and is simply rounded to result in the AGN column. The AGN column is 1 for a predicted AGN and 0 for a predicted SFG.

It is important to note that the output column **does not** have to correspond to a likelihood that a source is an AGN. It entirely depends on how well the classifier works on the whole dataset. It might be of interest to analyse histograms of this column, but be careful when using this value. 

## Troubleshooting

Here are a few issues you might run into and some potential solutions:

**The algorithm does not recognise a waveband I have put in**

- Make sure you spelled the name correctly and saved the new file with that name.

**Can I use this algorithm with 1.4 GHz data**

- Yes, but you will have to convert it yourself (this might be added to the model itself later). See the corresponding paper for performance with generated 150 MHz data

**The model seems to classify wrongly (a lot of misclassifications according to other criteria, or all SFG/AGN classifications)**

- Check that you converted all the units to μJy. 
- Remove data columns with very few samples, the model might make wrong predictions based on this. 
- Play around with removing some features from the data, particurarly radio data can be tricky to cross-match. Wrongly cross-matched data can give bad results.
- Ensure that you used 150 MHz radio data, not 1.4 GHz or some other waveband.
- If this issue still persists, feel free to make an issue on this github page or send me a message. This is a relatively new algorithm, so issues are to be expected.

## Issues, Questions and Suggestions 

In case you have issues, questions or suggestions for the algorithm or anything related to it, please create an issue in this repository. Alternatively you can also send me an email at the email displayed on my profile. I'd be happy to be of assistance.

## Citation

If you use this algorithm in your research please use the following citation:

```
@article{Karsten2023,
	author = {{Karsten, J.} and {Wang, L.} and {Margalef-Bentabol, B.} and {Best, P. N.} and {Kondapally, R.} and {La Marca, A.} and {Morganti, R.} and {R\"ottgering, H. J. A.} and {Vaccari, M.} and {Sabater, J.}},
	title = {A multi-band AGN-SFG classifier for extragalactic radio surveys using machine learning},
	DOI= "10.1051/0004-6361/202346770",
	url= "https://doi.org/10.1051/0004-6361/202346770",
	journal = {A\&A},
	year = 2023,
	volume = 675,
	pages = "A159",
}
```

The corresponding paper can be found at: https://www.aanda.org/articles/aa/full_html/2023/07/aa46770-23/aa46770-23.html.
