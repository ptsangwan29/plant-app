# 🌿 Plant Identifier App

A simple web-based application that identifies plant species from an image of a leaf and returns the most likely plant names along with confidence scores.

---

## 🚀 Features

- Upload an image of a leaf
- Get top 3 predicted plant names
- Displays:
  - Common name
  - Scientific name
  - Confidence score
- Image preview before upload
- Simple and clean UI

---

## 🧠 How It Works

1. User uploads an image from the browser
2. Image is sent to a FastAPI backend
3. Backend:
   - Reads the image
   - Converts it into Base64 format
   - Sends it to the Plant.id API
4. The API uses a trained deep learning model to classify the plant
5. Results are returned and displayed on the UI

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- Requests
- Uvicorn

### Frontend
- HTML
- CSS
- JavaScript (Vanilla)

### External API
- Plant.id (Kindwise API)

---

## 📁 Project Structure
plant-app/
│
├── main.py # Backend (FastAPI server)
└── index.html # Frontend (UI)


---

## ⚙️ Setup Instructions

### 1. Clone or download the project


git clone <your-repo-link>
cd plant-app


---

### 2. Install dependencies


pip install fastapi uvicorn requests python-multipart


---

### 3. Add your API key

Open `main.py` and replace:

api key="m3IH7yas1XxWJ6jPuHzAb0ImUwfUtm3RJC39nc5PRZZO24DF99"
API_KEY = "YOUR_API_KEY_HERE"


with your actual Plant.id API key.

---

### 4. Run the backend server


python -m uvicorn main:app --reload


Server will start at:

http://127.0.0.1:8000


---

### 5. Run the frontend

- Open `index.html` in your browser
- Upload an image
- Click "Identify"

---

## 📥 Input

- Image file (leaf photo)
  - Formats: JPG, PNG, etc.

---

## 📤 Output

Example:


🌱 Mango (Mangifera indica) - 92%
🌱 Neem (Azadirachta indica) - 5%
🌱 Guava (Psidium guajava) - 2%


---

## 🔑 Key Concepts Used

- REST API
- HTTP Requests
- Base64 Encoding
- File Upload Handling
- JSON Parsing
- AI API Integration

---

## ⚠️ Limitations

- Depends on external API accuracy
- Requires internet connection
- Some plants may not have common names
- Free API tier may have request limits

---

## 💡 Future Improvements

- Deploy online (so others can use it)
- Add mobile support
- Show plant details (uses, region, etc.)
- Add drag & drop upload
- Improve UI/UX

---

## 👨‍💻 Author

- Priti and PRITI
---

## 📌 Note

This project demonstrates how to integrate AI APIs into real-world applications without building models from scratch.


Push Folder to GitHub

Pushing a folder to GitHub involves initializing it as a Git repository, committing the files, and linking it to a remote repository. Follow these steps to achieve this:

1. Prepare Your Folder

Ensure Git is installed on your system. Verify by running:

git --version
Copy
Navigate to the folder you want to push:

cd /path/to/your/folder
Copy
2. Initialize the Repository

Initialize the folder as a Git repository:

git init
Copy
Add all files in the folder to the staging area:

git add
Copy
Commit the files with a descriptive message:

git commit -m "Initial commit"
Copy
3. Create a Remote Repository on GitHub

Log in to your GitHub account and create a new repository.

Copy the repository URL (e.g., https://github.com/yourusername/your-repository.git).

4. Link Local Repository to GitHub

Add the remote repository URL:

git remote add origin https://github.com/yourusername/your-repository.git
Copy
Push the files to GitHub:

git push -u origin main
Copy
5. Verify on GitHub

Visit your GitHub repository in a browser to confirm that all files have been uploaded.

Tips for Future Updates

After making changes, repeat these commands:

git add
git commit -m "Your commit message"
git push
Copy
By following these steps, you can efficiently manage and share your projects on GitHub.








How to run 
Go to current repo and: python -m uvicorn main:app --reload