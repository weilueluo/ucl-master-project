# Project Time-line

## Initial

### 25 Apr | Tobias Meeting

- I talked about my findings such as rife, tobias recommended pix2pix, unet

### 3 May | Tobias Meeting

- Asked me to sign, 1-way NDA before tomorrow so that I can join meeting, which I did

### 4 May | Tobias + NoGhost Meeting

- Revised on project goals
- Tobias asked about data and funding

### 10 May | NoGhost Meeting

- Tried to access NoGhost dataset, unsuccessful
- Received 5 shots of data through [google drive](https://drive.google.com/drive/folders/1AJ3mQMtnEIs9Klk34a03Jo0hyF3F74uR).

### 22 May

- Exam ended yesterday, started working on the code
- papers and dataset read.

### 23 May

- Finished setting up jupyter notebook, google colab and drive.
- Create save file function that works both on google colab and local jupyter notebook is tough

### 25 May

- Read source code
- Finished and validated Unet Generator implementation

### -31 May | NoGhost Meeting

- Trained label to build & edge to color
- New Quadro RTX 8000 GPU
- Shared Google drive for storage
- 12 May DDL for demo, promised 9 May for test

### 3-8 Jun Holiday

### 9 Jun Meeting

- Gonna get new batch of data

### 10 Jun

- Got a new batch of data in the late afternoon

### 11 Jun

- Rebuilt dataset preprocessing pipeline to suit the new batch of dataset as well as extract tie-down dataset.
- Experimented with naive smaller models, but not very good result.

### 12 Jun

- Rebuilt training pipeline so that I can develop in the IDE and run code in colab.

### 17 Jun

- Gitlab access
- know about the preprocessing stage in the company, they will ask for my input
- segmentation models for different part of the image

### 20 Jun

- packed codebase into gitlab
- Read about image segmentation.
- Started reading about nerf.
- abit busy cause working with my cv

### 21 Jun

- 4-8 computing hardware
- nerf: light field demo from Google

### 23 Jun

- connected to noghost network folder
- failed to connect to gpu machine
- found a bunch of image segmentation models, but not for 2d cartoon characters
  - human segmentation model performs poorly on cartoon style characters

### 24 Jun

- Got a new batch of data
  - finished preprocess them

### 26 Jun

- pretrain model seems to be good
  - try pretrain own model
    - gathered 20k images
    - extract line segments using various methods
    - implemented xdog, line extraction using some models as well

### 1 Jul

- done pretraining alacgan

### 3 Jul

- done finetuning

### 8 Jul

- Read about some paper on sketch simplification
- implemented Sketch Simplification

### 10 Jul

- Result does not look fine

### 13 Jul

- Read some super resolution paper

### 16 Jul

- attempted multiple approach, hard to finetune high level details
- probably because it is essentially a blurring processing

### 19 Jul

- Report Requirements
  - most useful: pros and cons
  - research side: newest papers, directions, SOTA
  - abilities to make edits

### 22 Jul

- Implemented carn-m model
- result looks fine
- disconnected remote

### 24 Jul

- setup latex template

### 26 Jul

- reconnect remote
- where my training? 
- retrain

### 2 Aug

- Trained super resolution

### 8 Aug

- finetuned super resolution
- implementing frame interpolation

### 16  Aug

- explored colorization
- written approach for colorization
- still implementing frame interpolation

