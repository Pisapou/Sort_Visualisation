import pygame
import random
import time

def tri_bulles(tab,sleep=0.001):
    for i in range(len(tab),0,-1):
        for j in range(0,i-1):
            if tab[j+1] < tab[j]:
                tab[j+1] , tab[j] = tab[j] , tab[j+1]
            draw_tab(sleep,[j])

def tri_selection(tab,sleep=0.01):
    for i in range(len(tab)):
        ind_mini = i
        for j in range(i+1, len(tab)):
            if tab[ind_mini] > tab[j]:
                ind_mini = j
                draw_tab(sleep,[j])
        tab[i],tab[ind_mini] = tab[ind_mini],tab[i]
    return None

def tri_insertion(tab,sleep=0.001): 
    for i in range(1, len(tab)): 
        k = tab[i]
        j = i-1
        while j >= 0 and k < tab[j] :
                tab[j + 1] = tab[j]
                j -= 1
                draw_tab(sleep,[j])
        tab[j + 1] = k
    return None 
 
def fusion(tab, sleep, start, mid, end):
    start2 = mid + 1
    if (tab[mid] <= tab[start2]):
        return None
    while (start <= mid and start2 <= end):
        if (tab[start] <= tab[start2]):
            start += 1
        else:
            value = tab[start2]
            index = start2
            while (index != start):
                tab[index] = tab[index - 1]
                index -= 1
                draw_tab(sleep,[index])
            tab[start] = value
            start += 1
            mid += 1
            start2 += 1
    return None
 
 
def tri_fusion(tab,sleep=0.001,l=None,r=None):
    if l is None:
        l,r = 0, len(tab)-1
    if l<r:
        m = l+(r-l)//2
        tri_fusion(tab, sleep, l, m)
        tri_fusion(tab, sleep, m + 1, r)
        fusion(tab, sleep, l, m, r)
    return None

def tri_cocktail(tab):
    echange=True
    while echange:
        echange=False
        for i in range(0,len(tab)-1):
            draw_tab(0.0005,[i])
            if tab[i]>tab[i+1]:
                tab[i],tab[i+1]=tab[i+1],tab[i]
                echange=True
        for i in range(len(tab)-2,-1,-1):
            draw_tab(0.0005,[i])
            if tab[i]>tab[i+1]:
                tab[i],tab[i+1]=tab[i+1],tab[i]
                echange=True
    return None
        
def draw_tab(sleep, rouge):
    time.sleep(sleep)
    pygame.event.pump()
    pygame.draw.rect(screen, (0,0,0), (0, 0, size[0], size[1]))
    for i in range(len(tab)):
        if i in rouge:
            pygame.draw.rect(screen, (255,0,0), (12*i, size[1]-tab[i]*7, 10, tab[i]*7))
        else:
            pygame.draw.rect(screen, (255,255,255), (12*i, size[1]-tab[i]*7, 10, tab[i]*7))
    pygame.display.update()
    return None

def verif_tab():
    for i in range(len(tab)-1):
        if tab[i] < tab[i+1]:
            pygame.draw.rect(screen, (0,255,0), (12*i, size[1]-tab[i]*7, 10, tab[i]*7))
        time.sleep(0.01)
        pygame.display.update()
    pygame.draw.rect(screen, (0,255,0), (12*(len(tab)-1), size[1]-tab[(len(tab)-1)]*7, 10, tab[(len(tab)-1)]*7))
    pygame.display.update()
    return None
        
      
        
NB_VAL = 100
        
tab = [i+1 for i in range(NB_VAL)]
random.shuffle(tab)
        
size = (NB_VAL*12, NB_VAL*7+10)  # largeur d'une val = 10 (2 entre chaque) // hauteur d'une val = 7
screen = pygame.display.set_mode(size)
run = True
triee = False

draw_tab(0,[])

while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not triee:
                # C'est ici qu'on choisit le tri (parmis: bulles, selection, insertion, fusion, cocktail)
                # Pour personnaliser le temps de "pause" entre chaque comparaison, ajoutez le en paramètre (ex: tri_selection(tab,0.01))
                tri_bulles(tab)
                draw_tab(0,[])
                time.sleep(1)
                verif_tab()
            
pygame.quit()
