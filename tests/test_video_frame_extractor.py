# tests/test_video_frame_extractor.py

import os
import shutil
import unittest

from src.video_frame_extractor import extract_frames

class TestVideoFrameExtractor(unittest.TestCase):

    def test_extract_frames(self):
        video_path = "data/input_video.mp4"
        output_dir = "data/test_frames/"
        
        # Ensure a clean test directory
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)
        
        # Extract frames at 1 frame per second
        extract_frames(video_path, output_dir, fps=1)
        
        # Check if frames are extracted
        self.assertTrue(os.path.exists(output_dir))
        self.assertTrue(len(os.listdir(output_dir)) > 0)
        print("Test passed: Frames extracted successfully.")

if __name__ == "__main__":
    unittest.main()
