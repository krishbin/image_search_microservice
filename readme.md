# Connecting Text and Images Project

This project is designed to connect text and images using a Milvus database, providing a seamless search experience.

## Milvus Server Setup

1. Navigate to the `milvus_server` folder:
    ```bash
    cd milvus_server
    ```

2. Run Docker Compose to set up the Milvus database:
    ```bash
    docker-compose up -d
    ```

## Backend Setup

1. Return to the root folder:
    ```bash
    cd ..
    ```

2. (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux
    .\venv\Scripts\activate   # Windows
    ```

3. Install required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Install the CLIP library:
    ```bash
    pip install git+https://github.com/openai/CLIP.git
    ```

5. Run the backend server:
    ```bash
    uvicorn main:imagesearch --reload
    ```

## Frontend Setup

1. Return to the root folder:
    ```bash
    cd ..
    ```

2. Enter the `frontend` directory:
    ```bash
    cd frontend
    ```

3. Install Node.js dependencies:
    ```bash
    npm install
    ```

4. Run the frontend application using Vite:
    ```bash
    npx vite
    ```

Your project is now set up, and you can explore the connected text and images functionality. Open your browser and access the specified localhost address for the frontend application.

Feel free to customize and add more details as needed!
