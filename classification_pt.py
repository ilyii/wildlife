from tqdm import tqdm

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split
import torchvision
import torchvision.transforms as transforms

from config import Config


def build_dataset(cfg):
    transform = transforms.Compose([
        transforms.Resize((cfg.img_size, cfg.img_size)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomVerticalFlip(),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2),
        transforms.RandomRotation(20),
        transforms.RandomAffine(degrees=0, translate=(0.2, 0.2)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    dataset = torchvision.datasets.ImageFolder(root=cfg.datapath, transform=transform)
    dataset_size = len(dataset)
    train_size = int((1-cfg.validation_split) * dataset_size)
    val_size = dataset_size - train_size

    dataset_train, dataset_val = random_split(dataset, [train_size, val_size])

    dataloader_train = DataLoader(dataset_train, batch_size=cfg.batch_size, shuffle=True)
    dataloader_val = DataLoader(dataset_val, batch_size=cfg.batch_size, shuffle=False)

    return dataloader_train, dataloader_val


if __name__ == '__main__':
    cfg = Config()
    dataloader_train, dataloader_val = build_dataset(cfg)
    
    model = torchvision.models.mobilenet_v3_large(pretrained=True)
    model.classifier[3] = nn.Linear(model.classifier[3].in_features, cfg.num_classes)
    model.to(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(10):
        for images, labels in tqdm(dataloader_train, desc=f'[TRAIN] Epoch {epoch + 1}'):
            images, labels = images.to(torch.device('cuda' if torch.cuda.is_available() else 'cpu')), labels.to(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
            outputs = model(images)
            loss = criterion(outputs, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        correct = 0
        total = 0
        with torch.no_grad():
            for images, labels in tqdm(dataloader_val, desc=f'[VAL] Epoch {epoch + 1}'):
                images, labels = images.to(torch.device('cuda' if torch.cuda.is_available() else 'cpu')), labels.to(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
                outputs = model(images)
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        print('Epoch [{}/10], Loss: {:.4f}, Accuracy: {:.2f}%'.format(epoch + 1, loss.item(), 100 * correct / total))

    torch.save(model.state_dict(), 'mobilenetv3_large_100_224.pt')
