# SIMPLE-AI-RECOGNIZES-DIGIT-APP

### Description
* This is a simple app that user can draw a number on canvas and it will predict what number has been drawn.
* It's implemented in Python using Tkinter.

### More details
* Look at the AI RECOGNIZER Jupyter Notebook to have a sense about how I train the model.
* The dataset I used is pretty small (20 images for each label 0-9, created by me), therefore, the accuracy of the model is not really good. You can use your own dataset to get better-perfomance model.
* The model is a simple neural network with 3 layers.

### About the app
* The main canvas is used to draw number by dragging mouse.
* There are 4 buttons:
  * Clear: to clear the canvas drawing.
  * Predict: take the canvas number and display model prediction.
  * Save: save canvas drawing in images folder (to increase the dataset and can use for later training).
  * Exit: to close the app.

![image](https://user-images.githubusercontent.com/70113806/124999594-59243180-e003-11eb-80e9-5614e67bcf42.PNG)
