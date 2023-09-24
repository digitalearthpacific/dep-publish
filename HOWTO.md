# HOWTO Mosaics

1. Register

    ```bash
    curl -u admin:geoserver -XPUT --write-out %{http_code} -H "Content-type:application/zip" --data-binary @wofs_mosaic.zip http://localhost:8080/geoserver/rest/workspaces/dep/coveragestores/wofs/file.imagemosaic?configure=none

    curl -u admin:geoserver -XPUT --write-out %{http_code} -H "Content-type:application/zip" --data-binary @mangroves_mosaic.zip http://localhost:8080/geoserver/rest/workspaces/dep/coveragestores/mangroves/file.imagemosaic?configure=none
    ```

2. Modify product parameters and run `loader.py`. Execute generated loader.sh on the Geoserver instance.

3. Init and Register Mosiac after modifying `coverage.xml`

    ```bash
    curl -v -u admin:geoserver -XGET http://localhost:8080/geoserver/rest/workspaces/dep/coveragestores/mangroves/coverages.xml?list=all
    curl -v -u admin:geoserver -XPOST -H "Content-type: text/xml" -d @"coverage.xml" "http://localhost:8080/geoserver/rest/workspaces/dep/coveragestores/mangroves/coverages"
    ```

4. Apply styles

## HOWTO Coastlines

1. Reproject to 3832 (PDC Mercator) if required. (or use QGIS, force multi-type)

    ```bash
    ogr2ogr -nlt PROMOTE_TO_MULTI -f gpkg -t_srs epsg:3832 1.gpkg coastlines_4Sep2023.gpkg 
    ```

2. Populate PostGIS from GeoPackage Output.

    ```bash
    ogr2ogr -nlt PROMOTE_TO_MULTI -f PostgreSQL "PG:user=postgres password=erlang44 dbname=dep" 1.gpkg
    ```

3. Reproject columns (i required)

    ```bash
    ALTER TABLE coastlines ALTER COLUMN geom TYPE Geometry(MultiLineString) USING ST_Transform(geom, 3832); 
    ```

4. Explode and Optimise

    ```sql
    ALTER TABLE coastlines rename TO coastlines_old;

    CREATE TABLE coastlines(fid SERIAL PRIMARY KEY, year int, geom geometry(LineString, 3832));

    INSERT INTO coastlines(year, geom)
    SELECT
        year,
        (ST_Dump(geom)).geom
    FROM coastlines_old
    WHERE ST_GeometryType(geom) = 'ST_MultiLineString';

    CREATE INDEX coastlines_index ON coastlines USING gist (geom);

    DROP TABLE coastlines_old;
    ```

5. Register in Geoserver instance using Import Data plugin.

6. Apply styles.
