### Endless UP42 Signed URL

This programe continuously validates an UP42 signed url for a given stac_item in your data managament/storage space. It creates a GDAL .vrt file so that you can conveniently load the streamed raster data into any GIS software or other wed apps that can read GDAL .vrt virtual files.

To run the python program you must have GDAL installed and an UP42 account.

Try the following steps to get started.

1.Install miniconda: https://docs.anaconda.com/miniconda/
2.Create new virtual env:
	conda create -n up42
	conda activate up42
3.install gdal:
	conda install -c conda-forge gdal
4.install up42:
	conda install -c conda-forge up42-py
5.install schedule:
	conda install conda-forge::schedule

You will need to create a json credentials file.

If you need help or have questions email me at alex.bishop@up42.com.

Good luck!!

Alex