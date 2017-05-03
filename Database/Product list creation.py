## Initialise Global Variable for the list and create an empty list
global items
items = []

## Enter While loop
while 1:
## Collect Text input. This will be changed to the scanned input
    text = raw_input('Enter Value: ')

## Fail safe: if there are no items in the list add an item to the list
    if len(items)==0:
        items = ['123456789']

## Check through all values in the list
    for item in items:
        if text == item:
            items.remove(text) ## Remove the item if it exits already
            break
        elif (text != item and item == items[len(items)-1]):
## Add the value if it reaches the end of the list and has not found the value
            items = items + [text]

## Remove failsafe value before continuing
        if item == '123456789':
            items.remove(item)

## Display the list
    print items

