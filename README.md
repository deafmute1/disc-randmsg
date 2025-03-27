run the docker compose dummy uwu

Commands:
- \$randmsg <channel name (default: current)> - uses random dates to approximate getting random message. The library sometimes breaks when getting messages from around a date, so it falls back on getting messages on a date and iterates until it finds at least one message on a date. This will take a long time on sparse channels
- \$randmsgproper <channel name (default: current)> - actually gets every message and selects a random one. Can potentially take a long time. For reference, it took ~30mins on a channel with ~200k messages

inv link: https://discord.com/api/oauth2/authorize?client_id=1114111160279650314&permissions=274878121984&scope=bot 
