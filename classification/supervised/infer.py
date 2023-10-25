import os

from config import Config


if __name__ == '__main__':
    cfg = Config()
    
    # dataloader_train, dataloader_val = build_dataset(cfg)
    
    # model = torchvision.models.mobilenet_v3_large(pretrained=True)
    # model.classifier[3] = nn.Linear(model.classifier[3].in_features, cfg.num_classes)
    # model.to(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))

    # criterion = nn.CrossEntropyLoss()
    # optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    # for epoch in range(cfg.num_epochs):
    #     for images, labels in tqdm(dataloader_train, desc=f'[TRAIN] Epoch {epoch + 1}'):
    #         images, labels = images.to(torch.device('cuda' if torch.cuda.is_available() else 'cpu')), labels.to(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
    #         outputs = model(images)
    #         loss = criterion(outputs, labels)

    #         optimizer.zero_grad()
    #         loss.backward()
    #         optimizer.step()

    #     correct = 0
    #     total = 0
    #     with torch.no_grad():
    #         for images, labels in tqdm(dataloader_val, desc=f'[VAL] Epoch {epoch + 1}'):
    #             images, labels = images.to(torch.device('cuda' if torch.cuda.is_available() else 'cpu')), labels.to(torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
    #             outputs = model(images)
    #             _, predicted = torch.max(outputs.data, 1)
    #             total += labels.size(0)
    #             correct += (predicted == labels).sum()

    #     print(f'Accuracy of the network on the {total} validation images: {100 * correct / total}%')