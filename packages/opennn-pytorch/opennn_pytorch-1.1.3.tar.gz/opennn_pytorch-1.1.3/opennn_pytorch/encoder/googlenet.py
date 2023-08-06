import torch
from torch import nn


class ConvBlock(nn.Module):
    def __init__(self, inc, outc, **kwargs):
        super().__init__()
        self.conv = nn.Conv2d(inc, outc, bias=False, **kwargs)
        self.bn = nn.BatchNorm2d(outc, eps=0.001)
        self.relu = nn.ReLU()

    def forward(self, x):
        return self.relu(self.bn(self.conv(x)))


class InceptionBlock(nn.Module):
    def __init__(self, inc, c1x1, cr3x3, c3x3, cr5x5, c5x5, pool):
        super().__init__()
        self.branch1 = ConvBlock(inc, c1x1, kernel_size=(1, 1))
        self.branch2 = nn.Sequential(
            ConvBlock(inc, cr3x3, kernel_size=(1, 1)),
            ConvBlock(cr3x3, c3x3, kernel_size=(3, 3), padding=(1, 1))
        )
        self.branch3 = nn.Sequential(
            ConvBlock(inc, cr5x5, kernel_size=(1, 1)),
            ConvBlock(cr5x5, c5x5, kernel_size=(5, 5), padding=(2, 2))
        )
        self.branch4 = nn.Sequential(
            nn.MaxPool2d(kernel_size=3, stride=1, padding=1),
            ConvBlock(inc, pool, kernel_size=(1, 1))
        )

    def forward(self, x):
        br1 = self.branch1(x)
        br2 = self.branch2(x)
        br3 = self.branch3(x)
        br4 = self.branch4(x)
        cat_br = torch.cat((br1, br2, br3, br4), dim=1)
        return cat_br


class GoogleNet(nn.Module):
    def __init__(self, inc):
        super().__init__()
        self.features = 1024

        self.conv1 = ConvBlock(inc,
                               64,
                               kernel_size=(7, 7),
                               stride=(2, 2),
                               padding=(3, 3))
        self.maxpool1 = nn.MaxPool2d(kernel_size=3, stride=2)
        self.conv2 = ConvBlock(64, 64, kernel_size=(1, 1))
        self.conv3 = ConvBlock(64, 192, kernel_size=(3, 3), padding=(1, 1))
        self.maxpool2 = nn.MaxPool2d(kernel_size=3, stride=2)

        self.inception3a = InceptionBlock(192, 64, 96, 128, 16, 32, 32)
        self.inception3b = InceptionBlock(256, 128, 128, 192, 32, 96, 64)
        self.maxpool3 = nn.MaxPool2d(kernel_size=3, stride=2)

        self.inception4a = InceptionBlock(480, 192, 96, 208, 16, 48, 64)
        self.inception4b = InceptionBlock(512, 160, 112, 224, 24, 64, 64)
        self.inception4c = InceptionBlock(512, 128, 128, 256, 24, 64, 64)
        self.inception4d = InceptionBlock(512, 112, 144, 288, 32, 64, 64)
        self.inception4e = InceptionBlock(528, 256, 160, 320, 32, 128, 128)
        self.maxpool4 = nn.MaxPool2d(kernel_size=3, stride=2)

        self.inception5a = InceptionBlock(832, 256, 160, 320, 32, 128, 128)
        self.inception5b = InceptionBlock(832, 384, 192, 384, 48, 128, 128)

        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))

    def forward(self, x):
        pr = self.maxpool2(self.conv3(
            self.conv2(self.maxpool1(self.conv1(x)))))
        inc3 = self.maxpool3(self.inception3b(self.inception3a(pr)))
        inc4 = self.maxpool4(self.inception4e(self.inception4d(
            self.inception4c((self.inception4b(self.inception4a(inc3)))))))
        inc5 = self.avgpool(self.inception5b(self.inception5a(inc4)))
        return inc5

    def out_features(self):
        return self.features
