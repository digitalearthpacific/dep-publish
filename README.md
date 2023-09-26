# Digital Earth Pacific: Geoserver Publishing Artefacts

See: [HOWTO](HOWTO.md) for previous notes

## Dev environment

Run up the environment with `docker-compose up`.

The Docker Compose environment includes the following services:

* Terria [http://localhost:3001](http://localhost:3001)
* GeoServer [http://localhost:8080](http://localhost:8080)
* PostGIS (at port `5432`)

Insert the coastlines data with a command like:

```bash
    ogr2ogr \
        -nln "coastlines" \
        -nlt PROMOTE_TO_MULTI \
        -lco OVERWRITE=yes \
        -f PostgreSQL ${CONNECTION} \
        coastlines_merged.gpkg
```

CONNECTION should be `"PG:user=postgres password=postgres dbname=postgres host=localhost"`

The GeoServer username/password is `admin:geoserver`.

## How to create an image mosaic and populate it

### Create the image mosaic on GeoServer

Run the command `python mosaic-maker.py example_product http://localhost:8080`

Note that `example_product` should match the name of the STAC Collection
you're reading from, so we have consistent layer names.

And the second argument is the GeoServer hostname including port.

You need to have two environment variables exported:

```bash
GEOSERVER_USERNAME
GEOSERVER_PASSWORD
```

### Populate the image mosaic

Run the command:

```bash
python mosaic-builder.py \
    https://stac.staging.digitalearthpacific.org \
    dep_ls_wofs \
    mean \
    http://localhost:8080
```

The first argument is the STAC API hostname, the second is the STAC Collection
the third is the asset name and the fourth, the GeoServer hostname.

This script will get all the items for a collection and insert the specified
asset into the mosaic.

### What next

After you have done the above two steps for a product, you need to set
up a layer and styles in GeoServer. Example styles are in the `styles`
folder. Make sure you configure the `Dimensions` tab for the layer
to publish the Time dimension.
