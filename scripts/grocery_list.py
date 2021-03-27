import reminders

grocery_list = [
    'turkey'
    , 'chicken'
    , 'fish'
    , 'eggs'
    , 'carrots'
    , 'broccoli'
    , 'asparagus'
    , 'cauliflower'
    , 'spinach'
    , 'bananas'
    , 'berries'
    , 'almond milk'
    , 'yogurt'
    , 'shredded cheese'
    , 'string cheese'
    , 'peanut butter'
    , 'rice'
    , 'yukon potatoes'
    , 'oats'
    , 'bread'
]

# Creates reminder list if not exist
if 'Grocery' not in reminders.get_all_calendars():
    new_calendar = reminders.Calendar()
    new_calendar.title = 'Grocery'
    new_calendar.save()

# Adds each grocery item to reminder list
for item in grocery_list:
    for calendar in reminders.get_all_calendars():
        if calendar.title == 'Grocery':
            r = reminders.Reminder(calendar)
            r.title = item
            r.save()
            break
