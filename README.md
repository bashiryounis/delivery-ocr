# 📦 Delivery OCR API

**Delivery OCR API** is a FastAPI-based service that extracts structured delivery information from uploaded images using Google's Gemini 1.5 Pro model. It processes images to retrieve details such as delivery dates, distances, and individual delivery items.

## 🚀 Features

- **Image Upload**: Accepts delivery images in JPEG format.
- **OCR Processing**: Utilizes Gemini 1.5 Pro for extracting structured data.
- **Structured Output**: Returns data in a clean JSON format.
- **Asynchronous Handling**: Efficiently manages file uploads and processing.

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.12
- [Poetry](https://python-poetry.org/docs/#installation) for dependency management
- Docker & Docker Compose (for containerized deployment)

### Installation

1. **Clone the Repository**:

   ```bash
   https://github.com/bashiryounis/delivery-ocr.git
   cd delivery-ocr/api
   ```

2. **Install Dependencies**:

   ```bash
   poetry install
   ```

3. **Configure Environment Variables**:

   Create a `.env` file in the `api` directory with the following content:

   ```env
   GOOGLE_API_KEY=your_google_api_key
   GENERATIVE_MODEL=gemini-1.5-pro
   MAIN_DIR=./main_dir
   ```

   Replace `your_google_api_key` with your actual Google API key. You can obtain it from [Google AI Studio](https://ai.google.dev/aistudio).

4. **Run the Application**:

   ```bash
   make dev
   ```

   This command utilizes the `Makefile` to start the FastAPI application.

5. **Access the API Documentation**:

   Navigate to [http://localhost:8000/docs](http://localhost:8000/docs) to explore the interactive Swagger UI.



### Endpoints: 

Perfect! Here's the improved version of your **Endpoints section** with an added **"Endpoint"** column so you can list multiple routes consistently:

---

###  API Endpoints

| Endpoint             | Method | Content-Type         | Form Field           | Description                                                   | Response Type |
|----------------------|--------|----------------------|----------------------|---------------------------------------------------------------|---------------|
| `/extract/delivery`  | POST   | `multipart/form-data`| `file` (UploadFile)  | Upload a delivery image to extract structured delivery data   | JSON          |





## 🧰 Project Structure

```
delivery-ocr/
├── api/
│   ├── dev_start.sh
│   ├── Dockerfile
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── src/
│       ├── core/
│       │   ├── config.py
│       │   ├── llm.py
│       │   ├── logger_config.py
│       │   ├── prompt.py
│       │   └── schema.py
│       ├── main.py
│       └── service/
│           ├── ocr_delivery.py
│           └── utils.py
├── docker-compose.yaml
├── docs/
│   ├── delivery_ocr.ipynb
│   ├── sample1.jpeg
│   └── sample2.jpeg
├── Makefile
└── README.md
```

## 🧠 Model Information

This application leverages **Gemini 1.5 Pro**, a multimodal model by Google DeepMind, capable of processing text and images to generate structured outputs. For more details, visit the [Gemini API Documentation](https://ai.google.dev/gemini-api/docs/models).

## 🐳 Docker Deployment

To run the application in a Docker container:

1. **Build and Start Containers**:

   ```bash
   docker-compose up --build
   ```

2. **Access the API**:

   Navigate to [http://localhost:8000/docs](http://localhost:8000/docs) to interact with the API.
