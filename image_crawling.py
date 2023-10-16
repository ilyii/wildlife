from bing_image_downloader import downloader
import os

animals = [
    'Cow', 'Pig', 'Sheep', 'Goat', 'Horse', 'Donkey', 'Chicken', 'Duck', 'Turkey', 'Geese',
    'Rabbit', 'Elephant', 'Giraffe', 'Zebra', 'Lion', 'Tiger', 'Rhino', 'Hippopotamus', 'Gorilla', 'Chimpanzee',
    'Wolf', 'Fox', 'Bear', 'Deer', 'Moose', 'Elk', 'Coyote', 'Jaguar', 'Leopard', 'Cheetah', 'Hyena', 'Kangaroo',
    'Koala', 'Panda', 'Sloth', 'Toucan', 'Crocodile', 'Alligator', 'Snake', 'Lizard', 'Salmon', 'Catfish', 'Clownfish',
    'Frogs', 'Toads', 'Turtles', 'Crayfish', 'Snails', 'Otters', 'Beavers', 'Alligators', 'Crocodiles', 'Water snakes',
    'Jaguar', 'Sloth', 'Toucan', 'Monkey', 'Parrot', 'Anaconda', 'Gorilla', 'Tiger', 'Elephant', 'Orangutan', 'Chimpanzee',
    'Crocodile', 'Panther', 'Tapir', 'Capybara', 'Dolphin', 'Humpback Whale', 'Blue whale', 'Bottlenose dolphin',
    'Bowhead whale', 'Bryde\'s whale', 'Common dolphin', 'Dusky dolphin', 'False killer whale', 'Fin whale', 'Gray whale',
    'Humpback dolphin', 'Humpback whale', 'Irrawaddy dolphin', 'Orca', 'Minke whale', 'Pilot whale', 'Right whale',
    'Sei whale', 'Sperm whale', 'Jaguar', 'Sloth', 'Toucan', 'Monkey', 'Parrot', 'Anaconda', 'Gorilla', 'Tiger',
    'Elephant', 'Orangutan', 'Chimpanzee', 'Crocodile', 'Panther', 'Tapir', 'Capybara', 'Mountain goat', 'Snow leopard',
    'Alpine ibex', 'Golden eagle', 'Himalayan tahr', 'Rocky Mountain elk', 'Chamois', 'Bighorn sheep', 'Pika', 'Marmot',
    'Black bear', 'Lynx', 'Wolverine', 'Red panda', 'Bison', 'Prairie dog', 'Zebra', 'Lion', 'Giraffe', 'Cheetah',
    'Wildebeest', 'Gazelle', 'Antelope', 'Hyena', 'Warthog', 'Ostrich', 'Kangaroo', 'Fox', 'Gorilla', 'Jaguar',
    'Anaconda', 'Toucan', 'Sloth', 'Macaw', 'Monkey', 'Capybara', 'Okapi', 'Tiger', 'Orangutan', 'Poison dart frog',
    'Tapir', 'African elephant', 'Lion', 'Giraffe', 'Zebra', 'Cheetah', 'African buffalo', 'Wildebeest', 'Hippopotamus',
    'Warthog', 'Ostrich', 'Spotted hyena', 'Antelope'
]

# for animal in animals:
#     QUERY = f'{animal} (animal)'
#     downloader.download(QUERY, limit=100,  output_dir=f'D:\Database\\animals\crawled', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)

for folder in os.listdir('D:\Database\\animals\crawled'):
    if folder.endswith(' (animal)'):
        folder_name = folder[:-9]
        os.rename(f'D:\Database\\animals\crawled\\{folder}', f'D:\Database\\animals\crawled\\{folder_name}')
"""
Cow
Pig
Sheep
Goat
Horse
Donkey
Chicken
Duck
Turkey
Geese
Rabbit
Elephant
Giraffe
Zebra
Lion
Tiger
Rhino
Hippopotamus
Gorilla
Chimpanzee
Wolf
Fox
Bear
Deer
Moose
Elk
Coyote
Jaguar
Leopard
Cheetah
Hyena
Kangaroo
Koala
Panda
Sloth
Toucan
Crocodile
Alligator
Snake
Lizard
Salmon
Catfish
Clownfish
Frogs
Toads
Turtles
Crayfish
Snails
Otters
Beavers
Alligators
Crocodiles
Water snakes
Jaguar
Sloth
Toucan
Monkey
Parrot
Anaconda
Gorilla
Tiger
Elephant
Orangutan
Chimpanzee
Crocodile
Panther
Tapir
Capybara
Dolphin
Humpback Whale
Blue whale
Bottlenose dolphin
Bowhead whale
Bryde's whale
Common dolphin
Dusky dolphin
False killer whale
Fin whale
Gray whale
Humpback dolphin
Humpback whale
Irrawaddy dolphin
Orca
Minke whale
Pilot whale
Right whale
Sei whale
Sperm whale
Jaguar
Sloth
Toucan
Monkey
Parrot
Anaconda
Gorilla
Tiger
Elephant
Orangutan
Chimpanzee
Crocodile
Panther
Tapir
Capybara
Mountain goat
Snow leopard
Alpine ibex
Golden eagle
Himalayan tahr
Rocky Mountain elk
Chamois
Bighorn sheep
Pika
Marmot
Black bear
Lynx
Wolverine
Red panda
Bison
Prairie dog
Zebra
Lion
Giraffe
Cheetah
Wildebeest
Gazelle
Antelope
Hyena
Warthog
Ostrich
Kangaroo
Fox
Gorilla
Jaguar
Anaconda
Toucan
Sloth
Macaw
Monkey
Capybara
Okapi
Tiger
Orangutan
Poison dart frog
Tapir
African elephant
Lion
Giraffe
Zebra
Cheetah
African buffalo
Wildebeest
Hippopotamus
Warthog
Ostrich
Spotted hyena
Antelope
"""