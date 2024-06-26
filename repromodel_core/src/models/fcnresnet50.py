# wrapped model from torchvision library. Corresponding License stated in the ReproModel repository.
import torch
import torch.nn as nn
import torchvision.models.segmentation as models
import unittest

# Assuming the enforce_types_and_ranges and tag decorators are defined in decorators.py
from ..decorators import enforce_types_and_ranges, tag  # Adjust the import path accordingly

#standardize the output for torchvision models
from ..utils import extract_output

@tag(task=["segmentation"], subtask=["binary", "multi-class"], modality=["images"], submodality=["RGB"])
class FCNResNet50(nn.Module):
    @enforce_types_and_ranges({
        'num_classes': {'type': int, 'default': 21, 'range': (1, 10000)},
        'pretrained': {'type': bool, 'default': False}
    })
    def __init__(self, num_classes=21, pretrained=False):
        super(FCNResNet50, self).__init__()
        self.num_classes = num_classes
        self.pretrained = pretrained

        # Load the FCN ResNet50 model with the specified parameters
        self.fcn = models.fcn_resnet50(pretrained=self.pretrained, num_classes=self.num_classes)

    def forward(self, x):
        return extract_output(self.fcn(x))

class _TestFCNResNet50(unittest.TestCase):
    def test_fcn_resnet50_initialization(self):
        # Test with default parameters
        model = FCNResNet50()
        self.assertIsInstance(model, FCNResNet50, "Model is not an instance of FCNResNet50")
        self.assertEqual(model.num_classes, 21, "Default num_classes is not 21")
        self.assertFalse(model.pretrained, "Default pretrained is not False")

        # Test with custom parameters
        model = FCNResNet50(num_classes=10, pretrained=False)
        self.assertEqual(model.num_classes, 10, "Custom num_classes is not 10")
        self.assertFalse(model.pretrained, "Custom pretrained is not False")

        # Test with pretrained model
        model = FCNResNet50(num_classes=21, pretrained=True)
        self.assertEqual(model.num_classes, 21, "Pretrained num_classes should be 21")
        self.assertTrue(model.pretrained, "Pretrained parameter should be True")

    def test_fcn_resnet50_forward_pass(self):
        model = FCNResNet50(num_classes=10, pretrained=False)
        input_tensor = torch.randn(2, 3, 224, 224)  # Example input tensor for FCNResNet50 with batch size 2
        output = model(input_tensor)
        self.assertEqual(output.shape, (2, 10, 224, 224), f"Output shape is not correct: {output.shape}")

    def test_fcn_resnet50_tags(self):
        # Check if the class has the correct tags
        model = FCNResNet50()
        self.assertEqual(model.task, ["segmentation"], "Task tag is incorrect")
        self.assertEqual(model.subtask, ["binary", "multi-class"], "Subtask tag is incorrect")
        self.assertEqual(model.modality, ["images"], "Modality tag is incorrect")
        self.assertEqual(model.submodality, ["RGB"], "Submodality tag is incorrect")

if __name__ == "__main__":
    unittest.main()