# hike_trip_garmin_sync


Taking a route from ut.no and syncing it to a garmin device as a course.

- A blogpost showing how they built the UT.no page. https://www.bouvet.no/bouvet-deler/utbrudd/ut-no-hiking-in-the-cloud 
- Nasjonal Turbasen API Server. https://github.com/Turbasen/Turbasen
- The national Turbase is closed and only accessible via UT.no: https://hjelp.ut.no/hc/no/articles/360011064359-Om-Nasjonal-Turbase-NTB-/

## UT.no information

Link to GPX from UT.no: https://ut.no/api/trip/117966/gpx
Link to the JSON data:  https://ut.no/api/trip/117966/	
To the trip itself: 	https://ut.no/turforslag/117966/

## Garmin information

Developer pages:        https://developer.garmin.com
The Garmin devices use a FIT format: https://wiki.openstreetmap.org/wiki/FIT

A blogpost with a gpx to fit converter: https://www.pyrites.org.uk/post/gpx-to-fit-conversion/
- link to the GitLab project: https://gitlab.com/nwholloway/fit-route
- link to the tool: https://fit-route.pyrites.org.uk
### Online tutorial
Once you've got your converted FIT file, connect the device and copyt the ```.fit``` file to the ```/GARMIN/NewFiles/``` folder.
### The .fit files location
The .fit files are stored in the ```/GARMIN/Courses/``` folder. Could be the place to put them?


# Aternatives
NOTE: Need a Pro account to download maps...
- AllTrails: https://www.alltrails.com

