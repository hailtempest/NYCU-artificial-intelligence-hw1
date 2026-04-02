This dataset is provided by a collaborative pig farm for course experimental purposes only. Unauthorized use, reproduction, or distribution for non-VoIP Lab or non-academic purposes is strictly prohibited.

1. Dataset Overview
Data Type: RGB Images (.jpg) and Object Detection Labels (.txt in YOLO format).

Total Samples: 1,100 images.

Original: 1,000 real-world surveillance frames.

Augmented: 100 synthetic images generated via Stable Diffusion (img2img).

Unused Raw Data: An additional extracted frames that were not utilized for training or validation are included in this project for reproducibility and documentation purposes.

Source: Authentic surveillance footage from a partner pig farm in Taiwan (distinct from previous research datasets).

2. Data Collection & Conditions
Environment: Controlled farrowing pens containing a sow and her piglets.

Lighting Variations: Footage was extracted from three distinct periods (Morning, Noon, and Afternoon) to ensure model robustness against varying illumination.

Sampling Strategy: To minimize temporal redundancy, frames were sampled every 2 seconds from 3 hours of raw video.

Hardware: Fixed-angle industrial IP cameras mounted above the farrowing crates.

3. Annotation & Processing
Software Tools: * Annotation: LabelImg (Manual bounding box labeling).

Augmentation: Stable Diffusion (Used for class balancing and environmental enrichment).

Libraries: OpenCV, scikit-image, scikit-learn.

Label Format: YOLO standard [class_index x_center y_center width height].

Class Mapping: 
0: Sit 

1: Stand 

2: Lie 

Annotation Protocol: Tight bounding boxes were drawn around the sow's main body, excluding piglets and external crate structures to minimize background noise.