import cv2
import os
import argparse
from pathlib import Path

def extract_frames(video_path, frames_folder, fps):
    """
    Extracts frames from a video file and saves them as images in a new subfolder within the frames folder.
    
    Args:
        video_path (str): Path to the input video file.
        frames_folder (str): Path to the frames folder where the new subfolder will be created.
        fps (int): Number of frames to extract per second.
    """
    # Create a new subfolder within the frames folder
    batch_num = 1
    while True:
        output_folder = Path(frames_folder) / f"batch_{batch_num}"
        if not output_folder.exists():
            output_folder.mkdir()
            break
        batch_num += 1
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Get the frame rate and the total number of frames
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Calculate the step size based on the desired frames per second
    step_size = int(frame_rate / fps)
    
    # Initialize the frame counter
    frame_count = 0
    
    # Loop through the frames and save them as images
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame_count % step_size == 0:
            frame_path = output_folder / f"frame_{frame_count // step_size}.jpg"
            cv2.imwrite(str(frame_path), frame)
        
        frame_count += 1
    
    # Release the video capture object
    cap.release()
    
    print(f"Extracted {frame_count // step_size} frames from the video to {output_folder}")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Extract frames from a video file.")
    parser.add_argument("video_path", help="Path to the input video file.")
    parser.add_argument("fps", type=int, help="Number of frames to extract per second.")
    args = parser.parse_args()
    
    # Set the paths
    project_root = Path(__file__).parent.parent
    data_folder = project_root / "data"
    frames_folder = data_folder / "frames"
    
    # Call the frame extraction function
    extract_frames(data_folder / args.video_path, frames_folder, args.fps)