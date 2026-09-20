from tifffile import imread
import matplotlib.pyplot as plt

image = imread("data/set1/control/control_1_dapi.tif")

print("Image shape:", image.shape)

for i in range(image.shape[2]):
    print(
        "Channel", i,
        "minimum:", image[:, :, i].min(),
        "maximum:", image[:, :, i].max()
    )

fig, axes = plt.subplots(1, 4, figsize=(12, 3))

for i in range(4):
    axes[i].imshow(image[:, :, i], cmap="gray")
    axes[i].set_title(f"Channel {i}")
    axes[i].axis("off")

plt.tight_layout()
plt.savefig(
    "figures/control_1_dapi_channels.png",
    dpi=150,
    bbox_inches="tight"
)

print("Channel preview saved.")
