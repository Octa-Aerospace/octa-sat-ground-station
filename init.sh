echo "Starting Device..."
echo "[ 0 ] Installing dependencies."
pip3 install -r requirements.txt
echo "[ 1 ] Dependencies successfully installed."
echo "[ 0 ] Running octaAPI.py with Uvicorn in the background."
uvicorn octaAPI:app &
echo "[ 0 ] Running main script in the background."
python3 main.py &

