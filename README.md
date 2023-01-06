# Repository for code around integrating custom elements using Excel to Purview - Invokes Apache Atlas API


This work borrows heavily from the work by Will Johnson
https://github.com/wjohnson/pyapacheatlas

# Setting up Authentication for Purview to work with Apache Atlas API
https://learn.microsoft.com/en-us/azure/purview/tutorial-using-rest-apis

Make sure of step 6 - permissions that the App is required within the Purview portal
The three that are required are,
* Data Curator role to access Catalog Data plane.
* Data Source Administrator role to access Scanning Data plane.
* Collection Admin role to access Account Data Plane and Metadata policy Data Plane.

# Refer to the Excel file for the excel file and the python code for updating the lineage. All of these are found under the Assets folder

One important thing to note is that you need to grab the fully qualified name of the data source from Purview for the Excel file to work properly. Refer to the screenshot below to get the details

![API Call](https://github.com/ujvalgandhi1/ApacheAtlasIntegrationwithPurview/blob/main/Assets/APICall.png)

