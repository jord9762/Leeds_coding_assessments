import matplotlib
matplotlib.use('TkAgg')
#imports random library which is helpful for testing outcomes, contains functions such as shuffle
import random
#imports operators which may be missing from default Spyder
import operator
#imports the csv library necessary for reading the 'environmental' csv data (in.csv). 
import csv
#imports the agentframework file which must be in the same directory to work, by importing this we can import the agent class.
import agentframework
#imports animations from pyplot which will allow 
import matplotlib.animation 
import matplotlib.pyplot
import requests
import bs4
#provides connection between the standard python interface to the Tk GUI toolkit
import tkinter


"""WARNING!!!!!"""
"""Note to visualise the code in this file the code %matplotlib qt must be inputted in to the ipython console first. Or alternatively
the code can be ran in the command prompt. Note to run this code more than once in the Jupyter terminal may require a restart of the kernel."""

"""https://www.youtube.com/watch?v=8exB6Ly3nx0 this excellent resource had info on combining GUI with matplotlib data"""

#creates a new empty list for what will be the csv environment data
environment = []
#empty list for agents
agents = []
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

#specifies pop up figure dimensions
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

carry_on = True

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()  #show did not work see here for solution https://stackoverflow.com/questions/50165115/unable-to-call-canvas-show
   


 
#used to call GUI 
root = tkinter.Tk()
root.wm_title("Model")
#Open window having dimension 700x700
root.geometry('700x700')
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
#configures GUI background to grey
root.configure(background="grey")

#my_button class and parameters below change the GUI button to blue
my_button = tkinter.Button(root, text="Run model", command=run, bg='blue')#https://pythonexamples.org/python-tkinter-button-background-color/#:~:text=You%20can%20change%20the%20background,bg%20property%20as%20shown%20below.&text=The%20default%20color%20of%20Tkinter%20Button%20is%20grey.
my_button.pack(side=tkinter.TOP)#https://www.youtube.com/watch?v=Uk2FivOD8qo got idea from here


canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)



f = open('in.csv', newline='')
#Note that the correct directory must be navigated to in the terminal else the full file path will be needed
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader: # A list of rows
    rowlist = []
    for value in row: # A list of value
     rowlist.append(value)
     environment.append(rowlist)
 
 # Make the agents.
for i in range(num_of_agents):
       agents.append(agentframework.agent(environment, agents))   
 
def update(frame_number):
    
    fig.clear()   
    global carry_on
    
         
    
    # Move the agents.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
        
           
            
    #plot agents 
    matplotlib.pyplot.xlim(0, 100)
    matplotlib.pyplot.ylim(0, 100)
    matplotlib.pyplot.imshow(environment)
    
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)


"""In the gen_function function we are assigning the number of iterations the animation will go through. a=0
means starting at 0 and carry_on while a =<10 leads to 10 iterations being called as the anmation will carry
on until the store reaches 9."""
def gen_function(b = [0]):
    store = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (store < 10) & (carry_on) :
        yield store			# Returns control and waits next call.
        store = store + 1





#script is ended by calling of tkinter mainloop      
tkinter.mainloop()

