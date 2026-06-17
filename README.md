# Email Phishing Detector

## Overview

The Email Phishing Detector is a machine learning-based web application that identifies whether an email message is legitimate or phishing. The project helps users detect suspicious emails and improve cybersecurity awareness.

## Features

* Detects phishing and legitimate emails
* User-friendly web interface built with Flask.
* Machine Learning model for email classification.
* Real-time prediction of email messages.
* Easy deployment and integration.

## Technologies Used

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* HTML/CSS
* Pickle

## Project Structure

```
phishingdetector/
│
├── app.py
├── phishing_model.pkl
├── emails.csv
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md
```

## Dataset

The dataset contains email messages labeled as:

* Phishing
* Legitimate

Example:

| Email Text                      | Label      |
| ------------------------------- | ---------- |
| Verify your account immediately | Phishing   |
| Click here to claim your prize  | Phishing   |
| Meeting scheduled for tomorrow  | Legitimate |
| Project discussion at 2 PM      | Legitimate |

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/phishingdetector.git
```

2. Navigate to the project folder:

```bash
cd phishingdetector
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Open your browser and visit:

```
http://127.0.0.1:5000
```

## How It Works

1. User enters an email message.
2. The text is processed and converted into numerical features.
3. The trained machine learning model analyzes the message.
4. The system predicts whether the email is:

   * Phishing
   * Legitimate

## Future Enhancements

* Deep Learning-based phishing detection.
* URL and attachment analysis.
* Email sender reputation checking.
* Dashboard for phishing statistics.
* Deployment on cloud platforms.

## Applications

* Educational cybersecurity projects.
* Email security systems.
* Awareness training platforms.
* Enterprise email filtering solutions.

## Author

Vinodhini

## License

This project is developed for educational and research purposes.
