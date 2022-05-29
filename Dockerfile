# Add python env to the build
FROM python:3.9-slim

# Add PYTHONPATH system param
WORKDIR $HOME/code

# Add required files for the project
ADD requirements.txt .
ADD functions ./functions
ADD other ./other
ADD tgfunks ./tgfunks
ADD main.py .

# Install required packages
RUN pip install --user -r ./requirements.txt

# Run application
CMD ["python", "bot.py"]
#CMD ["sh", "-c", "python", "bot.py"]