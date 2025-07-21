from inference import InferencePipeline
import cv2

def my_sink(result, video_frame):
    if result.get("output_image"): 
        cv2.imshow("Workflow Image", result["output_image"].numpy_image)
        cv2.waitKey(1)
    print(result) 


pipeline = InferencePipeline.init_with_workflow(
    api_key="dl4ZXP4FuwOFN02vxgeJ",
    workspace_name="avam-yoi6b",
    workflow_id="custom-workflow",
    video_reference=0, # Path to video (webcam=0)
    on_prediction=my_sink
)
pipeline.start() 
pipeline.join() 
