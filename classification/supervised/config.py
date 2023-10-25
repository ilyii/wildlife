import os

class Config:
    # Seed
    seed = 1337
    
    # Data
    datapath = 'D:\Database\\animals\dataset' # Supervised
    validation_split = 0.2
    classes = os.listdir(datapath)
    num_classes = len(classes)
    # Params
    img_size = 224
    batch_size = 32
    num_epochs = 100


