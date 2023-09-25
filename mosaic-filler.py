from pystac_client import Client
import typer
from typing import Optional
from typing_extensions import Annotated
import requests
import os

GEOSERVER_URL = "{host}/geoserver/rest/workspaces/dep/coveragestores/{collection}/remote.imagemosaic"
GEOSERVER_USERNAME = os.environ.get("GEOSERVER_USERNAME", "admin")
GEOSERVER_PASSWORD = os.environ.get("GEOSERVER_PASSWORD", "geoserver")

if GEOSERVER_USERNAME == "admin":
    print("Warning! Using default username and probably password...")


def main(
    catalog: Annotated[
        str, typer.Argument(help="Catalog HREF to query from STAC API.")
    ],
    collection: Annotated[
        str, typer.Argument(help="Collection ID to query from STAC API and use in geoserver.")
    ],
    asset_name: Annotated[
        str, typer.Argument(help="STAC asset name.")
    ],
    geoserver_host: Annotated[
        str, typer.Argument(help="Geoserver host to post configuration to.")
    ],
    datetime: Annotated[
        Optional[str],
        typer.Option(help="Datetime string that works as a STAC API query."),
    ] = None,
):
    client = Client.open(catalog)

    query = {}
    if datetime is not None:
        query["datetime"] = datetime

    items = client.search(collections=collection, **query).items()

    url = GEOSERVER_URL.format(host=geoserver_host, collection=collection)
    added = []
    for item in items:
        asset_href = item.assets[asset_name].href
        print(f"Adding {asset_href} to {url}")
        response = requests.post(
            url,
            headers={"Content-Type": "text/plain"},
            data=asset_href,
            auth=(GEOSERVER_USERNAME, GEOSERVER_PASSWORD),
        )

        # Look for bad errors
        if response.status_code == 500:
            print(response.text)
        response.raise_for_status()

        added.append(asset_href)

    print(f"Added {len(added)} items to {url}.")


if __name__ == "__main__":
    typer.run(main)
