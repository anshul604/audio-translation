# Audio Translation from English to Hindi

## Project Overview

This project implements an audio translation system that converts English audio to Hindi text but only after 6 PM IST. It includes a machine learning model, necessary scripts, and a user-friendly Python GUI.

## Repository Structure

- `data/` - Directory for storing audio data samples.
- `models/` - Directory for saving trained models.
- `src/` - Directory for source code.
  - `data_preprocessing.py` - Script for data preprocessing.
  - `model_training.py` - Script for training the model.
  - `audio_translation.py` - Script for translating audio.
  - `gui.py` - Script for the Python GUI.
- `requirements.txt` - File listing all dependencies.
- `README.md` - Detailed explanation of the project.
- `config.yaml` - Configuration file for specifying parameters and settings.

## Setup

1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Run the GUI using `python src/gui.py`.

## Usage

Upload an audio file through the GUI, and the system will translate the audio to Hindi text if the current time is after 6 PM IST.
