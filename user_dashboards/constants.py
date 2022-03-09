from BI.utilities import RangeDict

PHONE_NUMBER_VALIDATION_MESSAGE = "Phone number must be entered in the format: '+987654321000'. Up to 15 digits allowed."
GENERAL_DATETIME_FORMAT = '%b %d, %Y, %I:%M%p'
GENERAL_DATE = '%b %d, %Y'
GENERAL_TIME = '%I:%M%p'

ALARM_COLOR = RangeDict({
    range(-999, 0): 'black',
    range(2): 'red',
    range(2,5): 'blue', #2-4
    range(5,999): 'green', #5---
})