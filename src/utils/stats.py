class Stats:

    names = 'strength', 'dexterity', 'wisdom', 'intelligence', 'charisma', 'constitution'

    def __init__(self, **options):
        for stat in stats.names:
            setattr(self, stat, options[stat])

    def __add__(self, other):
        assert isinstance(other, stats)
        return ({
            item: getattr(self, item) + getattr(other, item)
            for item in stats.names
        })

