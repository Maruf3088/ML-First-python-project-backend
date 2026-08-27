# Student Placement Prediction API

A Flask REST API that predicts whether a student is likely to get a job placement based on **IQ score** and **CGPA**. The model is served using a pre-trained scikit-learn classifier and a saved `StandardScaler`.

## Live API

**Base URL:** [https://ml-first-python-project-backend-1.onrender.com](https://ml-first-python-project-backend-1.onrender.com)

**Frontend:** [https://ml-first-python-project.vercel.app](https://ml-first-python-project.vercel.app)

## Features

- REST API built with Flask
- CORS enabled for frontend integration
- Machine learning inference using pickled model and scaler
- JSON-based request/response

## Tech Stack

- **Python**
- **Flask** — web framework
- **Flask-CORS** — cross-origin requests
- **scikit-learn** — ML model & scaling
- **NumPy** — input preprocessing
- **Gunicorn** — production WSGI server

## Project Structure

```
backend/
├── app.py                 # Flask application & API routes
├── placement_model.pkl    # Trained ML model (required)
├── scaler.pkl             # StandardScaler used during training (required)
├── requirements.txt       # Python dependencies
└── README.md
```

## API Endpoints

### `GET /`

Health check endpoint.

**Response:**
```
Student Placement Prediction API is running!
```

### `POST /predict`

Predict placement likelihood from IQ and CGPA.

**Request body (JSON):**
```json
{
  "iq": 120,
  "cgpa": 3.5
}
```

**Success response (JSON):**
```json
{
  "prediction": 1,
  "result": "Likely to get placement"
}
```

| Field        | Type    | Description                                    |
|--------------|---------|------------------------------------------------|
| `prediction` | integer | `1` = likely placed, `0` = likely not placed |
| `result`     | string  | Human-readable prediction message              |

**Example (curl):**
```bash
curl -X POST https://ml-first-python-project-backend-1.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{"iq": 120, "cgpa": 3.5}'
```

## Local Setup

### Prerequisites

- Python 3.10+ recommended
- `placement_model.pkl` and `scaler.pkl` in the `backend/` directory

### Installation

```bash
# Clone the repository
git clone https://github.com/Maruf3088/ML-First-python-project-backend.git
cd ML-First-python-project-backend

# Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run locally

```bash
python app.py
```

The API runs at `http://127.0.0.1:5000`.

### Run with Gunicorn (production-style)

```bash
gunicorn app:app
```

## Deployment

This backend is deployed on [Render](https://render.com). Ensure `placement_model.pkl` and `scaler.pkl` are included in the deployment bundle.

**Suggested Render settings:**
- **Build command:** `pip install -r requirements.txt`
- **Start command:** `gunicorn app:app`

## Model Notes

- Input features: **IQ** and **CGPA**
- Inputs are scaled with the same `StandardScaler` used during training before prediction
- Output is a binary classification (`0` or `1`)

## Author

**Maruf Islam** — [GitHub](https://github.com/Maruf3088)

## License

This project is open source and available for learning purposes.
