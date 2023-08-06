# PyCOCOSIoU Extension

This is a fork from [cocoapi repository](https://github.com/cocodataset/cocoapi). More specifically, it is a fork of the Python API provided by the original authors. 

It allows different box criteria for object detection model evaluation. Here is the list of the available criteria:

- Intersection over Union.
- Scaled Intersection over Union [paper](url_siou).
- Normalized Wasserstein Distance [paper](https://arxiv.org/abs/2110.13389).
- Alpha-Intersection over Union [paper](https://openreview.net/forum?id=rbdKZJxDWWx). (TO COME)

## Employ different criterion

Explain how to use the new API 

Add possibility to change params of criteria

## Installation notes

Simply run the following command, pip will install dependancies and the package. Only `numpy` must be installed beforehand.
```
pip install git+https://github.com/pierlj/extended_pycocotools.git
```
