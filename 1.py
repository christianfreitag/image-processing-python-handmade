import cv2 as cv2
import numpy as np
import math
import matplotlib.pyplot as plt
img = cv2.imread("lena.jpg")


def getsize(img): 
    w  = img.shape[0] #width
    h = img.shape[1] #height
    c = img.shape[2]#channels
    return w,h,c;
w,h,c = getsize(img);  

#mostrando janela com imagem
def display(img):

    cv2.imshow("resukt",img) # definindo titulo como 'imagem'
    cv2.waitKey(0) #fechandp janela com qualquer tecla
    cv2.destroyAllWindows() #destruindo janelas
    #cv2.imwrite('translação.jpg',img)
  
def gray(img):
    gray = []
    for i in range(h):
        for j in range(w):
            a = img[i,j][0]*0.2627+ img[i,j][1]*0.7152 + img[i,j][2]*0.0722  

            if a>255:
                a = 255
            elif a<0:
                a =0
            for p in range(c):
                img[i,j][p] = a;
           
def diff(img):
    for i in range(h):
        for j in range(w):
             for p in range(c):
                    img[i,j][p] = 255-img[i,j][p];

def bina(img):
    v =0;
    for i in range(h):
        for j in range(w):
            if img[i,j][0]>70:
                v = 255
            else:
                v = 0
            for p in range(c):
                img[i,j][p] = v
                
def fatiamento(img):
    v =0;
    for i in range(h):
        for j in range(w):
            if img[i,j][0]>100 and img[i,j][0]<150:
                v = img[i][j][0];
            else:
                v =0
            
            for p in range(c):
                img[i,j][p] = v
                                   
def contraste(img):
    for i in range(h):
        for j in range(w):
            for p in range(c):
                img[i,j][p] = (img[i,j][p]-25)*((255-0)/(225-25))+0

def pbaixa(img):
    for i in range(h-1):
        for j in range(w-1):
             for p in range(c):
                 if (i and j>0):
                     a = np.uint8(((img[i-1,j-1][p]*1) + img[i-1,j][p]*1  + img[i-1,j+1][p]*1  + img[i,j+1][p]*1  + img[i+1,j+1][p]*1 +img[i+1,j][p]*1  +img[i+1,j-1][p]*1  + img[i,j-1][p]*1 )/9)
                     img[i,j][p] = a  

def escala(img,tx,ty):
    b=0;
    if(tx and ty <0):
        tx,ty =1,1;
    nwImg = np.zeros((h*ty,w*tx,3), np.uint8)
    for i in range((h)):
            for j in range((w)):
                a = np.dot([[tx,0,0],[0,ty,0]],[[j],[i],[1]])
                if(a[0][0]>0):
                    for z in range(a[1][0]-ty,a[1][0]) :   
                        for p in range(a[0][0]-tx,a[0][0]):
                            nwImg[z,p][:]= img[i,j][:];           
    
    return nwImg;

def rotacao(img,ang):
    nwImg = np.zeros((h+ang,w+ang,3), np.uint8)
    for i in range(0,h):
            for j in range(0,w):
               
               a = np.dot([[np.cos(ang), -np.sin(ang), 0],
              [np.sin(ang), np.cos(ang), 0]],[[j],[i],[1]])
               a = a.astype(np.int);
               nwImg[a[0][0],a[1][0]][:]= img[i,j][:];
    
    return nwImg;

def espelha(img):
    nwImg = np.zeros((h,w,3), np.uint8)
    for i in range(0,h):
            for j in range(0,w):
               
               a = np.dot([[-1, 0, 0],
              [0, -1, 0]],[[j],[i],[1]])
               
               nwImg[a[1][0],a[0][0]][:]= img[i,j][:];
    
    return nwImg;

def agucamento(img):
    for i in range((h-1)):
        for j in range((w-1)):
             for p in range(c):
                 if (i and j>0):
                     a= np.uint8(((img[i-1][j-1][p]*-1) + img[i-1][j][p]*0  + img[i-1][j+1][p]*1  + img[i][j-1][p]*-2  + img[i][j][p]*0 +img[i][j+1][p]*2  +img[i+1][j-1][p]*-1  + img[i+1][j][p]*0+ img[i+1][j+1][p]*-1 )/9)
                     img[i,j][p] =a
                    
def transla(img,tx,ty):
    nwImg = np.zeros((h+ty,w+tx,3), np.uint8)
    for i in range((h)):
            for j in range((w)):
               a = np.dot([[1,0,tx],[0,1,ty]],[[j],[i],[1]])
               #print(a)
               nwImg[a[1][0],a[0][0]][:]= img[i,j][:];
    return nwImg;
        
                
#gray(img)

#diff(img)

#bina(img)

#contraste(img)

#img = escala(img,3,3)
#w,h,c = getsize(img);

#pbaixa(img)

#img = rotacao(img,90)

#img = espelha(img)

#agucamento(img)
#diff(img)
#bina(img)

#img = transla(img,100,20)

#fatiamento(img)

display(img)


