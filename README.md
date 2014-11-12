Just a little piece of code to get the number of skillbooks (or any item really) from a corp container in EVE Online.

/!\ Current HEAD is a major refactoring operation, you probably don't want to use that. Version 0.9-dirty is, well, dirty, but should work.

Requirements:
* Depends on evelink: https://github.com/eve-val/evelink
* is mostly a Google App Engine app, although there's a CLI that also gives results. You can also download a development appserver (https://developers.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python) to run it locally.
* Create a file keys.py containing your keyid and vcode for a corp API key that can access Assets and Locations. File should look like
```python
keyid = your_key_id
vcode = 'your_vcode'
```
* Put the skillbooks you're interested in in the "skillbooks-list" file (or another file if you want to)
* Configure the app in config.py: 
  - stationname is the station name
  - container name is the container name that you're interested in
  - dbname is the name of the sqlite db containing eve static data - only useful if you want to regenerate the item ids list
  - booklist is the list of skillbooks (or items) to track
  - bookids is the fil containing the id <-> item name list (from eve static dump, generated with skillbooks_id_export.py
  - allitems is a Boolean - True if we want to return all the items in the container, False to return only those tracked in the list
* Check with skillbooks-cli.py that everything works: it should display the skillbooks of your list followed by the number of books in the hangar. ERROR in the skillbooks list means that you probably have a typo in the skillbook name, or that your sqlite DB dump is not up to date (esp. with recent-ish skill namechanges).
* To update the item list (skillbooks-ids, by default), get a sqlite DB dump from https://www.fuzzwork.co.uk/dump/, decompress it, rename it if you want to (default is eve-dump.db), and start skillbooks_id_export.py.
