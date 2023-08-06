# Author: Olin Gallet
# Date: 14 Oct 2022
from .trellobot.trellobot import TrelloBot as tb
from .trellobot.system.environment import Environment as Env
from .trellobot.system.terminal import Terminal
from .trellobot.exceptions.environmentvarsnotsetexception import EnvironmentVarsNotSetException
import sys

def main():
    if len(sys.argv) <= 1:
        Terminal.display_full_help()     
    else:
        try:
            if sys.argv[1] == 'buildweek':
                if Env.has_trello_keys():
                    bot = tb(Env.get_trello_api_key(), Env.get_trello_api_secret(), Env.get_trello_token())
                    bot.build_weekly_board()
                    Terminal.display_buildweek_completion()
                else:
                    raise EnvironmentVarsNotSetException()
            elif sys.argv[1] == 'startweek':
                if Env.has_trello_keys():
                    bot = tb(Env.get_trello_api_key(), Env.get_trello_api_secret(), Env.get_trello_token())
                    bot.create_weekly_lists()
                    Terminal.display_startweek_completion()
                else:
                    raise EnvironmentVarsNotSetException() 
            elif sys.argv[1] == 'endweek':
                if Env.has_trello_keys():
                    bot = tb(Env.get_trello_api_key(), Env.get_trello_api_secret(), Env.get_trello_token())
                    bot.archive_all_lists()
                    Terminal.display_endweek_completion()
                else:
                    raise EnvironmentVarsNotSetException()
            elif sys.argv[1] == 'loadweek' and len(sys.argv) == 3:
                if Env.has_trello_keys():
                    bot = tb(Env.get_trello_api_key(), Env.get_trello_api_secret(), Env.get_trello_token())
                    bot.upload_schedule(sys.argv[2])
                    Terminal.display_loadweek_completion()
                else:
                    raise EnvironmentVarsNotSetException()        
            else:
                Terminal.display_full_help()
        except Exception as ex:
            print(ex)

if __name__ == '__main__':
   main()