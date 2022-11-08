import logging
from util import logcfg
from copy import deepcopy, copy

def main():
    mystr = "Módulo DAM, curso 2"
    mylist = ["Sergio", "Manuel", "Adrián", "Rubén"]
    mynum = 27
    mydict = {"l": mylist, "s": mystr, "n": mynum}
    logging.info(mydict)
    
    mydict_clone = mydict
    logging.info(f"id(mydict) == id(mydict_clone) {id(mydict) == id(mydict_clone)}")
    logging.info(f"mydict == mydict_clone {mydict == mydict_clone}")
    
    mydict_copy = copy(mydict)
    logging.info(f"id(mydict) == id(mydict_copy) {id(mydict) == id(mydict_copy)}")
    logging.info(f"mydict == mydict_copy {mydict == mydict_copy}")
    logging.info(f"id(mydict['l']) == id(mydict_copy['l']) {id(mydict['l']) == id(mydict_copy['l'])}")

    mydict_deep_copy = deepcopy(mydict)
    logging.info(f"id(mydict) == id(mydict_deep_copy) {id(mydict) == id(mydict_deep_copy)}")
    logging.info(f"mydict == mydict_deep_copy {mydict == mydict_deep_copy}")
    logging.info(f"id(mydict['l']) == id(mydict_deep_copy['l']) {id(mydict['l']) == id(mydict_deep_copy['l'])}")


if __name__ == "__main__":
    logcfg(__file__)
    logging.debug("Comienzo de programa")
    main()
    logging.debug("Fin de programa")