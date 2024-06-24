from moviepy.editor import VideoFileClip
import os

def convert_video_to_9_16(input_path, output_path, crop_position="center"):
    clip = VideoFileClip(input_path)
    
    # Get original dimensions
    original_width, original_height = clip.size
    aspect_ratio = original_width / original_height

    # Calculate new dimensions for 9:16 aspect ratio
    new_width = original_height * (9 / 16)
    new_height = original_height

    # Calculate cropping dimensions
    if crop_position == "center":
        x_center = original_width / 2
        x1 = x_center - new_width / 2
        x2 = x_center + new_width / 2
        y1, y2 = 0, original_height
    elif crop_position == "left":
        x1, x2 = 0, new_width
        y1, y2 = 0, original_height
    elif crop_position == "right":
        x1, x2 = original_width - new_width, original_width
        y1, y2 = 0, original_height
    else:
        raise ValueError("Invalid crop position. Choose from 'center', 'left', 'right'.")

    # Crop the clip
    cropped_clip = clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)

    # Resize to 9:16 aspect ratio
    resized_clip = cropped_clip.resize(height=original_height)

    # Write the result to a file with compatible settings
    resized_clip.write_videofile(output_path, codec='libx264', fps=60, audio_codec='aac')

# Usage example
input_folder = "clips"
output_folder = "output"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Process each file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith((".mp4", ".mov", ".avi")):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"9_16_{filename}")
        
        # Example usage: crop_position can be "center", "left", or "right"
        convert_video_to_9_16(input_path, output_path, crop_position="center")
