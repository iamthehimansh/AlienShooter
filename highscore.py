import json
import os
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path=""
    #A:\py_game
    return os.path.join(base_path, relative_path)


class highscore():

    def main(self,score):    
        with open(resource_path("highscore.json"),"r") as read:
            a=json.load(read)
            # print(a)
            with open(resource_path("highscore.json"),"w") as write:
                if score>a["highscore"]:
                    a["highscore"]=score
                json.dump(a,write)
                return a["highscore"]



