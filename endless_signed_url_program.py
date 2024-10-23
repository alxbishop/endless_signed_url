# Libraries
import up42
import time
import schedule
import subprocess

# Note : For this program to run you must have GDAL installed and have your UP42 credentials saved to a json file.

# Function to build signed urls, takes as input 'assets', this 'asset' object is the result of searching for assets in your storage, see main function below
def build_signed_url(assets):

    # Loop for each asset returned from the search
    for asset_number in range(len(assets)):
        
        try:

            # Get the stac items corresponding to the asset in storage - typically an asset is composed of one stac item however there a situations where
            # an asset can have multiple stac items, for instance pneo stereo products or some vexcel orders. In this instance we would need to adapt our program
            # to handle these cases. When you stac_items[0] in the code below, it means we are looking at the first (and often only) stac_item.
            stac_items = assets[asset_number].stac_items

            # For logging we print some info
            stac_item_id = stac_items[0].id
            print(asset_number, stac_item_id)

            # Create a list of the stac_asset keys, these keys are needed by the get_stac_asset_url() function to then generate the signed urls
            asset_key_list = [stac_asset for stac_asset in stac_items[0].get_assets(role='data').keys()]
            # print(asset_key_list)

        except:

            # It is possible for some assets to not be stac enabled
            print(f'WARNING: No STAC metadata - skipping asset {stac_item_id}')
            continue


        # For each stac asset we retrieved from the stac items above, we create a signed url and build a virtual raster using gdal
        for asset_key in asset_key_list:
            stac_asset_url = assets[asset_number].get_stac_asset_url(stac_items[0].get_assets().get(asset_key))
            print(asset_key)

            try:
                cmd_vrt = ['gdalbuildvrt',
                           f'./vrt/{asset_key}.vrt',
                           '-overwrite',
                           stac_asset_url
                           ]
                print(' - Building VRT raster file')
                subprocess.run(cmd_vrt)
                print(' - Created VRT raster file')

            except:
                print(f'Some error building VRT file {asset_key}')


# The main program to find assets and build the relevant signed urls
def main():

    # Authenticate
    up42.authenticate('./creds/credentials.json') # < - - - - - - - - - - - - you MUST update this file with your credentials !!!
    
    # Initialize the storage class to manage data in your storage
    storage = up42.initialize_storage()

    # # # Search for assets - CHANGE THESE PARAMETERS TO FIND ASSETS YOUR STORAGE # # #
    assets = storage.get_assets(workspace_id='', # < - - - - - - - - - - - - - - - -  you can change this parameter
                            limit=5, # < - - - - - - - - - - - - - - - - - - - - - -  you can change this parameter
                            collection_names=['vexcel-us-15cm-ortho'], # < - - - - -  you can change this parameter
                            tags=['VEXCEL']) # < - - - - - - - - - - - - - - - - - -  you can change this parameter
    

    # Call the function to build the signed url passing the "assets" object from above, which contains the assets found in your storage.
    build_signed_url(assets)

    print('Wainting for next run ...')

# Run onetime 
main()

# Run the program every 4 minutes 
if __name__ == "__main__":
    schedule.every(4).minutes.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)