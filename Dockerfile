FROM python:3.13.7
EXPOSE 5000
EXPOSE 5001
WORKDIR /app
# For ffprobe
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    rm -rf /var/lib/apt/lists/*notes
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_RUN_PORT=5001
COPY requirements.txt .
RUN pip install -r requirements.txt 
CMD ["flask", "run", "--host=0.0.0.0", "--reload"]
# docker build -t r3vids-api .
# docker run -it --rm  r3vids-api:latest
# docker run -it --rm -p 5000:5000 r3vids-api:latest
