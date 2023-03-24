def sposti_ok(sposti):
    # tarkastetaan, että @ on vain kerran
    if "@" in sposti:
        at = sposti.find("@")
        atilman = sposti.replace(sposti[at], "", 1)
        if "@" in atilman:
            return False
        else:
        # tarkastetaan, että @jälkeen löytyy väh. 1 piste
            x = at
            while x >= 0:
                atjalkeen = sposti.replace(sposti[x], "", 1)
                x +=1
                print(atjalkeen)
                
    else:
        False



 
print(sposti_ok("my.ownsite@ur-earth.org"))