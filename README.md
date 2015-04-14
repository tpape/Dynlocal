# Dynlocal
*Dynlocal* stands for Local Dynamism.
This is a web platform that aims to gather informations about social, environmental, or commercial initiatives, in order to link local interested parties. 

## Functionnal key points 
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

### Use cases

#### UC_1 - User location

The user sets his position on a map with a clic or a typing his adresse on the magic-bar (see UC_3 - Magic bar).

> **Technical notes** :  
>We will use OpenStreetMap as map provider, and we will use a JavaScript library for the frontend integration (For example, [Leaflet](http://leafletjs.com/)). 

#### UC_2 - Map based search

The user defines a radius in km or duration to limit the search perimeter. Profiles that are located on this perimeter will be displayed as pin on the same map.

> **Technical notes** :  
> The calculation of the perimeter will be based on real road circuit. The distance can be estimated by using a home-hosted service ([OSRM backend](https://github.com/Project-OSRM/osrm-backend/wiki/Server-api)) or with a external commercial service ([graphhopper API](https://github.com/graphhopper/directions-api/blob/master/docs-matrix.md)).   
>We can pre-estimate wich profil is in the perimeter by drawing a virtual rectangle and verify the distance criteria afterward to give à precise information to the user.

#### UC_3 - Magic bar

A search bar that provide lots of service, as setting user location, selecting a specific profile, searching for profiles with key-words, adding somme tags to limit the search results...

#### UC_4 - User authentification

To limit the number of users, we will requiere a regristration to access to the data. A unauthentified user will only have access to the UC_1 and UC_2. But not to any profile detail other than the pin on the map. A registration will be charged for, and some invitations will be given to the profiles for their clients.   
By now, the term user will exclusivly refer to a registered user.

#### UC_5 - Search results 

The user can clic on a pin mentionned on the UC_2 to display a little tooltip that contains a quick  description of the profile (Name, activity, exact distance, phone number, ...) and a link to the full description (google map style).  
We can think about adding the result list under the map. 

#### UC_6 - Search criteria

The user will be able to filter his search results with : 
- Location and radius
- Key words
- Pre-defined Tags

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
