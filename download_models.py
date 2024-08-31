from diffsynth import download_models


# Download models (automatically)
# `models/stable_diffusion/aingdiffusion_v12.safetensors`: [link](https://civitai.com/api/download/models/229575)
# `models/stable_diffusion/flat2DAnimerge_v45Sharp.safetensors`: [link](https://civitai.com/api/download/models/266360?type=Model&format=SafeTensor&size=pruned&fp=fp16)
# `models/AnimateDiff/mm_sd_v15_v2.ckpt`: [link](https://huggingface.co/guoyww/animatediff/resolve/main/mm_sd_v15_v2.ckpt)
# `models/ControlNet/control_v11p_sd15_lineart.pth`: [link](https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_lineart.pth)
# `models/ControlNet/control_v11f1e_sd15_tile.pth`: [link](https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11f1e_sd15_tile.pth)
# `models/Annotators/sk_model.pth`: [link](https://huggingface.co/lllyasviel/Annotators/resolve/main/sk_model.pth)
# `models/Annotators/sk_model2.pth`: [link](https://huggingface.co/lllyasviel/Annotators/resolve/main/sk_model2.pth)
# `models/textual_inversion/verybadimagenegative_v1.3.pt`: [link](https://civitai.com/api/download/models/25820?type=Model&format=PickleTensor&size=full&fp=fp16)
download_models([
    "AingDiffusion_v12",
    "Flat2DAnimerge_v45Sharp",
    "AnimateDiff_v2",
    "ControlNet_v11p_sd15_lineart",
    "ControlNet_v11f1e_sd15_tile",
    "TextualInversion_VeryBadImageNegative_v1.3"
])