# Natrul AI | Demo Flask App

This is a lightweight Flask application demonstrating how to quickly integrate with the [Natrul AI](https://www.natrul.ai) API platform.

It showcases how to:
- Query AI models using your own uploaded documents
- Retrieve relevant document context
- Enhance user input with smart AI suggestions
- Manage context through a no-code dashboard

---

## 🚀 Getting Started

### 1. Fork the Repository

Click **Fork** at the top of the repository to create your own copy.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/natrul-ai-demo.git
cd natrul-ai-demo
```

### 3. Install Dependencies

Make sure you have a virtual environment set up, then run:

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root of the project and add your credentials:

```env
app_id=your_natrul_app_id
owner_id=your_natrul_owner_id
```

You can obtain both by:
- Signing up at [https://www.natrul.ai](https://www.natrul.ai)
- Navigating to your [Workspace](https://www.natrul.ai/workspace)
- Creating an app and uploading at least one document

---

## 🧪 Running the App

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

You can sign in with any email associated with the users in your app (see the **Users** section on your app's dashboard in Natrul AI).

---

## ✨ Features

- **Ask**: Ask questions and receive context-aware answers powered by your uploaded documents.
- **Search**: Retrieve relevant document excerpts via vector search.
- **Create**: Use AI to enhance typed input (e.g. formatting raw input into polished email copy).
- **My Context**: Direct link to manage documents in your [Natrul AI dashboard](https://www.natrul.ai/my-context).

---

## 🔒 Authentication Note

The sign-in flow is for demo purposes and uses a simplified validation check against the user list from Natrul AI.  
**You should enhance authentication if adapting this app for production.**

---

## 📬 Support

For help, feature requests, or bug reports, email us at **[support@natrul.ai](mailto:support@natrul.ai)**.

---

## 📄 License

This project is open for forking and modification. Feel free to use it as a foundation for your own Natrul AI-powered project.
