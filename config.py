

class Config:
    # Seed
    seed = 1337
    # Data
    datapath = 'D:\Database\\animals\images' # Unsupervised
    # datapath = 'D:\Database\\animals\data\classified' # Supervised
    labelfile = "D:\Database\\animals\\name of the animals.txt"
    validation_split = 0.2

    classes = ["antelope","badger","bat","bear","bee","beetle","bison","boar","butterfly","cat",
               "caterpillar","chimpanzee","cockroach","cow","coyote","crab","crow","deer","dog","dolphin",
               "donkey","dragonfly","duck","eagle","elephant","flamingo","fly","fox","goat","goldfish",
               "goose","gorilla","grasshopper","hamster","hare","hedgehog","hippopotamus","hornbill","horse","hummingbird",
               "hyena","jellyfish","kangaroo","koala","ladybugs","leopard","lion","lizard","lobster","mosquito","moth","mouse",
               "octopus","okapi","orangutan","otter","owl","ox","oyster","panda","parrot","pelecaniformes",
               "penguin","pig","pigeon","porcupine","possum","raccoon","rat","reindeer","rhinoceros","sandpiper",
               "seahorse","seal","shark","sheep","snake","sparrow","squid","squirrel","starfish","swan",
               "tiger","turkey","turtle","whale","wolf","wombat","woodpecker","zebra"]
    
    num_classes = len(classes)
    # Params
    img_size = 224
    batch_size = 32


