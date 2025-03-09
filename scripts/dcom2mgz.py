import os
import numpy as np
import pydicom
import nibabel as nib
import argparse

def dicom_to_mgz(dicom_dir, output_mgz):
    # Load all DICOM files from the directory
    dicom_files = [os.path.join(dicom_dir, f) for f in os.listdir(dicom_dir) if f.endswith(".dcm")]
    
    if not dicom_files:
        print("No DICOM files found in the directory.")
        return

    # Read DICOM slices and sort them by slice location
    dicom_slices = [pydicom.dcmread(f) for f in dicom_files]
    dicom_slices.sort(key=lambda x: float(x.ImagePositionPatient[2]))  # Sort by Z-axis
    
    # Extract pixel data and convert to a 3D numpy array
    image_data = np.stack([s.pixel_array for s in dicom_slices], axis=-1)

    # Get voxel spacing from DICOM metadata
    voxel_spacing = list(map(float, dicom_slices[0].PixelSpacing)) + [float(dicom_slices[0].SliceThickness)]
    
    # Convert to a NIfTI image
    affine = np.eye(4)  # Identity matrix (modify if needed)
    nifti_img = nib.Nifti1Image(image_data, affine)
    
    # Save as MGZ format
    nib.save(nifti_img, output_mgz)
    print(f"Converted {len(dicom_files)} DICOM slices to {output_mgz}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert DICOM series to MGZ format")
    parser.add_argument("dicom_dir", type=str, help="Path to directory containing DICOM files")
    parser.add_argument("output_mgz", type=str, help="Output MGZ file path")
    args = parser.parse_args()

    dicom_to_mgz(args.dicom_dir, args.output_mgz)
