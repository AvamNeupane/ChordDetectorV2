# 🎸 Guitar Chord Detector App

A real-time chord recognition app that detects the guitar chord you're playing using computer vision and keypoint detection.


## 🔍 Model: Roboflow 3.0 Keypoint Detection

I trained the model using Roboflow’s **Keypoint Detection** architecture.

![Roboflow Model Interface](insert-image-url-or-path-here)

This model was designed to track individual finger positions and map them to specific chord shapes.


## 🖼️ Training Dataset

I used a small dataset of **10–15 labelled images**, marking key points on each finger across different chord shapes (e.g. A minor, G major). This allows the model to understand what each chord visually looks like from a top-down perspective.

![Labeled Keypoints on Fingers](insert-image-url-or-path-here)


## 🖥️ Local Deployment via Docker

Once trained, the custom model was deployed locally using Docker. The app launches the webcam and processes the live video feed to predict in real time which chord is being played.

![Webcam Chord Detection Demo](insert-image-url-or-path-here)


