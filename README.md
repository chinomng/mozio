# Mozio providers and areas API

###### ```HOST/area_api/provider/``` Method GET. List all providers
###### ```HOST/area_api/provider/``` Method POST. Add a provider. Requires the following variables name, email_address, phone_number, currency, lang
###### ```HOST/area_api/provider/<id>/``` Method UPDATE. Update a provider with a given id. Requires the following variables name, email_address, phone_number, currency, lang
###### ```HOST/area_api/provider/<id>/``` Method GET. Details for the provider with a given id
###### ```HOST/area_api/provider/<id>/``` Method DELETE. Remove the provider with a given id

###### ```HOST/area_api/area/``` Method GET. List all areas
###### ```HOST/area_api/area/``` Method POST. Add an area. Requires the following variables name, area (geojson representing a polygon), provider (a provider id), price
###### ```HOST/area_api/area/<id>/``` Method UPDATE. Update an area with a given id. Requires the following variables name, area (geojson representing a polygon), provider (a provider id), price
###### ```HOST/area_api/area/<id>/``` Method GET. Details for the area with a given id
###### ```HOST/area_api/area/<id>/``` Method DELETE. Remove the area with a given id

###### ```HOST/area_api/search_areas/<latiture>/<longitude>/``` List all areas containing a point for a given latitude and longitude
