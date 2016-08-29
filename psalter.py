from bible.bible import TomlBible
from datetime import datetime,timedelta

class Psalter(object):
    def __init__(self):
        self._bible = TomlBible()

    def get_psalm(self, number):
        return self._bible["Psalm %d" % int(number)]

def cycle_psalms_weekly(psalmlist, batch_size=1, weekday=None, start_day = 6):
    """
    Get a chunck of psalms for a day from a list. Cycles based on the current
    weekday. The cycle resets on start_day

    @type psalmlist: List
    @param psalmlist: A list of psalms.
    @type batch_size: integer
    @param batch_size: The number of psalms to include in a batch
    @type weekday: integer
    @param weekday: The day of the week to produce output for. If this is None
        then use today.
    @type start_day: integer
    @param start_day: The day to restart the cycle on.
    """
    if weekday is None:
        today = datetime.today().weekday()
    else:
        today = weekday.weekday()
    if today is start_day:
        today = 0
    else:
        today = today%start_day

    start_psalm = ((today*batch_size)%(len(psalmlist)))
    end_psalm = start_psalm + batch_size
    print today, start_psalm, end_psalm
    if end_psalm > len(psalmlist):
        return psalmlist[start_psalm:] + psalmlist[:(end_psalm-len(psalmlist))]
    else:
        return psalmlist[start_psalm:end_psalm]

if __name__ == "__main__":
    base = datetime.today()
    date_list = [base + timedelta(days=x) for x in range(0,11)]
    for day in date_list:
        print day
        print cycle_psalms_weekly([121,134],1, day)
    print Psalter().get_psalm(3)

