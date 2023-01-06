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
