from coop_fetch.ServerResponseException import ServerResponseException
from coop_fetch.Config import Config
from coop_fetch.Fetch import Fetch
from coop_fetch.Cipher import Cipher


config = Config("http://localhost/task/server/arws.php", "seraagaldnialaldshgadl12312lasdfaaa")

fetch = Fetch(config)

try:
    tr = fetch.getInt('server.ctl.main.Test', 't1', [1])
except Exception as e:
    print(e)
