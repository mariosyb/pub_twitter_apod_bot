# emojis unicodes, '+' is replaced for '000' for python
GALAXY = '\U0001F30C'
TELESCOPE = '\U0001F52D'
COMET = '\U00002604'
SATELLITE = '\U0001F6F0'
ROCKET = '\U0001F680'
FLYING_SAUCER = '\U0001F6F8'
SATURN = '\U0001FA90'
STAR = '\U00002B50'
ASTRONAOUT = '\U0001F468'
EARTH = '\U0001F30E'
ALIEN = '\U0001F47E'


def getSpaceEmojis():
    emojis = dict()
    emojis['galaxy'] = GALAXY
    emojis['telescope'] = TELESCOPE
    emojis['comet'] = COMET
    emojis['satellite'] = SATELLITE
    emojis['rocket'] = ROCKET
    emojis['saucer'] = FLYING_SAUCER
    emojis['saturn'] = SATURN
    emojis['star'] = STAR
    emojis['astronaout'] = ASTRONAOUT
    emojis['earth'] = EARTH
    emojis['alien'] = ALIEN

    return emojis
