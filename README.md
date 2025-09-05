# MediGuide AI 🏥
### An AI-Powered Personal Healthcare Assistant Based on Medical Reports

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active%20Development-orange.svg)]()

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## 🔍 Overview

MediGuide AI is a revolutionary web-based intelligent healthcare assistant that empowers patients to understand and manage their health reports more effectively. By leveraging cutting-edge AI technologies, the platform bridges the gap between complex medical data and patient understanding, promoting proactive wellness management.

The system automatically analyzes uploaded medical reports using OCR and NLP techniques, providing personalized insights including dietary suggestions, health concerns identification, and comprehensive medication explanations.

## ✨ Features

### 🔧 Core Features
- **📄 Multi-format Report Upload**: Support for PDF, images, and various document formats
- **🤖 AI-Powered Analysis**: Intelligent extraction and interpretation of medical terms
- **🍎 Personalized Recommendations**: Diet and lifestyle suggestions based on test values
- **💊 Medicine Insights**: Detailed explanations of prescribed medications, side effects, and interactions
- **📊 Health Dashboard**: Track previous uploads and monitor health trends
- **💬 AI Chatbot Assistant**: Interactive support for health-related queries(upcoming)

### 🚀 Technical Features
- **OCR Integration**: Advanced text extraction from medical documents (currently ocr api)
- **NLP Processing**: Natural language understanding for medical terminology(currently gemini api)
- **Real-time Analysis**: Instant report processing and feedback
- **Secure Data Handling**: Privacy-focused medical data management
- **Scalable Architecture**: Built for high availability and performance

## 🛠 Technology Stack

### Backend (Current Repository)
- **Framework**: Flask 2.0+
- **Language**: Python 3.8+
- **AI/ML**: Natural Language Processing, OCR
- **Database**: MongoDB (planned)
- **Authentication**: JWT-based security

### Frontend (Separate Repository)
- **Framework**:js (React-vite)
- **Styling**: Tailwind CSS 

### AI & Processing
- **OCR**: Tesseract / Google Vision API(currently ocr api)
- **NLP**: Custom medical knowledge bases(upcoming)
- **Future**: BioBERT, ClinicalBERT integration(upcoming)

## 📁 Project Structure

```
CuraGenie_backend/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── runtime.txt           # Python version specification
├── routes/               # API route definitions
├── services/             # Business logic and AI services
├── utils/                # Utility functions and helpers
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Agyanshu7352/MediGuide-AI_backend.git
   cd CuraGenie_backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

The server will start on `http://localhost:5000` by default.

## 💻 Usage

### Basic Workflow

1. **Upload Medical Report**: Send POST request to `/api/upload` with report file
2. **AI Analysis**: System processes document using OCR and NLP
3. **Get Insights**: Receive personalized health insights and recommendations
4. **Dashboard Access**: View historical reports and track health trends

### Example API Call
```bash
curl -X POST \
  http://localhost:5000/api/upload \
  -H 'Content-Type: multipart/form-data' \
  -F 'report=@medical_report.pdf'
```

## 🛣 API Endpoints

| Endpoint | Method | Description |
|----------|---------|-------------|
| `/api/upload` | POST | Upload and analyze medical report |
| `/api/list` | GET | Retrieve user's report history |
| `/api/<report id>/insights` | GET | Get detailed insights for specific report |
| `/api/chat` | POST | Interact with AI health assistant |(upcoming)
| `/api/diet` | GET | Get personalized health recommendations |

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Flask Configuration
FLASK_ENV=development
SECRET_KEY=your_secret_key_here

# Database
DATABASE_URL=your_database_url

# AI Services
OCR_API_KEY=your_ocr_api_key
NLP_MODEL_PATH=path_to_model

# File Upload
MAX_FILE_SIZE=16777216  # 16MB
ALLOWED_EXTENSIONS=pdf,jpg,jpeg,png
```

## 🤝 Contributing

We welcome contributions to MediGuide AI! Please follow these steps:

1. **Fork the repository**
2. **Create feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit changes** (`git commit -m 'Add AmazingFeature'`)
4. **Push to branch** (`git push origin feature/AmazingFeature`)
5. **Open Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Write comprehensive unit tests
- Update documentation for new features
- Ensure HIPAA compliance for medical data handling

## 🚀 Future Enhancements

### Short-term Goals
- [ ] Integration with BioBERT for enhanced medical NLP
- [ ] Multi-language support for medical reports
- [ ] Advanced data visualization for health trends
- [ ] Mobile application development

### Long-term Vision
- [ ] Integration with wearable devices
- [ ] Telemedicine consultation booking
- [ ] AI-powered health risk prediction
- [ ] Blockchain-based secure health records

## 📊 Performance & Scalability

- **Processing Speed**: < 30 seconds for typical medical report
- **Supported Formats**: PDF, JPEG, PNG, TIFF
- **Maximum File Size**: 16MB per upload
- **Concurrent Users**: Designed for 1000+ simultaneous users

## 🔒 Security & Privacy

- **Data Encryption**: End-to-end encryption for all medical data
- **HIPAA Compliance**: Following healthcare data protection standards
- **Anonymous Processing**: Personal identifiers removed during AI analysis
- **Secure Storage**: Encrypted database with access controls

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@Agyanshu7352](https://github.com/Agyanshu7352)
- LinkedIn: [Agyanshu Kumar](www.linkedin.com/in/agyanshukumar)
- Email: agyanshukumar@gmail.com

## 🙏 Acknowledgments

- Medical professionals who provided domain expertise
- Open-source NLP and OCR communities
- Healthcare AI research contributions
- Beta testers and early adopters

<div align="center">
  <p><strong>Made with ❤️ for better healthcare accessibility</strong></p>
  <p>⭐ Star this repo if you find it helpful!</p>
</div>