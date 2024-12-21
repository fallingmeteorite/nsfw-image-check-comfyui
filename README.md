# nsfw-image-check-comfyui Manual

## Installation
In the custom_nodes directory
```
git clone https://github.com/fallingmeteorite/nsfw-image-check-comfyui.git
cd nsfw-image-check-comfyui
pip install -r requirements.txt
```

## Node introduction
Node name:Nsfw Image Check Node

Block NSFW image output

![img.png](img.png)
Input (image_requires_in) is IMAGE

Output (image_requires_out) is IMAGE

Output (Colespontin_Fürth_Entris) is Sterling


image_requires_in: Input diagram. It is usually followed by VAE Decode or load image

image_requires_out: Used to output pictures, filter by outputting the original image or output the warning image

corresponding_filter_entries: Used to tell the triggered feature filtering


## Use
The model is pre-downloaded, and the plug-in does not need to be connected to the Internet

enabled_check: Whether to enable detection, True by default

Suffix threshold: trigger the filter threshold, the lower the filter, the stronger the effect, the range (0~1), the default is 0.5

Suffix enabled: whether to enable the detection of the feature (takes effect when the filter_choose is auto)

filter_choose: The enabled filtering mode is a single feature except auto, and it is recommended to select auto

The image you want to replace is placed in the img folder with the suffix .jpg, and the file life needs to be changed to a number

## Refer
Plugins are used:https://github.com/deepghs/imgutils

However, because the plugin disables model downloading, etc., this library is not installed, but part of the modified code is directly stored in the plugin folder



