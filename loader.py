import azure.storage.blob
from azure.storage.blob import ContainerClient

account_url = "https://deppcpublicstorage.blob.core.windows.net/output?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2025-10-31T06:39:05Z&st=2023-08-23T22:39:05Z&spr=https,http&sig=uvBatSiUx4NqE%2BTzyjXFjfxOl%2BjlOrpBYhKMdHGuzRU%3D"
container_client = ContainerClient.from_container_url(account_url)

#product = "wofs"
#product_path = "wofs/0.0.1/wofs/2022/"
#product_path = "dep_ls_wofs/0-0-3/"
product = "mangroves"
product_path = "dep_s2_mangroves/0-0-2/"

f = open("loader.sh", "w")
blob_list = container_client.list_blobs()
for blob in blob_list:
    fn = blob.name
    if fn.startswith(product_path):
      if fn.endswith(".tif"):
        cmd = 'curl -u admin:geoserver -XPOST -H "Content-type: text/plain" --write-out %{http_code} -d "https://deppcpublicstorage.blob.core.windows.net/output/' + fn + ' "http://localhost:8080/geoserver/rest/workspaces/dep/coveragestores/' + product + '/remote.imagemosaic"'
        print(cmd)
        f.write(cmd + "\r\n")
f.close()
print("Finished.")
