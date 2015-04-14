# Dynlocal
*Dynlocal* stands for Local Dynamism.
This is a web platform that aims to gather informations about social, environmental, or commercial initiatives, in order to link local interested parties. 

## Functionnal key points
[**See the functionnal specifications**](https://github.com/tpape/Dynlocal/wiki#specifications).   
*Sorted by priority*

- Contributor side : 
	- Login
	- Create a profile
	- Complete the profile : 
		- Location (accurate, on a map)
		- Name
		- Description
		- Contact
		- Tags
	- News publishing (articles)
		- Title 
		- Content
		- Tags
		- Public comments
	- Public notation ? Comments ? 

- Visitor side :
	- Set his position on the map
	- Editable distance radius	
	- Display the list of profiles found in the area
	- On clic on a profile, display the content

## Architecture

The backend of the application will be built using Python/Django, to avoid additional developments.
The frontend will be implemented in AngularJs. Communications between the both ends will be made RESTfull. 

In order to take leverage of SSL/TLS certificate to build a browser friendly website the application will be hosted by a cloud platform.
This is the list of the cloud platform that supports Django:
- Heroku
- Amazon EC2
- Google App Engine
- Linode
- OpenShift
- dotCloud
- Jelastic
- nitrous.io
- pythonanywhere

This architecture ensure futur use of the API by other derived apps. 

## Data

The data will remains proprietary on the first time.
A next step could be a creation of a French 1901 law type association to manage the hosting.
