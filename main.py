Lista_zakupow = {
    "piekarnia": ['pączek', 'bułki', 'ciasteczko'], 
    "warzywniak": ['seler', 'rukola']
}

print("Lista zakupów")
for key, values in Lista_zakupow.items():
    key_capitalize = key.capitalize()
    value_capitalize = [item.capitalize() for item in values]
    print(f"Idę do {key_capitalize}, kupuję tu następujące rzeczy: {value_capitalize} ")

value_number = sum(len(value) for value in Lista_zakupow.values())
print(f"W sumie kupuję {value_number} produktów")
