import evelink
import mapper
import util
from keys import keyid, vcode

cache = util.setup_cache()
eve = evelink.eve.EVE()
corp = evelink.corp.Corp(evelink.api.API(api_key=(keyid, vcode)))
sheet = corp.corporation_sheet().result
idmap = mapper.IDMap(sheet)
