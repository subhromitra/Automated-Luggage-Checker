# Automated-Luggage-Checker

## Problem Statement :-
**Detecting various objects from X-ray images of bags.**

Airports & railway stations around the world, mostly check luggage contents manually. This is done by viewing X-ray images of the bag which reveal its contents. This project aims at automating this exact process , using deep learning based object detectors. 
    Here I have used YOLOv3 because of its real time speed.
    
## Database used :-

I have used images from **GRIMA database**. Further info about this database can be found in this paper :-

Mery, D.; Riffo, V.; Zscherpel, U.; Mondragón, G.; Lillo, I.; Zuccar, I.; Lobel, H.; Carrasco, M. (2015): GDXray: The database of X-ray images for nondestructive testing. Journal of Nondestructive Evaluation, 34.4:1-12.
http://dmery.sitios.ing.uc.cl/Prints/ISI-Journals/2015-JNDE-GDXray.pdf

Also, I'm highly grateful to **Professor Domingo Mery**. He had clarified all the doubts I had regarding meta-data of this database.

## Object Classes :-

From the images, I have used **14 types of objects** as labels. I had to annotate most of them , since GRIMA database did not contain annotations for those objects. The types of objects used were :-

![Classes](https://raw.githubusercontent.com/subhromitra/Automated-Luggage-Checker/master/objnames_img.JPG)

I have used **LabelImg** as a tool for annotating the objects. Its an open-source desktop-app based tool.

## Train-Test split :-

1102 images were used from this database, 1043 were used for training. The rest 59 were augmented (by flipping images) to produce 59\*3 images. 

## Object Detector used :-

A pre-trained (MS COCO) **YOLOv3** object detector was used. It was trained again on the 1043 images from GRIMA database. 

## Results :-

Sample detections are as follows :-

![Sample Detections](https://github.com/subhromitra/Automated-Luggage-Checker/blob/master/sample_detections.JPG)
