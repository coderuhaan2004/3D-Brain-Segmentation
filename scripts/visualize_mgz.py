import nibabel as nib
import numpy as np
import pyvista as pv
from skimage import measure
import json

# Load MGZ segmentation
mgz_img = nib.load("output/subjects/subjectX/mri/segment.mgz")
seg_data = mgz_img.get_fdata().astype(np.int16)

# Load LUT (label -> RGBA or label -> color)
lut = json.load(open("labels.json", "r"))

# **User Input: Choose a Label ID to Highlight**
highlight_label = int(input("Enter the label ID you want to highlight: "))

# Create a PyVista Plotter
plotter = pv.Plotter()

# **Process Highlighted Label First**
if str(highlight_label) in lut:
    color_rgb = lut[str(highlight_label)][0][:3]  # Get RGB color
    color_rgb = [c / 255.0 for c in color_rgb]  # Normalize to [0,1]
    
    # Create a binary mask
    mask = (seg_data == highlight_label)

    if np.sum(mask) > 0:
        verts, faces, _, _ = measure.marching_cubes(
            mask, level=0.5, spacing=mgz_img.header.get_zooms()
        )
        faces = np.c_[np.full(len(faces), 3), faces]  # Convert to pyvista format

        mesh = pv.PolyData(verts, faces)
        plotter.add_mesh(mesh, color=color_rgb, name=f"Label_{highlight_label}")
    else:
        print(f"Label {highlight_label} not found in MGZ data.")

# **Process the Rest of the Brain with Gray Color & Lower Opacity**
mask_brain = (seg_data > 0)  # Mask for all non-zero areas
mask_brain &= (seg_data != highlight_label)  # Exclude the highlighted label

if np.sum(mask_brain) > 0:
    verts, faces, _, _ = measure.marching_cubes(
        mask_brain, level=0.5, spacing=mgz_img.header.get_zooms()
    )
    faces = np.c_[np.full(len(faces), 3), faces]

    mesh_brain = pv.PolyData(verts, faces)
    plotter.add_mesh(mesh_brain, color=[0.5, 0.5, 0.5], opacity=0.3, name="Brain")

# Show the 3D plot
plotter.show()
