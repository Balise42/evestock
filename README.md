Just a little piece of code to get the number of skillbooks (or any item really) from a corp container in EVE Online.

Requirements:
* Depends on evelink: https://github.com/eve-val/evelink
* Create a file keys.py containing your keyid and vcode for a corp API key that can access assets. File should look like
```python
keyid = your_key_id
vcode = 'your_vcode'
```
* Put the skillbooks you're interested in in the "skillbooks-list" file (or another file if you want to)
* Configure the app in config.py: sysid is the system id, stationid is the station id, smallcontainerid is the container containing the skillbooks, dbname is the database dump file name, booklist is the skillbook list file name (the books that you want to track), bookids is the DB dump for the id-name matching in the DB.
* Check with skillbooks-cli.py that everything works: it should display the skillbooks of your list followed by the number of books in the hangar. ERROR in the skillbooks list means that you probably have a typo in the skillbook name, or that your sqlite DB dump is not up to date (esp. with recent-ish skill namechanges).
* To update the item list (skillbooks-ids, by default), get a sqlite DB dump from https://www.fuzzwork.co.uk/dump/, decompress it, rename it if you want to (default is eve-dump.db), and start skillbooks_id_export.py.
