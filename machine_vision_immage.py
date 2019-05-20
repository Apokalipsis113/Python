import pandas as pd
from imageai.Detection import ObjectDetection
def machine_vision_immage(filename, savenewfile=False, sensitivity=20, newfilepath="result.jpg"):
    path = 'resnet50_coco_best_v2.0.1.h5'
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(path)
    detector.loadModel()
    if savenewfile is True:
        return pd.DataFrame(detector.detectCustomObjectsFromImage(input_image=filename, output_image_path=newfilepath, minimum_percentage_probability=sensitivity, display_object_name=True, display_percentage_probability=False))
    else:
        return pd.DataFrame(detector.detectCustomObjectsFromImage(input_image=filename, minimum_percentage_probability=sensitivity, display_object_name=True, display_percentage_probability=False))