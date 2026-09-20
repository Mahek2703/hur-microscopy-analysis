# Python-based Analysis of HuR Fluorescence in Confocal Microscopy Images

## Overview

This project demonstrates a beginner-friendly Python workflow for quantitative analysis of fluorescence microscopy images.

The workflow focuses on measuring HuR fluorescence within DAPI-defined nuclei across Control, CMLD2, and PMA conditions.

## Analysis workflow

1. Load TIFF microscopy images
2. Extract the DAPI channel for nuclear identification
3. Segment nuclei using image-processing methods
4. Measure HuR fluorescence within detected nuclei
5. Calculate mean nuclear HuR fluorescence for each imaging field
6. Visualize variation across imaging fields and experimental conditions

## Tools

- Python
- NumPy
- pandas
- matplotlib
- scikit-image
- tifffile

## Data

The original microscopy images are not included in this repository because they are experimental data.

The repository focuses on the analysis workflow and documentation.

## Note

This project is based on one confocal microscopy experiment with six imaging fields per condition.

The analysis is exploratory and demonstrates a bioimage-analysis workflow rather than providing statistical evidence from independent biological replicates.
## Conclusion

This bioimage analysis workflow showed higher mean nuclear HuR fluorescence in CMLD2- and PMA-treated imaging fields compared with Control fields, with the highest mean nuclear HuR intensity observed in PMA-treated fields. These results demonstrate how Python-based image analysis can be used to quantify nuclear fluorescence across microscopy images.

As this analysis was performed on one confocal microscopy experiment with six imaging fields per condition, the findings are exploratory and describe variation between imaging fields rather than independent biological replicates.
