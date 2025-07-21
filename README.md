# 🎸 Guitar Chord Detector App

A real-time chord recognition app that detects the guitar chord you're playing using computer vision and keypoint detection.

<img width="1320" height="700" alt="Image" src="https://github.com/user-attachments/assets/3ab8de1e-a82e-462a-9b37-bad59e8f953d" />


## 🖼️ Training Dataset

I used a small dataset of **10–15 labelled images**, marking key points on each finger across different chord shapes (e.g. A minor, G major). This allows the model to understand what each chord visually looks like from a top-down perspective.

<img width="1320" height="700" alt="Image" src="https://github.com/user-attachments/assets/10b6994a-c98c-4c45-9236-a87bb39d8486" />


## 🔍 Model: Roboflow 3.0 Keypoint Detection

I then trained the model using Roboflow’s **Keypoint Detection** architecture.

<img width="1320" height="700" alt="Image" src="https://github.com/user-attachments/assets/078e4f78-ddf2-4dad-befc-104028469f7f" />

This model was designed to track individual finger positions and map them to specific chord shapes.


## 🖥️ Local Deployment via Docker

Once trained, the custom model was deployed locally using Docker. The app launches the webcam and processes the live video feed to predict in real time which chord is being played.

![Webcam Chord Detection Demo](insert-image-url-or-path-here)


