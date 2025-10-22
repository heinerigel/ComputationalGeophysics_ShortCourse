# ComputationalGeophysics_ShortCourse

### Short Course on *Computational Methods in Geophysics*

You find here the course material and access to executible Jupyter Notebooks for the Short Course on Numerical Methods in Geophysics. 

There are several options to run the Jupyter notebooks during the course with Cloud resources. It is wise to use all access methods as resources are limited. 

I. Use the repository with mybinder directly clicking on the following icon:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/heinerigel/ComputationalGeophysics_ShortCourse/HEAD?urlpath=/tree/)

II. Use the online Jupyter notebook library seismo-live:

[Seismo-live](https://seismo-live.github.io)

III. Sign up to the COURSERA course linked below (free!) and use the Jupyter Notebooks in the Labs (directions will be given):

[Coursea](https://www.coursera.org/learn/computers-waves-simulations) 

IV. Install an anaconda environment on your computer and run the notebooks locally (preferred if you want to work with them later, modify them etc.)

Download the entire repository. 

Instructions for Windows (10, 11 should be similar). Any other operating system (MAC-OS, Linux) should work very similar.

1. Install anaconda environment for your operating system (www.anaconda.com), -> free download -> give your  email address -> download

2. After download run  executable  with all  default settings

3. Create local folder for all your Jupyter notebooks 

4. Open terminal window (under Windows type "anaconda prompt" in the search space bottom left)

5. "cd" to your notebook folder. Remember "cd .." goes one folder up "cd Folder" changes into the "Folder" directory. Remember to use tab completion ... 

6. Create an environment for you with the environment.yml file from the repository

7. Run the following command in your base environment (the > is the prompt)

> conda env create -f environment.yml

8. Activate (each time you want to use the notebooks) the environment "shortcourse"

> conda activate shortcourse

9. Now you should be able to run jupyter notebooks 

> jupyter notebook

10. You should now see either a file directory or a list of jupyter notebooks, just go inside the desired folder or click on the notebook. 

11. Enjoy. 
  
 
