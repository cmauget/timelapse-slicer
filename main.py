from scripts.Slicing import Slicing

if __name__=='__main__':

    s = Slicing()

    num_premiere_photo = 0
    num_derniere_photo = 2
    inputStr = "input"
    outputStr = "output"
    nb_bandes = (num_derniere_photo-num_premiere_photo)+1
    m=2

    for i in range(6):
        s.slice(nb_bandes, num_derniere_photo, num_premiere_photo, inputStr, outputStr, mode=m, decalage=i*10000)
