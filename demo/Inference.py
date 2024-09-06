from ultralytics import YOLO
import os
import requests
def check_path_type(path):
    if os.path.isdir(path):
        return "Directory"
    elif os.path.isfile(path):
        return "File"
    else:
        return "Path does not exist"
def create_directory_if_not_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created.")
    else:
        print(f"Directory '{directory_path}' already exists.")
def inference(input_path, output_path=r'./forest-fire-detection/output', model_path='best.pt'):
    input_file_type = check_path_type(input_path)
    create_directory_if_not_exists(output_path)
    model = YOLO(model_path)
    counter = 1
    flag = False
    if input_file_type == "Directory":
        images = []
        flag = True
        for filename in os.listdir(input_path):
            image_path = os.path.join(input_path, filename)
            images.append(image_path)
        results = model(images)
    elif input_file_type == "File":
        flag = True
        results = model(input_path)
    else:
        flag = False
    if flag:
        for result in results:
            result.save(filename=f'{output_path}/result{counter}.jpg')
            counter += 1
inference(r'./forest-fire-detection/demo/input')



