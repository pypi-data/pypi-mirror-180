# TDS2STAC

A STAC catalog creator from Thredds data server web services

## Installation

```bash
pip install tds2stac
```

## Usage


### Use case

You can use the following template for creating STAC catalog from the TDS web service for your project.

```python
from tds2stac.tds2stac import Converter

converter = Converter("http://172.27.80.119:8088/thredds/catalog/regclim/raster/global/era5/sfc/catalog.html",
                     stac=True, stac_dir="/path/to/save/stac/catalogs/",
                     stac_id = "sample",
                     stac_description = "sample")

output:

Start Scanning datasets of http://172.27.80.119:8088/thredds/catalog/regclim/raster/global/era5/sfc/catalog.xml
|__ http://172.27.80.119:8088/thredds/catalog/regclim/raster/global/era5/sfc/catalog.xml |  Number of branches:  5
|_______ http://172.27.80.119:8088/thredds/catalog/regclim/raster/global/era5/sfc/static/catalog.xml |  Number of data:  1
|_______ http://172.27.80.119:8088/thredds/catalog/regclim/raster/global/era5/sfc/monthly/catalog.xml |  Number of data:  246
|_______ http://172.27.80.119:8088/thredds/catalog/regclim/raster/global/era5/sfc/daily/catalog.xml |  Number of data:  360
|_______ http://172.27.80.119:8088/thredds/catalog/regclim/raster/global/era5/sfc/climatology/catalog.xml |  Number of data:  7
|_______ http://172.27.80.119:8088/thredds/catalog/regclim/raster/global/era5/sfc/aggregated/catalog.xml |  Number of data:  1
615 data are going to be set as items
5 data are going to be set as items
Start processing:  http://172.27.80.119:8088/thredds/catalog/regclim/raster/global/era5/sfc/static/catalog.xml
5 / 5 STAC catalogs are created
1 / 615 STAC items are connected to the related catalog
100%|████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 11.02it/s]
Start processing:  http://172.27.80.119:8088/thredds/catalog/regclim/raster/global/era5/sfc/monthly/catalog.xml
5 / 5 STAC catalogs are created
247 / 615 STAC items are connected to the related catalog
100%|████████████████████████████████████████████████████████████████████████████████████████| 246/246 [00:43<00:00,  5.64it/s]
Start processing:  http://172.27.80.119:8088/thredds/catalog/regclim/raster/global/era5/sfc/daily/catalog.xml
5 / 5 STAC catalogs are created
607 / 615 STAC items are connected to the related catalog
100%|████████████████████████████████████████████████████████████████████████████████████████| 360/360 [01:10<00:00,  5.11it/s]
Start processing:  http://172.27.80.119:8088/thredds/catalog/regclim/raster/global/era5/sfc/climatology/catalog.xml
5 / 5 STAC catalogs are created
614 / 615 STAC items are connected to the related catalog
100%|████████████████████████████████████████████████████████████████████████████████████████| 7/7 [00:00<00:00,  7.89it/s]
Start processing:  http://172.27.80.119:8088/thredds/catalog/regclim/raster/global/era5/sfc/aggregated/catalog.xml
5 / 5 STAC catalogs are created
615 / 615 STAC items are connected to the related catalog
100%|████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:22<00:00, 22.02s/it]
Start processing:  http://172.27.80.119:8088/thredds/catalog/regclim/raster/global/era5/sfc/catalog.xml
5 / 5 STAC catalogs are created
615 / 615 STAC items are connected to the related catalog
0it [00:00, ?it/s]
```
