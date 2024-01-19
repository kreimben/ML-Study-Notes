#!/usr/bin/env sh
# check venv
if [ -z "$VIRTUAL_ENV" ]; then
    echo "No virtual environment detected"
    echo "Please activate your virtual environment"
    exit 1
fi
# install preview packages
pip install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu


#pip install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu
