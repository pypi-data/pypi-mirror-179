# MPS Portal Services

# Installation Instructions
1. Install python 3.7
1. pip install Maxar-Portal-SDK
1. Create a credentials file called `.mps-config` 
   * The file should look like:
   ```
   [mps]
   user_name=<your-user-name>
   user_password=<your-password>
   ```
# Usage Instructions
```
from MPS_Portal_SDK import Interface
interface = Interface()
print(help(sw_ogc))
```
# Documentation

Documentation site: https://maxar-portal.readthedocs.io/en/latest/

Github site: https://github.com/Maxar-Corp/maxar-portal

# How to Install Jupyter Notebooks
## Link to Jupyter labs install instructions Here
```
https://jupyter.org/install
```
## Recommended Steps

In your python 3.7 environment run the following installation commands
```
pip install notebook
```
After Installation is completed launch the Jupyter Notebook in your python environment with 
```
jupyter notebook
```

## (Optional) Creating a Shortcut for your Specific Python Environment Jupyter Notebook.
Create a new Short cut on your desktop. 
After Naming your shortcut right click and select Properties
Under the Shortcut tab
In the target box input the following command. Substituting in the Path to your Anaconda3 and the name of your python environment. 

```
%windir%\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& '<Path to Anaconda3>\condabin\conda-hook.ps1' ; "conda activate <PythonEnvironmentName>"; "jupyter notebook"
```
in the Start In box input 
```
%cd%
```
This will allow you to store this shortcut anywhere on your computer.