import os
import os.path as osp
import sys

from bing_image_downloader import downloader

ANIMALS = [
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

def crawl(animals: List, output_dir:str):
    '''
    Search and download images

    Args:
        animals (List): List of animals to search for
        output_dir (str): Path to output directory
    '''
    for animal in animals:
        QUERY = f'{animal} (animal)'
        downloader.download(QUERY, limit=100,  output_dir=f'D:\Database\\animals\crawled', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)

    # Remove (animal) from folder name
    for folder in os.listdir(output_dir):
        if folder.endswith(' (animal)'):
            folder_name = folder[:-9]
            os.rename(osp.join(output_dir, folder), osp.join(output_dir, folder_name))


def create_classlist(animals: List, output_dir:str):
    '''
    Create a classlist file from a list of animals

    Args:
        animals (List): List of animals to search for
        output_dir (str): Path to output directory
    '''
    with open(osp.join(output_dir, 'classes.txt'), 'w+') as f:
        for animal in animals:
            f.write(f'{animal}\n')


if __name__ == '__main__':
    '''
    This script is used to crawl for images using the Bing Image Downloader. It seperates the images into folders based on the class name and creates a classlist file.
    '''

    output_dir = sys.argv[1]
    if len(sys.argv) > 2:
        ANIMALS = sys.argv[2][1:-1].split(',') # [animal1, animal2, ...]
    crawl(ANIMALS, output_dir)
    create_classlist(ANIMALS, output_dir)