import json, os

from openpyxl import Workbook
from openpyxl import load_workbook 

# PyApacheAtlas packages
# Connect to Atlas via a Service Principal
from pyapacheatlas.auth import ServicePrincipalAuthentication
from pyapacheatlas.core import PurviewClient, AtlasEntity
from pyapacheatlas.readers import ExcelConfiguration, ExcelReader

if __name__ == "__main__":
    """
    This sample provides an end to end sample of reading an excel file and
    generating custom lineage that can be incorporated within Purview.
    """

    # Authenticate against your Atlas server
    oauth = ServicePrincipalAuthentication(
        tenant_id="72f988bf-86f1-41af-91ab-2d7cd011db47",
        client_id="808f705a-7154-4f00-8cba-d4dbbd3fcc85",
        client_secret="DBS8Q~KxVZfIgOgIo~bSIC2QFy28FI5adFFg4bhB"
    )
    client = PurviewClient(
        account_name = "pvlab-43aef4-pv",
        authentication=oauth
    )

    # SETUP: This is just setting up the excel file for you
    file_path = "./demo_update_lineage_upload.xlsx"
    excel_config = ExcelConfiguration()
    excel_reader = ExcelReader(excel_config)

    # ACTUAL WORK: This parses our excel file and creates a batch to upload
    lineage_processes = excel_reader.parse_update_lineage(file_path)

    results = client.upload_entities(lineage_processes)

    print(json.dumps(results, indent=2))

    print("Completed bulk upload of lineage processes successfully!")
    