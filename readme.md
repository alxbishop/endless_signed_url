### Endless UP42 Signed URL

This program continuously validates an UP42 signed url for a given stac_item in your data management/storage space. It creates a GDAL .vrt file so that you can conveniently load the streamed raster data into any GIS software or other wed apps that can read GDAL .vrt virtual files.

To run the python program you must have GDAL installed and an UP42 account.

#### Try the following steps to get started.

1. Install miniconda: https://docs.anaconda.com/miniconda/
1. Create new virtual env:
	conda create -n up42
	conda activate up42
1. install gdal:
	conda install -c conda-forge gdal
1. install up42:
	conda install -c conda-forge up42-py
1. install schedule:
	conda install conda-forge::schedule

You will need to update the provided json credentials file.

Good luck!!

Alex