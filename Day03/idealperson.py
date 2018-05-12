from PIL import Image
import matplotlib.pyplot as plt

def create_candidates():
    candidates = {"ljj": {
                    "height":180, 
                    "age":45, 
                    "attract":"fitted body, asian typical handsome guy", 
                    "picture":"images/f.jpg"}, 
              "wb": {
                    "height":180, 
                    "age":45, 
                    "attract":"bright smile", 
                    "picture":"images/g.jpg"}}
    return candidates

def imgshow(file1, file2):
    img1 = Image.open(file1)
    img2 = Image.open(file2)
    fig, axes = plt.subplots(1, 2)
    axes[0].imshow(img1)
    axes[1].imshow(img2)
    return plt

if __name__ == "__main__":
    c = create_candidates()
    lst = c.keys()
    imgshow(c[lst[0]]["picture"], c[lst[1]]["picture"])
    plt.show()









    
