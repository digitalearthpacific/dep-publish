CONNECTION = "PG:user=postgres password=postgres dbname=postgres host=localhost"

insert_coastlines:
	ogr2ogr -nln "coastlines" -nlt PROMOTE_TO_MULTI -lco OVERWRITE=yes -f PostgreSQL ${CONNECTION} coastlines_merged.gpkg

create_mangroves_geoserver:
	zip -r /tmp/mangroves.zip mangroves_mosaic
	curl -u admin:geoserver -XPUT --write-out %{http_code} \
		 -H "Content-type:application/zip" \
		 --data-binary @/tmp/mangroves.zip \
		 http://localhost:8080/geoserver/rest/workspaces/dep/coveragestores/dep_s2_mangroves/file.imagemosaic?configure=none

create_wofs_geoserver:
	zip -r /tmp/wofs.zip wofs_mosaic
	curl -u admin:geoserver -XPUT --write-out %{http_code} \
		 -H "Content-type:application/zip" \
		 --data-binary @/tmp/wofs.zip \
		 http://localhost:8080/geoserver/rest/workspaces/dep/coveragestores/dep_ls_wofs/file.imagemosaic?configure=none
