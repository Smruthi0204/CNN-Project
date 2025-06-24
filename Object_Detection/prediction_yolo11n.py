if __name__ == '__main__':

    from ultralytics import YOLO
    model = YOLO("C:\\Users\\smrut\\OneDrive\\Desktop\\SEM Y\\Internship\\project1 BC\\object_detection\\runs\\detect\\train4\\weights\\best.pt")  
    results = model.predict(source="C:\\Users\\smrut\\OneDrive\\Desktop\\SEM Y\\Internship\\project1 BC\\object_detection\\Pedestrian and Auto dataset\\test\\images", save=True)
