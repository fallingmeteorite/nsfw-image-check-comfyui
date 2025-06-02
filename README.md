# nsfw-image-check-comfyui Manual

## Installation

```
git clone https://github.com/fallingmeteorite/nsfw-image-check-comfyui.git
cd nsfw-image-check-comfyui
pip install -r requirements.txt

```

or

```
comfy node registry-install nsfw-image-check-comfyui
```

## Node introduction

Node name:Nsfw Image Check Node

Block NSFW images and output warning images

![img0.png](img0.png)

Node name:Nsfw area coverage

![img2.png](img1.png)

Interface

`image_requires_in` is IMAGE

`image_requires_out` is IMAGE

`custom_image_out` is IMAGE

`corresponding_filter_entries` is string to inform triggered filters during automatic checks

`image_requires_in`: Input diagram. It is usually followed by VAE Decode or load image

`image_requires_out`: Used to output pictures, filter by outputting the original image or output the warning image

`custom_image_out` Custom images are used to replace the images that trigger detection, which is unnecessary.

`corresponding_filter_entries`: Used to tell the triggered feature filtering

## Use

The model is pre-downloaded, and the plug-in does not need to be connected to the Internet

`enabled_check`: Whether to enable detection, True by default

`Suffix threshold`: Trigger the filter threshold, the lower the filter, the stronger the effect, the range (0~1), the
default is 0.5

`Suffix enabled`: Whether to enable this type of detection during testing (effective when `filter_choose` is set to `auto`).

`filter_choose`: The enabled filtering mode is a single feature except auto, and it is recommended to select `auto`

The image you want to replace is placed in the `img` folder with the suffix .jpg, and the file name needs to be changed
to a number

## Refer

Plugins are used:https://github.com/deepghs/imgutils

However, because the plugin disables model downloading, etc., this library is not installed, but part of the modified
code is directly stored in the plugin folder



