from roboflow import Roboflow
rf = Roboflow(api_key="Ib5yjMqowwu83qrBaC4C")
project = rf.workspace("teste-maiic").project("fire-1-yeank")
version = project.version(1)
dataset = version.download("yolov8")
