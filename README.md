# Dynlocal
For Local Dynamism. A web plateforme that the aim is to gather socials, environmentals, or commercials local initiatives.

## Functionnal key points 
*Sorted by priority*

- Contributor side : 
	- Loggin
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

On the first time, the application will probably be hosted by a cloud plateform (Heroku ?) to advantage of a browsner-friendly SSL/TLS certificate.

The application will be build by using a Python server. Probably Django to avoid the cost of developping lots of home made services.
The client side will be based on the AngularJs framework and will be linked to the server by secured REST web services.

This architecture allows futur utilisations of the API by others client apps. 

## Data

The data will remains proprietary on the first time. A next step could be a creation of a French 1901 law type association to manage the hosting.
