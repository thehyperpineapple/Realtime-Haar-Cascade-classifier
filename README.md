
# Realtime-Haar-Cascade-classifier

Computer Vision project that involves detecting objects in real-time using Haar Cascade Classifier


## Tech Stack
- Python
- OpenCV


## Installation

To run the application, you will need Python installed on your system. 

### Clone the repository

```bash
https://github.com/your-username/Realtime-Haar-Cascade-classifier.git
```

### Create a Virtual Environment and Install Dependencies
- Once the repository has been cloned, navigate to the project directory using the cd command:

```bash
    cd Realtime-Haar-Cascade-classifier
```
- Create a new virtual environment for the project using the following command:
```python
    python -m venv venv
```

- Activate the virtual environment using the following command:

```bash
    source venv/bin/activate
```

- Install the required dependencies using the following command:

```python
    pip install -r requirements.txt
```
- Create an `images` directory that contains labelled images
## Usage

Once you’ve installed all the necessary dependencies, first run `model_training.py` with the following command:
```python
    python model_training.py
```
It will then create a `trainer_final.yml` file. Once created run `realtime-predictor.py` to start making predictions. Use the  `Esc` to exit the program




## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License. See the LICENSE.md file for details.

