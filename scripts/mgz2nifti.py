import numpy as np
import nibabel as nib
import json

# Load MGZ file
mgz_path = "output/subjects/subjectX/mri/segment.mgz"
mgz_img = nib.load(mgz_path)
mgz_array = mgz_img.get_fdata().astype(np.int32)  # Convert to integer labels

# Load LUT (Look-Up Table)
lut = json.load(open("labels.json", "r"))  # LUT stored in JSON format

# User input for the label to highlight
highlight_label = int(input("Enter the label ID you want to highlight: "))

# Initialize output grayscale image
highlighted_array = np.zeros_like(mgz_array, dtype=np.uint8)  # Single-channel grayscale

if str(highlight_label) in lut:
    color_rgb = np.array(lut[str(highlight_label)][0][:3], dtype=np.uint8)  # Extract RGB color

    # Convert RGB to grayscale intensity
    grayscale_value = int(0.2989 * color_rgb[0] + 0.5870 * color_rgb[1] + 0.1140 * color_rgb[2])

    mask = (mgz_array == highlight_label)  # Binary mask for selected label

    # Assign grayscale intensity for the highlighted region
    highlighted_array[mask] = grayscale_value  # Highlighted label

    # Assign a fixed gray value for the rest of the brain
    highlighted_array[~mask] = 100  # Mid-gray for other regions

    # Convert to NIfTI format
    highlighted_nifti = nib.Nifti1Image(highlighted_array, affine=mgz_img.affine, header=mgz_img.header)

    # Save the new highlighted NIfTI file
    nib.save(highlighted_nifti, "highlighted_brain_gray.nii.gz")
    print("Saved grayscale highlighted NIFTI image as highlighted_brain_gray.nii.gz")
else:
    print("Label ID not found in LUT.")
