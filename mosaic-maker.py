import requests
import os
import zipfile
import io
from typing_extensions import Annotated
import typer

GEOSERVER_URL = "{host}/geoserver/rest/workspaces/dep/coveragestores/{collection}/file.imagemosaic?configure=none"
GEOSERVER_USERNAME = os.environ.get("GEOSERVER_USERNAME", "admin")
GEOSERVER_PASSWORD = os.environ.get("GEOSERVER_PASSWORD", "geoserver")

if GEOSERVER_USERNAME == "admin":
    print("Warning! Using default username and probably password...")


DATASTORE = """
user={username}
port=5432
passwd={password}
url=jdbc\:postgresql\:{hostname}
host={hostname}
database=postgres
driver=org.postgresql.Driver
schema=public
SPI=org.geotools.data.postgis.PostgisNGDataStoreFactory
fetch\ size=1000
max\ connections=20
min\ connections=5
validate\ connections=true
Loose\ bbox=true
Expose\ primary\ key=false
Max\ open\ prepared\ statements=50
preparedStatements=false
Estimated\ extends=false
Connection\ timeout=20
"""

INDEXER = """
Cog=true
PropertyCollectors=TimestampFileNameExtractorSPI[timeregex](time)
TimeAttribute=time
Schema=*the_geom:Polygon,location:String,time:java.util.Date
CanBeEmpty=true
Name={collection}
"""

TIMEREGEX = """
regex=[0-9]{4},format=yyyy
"""


def main(
    collection: Annotated[
        str, typer.Argument(help="Collection ID to use as a name for the mosaic.")
    ],
    geoserver_host: Annotated[
        str, typer.Argument(help="Geoserver host to post configuration to.")
    ],
):
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
        zip_file.writestr(
            "datastore.properties",
            DATASTORE.format(
                username=GEOSERVER_USERNAME,
                password=GEOSERVER_PASSWORD,
                hostname="database",
            ),
        )
        zip_file.writestr(
            "indexer.properties",
            INDEXER.format(
                collection=collection,
            ),
        )
        zip_file.writestr("timeregex.properties", TIMEREGEX)

    zip_buffer.seek(0)

    url = GEOSERVER_URL.format(host=geoserver_host, collection=collection)
    print(f"Posting zip contents to {url}")
    response = requests.put(
        url,
        headers={"Content-Type": "application/zip"},
        data=zip_buffer,
        auth=(GEOSERVER_USERNAME, GEOSERVER_PASSWORD),
    )
    if response.status_code == 500:
        print(response.text)

    response.raise_for_status()


if __name__ == "__main__":
    typer.run(main)
