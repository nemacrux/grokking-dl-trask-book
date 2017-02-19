# Jupyter Notebooks for the book Grokking Deep Learning (some chapters)

## Instructions

1. Download/clone this project
2. `cd` into `gdl-trask-book` 
3. The best way to run this notebook is using anaconda or [miniconda](https://conda.io/docs/install/quick.html)
4. Create a new conda environment:

    ```
    conda create --name trask-book python=3`
    ```
5. Enter your new environment:

  * Mac/Linux: `>> source activate trask-book`
  * Windows: >> `activate trask-book`
6. Install required libraries:
   
    ```
    conda install numpy jupyter notebook
    ```
7. `cd`into the chapter you want and run the following to open up the notebook:
   
    ```
    jupyter notebook chapter-<number of chapter>.ipynb
    ```