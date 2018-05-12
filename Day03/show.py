from PIL import Image
from matplotlib.image import imread
import matplotlib.pyplot as plt
import random

def create_candidates():
    candidates = {"Bella": {"picture":"images/c1.jpg"}, 
                  "Lucy":  {"picture":"images/c2.jpg"},
                  "Molly": {"picture":"images/c3.jpg"}, 
                  "Daisy": {"picture":"images/c4.jpg"}, 
                  "Lucky": {"picture":"images/c5.jpg"}, 
                  "Sophie":{"picture":"images/c6.jpg"}, 
                  "Jack":  {"picture":"images/c7.jpg"}, 
                  "Teddy": {"picture":"images/c8.jpg"} }      
                
    return candidates

def imgshow2(file1, file2):
    img1 = Image.open(file1)
    img2 = Image.open(file2)
    fig, axes = plt.subplots(1, 2)
    axes[0].imshow(img1)
    axes[1].imshow(img2)
    return plt

def imgshow1(file1):
    img1 = imread(file1)
    plt.imshow(img1)
    plt.show()

def pickme(lst):
    """
    lstX=pickme(lst)-> lst is Battle list, return lstX that is 
    debouchment list.
    """
    lstX=[]
    while(len(lst)!=0):
        name1=random.choice(lst)
        name2=random.choice(lst)
        while(name1==name2):
            name2=random.choice(lst)
        imgshow2(c[name1]["picture"],c[name2]["picture"])
        plt.show()
        choice=input("choice between left and right:\nEnter 1 for left, 2 for right>>>")
        
        if choice==1:
            lstX.append(name1)
        elif choice==2: 
            lstX.append(name2)
        else: 
            lstX.append(name1)
        lst.remove(name1)
        lst.remove(name2)
        
    return lstX

if __name__ == "__main__":
    c = create_candidates()
    lst = c.keys()
    imgshow1("images/top8.jpg")
    list4 = pickme(lst)
    imgshow1("images/top4.jpg")
    list2 = pickme(list4)
    imgshow1("images/final.jpg")
    list1 = pickme(list2)
    plt=imgshow2(c[list1[0]]["picture"],"images/youwin.jpg")
