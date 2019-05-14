import json
from util.entity.pylocale import Locale
from util.entity.pyagentsender import AgentSender
from util.entity.pylogin import Login

user = Login()
Locale()
login, sysname, nodename, date, kernel = user.get_login_user()
user = dict(
    login = login,
    sysname = sysname,
    nodename = nodename,
    date = date,
    kernel = kernel
)
user = json.dumps(user)
agent_sender = AgentSender(message=user)

