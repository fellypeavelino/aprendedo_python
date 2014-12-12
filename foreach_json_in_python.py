continents = {
    'africa': 'Africa',
    'europe': 'Europe',
    'north-america': 'North America'
}

# without keys
for continent in continents.values():
    print (continent);
print('\n');
# with keys
for (slug, title) in continents.items():
    print (slug, title)
