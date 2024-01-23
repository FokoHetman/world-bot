import numpy as np
import matplotlib.pyplot as plt
import math
import cv2
import time
import random
class Map:
    def __init__(self,countries):
        self.countries=countries
    def gen(self):
        def show(a):
            plt.title("Mapa Familia World")
            fig=plt.figure(figsize = (10,10))
            plt.plot(0,0,marker="o")
            plt.plot(1000,1000,marker="o")
            x = np.linspace(0, 20, 1000)
            colors=['b','r','y','g','m','c','b','w']
            colours=["blue","red","yellow","green","magenta",'cyan','black','white']
            countr=0

            for i in self.countries:
                country=self.countries[i]
                if countr+1>len(colors):
                    countr=0
                x,y=i.split()
                x=int(x)
                y=int(y)
                terrain=a[int(x)][int(y)]
                while terrain>0.15:
                    if x+50>1024:
                        x=x-100
                    if x-50<0:
                        x=x+100
                    if x>512:
                        x+=random.randint(-50,20)
                    else:
                        x+=random.randint(-20,50)
                    if y+50>1024:
                        y=y-100
                    if y-50<0:
                        y=y+100
                    if y>512:
                        y+=random.randint(-50,20)
                    else:
                        y+=random.randint(-20,50)
                    terrain=a[int(x)][int(y)]
                plt.plot(int(x), int(y), f"-{colors[countr]}", marker="*",markersize=10,label=country)
                plt.text(x,y-15, country,
        color=colours[countr], fontsize=15,ha="center",va='center')
                
                countr+=1
        #plt.plot(range(1000), linestyle='--', marker='o', color='b', label='line with marker')
            #plt.plot(xpoints, ypoints, '-gD', marker='1', markersize=20,label='line with select markers')
            plt.legend(loc="upper right")
        
            plt.imshow(a)
            fig.savefig("map.png")
        def generate ( map_size = 10, start_point = 0, extra_layers=[] ):
            
            size = 2**map_size
            
            # Choose what layers you want
            _ranges = list(range(start_point,map_size))
            _ranges.extend(extra_layers)
            
            # The output map
            a = np.zeros((size,size))
            
            # Compute layers
            for layer in _ranges:
                l = 2**layer
                rand = np.random.rand(l,l) /l
                a += cv2.resize( rand, (size,size) )   
                
            # Return
            return (a-a.min())/(a.max()-a.min())
        # Simple gradient

        def select (a, v, r):
            _r = np.logical_and(a > (v-r), a < (v+r))
            a[_r] = 0
            a[a < (v-r)] *= 0.8
            return a
        # Apply some borders





        _ = generate( map_size=10, start_point=5, extra_layers=[2] )
        _ = select(_,0.4, 0.01)

        



        show( _ )
        
        
m=Map({"1000 1000":"Rosja","800 800":"Finlandia", "654 194":"Czechy"})
m.gen()
