# GEOG 590 Final Project Proposal
#### Jason Roebuck ([@jtroe](http://github.com/jtroe))

Earlier this semester, I spend a significant amount of time, together with a few coworkers, developing  [a tool](http://github.com/ResourceDataInc/Centroid) designed to handle configuration for applications, especially cross-platform applications utilizing multiple languages.

One of the core supported languages was Python.

I'd like to take some lessons learned from previous projects in my GIS Development career, and create a repository of tools which assist in the management of ArcGIS Server using arcpy.

Specifically, I'd like to implement functionality for the following:

* Changing SDE data source from one server to another
* Analyzing MXD for ArcGIS Server Publish => json
* Publishing MXD to ArcGIS Server
* Retrieving MXD metadata (e.g. layer info: index, name, source) => json
* Disabling Schema Locking on ArcGIS Server dynamic service 
* ...

The result will be open-sourced and made publicly available on github, likely under the MIT license. 
