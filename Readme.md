# Python Multithreading and Multiprocessing


This repo exercises multithreading and multiprocessing in Python. It includes:
   * #### Creating threads and assigning tasks to them  
   * #### Creating threads and synchronizing them using locks   
   * #### Changing text files using threads
   * #### Analyzing time for executing I/O and CPU bound tasks with threads and processes

All files are build using **Python 3.11**.

### In order to run the python files:
**1. Create virtual environment**  
*From the **root** directory run:*

      python -m venv venv  

**2. Activate the environment**  
*On MacOS:* 

    source venv/bin/activate
*On Windows :*  

    venv\Scripts\activate

**3. Install required dependencies**  
*From the **root** directory run:* 

    pip install -r requirements.txt  

**4. Run the files**  
*From the **root** directory run:* 

    py the-python-file's-name.py  
**5. Before running the change_files.py**

*You have to **create** as many .txt files as you want. **In order to change their content first write in each of them:*** 

    IDs