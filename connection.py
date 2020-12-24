from zenmoney import *

oauth = OAuth2('g6fc0b73892724ad14c347822e93e1', 'b2c269024d', 'levelgameclub', 'level9898')
api = Request(oauth.token)
diff = api.diff(Diff(**{'serverTimestamp': 1601510401}))