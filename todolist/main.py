from tkinter import *
from tkinter.messagebox import *
from pickle import *
from tkcalendar import Calendar
import datetime as dt 


fenetre = Tk()
fenetre.title("To-Do List by Ravin THILAGARASA")
# Date
date = dt.datetime.now()
label = Label(fenetre, text=f"{date:%A %d %B %Y}", font="Calibri, 12")
label.pack()


# Fonction pour enregistre un task et verifier 
def entretask():
    input_task=""
    # Creation du calendire 
    def grad_date():
        date.config(text = "date selectionne est : " + cal.get_date()) 
    def add_task():
        input_task = entre_task.get(1.0, "end-1c")
        date_task = cal.get_date() 
        if input_task == "" or input_task == " ":
            showwarning("Attention!", "Entre votre task")
        else:
            listbox_tasks.insert(END, input_task + "  " + "finir pour le " + date_task)
            fenetre2.destroy()
   # Creation d'une autre fenetre 
    fenetre2=Tk()
    fenetre2.title("Add task")
    entre_task=Text(fenetre2,width=40,height=4)
    entre_task.pack()
    # Calendrier 
    cal = Calendar(fenetre2, selectmode = 'day', annee = 2022, mois = 11, jour = 20 )
    cal.pack()
    button_date = Button(fenetre2, text = "date", command = grad_date)
    button_date.pack()
    date = Label(fenetre2, text = "")
    date.pack()
    if cal.get_date() == "":
        showwarning("Attention!", "Entre votre une date")
    else:
        button_temp=Button(fenetre2,text="Add task",command=add_task)
        button_temp.pack()
    
    fenetre2.mainloop()
    
    

def delete_task():
    # Selection d'un element 
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    # Si aucun element n'a étais choisi un message d'erreur appait 
    except:
        showwarning("Attention!", "Veuillez selectionne votre task")

def modifier():
    try:
        task_index = listbox_tasks.curselection()[0]
        open("tasks.txt","bw")
        entretask()
    # Si aucun element n'a étais choisi un message d'erreur appait 
    except:
        showwarning("Attention!", "Veuillez selectionne votre task")
    

def load_task():
    try: 
        tasks = load(open("tasks.txt","rb"))
        listbox_tasks.delete(0,END)
        for task in tasks : 
            listbox_tasks.insert(END, task)
    except:
        showwarning("Attention!", "texte.txt n'est plus accesible")

def save_task():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    # Enregistre le task dans task.txt en binaire 
    dump(tasks, open("tasks.txt","bw")) 

def complete():
    try :
        marked=listbox_tasks.curselection()
        temp=marked[0]
        #store the text of selected item in a string
        temp_marked=listbox_tasks.get(marked)
        #update it 
        temp_marked=temp_marked+" ✔"
        #delete it then insert it 
        listbox_tasks.delete(temp)
        listbox_tasks.insert(temp,temp_marked)
    except:
        showwarning("Attention!", "rien n'a étais selectionne")


# Create GUI
frame_tasks = Frame(fenetre)
frame_tasks.pack()

listbox_tasks = Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=LEFT)

# Scrolle et posisionement 
scrollbar_tasks = Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=RIGHT, fill=Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)



# Boutton ajout de task 

button_add_task = Button(fenetre, text = "ajout task", width=48, command=entretask)
button_add_task.pack()

button_delete_task = Button(fenetre, text = "supprimer task", width=48, command=delete_task)
button_delete_task.pack()

button_load_tasks = Button(fenetre, text = "charger task", width=48, command=load_task)
button_load_tasks.pack()

button_save_task = Button(fenetre, text = "enregistre task", width=48, command=save_task)
button_save_task.pack()

button_modifier = Button(fenetre,text="modifier", width=48, command=modifier)
button_modifier.pack()

button_confirme=Button(fenetre,text="fini ",width=50,command=complete)
button_confirme.pack()





fenetre.mainloop()



# mettre la date en francais 
# mettre la date tout a gauche 
# mettre un compteur 
#rzgarde le module csv et au lieux de passer par le txt en back up mieux vaut utiiser en memoire 

