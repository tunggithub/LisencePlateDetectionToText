# Lisence Plate Detection To Text
recognize the license plate in the photo and output to a text file



## How it work

input: 




  ![test](https://user-images.githubusercontent.com/88756362/131938219-571553fe-0186-4e69-b8fb-a9046edca73d.jpg)

### Step 1: license plate recognition and draw bounding box using yolo tiny v4 with my dataset


![image](https://user-images.githubusercontent.com/88756362/131938414-6e387c52-e06f-4218-aacb-e75ad7b1b37a.png)

### Step2: crop and focus on the bouding box (license plate) 


![image](https://user-images.githubusercontent.com/88756362/131938661-e0117235-e4ae-4f3d-8bfa-be584c3eadc8.png)


### Step3: detect infomation of license plate using EasyOCR:

![image](https://user-images.githubusercontent.com/88756362/131939182-9cbd95d3-c791-4ccf-8e35-ec295547df42.png)


### it also works with photos with multiple license plates

![image](https://user-images.githubusercontent.com/88756362/131939389-23e05e66-adab-451e-96b7-58c9382dc49b.png)

