# Antimony Model Creator - Olivia Walsh, Matthew Van Ginneken
 
This package allows the user to visualize a reaction via a steady state graph.  The user can create and submit their own reactions on the Flask Webpage, or they can submit an antimony txt file or a SBML file also through the webpage.  The Webpage will run a simulation using the reactions with tellurium and show the steady state graph.  
 
## <b>Installation </b>
 
To install this package the user should open up to their terminal and use pip install to install the package 
> pip install AMC-OWMVG==1.1.0
 
Once the terminal has confirmed installation, the user must create a new folder in their desktop and move to that directory
> cd Desktop <br>
> cd newFolder (replace newFolder with the name of the folder)
 
Within this folder the user has to create a file and another folder called static.  We recommend using an IDE or an editor to make these.
> static (a folder) <br>
> runApp.py <br>
 
Within the static folder the user should make two .txt files that are empty.
> antimony1.txt <br>
> antimony2.txt <br>
 
Going back to the file runApp.py the user should type out the following into the file
> import AMCowmvg <br>
> from AMCowmvg.testing import runApp <br>
> runApp()
 
The user should then run the runApp.py in their terminal
> python runApp.py
 
This will produce a few lines of response including a website link, the user should copy and paste this into their browser.  The user now can create and visualize their reactions
 
##<b> Installation if you have access to the StarterAMC folder </b>
### <i>If the user has access to the StarterAMC folder they should download it to their desktop then run through the following commands </i>
 
To install this package the user should open up to their terminal and use pip install to install the package 
> pip install AMC-OWMVG==1.1.0
 
Once the terminal has confirmed installation the user must navigate to the StarterAMC directory
> cd Desktop <br>
> cd StarterAMC
 
Once the user is in the correct directory they should run the runApp.py file from their terminal
> python runApp.py
 
This will produce a few lines of response including a website link, the user should copy and paste this into their browser.  The user now can create and visualize their reactions
