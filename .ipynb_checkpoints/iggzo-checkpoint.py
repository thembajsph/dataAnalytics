{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import libraries\n",
    "import streamlit as st\n",
    "import math\n",
    "import pandas_datareader as web\n",
    "import  numpy as np\n",
    "import pandas as pd \n",
    "from sklearn.preprocessing import MinMaxScaler\n",
    "from keras.models import Sequential \n",
    "from keras.layers import Dense, LSTM\n",
    "import matplotlib.pyplot as plt\n",
    "plt.style.use('fivethirtyeight')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (0.84.0)\n",
      "Requirement already satisfied: toml in /home/thembajsph/.local/lib/python3.8/site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: tornado>=5.0 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from streamlit) (6.0.4)\n",
      "Requirement already satisfied: validators in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from streamlit) (0.18.2)\n",
      "Requirement already satisfied: blinker in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from streamlit) (1.4)\n",
      "Requirement already satisfied: python-dateutil in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from streamlit) (2.8.1)\n",
      "Requirement already satisfied: pyarrow; python_version < \"3.9\" in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from streamlit) (4.0.1)\n",
      "Requirement already satisfied: protobuf!=3.11,>=3.6.0 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from streamlit) (3.15.7)\n",
      "Requirement already satisfied: numpy in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from streamlit) (1.19.2)\n",
      "Requirement already satisfied: pandas>=0.21.0 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from streamlit) (1.1.3)\n",
      "Requirement already satisfied: click<8.0,>=7.0 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from streamlit) (7.1.2)\n",
      "Requirement already satisfied: gitpython in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from streamlit) (3.1.18)\n",
      "Requirement already satisfied: altair>=3.2.0 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from streamlit) (4.1.0)\n",
      "Requirement already satisfied: base58 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from streamlit) (2.1.0)\n",
      "Requirement already satisfied: pydeck>=0.1.dev5 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from streamlit) (0.6.2)\n",
      "Requirement already satisfied: pillow>=6.2.0 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from streamlit) (8.0.1)\n",
      "Requirement already satisfied: astor in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from streamlit) (0.8.1)\n",
      "Requirement already satisfied: packaging in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from streamlit) (20.4)\n",
      "Requirement already satisfied: attrs in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from streamlit) (20.3.0)\n",
      "Requirement already satisfied: watchdog; platform_system != \"Darwin\" in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from streamlit) (0.10.3)\n",
      "Requirement already satisfied: tzlocal in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from streamlit) (2.1)\n",
      "Requirement already satisfied: requests in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from streamlit) (2.24.0)\n",
      "Requirement already satisfied: cachetools>=4.0 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from streamlit) (4.2.1)\n",
      "Requirement already satisfied: six>=1.4.0 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from validators->streamlit) (1.15.0)\n",
      "Requirement already satisfied: decorator>=3.4.0 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from validators->streamlit) (4.4.2)\n",
      "Requirement already satisfied: pytz>=2017.2 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from pandas>=0.21.0->streamlit) (2020.1)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from gitpython->streamlit) (4.0.7)\n",
      "Requirement already satisfied: jinja2 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from altair>=3.2.0->streamlit) (2.11.2)\n",
      "Requirement already satisfied: entrypoints in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from altair>=3.2.0->streamlit) (0.3)\n",
      "Requirement already satisfied: toolz in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from altair>=3.2.0->streamlit) (0.11.1)\n",
      "Requirement already satisfied: jsonschema in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from altair>=3.2.0->streamlit) (3.2.0)\n",
      "Requirement already satisfied: ipywidgets>=7.0.0 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from pydeck>=0.1.dev5->streamlit) (7.5.1)\n",
      "Requirement already satisfied: ipykernel>=5.1.2; python_version >= \"3.4\" in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from pydeck>=0.1.dev5->streamlit) (5.3.4)\n",
      "Requirement already satisfied: traitlets>=4.3.2 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from pydeck>=0.1.dev5->streamlit) (5.0.5)\n",
      "Requirement already satisfied: pyparsing>=2.0.2 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from packaging->streamlit) (2.4.7)\n",
      "Requirement already satisfied: pathtools>=0.1.1 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from watchdog; platform_system != \"Darwin\"->streamlit) (0.1.2)\n",
      "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from requests->streamlit) (1.25.11)\n",
      "Requirement already satisfied: chardet<4,>=3.0.2 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from requests->streamlit) (3.0.4)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from requests->streamlit) (2020.6.20)\n",
      "Requirement already satisfied: idna<3,>=2.5 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from requests->streamlit) (2.10)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from gitdb<5,>=4.0.1->gitpython->streamlit) (4.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from jinja2->altair>=3.2.0->streamlit) (1.1.1)\n",
      "Requirement already satisfied: setuptools in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from jsonschema->altair>=3.2.0->streamlit) (50.3.1.post20201107)\n",
      "Requirement already satisfied: pyrsistent>=0.14.0 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from jsonschema->altair>=3.2.0->streamlit) (0.17.3)\n",
      "Requirement already satisfied: widgetsnbextension~=3.5.0 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (3.5.1)\n",
      "Requirement already satisfied: ipython>=4.0.0; python_version >= \"3.3\" in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (7.19.0)\n",
      "Requirement already satisfied: nbformat>=4.2.0 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.0.8)\n",
      "Requirement already satisfied: jupyter-client in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (6.1.7)\n",
      "Requirement already satisfied: ipython-genutils in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from traitlets>=4.3.2->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
      "Requirement already satisfied: notebook>=4.4.1 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (6.1.4)\n",
      "Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from ipython>=4.0.0; python_version >= \"3.3\"->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (3.0.8)\n",
      "Requirement already satisfied: pickleshare in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from ipython>=4.0.0; python_version >= \"3.3\"->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.7.5)\n",
      "Requirement already satisfied: pygments in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from ipython>=4.0.0; python_version >= \"3.3\"->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (2.7.2)\n",
      "Requirement already satisfied: backcall in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from ipython>=4.0.0; python_version >= \"3.3\"->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.2.0)\n",
      "Requirement already satisfied: jedi>=0.10 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from ipython>=4.0.0; python_version >= \"3.3\"->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.17.1)\n",
      "Requirement already satisfied: pexpect>4.3; sys_platform != \"win32\" in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from ipython>=4.0.0; python_version >= \"3.3\"->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (4.8.0)\n",
      "Requirement already satisfied: jupyter-core in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from nbformat>=4.2.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (4.6.3)\n",
      "Requirement already satisfied: pyzmq>=13 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from jupyter-client->ipykernel>=5.1.2; python_version >= \"3.4\"->pydeck>=0.1.dev5->streamlit) (19.0.2)\n",
      "Requirement already satisfied: nbconvert in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (6.0.7)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: prometheus-client in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.8.0)\n",
      "Requirement already satisfied: Send2Trash in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.5.0)\n",
      "Requirement already satisfied: terminado>=0.8.3 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.9.1)\n",
      "Requirement already satisfied: argon2-cffi in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (20.1.0)\n",
      "Requirement already satisfied: wcwidth in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=4.0.0; python_version >= \"3.3\"->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.2.5)\n",
      "Requirement already satisfied: parso<0.8.0,>=0.7.0 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from jedi>=0.10->ipython>=4.0.0; python_version >= \"3.3\"->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.7.0)\n",
      "Requirement already satisfied: ptyprocess>=0.5 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from pexpect>4.3; sys_platform != \"win32\"->ipython>=4.0.0; python_version >= \"3.3\"->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.6.0)\n",
      "Requirement already satisfied: bleach in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (3.2.1)\n",
      "Requirement already satisfied: mistune<2,>=0.8.1 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.8.4)\n",
      "Requirement already satisfied: testpath in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.4.4)\n",
      "Requirement already satisfied: pandocfilters>=1.4.1 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.4.3)\n",
      "Requirement already satisfied: nbclient<0.6.0,>=0.5.0 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.1)\n",
      "Requirement already satisfied: defusedxml in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.6.0)\n",
      "Requirement already satisfied: jupyterlab-pygments in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.1.2)\n",
      "Requirement already satisfied: cffi>=1.0.0 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.14.3)\n",
      "Requirement already satisfied: webencodings in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.1)\n",
      "Requirement already satisfied: nest-asyncio in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from nbclient<0.6.0,>=0.5.0->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.4.2)\n",
      "Requirement already satisfied: async-generator in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from nbclient<0.6.0,>=0.5.0->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.10)\n",
      "Requirement already satisfied: pycparser in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from cffi>=1.0.0->argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (2.20)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2021-07-11 00:17:45.619 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages/ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "st.write(\"description: this program uses an artificial neural network called lon short Term Memory (LSTM)to prsedict the closing stock price of corporation(Apple Inc.) using the past 60 day stock price.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting tensorflow\n",
      "  Downloading tensorflow-2.4.1-cp38-cp38-manylinux2010_x86_64.whl (394.4 MB)\n",
      "\u001b[K     |????????????????????????????????????????????????????????????????????????????????????????????????| 394.4 MB 1.8 kB/s eta 0:00:01    |????????????????????????                        | 94.2 MB 1.9 MB/s eta 0:02:41     |????????????????????????                        | 97.9 MB 3.5 MB/s eta 0:01:24     |??????????????????????????????                      | 116.6 MB 727 kB/s eta 0:06:22     |??????????????????????????????                      | 119.5 MB 411 kB/s eta 0:11:08     |??????????????????????????????????????????????????????              | 214.1 MB 1.1 MB/s eta 0:02:38\n",
      "\u001b[?25hRequirement already satisfied: six~=1.15.0 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from tensorflow) (1.15.0)\n",
      "\u001b[33mWARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ProtocolError('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))': /simple/astunparse/\u001b[0m\n",
      "Collecting astunparse~=1.6.3\n",
      "  Downloading astunparse-1.6.3-py2.py3-none-any.whl (12 kB)\n",
      "Collecting gast==0.3.3\n",
      "  Downloading gast-0.3.3-py2.py3-none-any.whl (9.7 kB)\n",
      "Requirement already satisfied: wrapt~=1.12.1 in /home/thembajsph/.local/lib/python3.8/site-packages (from tensorflow) (1.12.1)\n",
      "Collecting tensorflow-estimator<2.5.0,>=2.4.0\n",
      "  Downloading tensorflow_estimator-2.4.0-py2.py3-none-any.whl (462 kB)\n",
      "\u001b[K     |????????????????????????????????????????????????????????????????????????????????????????????????| 462 kB 338 kB/s eta 0:00:01\n",
      "\u001b[?25hRequirement already satisfied: h5py~=2.10.0 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from tensorflow) (2.10.0)\n",
      "Collecting termcolor~=1.1.0\n",
      "  Downloading termcolor-1.1.0.tar.gz (3.9 kB)\n",
      "Requirement already satisfied: wheel~=0.35 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from tensorflow) (0.35.1)\n",
      "Requirement already satisfied: numpy~=1.19.2 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from tensorflow) (1.19.2)\n",
      "Collecting keras-preprocessing~=1.1.2\n",
      "  Downloading Keras_Preprocessing-1.1.2-py2.py3-none-any.whl (42 kB)\n",
      "\u001b[K     |????????????????????????????????????????????????????????????????????????????????????????????????| 42 kB 143 kB/s eta 0:00:01\n",
      "\u001b[?25hCollecting google-pasta~=0.2\n",
      "  Downloading google_pasta-0.2.0-py3-none-any.whl (57 kB)\n",
      "\u001b[K     |????????????????????????????????????????????????????????????????????????????????????????????????| 57 kB 455 kB/s eta 0:00:01\n",
      "\u001b[?25hCollecting protobuf>=3.9.2\n",
      "  Downloading protobuf-3.15.7-cp38-cp38-manylinux1_x86_64.whl (1.0 MB)\n",
      "\u001b[K     |????????????????????????????????????????????????????????????????????????????????????????????????| 1.0 MB 518 kB/s eta 0:00:01\n",
      "\u001b[?25hRequirement already satisfied: typing-extensions~=3.7.4 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from tensorflow) (3.7.4.3)\n",
      "Collecting grpcio~=1.32.0\n",
      "  Downloading grpcio-1.32.0-cp38-cp38-manylinux2014_x86_64.whl (3.8 MB)\n",
      "\u001b[K     |????????????????????????????????????????????????????????????????????????????????????????????????| 3.8 MB 743 kB/s eta 0:00:01\n",
      "\u001b[?25hCollecting opt-einsum~=3.3.0\n",
      "  Downloading opt_einsum-3.3.0-py3-none-any.whl (65 kB)\n",
      "\u001b[K     |????????????????????????????????????????????????????????????????????????????????????????????????| 65 kB 317 kB/s eta 0:00:01\n",
      "\u001b[?25hCollecting flatbuffers~=1.12.0\n",
      "  Downloading flatbuffers-1.12-py2.py3-none-any.whl (15 kB)\n",
      "Collecting absl-py~=0.10\n",
      "  Downloading absl_py-0.12.0-py3-none-any.whl (129 kB)\n",
      "\u001b[K     |????????????????????????????????????????????????????????????????????????????????????????????????| 129 kB 1.4 MB/s eta 0:00:01\n",
      "\u001b[?25hCollecting tensorboard~=2.4\n",
      "  Downloading tensorboard-2.4.1-py3-none-any.whl (10.6 MB)\n",
      "\u001b[K     |????????????????????????????????????????????????????????????????????????????????????????????????| 10.6 MB 213 kB/s eta 0:00:01    |??????????????????????????????????????????????????????????????????????????????????????????  | 9.8 MB 1.6 MB/s eta 0:00:01\n",
      "\u001b[?25hCollecting markdown>=2.6.8\n",
      "  Downloading Markdown-3.3.4-py3-none-any.whl (97 kB)\n",
      "\u001b[K     |????????????????????????????????????????????????????????????????????????????????????????????????| 97 kB 821 kB/s eta 0:00:01\n",
      "\u001b[?25hCollecting google-auth-oauthlib<0.5,>=0.4.1\n",
      "  Downloading google_auth_oauthlib-0.4.4-py2.py3-none-any.whl (18 kB)\n",
      "Requirement already satisfied: requests<3,>=2.21.0 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from tensorboard~=2.4->tensorflow) (2.24.0)\n",
      "Requirement already satisfied: werkzeug>=0.11.15 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from tensorboard~=2.4->tensorflow) (1.0.1)\n",
      "Requirement already satisfied: setuptools>=41.0.0 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from tensorboard~=2.4->tensorflow) (50.3.1.post20201107)\n",
      "Collecting google-auth<2,>=1.6.3\n",
      "  Downloading google_auth-1.28.0-py2.py3-none-any.whl (136 kB)\n",
      "\u001b[K     |????????????????????????????????????????????????????????????????????????????????????????????????| 136 kB 1.3 MB/s eta 0:00:01\n",
      "\u001b[?25hCollecting tensorboard-plugin-wit>=1.6.0\n",
      "  Downloading tensorboard_plugin_wit-1.8.0-py3-none-any.whl (781 kB)\n",
      "\u001b[K     |????????????????????????????????????????????????????????????????????????????????????????????????| 781 kB 1.4 MB/s eta 0:00:01\n",
      "\u001b[?25hCollecting requests-oauthlib>=0.7.0\n",
      "  Using cached requests_oauthlib-1.3.0-py2.py3-none-any.whl (23 kB)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from requests<3,>=2.21.0->tensorboard~=2.4->tensorflow) (2020.6.20)\n",
      "Requirement already satisfied: chardet<4,>=3.0.2 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from requests<3,>=2.21.0->tensorboard~=2.4->tensorflow) (3.0.4)\n",
      "Requirement already satisfied: idna<3,>=2.5 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from requests<3,>=2.21.0->tensorboard~=2.4->tensorflow) (2.10)\n",
      "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /home/thembajsph/Downloads/anaconda/lib/python3.8/site-packages (from requests<3,>=2.21.0->tensorboard~=2.4->tensorflow) (1.25.11)\n",
      "Collecting cachetools<5.0,>=2.0.0\n",
      "  Downloading cachetools-4.2.1-py3-none-any.whl (12 kB)\n",
      "Collecting pyasn1-modules>=0.2.1\n",
      "  Downloading pyasn1_modules-0.2.8-py2.py3-none-any.whl (155 kB)\n",
      "\u001b[K     |????????????????????????????????????????????????????????????????????????????????????????????????| 155 kB 1.1 MB/s eta 0:00:01\n",
      "\u001b[?25hCollecting rsa<5,>=3.1.4; python_version >= \"3.6\"\n",
      "  Downloading rsa-4.7.2-py3-none-any.whl (34 kB)\n",
      "Collecting oauthlib>=3.0.0\n",
      "  Using cached oauthlib-3.1.0-py2.py3-none-any.whl (147 kB)\n",
      "Collecting pyasn1<0.5.0,>=0.4.6\n",
      "  Using cached pyasn1-0.4.8-py2.py3-none-any.whl (77 kB)\n",
      "Building wheels for collected packages: termcolor\n",
      "  Building wheel for termcolor (setup.py) ... \u001b[?25ldone\n",
      "\u001b[?25h  Created wheel for termcolor: filename=termcolor-1.1.0-py3-none-any.whl size=4830 sha256=b9f7dc2bfc693d4a5726296c954157457455b72b1e523e128265b6ac21561a6f\n",
      "  Stored in directory: /home/thembajsph/.cache/pip/wheels/a0/16/9c/5473df82468f958445479c59e784896fa24f4a5fc024b0f501\n",
      "Successfully built termcolor\n",
      "Installing collected packages: astunparse, gast, tensorflow-estimator, termcolor, keras-preprocessing, google-pasta, protobuf, grpcio, opt-einsum, flatbuffers, absl-py, markdown, oauthlib, requests-oauthlib, cachetools, pyasn1, pyasn1-modules, rsa, google-auth, google-auth-oauthlib, tensorboard-plugin-wit, tensorboard, tensorflow\n",
      "Successfully installed absl-py-0.12.0 astunparse-1.6.3 cachetools-4.2.1 flatbuffers-1.12 gast-0.3.3 google-auth-1.28.0 google-auth-oauthlib-0.4.4 google-pasta-0.2.0 grpcio-1.32.0 keras-preprocessing-1.1.2 markdown-3.3.4 oauthlib-3.1.0 opt-einsum-3.3.0 protobuf-3.15.7 pyasn1-0.4.8 pyasn1-modules-0.2.8 requests-oauthlib-1.3.0 rsa-4.7.2 tensorboard-2.4.1 tensorboard-plugin-wit-1.8.0 tensorflow-2.4.1 tensorflow-estimator-2.4.0 termcolor-1.1.0\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install tensorflow"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Open</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Adj Close</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2015-05-15</th>\n",
       "      <td>1920.0</td>\n",
       "      <td>1920.0</td>\n",
       "      <td>1920.0</td>\n",
       "      <td>1920.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1823.070679</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-05-18</th>\n",
       "      <td>2024.0</td>\n",
       "      <td>1897.0</td>\n",
       "      <td>1940.0</td>\n",
       "      <td>2024.0</td>\n",
       "      <td>45780048.0</td>\n",
       "      <td>1921.820435</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-05-19</th>\n",
       "      <td>2233.0</td>\n",
       "      <td>2116.0</td>\n",
       "      <td>2215.0</td>\n",
       "      <td>2170.0</td>\n",
       "      <td>47074401.0</td>\n",
       "      <td>2060.449463</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-05-20</th>\n",
       "      <td>2195.0</td>\n",
       "      <td>2145.0</td>\n",
       "      <td>2190.0</td>\n",
       "      <td>2149.0</td>\n",
       "      <td>16444462.0</td>\n",
       "      <td>2040.510010</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-05-21</th>\n",
       "      <td>2198.0</td>\n",
       "      <td>2165.0</td>\n",
       "      <td>2170.0</td>\n",
       "      <td>2175.0</td>\n",
       "      <td>11874554.0</td>\n",
       "      <td>2065.197021</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-04-12</th>\n",
       "      <td>3215.0</td>\n",
       "      <td>3177.0</td>\n",
       "      <td>3218.0</td>\n",
       "      <td>3185.0</td>\n",
       "      <td>32172.0</td>\n",
       "      <td>3185.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-04-13</th>\n",
       "      <td>3199.0</td>\n",
       "      <td>3177.0</td>\n",
       "      <td>3185.0</td>\n",
       "      <td>3177.0</td>\n",
       "      <td>13719.0</td>\n",
       "      <td>3177.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-04-14</th>\n",
       "      <td>3249.0</td>\n",
       "      <td>3190.0</td>\n",
       "      <td>3249.0</td>\n",
       "      <td>3197.0</td>\n",
       "      <td>231824.0</td>\n",
       "      <td>3197.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-04-15</th>\n",
       "      <td>3271.0</td>\n",
       "      <td>3222.0</td>\n",
       "      <td>3180.0</td>\n",
       "      <td>3252.0</td>\n",
       "      <td>83238.0</td>\n",
       "      <td>3252.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-04-16</th>\n",
       "      <td>3204.0</td>\n",
       "      <td>3169.0</td>\n",
       "      <td>3175.0</td>\n",
       "      <td>3200.0</td>\n",
       "      <td>116174.0</td>\n",
       "      <td>3200.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1505 rows ?? 6 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "              High     Low    Open   Close      Volume    Adj Close\n",
       "Date                                                               \n",
       "2015-05-15  1920.0  1920.0  1920.0  1920.0         0.0  1823.070679\n",
       "2015-05-18  2024.0  1897.0  1940.0  2024.0  45780048.0  1921.820435\n",
       "2015-05-19  2233.0  2116.0  2215.0  2170.0  47074401.0  2060.449463\n",
       "2015-05-20  2195.0  2145.0  2190.0  2149.0  16444462.0  2040.510010\n",
       "2015-05-21  2198.0  2165.0  2170.0  2175.0  11874554.0  2065.197021\n",
       "...            ...     ...     ...     ...         ...          ...\n",
       "2021-04-12  3215.0  3177.0  3218.0  3185.0     32172.0  3185.000000\n",
       "2021-04-13  3199.0  3177.0  3185.0  3177.0     13719.0  3177.000000\n",
       "2021-04-14  3249.0  3190.0  3249.0  3197.0    231824.0  3197.000000\n",
       "2021-04-15  3271.0  3222.0  3180.0  3252.0     83238.0  3252.000000\n",
       "2021-04-16  3204.0  3169.0  3175.0  3200.0    116174.0  3200.000000\n",
       "\n",
       "[1505 rows x 6 columns]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Get the stock quote\n",
    "df  = web.DataReader('S32.JO', data_source='yahoo', start='2012-01-01', end='2021-04-21')\n",
    "#Show the data\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Open</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Adj Close</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2021-04-08</th>\n",
       "      <td>130.389999</td>\n",
       "      <td>128.520004</td>\n",
       "      <td>128.949997</td>\n",
       "      <td>130.360001</td>\n",
       "      <td>88844600.0</td>\n",
       "      <td>130.360001</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-04-09</th>\n",
       "      <td>133.039993</td>\n",
       "      <td>129.470001</td>\n",
       "      <td>129.800003</td>\n",
       "      <td>133.000000</td>\n",
       "      <td>106513800.0</td>\n",
       "      <td>133.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-04-12</th>\n",
       "      <td>132.850006</td>\n",
       "      <td>130.630005</td>\n",
       "      <td>132.520004</td>\n",
       "      <td>131.240005</td>\n",
       "      <td>91420000.0</td>\n",
       "      <td>131.240005</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-04-13</th>\n",
       "      <td>134.660004</td>\n",
       "      <td>131.929993</td>\n",
       "      <td>132.440002</td>\n",
       "      <td>134.429993</td>\n",
       "      <td>91266500.0</td>\n",
       "      <td>134.429993</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-04-14</th>\n",
       "      <td>135.000000</td>\n",
       "      <td>131.660004</td>\n",
       "      <td>134.940002</td>\n",
       "      <td>132.029999</td>\n",
       "      <td>87222800.0</td>\n",
       "      <td>132.029999</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-04-15</th>\n",
       "      <td>135.000000</td>\n",
       "      <td>133.639999</td>\n",
       "      <td>133.820007</td>\n",
       "      <td>134.500000</td>\n",
       "      <td>89347100.0</td>\n",
       "      <td>134.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-04-16</th>\n",
       "      <td>134.669998</td>\n",
       "      <td>133.279999</td>\n",
       "      <td>134.300003</td>\n",
       "      <td>134.160004</td>\n",
       "      <td>84818500.0</td>\n",
       "      <td>134.160004</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  High         Low        Open       Close       Volume  \\\n",
       "Date                                                                      \n",
       "2021-04-08  130.389999  128.520004  128.949997  130.360001   88844600.0   \n",
       "2021-04-09  133.039993  129.470001  129.800003  133.000000  106513800.0   \n",
       "2021-04-12  132.850006  130.630005  132.520004  131.240005   91420000.0   \n",
       "2021-04-13  134.660004  131.929993  132.440002  134.429993   91266500.0   \n",
       "2021-04-14  135.000000  131.660004  134.940002  132.029999   87222800.0   \n",
       "2021-04-15  135.000000  133.639999  133.820007  134.500000   89347100.0   \n",
       "2021-04-16  134.669998  133.279999  134.300003  134.160004   84818500.0   \n",
       "\n",
       "             Adj Close  \n",
       "Date                    \n",
       "2021-04-08  130.360001  \n",
       "2021-04-09  133.000000  \n",
       "2021-04-12  131.240005  \n",
       "2021-04-13  134.429993  \n",
       "2021-04-14  132.029999  \n",
       "2021-04-15  134.500000  \n",
       "2021-04-16  134.160004  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail(7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1505, 6)"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Get the number of row and columns in data set\n",
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABDUAAAIdCAYAAAAtX0aAAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAADPTElEQVR4nOzdd3wTBf8H8M9lNk33prTsWRRQkK2CoiiIgnuhDw5cj4/6ONHf4+Pj41ZUnkfF7ePGLaAgyh6yZG8qe3XPtEmz7vdH6cjl7pK0SZu0n/fr5Ut6uSSXNM3dfe87hLKyMhFERERERERERBFG09obQERERERERETUFAxqEBEREREREVFEYlCDiIiIiIiIiCISgxpEREREREREFJEY1CAiIiIiIiKiiMSgBhERERERERFFJAY1iIiIwlxCQgImTJjQ2psRFp5//nkkJCRg5cqVrb0pzTZhwgQkJCS09mYQERFFNAY1iIiIWtiff/6Jxx57DCNHjkSnTp2QmpqKnj17YvLkyXj33XdRUVHR2psYNHfddRcSEhI8/uvQoQPOOussPPLIIzh58mRrb2KznH766UhISMDhw4cV16l7Dz7//POQPDcREVF7pmvtDSAiImpPZsyYgWeffRZutxuDBg3CNddcg7i4OBQVFWHNmjV45JFH8MILL+DAgQOtvalBNX78eJx++ukAgKKiIixevBjvvvsuvv/+eyxevBidO3f263GmTZuGK664AllZWaHc3Bbx9ttvw2q1tvZmEBERRTQGNYiIiFrI66+/jn//+9/o2LEjPvzwQwwdOtRrndWrV+ORRx5pha0LrQkTJuCGG26o/9nhcODyyy/HypUr8fLLL+ONN97w63GSk5ORnJwcqs1sUdnZ2a29CURERBGP5SdEREQt4MiRI3j22Weh1+sxe/Zs2YAGAIwcORJLlizx6zErKirw73//G2eddRbS09PRqVMnXHLJJZg3b57s+vPmzcOll16K3r17Iy0tDb1798a4ceMwY8YMr3VtNhv++9//4txzz0XHjh2RmZmJ0aNH48MPP4Qoiv6/cAV6vR5Tp04FAGzcuLF+eV1Jhc1mwzPPPIMzzjgDqampeOyxxwCo99TYv38/7rvvPgwYMADp6eno2rUrzjvvPLz88ste6+bn5+Oxxx7DmWeeifT0dHTu3BmTJ0/G8uXLm/3a/CXXU0MURXz22We48MIL0b17d6SnpyMnJwcTJ07Exx9/DAA4fPgwEhIScPToUQDwKO2R9l7ZunUrbr75ZvTs2ROpqano168f7rnnHhw6dMhre+re288//xwLFizARRddhOzsbHTu3Bm7d+9GQkICLrnkEsXXc9FFFyEhIQH79u1r3htDREQUAGZqEBERtYDPP/8cDocDkydPri/DUGI0Gn0+XllZGS666CLs2bMH/fv3x5133ony8nL8+OOPmDJlCh555BE8/vjj9et/8MEHePDBB5GWloZx48YhNTUVxcXF2Lt3Lz766CM8+OCD9etWVlZi0qRJ2LhxI/r374/rr78eALB48WL8/e9/x4YNGzBr1qwmvhP+uemmm7Bt2zacf/75SExMRJcuXVTXX7RoEW666SZYrVaMHj0akydPRlVVFXbv3o3nn38eDz/8cP26O3fuxOTJk1FYWIjzzjsP48ePR0lJCX7++WdMmjQJ//nPfzBlypSQvj4lTz31FGbOnIlOnTph0qRJiI+PR35+Pnbs2IHZs2fj5ptvRnx8PB599FHMmjULFRUVePTRR+vv36lTp/p///LLL7jpppvgdrsxceJEdO3aFTt37sTnn3+On376CXPnzsWAAQO8tuHHH3/EkiVLcOGFF2Lq1KnIz89H3759MXLkSKxatQr79u1Dr169PO6za9curF27FqNGjfK6jYiIKJQY1CAiImoBa9asAQCMGTMmKI/31FNPYc+ePbjhhhvwxhtvQBAEAMDDDz9cn50wbtw4DBo0CADw8ccfw2AwYOXKlUhPT/d4rOLiYo+fH3/8cWzcuBFPPfUU7r///vrlNTU1mDJlCr788ktMnDgR48ePb/L2O51O/O9//wMAnHnmmV63Hzt2DKtXr/ar1KS4uBi33HILbDYbvvnmG4wdO9brseq4XC7cfPPNKC8vx7x58zBq1Kj62/Ly8nD++efj4Ycfxrhx45CWlub365k1axbi4+Nlb9u+fbvfj/Pxxx+jQ4cOWLNmDcxms8dtdb+nhIQETJ8+HV988QUqKiowffp0r8exWCy4++674XA4MGfOHJxzzjn1t33yySf429/+hjvvvBO///57/WenzqJFi2Tfx9tvvx2rV6/GRx99hOeff97jto8++ggAcOutt/r9WomIiIKBQQ0iIqIWkJ+fDwDIzMxs9mM5HA58/fXXiI6Oxr/+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xx1ISEioXzc2NhY//fQTPv30U3zzzTf46aefYLPZkJqaik6dOuHJJ5/0CIKEg7Fjx2LZsmV4/fXXsXz5cqxcuRKxsbHo1q0bHn/8cY91c3JysHr1asyaNQvz58/Hl19+CVEUkZ6ejj59+uDee+9Fz549W/w1mM1mPP3001i5ciU2bNiABQsWwGQyoXPnznjmmWcwdepUj1GvDz74ICoqKjB//nzMnDkTTqcTI0eOxLXXXgsAuOiii/Drr7/i1VdfxfLlyzFnzhykpqbiuuuuwyOPPIIuXbo0eVuvueYaPPbYYwCAKVOmNOt1ExERNYdQVlYm+l6NiIiIiKjWunXrMG7cOEyaNAn/+9//WntziIioHWOuIBEREREF5NVXXwUA3H777a28JURE1N6x/ISIiIiIfNqxYwfmz5+Pbdu2YeHChTjvvPMwcuTI1t4sIiJq5xjUICIiIiKftm7diueeew5xcXG49NJLMWPGjNbeJCIiIvbUICIiIiIiIqLIxJ4aRERERERERBSRGNQgIiIiIiIioojEoAYRERERERERRSQGNYiCJDc3t7U3gdoBfs6oJfBzRi2BnzMKNX7GqKXws9a6GNQgIiIiIiIioojEoAYRERERERERRSQGNYiIiIiIiIgoIjGoQUREREREREQRiUENIiIiIiIiIopIDGoQERERERERUURiUIOIiIiIiIiIIhKDGkREREREREQUkRjUICIiIiIiIqKIxKAGEREREREREUUkBjWIiIiIiIiIKCIxqEFEREREREREEYlBDSIiIiIiIiKKSAxqEBEREREREVFEYlCDiIiIiIiIiCISgxpEREREREREFJEY1CAiIiJqg3LLHRjxYz46fnoCr2ytbO3NISIiCgkGNYiIiIjaoFe3WbCr1Ikqp4hnN1XgqMXZ2ptEREQUdAxqEBEREbVBX/5ZXf9vEcCnudXKKxMREUUoBjWIiIiI2gGbU2ztTSAiIgo6BjWIiIiI2gGbi0ENIiJqexjUICIiImoHGNQgIqK2iEENIiIionaAQQ0iImqLGNQgIiIiagdqGNQgIqI2iEENIiIionaAjUKJiKgtYlCDiIiIqB2wMKhBRERtEIMaRERERO2AxcGgBhERtT0MahARERG1MaLoHcCotLtbYUuIiIhCi0ENIiIiojbGIRO/KKlhUIOIiNoeBjWIiIiI2hi72ztTo8wuwimznIiIKJIxqEFERETUxshlagDM1iAioraHQQ0iIiKiNqbGJZ+RUWxjUIOIiNoWBjWIiIiI2hi58hMAKGamBhERtTEMahARERG1MQ6X/HJmahARUVvDoAYRERFRG1OjlKnBoAYREbUxDGoQERERtTF2xZ4aCikcREREEYpBDSIiIqI2Rmn6CXtqEBFRW8OgBhEREVEEq3GJ+Cy3Cj8crIZbrM3QUGwUyvITIiJqY3StvQFERERE1HRTlhTj12M1AIB7+jnw7JB4lfITBjWIiKhtYaYGERERUYQ6UeWqD2gAwJs7LQAAu0LsopBBDSIiamMY1CAiIiKKUMer5Bt/KpWfbC9xoIx9NYiIqA1hUIOIiIgoQlXIdAQVRVGx/AQAVubVKN5GREQUadhTg4iIiChClciUk5z+TT5sKkENi0P5NiIiokjDoAYRERFRhCqQCWocUyhJqeNQKE0hIiKKRCw/ISIiIopQRVb1AIYcBjWIiKgtYVCDiIiIKELtr3AGfB+ZNhxEREQRi0ENIiIiogj05IZyzD1sC/h+zNQgIqK2hEENIiIioghTYHXhvzssTbovMzWIiKgtYVCDiIiIKMKcqHKhqfkWzNQgIqK2hEENIiIioghTozKy1RdH4L1FiYiIwhaDGkREREQRxt6MEhJmahARUVvCoAYRERFRhLE3IzDhEBnUICKitoNBDSIiIqIIY2f5CREREYAwCmrMmDEDCQkJePjhh+uXiaKI559/Hn369EFGRgYmTJiA3bt3e9yvpqYGDz/8MLp164bMzExce+21OH78uMc6ZWVlmDZtGjp16oROnTph2rRpKCsra4mXRURERBR0LD8hIiKqFRZBjQ0bNuDjjz9Gv379PJbPnDkTb775Jl588UUsWbIEqampmDx5MiorK+vXmT59OubNm4cPPvgA8+fPR2VlJa655hq4XA2XIW677TZs27YN33zzDb799lts27YNd9xxR4u9PiIiIqJgak6mxvKTNUHcEiIiotbV6kGN8vJy3H777fjvf/+LhISE+uWiKGLWrFm4//77cdlllyEnJwezZs2CxWLBt99+W3/fTz/9FE8//TTGjBmDgQMH4p133sHOnTuxbNkyAMDevXuxaNEivP766xg6dCiGDBmC1157DQsXLkRubm4rvGIiIiKi5qlpRrbFwUoXrE5maxARUdvQ6kGN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\n",
      "text/plain": [
       "<Figure size 1152x576 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#visualize the closing price history\n",
    "plt.figure(figsize=(16, 8))\n",
    "plt.title('Close Price History')\n",
    "plt.plot(df['Close'])\n",
    "plt.xlabel('Date', fontsize=18)\n",
    "plt.ylabel('Close Price USD ($)', fontsize=18)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1204"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Creating a new dataframe with only the 'Close column'\n",
    "data = df.filter(['Close'])\n",
    "#Convert the dataframe to a numpy array\n",
    "dataset = data.values\n",
    "#Get the number of rows to train the model on\n",
    "training_data_len = math.ceil( len(dataset) * .8 )\n",
    "\n",
    "training_data_len\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.43223297],\n",
       "       [0.45603295],\n",
       "       [0.48944448],\n",
       "       ...,\n",
       "       [0.72446936],\n",
       "       [0.7370559 ],\n",
       "       [0.7251559 ]])"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Scale the data before entered in neural network\n",
    "scaler = MinMaxScaler(feature_range=(0,1))\n",
    "scaled_data = scaler.fit_transform(dataset)\n",
    "    \n",
    "scaled_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[array([0.43223297, 0.45603295, 0.48944448, 0.48463871, 0.49058871,\n",
      "       0.48257909, 0.48463871, 0.46839064, 0.4532868 , 0.45054065,\n",
      "       0.45671949, 0.45054065, 0.45191373, 0.4651868 , 0.45374449,\n",
      "       0.45282911, 0.45374449, 0.44413296, 0.45076949, 0.45557526,\n",
      "       0.45054065, 0.45054065, 0.45054065, 0.44596373, 0.43269066,\n",
      "       0.41575605, 0.39149837, 0.40019452, 0.40477144, 0.39744837,\n",
      "       0.38737914, 0.36746953, 0.36907146, 0.37570799, 0.37708107,\n",
      "       0.36746953, 0.37044453, 0.36335031, 0.35305223, 0.36655415,\n",
      "       0.36472338, 0.35442531, 0.35625608, 0.36312146, 0.36106185,\n",
      "       0.37044453, 0.3663253 , 0.36815607, 0.35511185, 0.36403684,\n",
      "       0.36037531, 0.35900223, 0.35740031, 0.366783  , 0.36746953,\n",
      "       0.36037531, 0.35007724, 0.35671377, 0.3663253 , 0.35625608])]\n",
      "[0.3528233880656788]\n",
      "\n",
      "[array([0.43223297, 0.45603295, 0.48944448, 0.48463871, 0.49058871,\n",
      "       0.48257909, 0.48463871, 0.46839064, 0.4532868 , 0.45054065,\n",
      "       0.45671949, 0.45054065, 0.45191373, 0.4651868 , 0.45374449,\n",
      "       0.45282911, 0.45374449, 0.44413296, 0.45076949, 0.45557526,\n",
      "       0.45054065, 0.45054065, 0.45054065, 0.44596373, 0.43269066,\n",
      "       0.41575605, 0.39149837, 0.40019452, 0.40477144, 0.39744837,\n",
      "       0.38737914, 0.36746953, 0.36907146, 0.37570799, 0.37708107,\n",
      "       0.36746953, 0.37044453, 0.36335031, 0.35305223, 0.36655415,\n",
      "       0.36472338, 0.35442531, 0.35625608, 0.36312146, 0.36106185,\n",
      "       0.37044453, 0.3663253 , 0.36815607, 0.35511185, 0.36403684,\n",
      "       0.36037531, 0.35900223, 0.35740031, 0.366783  , 0.36746953,\n",
      "       0.36037531, 0.35007724, 0.35671377, 0.3663253 , 0.35625608]), array([0.45603295, 0.48944448, 0.48463871, 0.49058871, 0.48257909,\n",
      "       0.48463871, 0.46839064, 0.4532868 , 0.45054065, 0.45671949,\n",
      "       0.45054065, 0.45191373, 0.4651868 , 0.45374449, 0.45282911,\n",
      "       0.45374449, 0.44413296, 0.45076949, 0.45557526, 0.45054065,\n",
      "       0.45054065, 0.45054065, 0.44596373, 0.43269066, 0.41575605,\n",
      "       0.39149837, 0.40019452, 0.40477144, 0.39744837, 0.38737914,\n",
      "       0.36746953, 0.36907146, 0.37570799, 0.37708107, 0.36746953,\n",
      "       0.37044453, 0.36335031, 0.35305223, 0.36655415, 0.36472338,\n",
      "       0.35442531, 0.35625608, 0.36312146, 0.36106185, 0.37044453,\n",
      "       0.3663253 , 0.36815607, 0.35511185, 0.36403684, 0.36037531,\n",
      "       0.35900223, 0.35740031, 0.366783  , 0.36746953, 0.36037531,\n",
      "       0.35007724, 0.35671377, 0.3663253 , 0.35625608, 0.35282339])]\n",
      "[0.3528233880656788, 0.3528233880656788]\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#Create the training data set\n",
    "#Create the scaled the training data set\n",
    "train_data = scaled_data[0:training_data_len , :]\n",
    "#Split the data into x_train and y_train data sets\n",
    "x_train = []\n",
    "y_train = []\n",
    "\n",
    "for i in range(60, len(train_data)):\n",
    "    x_train.append(train_data[i-60:i, 0])\n",
    "    y_train.append(train_data[i, 0])\n",
    "    if i <= 61:\n",
    "        print(x_train)\n",
    "        print(y_train)\n",
    "        print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Convert the x_train and y_train to numpy arrays to train the LSTM model\n",
    "x_train , y_train = np.array(x_train), np.array(y_train)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1144, 60, 1)"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Reshape the x data set to 3D (expected)\n",
    "x_train  = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))\n",
    "x_train.shape\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Build the LSTM model \n",
    "model = Sequential()\n",
    "model.add(LSTM(50, return_sequences=True, input_shape= (x_train.shape[1], 1)))\n",
    "model.add(LSTM(50, return_sequences= False))\n",
    "model.add(Dense(25))\n",
    "model.add(Dense(1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Compile the model\n",
    "model.compile(optimizer='adam', loss='mean_squared_error')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1144/1144 [==============================] - 29s 22ms/step - loss: 0.0135\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<tensorflow.python.keras.callbacks.History at 0x7f41dc4737f0>"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Train the model\n",
    "\n",
    "model.fit(x_train, y_train, batch_size=1, epochs=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create the testing data set\n",
    "#Create a new array containing scaled values from index 1802 to 2003\n",
    "test_data = scaled_data[training_data_len - 60: , :]\n",
    "#Create the data sets x_tests and y_tests\n",
    "x_test = []\n",
    "y_test = dataset[training_data_len:, :]\n",
    "for i in range(60, len(test_data)):\n",
    "    x_test.append(test_data[i-60:i, 0])\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Convert the data into a numpy array\n",
    "x_test = np.array(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Reshape the data \n",
    "x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Get the models predicted price values\n",
    "predictions = model.predict(x_test)\n",
    "predictions = scaler.inverse_transform(predictions)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "207.17385002465738"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Get the root mean squared error(RMSE)\n",
    "rmse = np.sqrt( np.mean( predictions - y_test)**2)\n",
    "rmse"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-30-b5d1a35ab357>:4: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  valid['Predictions'] = predictions\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABDUAAAIdCAYAAAAtX0aAAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAADm00lEQVR4nOzdd3gb9f0H8PedtuU94sSJs3cgCQQCCSGsMANlU6DMskcLFChQSktpKXv9KGVD2ZsAYY8MwkoImWTv7b1kWfvu94c8dEvDlmzJeb+eh4fodJK+tmXr7nOfITQ0NMggIiIiIiIiIsowYk8vgIiIiIiIiIioMxjUICIiIiIiIqKMxKAGEREREREREWUkBjWIiIiIiIiIKCMxqEFEREREREREGYlBDSIiIiIiIiLKSAxqEBER0V5p27ZtyM/Px8yZM7v8XMl6HiIiIkoMgxpERETULfLz89v/27hxo+F+p5xySvt+L7zwQjeukIiIiDINgxpERETUbcxmMwDg5Zdf1r1/69atmD9/fvt+RERERNEwqEFERETdprCwEAceeCDeeOMNBAIBzf2vvPIKZFnGcccd1wOrIyIiokzDoAYRERF1qwsuuADV1dX49NNPFduDwSBee+01TJo0CePGjTN8/ObNm3H11Vdj7NixKCkpwYgRI3DRRRdh5cqVuvu7XC785S9/wdixY1FaWooDDzwQjz/+OGRZNnwNSZLw8ssv49hjj8XAgQNRWlqKKVOm4OGHH4bf7+/cF05ERERJx6AGERERdavTTjsNOTk5mhKUL774AhUVFbjwwgsNH7t06VIcfvjheP3117HvvvviD3/4A6ZNm4aPP/4YM2bMwFdffaXY3+fz4eSTT8Z///tf5Ofn48orr8S0adPw0EMP4dZbb9V9jWAwiHPPPRd//OMfUVtbi9NPPx0XX3wxzGYz7rrrLpx55pkIBoNd/0YQERFRl7FglYiIiLqV0+nEGWecgZdeegnbt2/HwIEDAYT7bGRnZ+O0007D448/rnmcLMu48sor0dTUhP/+978499xz2++bN28eTj31VFx55ZVYuXIlsrKyAAD/+c9/sGTJEpxwwgl49dVXIYrh6zk33HADDj/8cN31PfLII/j8889x2WWX4d5774XJZAIQzt644YYb8NJLL+G5557DlVdemcxvCxEREXUCMzWIiIio21144YWQJAmvvPIKAGDXrl34+uuvcfrppyM7O1v3MQsXLsS6deuw//77KwIaAHD44YfjxBNPRG1tLT755JP27a+99hoEQcA//vGP9oAGAAwcOBBXXHGF5jUkScJTTz2FkpIS3HPPPe0BDQAQRRF33XUXBEHAW2+91aWvn4iIiJKDmRpERETU7SZOnIjx48fjtddew6233opXXnkFoVAoaunJ8uXLAQDTp0/Xvf/www/H7NmzsXz5cpx55plwuVzYvHkz+vbtixEjRmj2P+SQQzTbNm7ciNraWgwZMgQPPPCA7us4HA5s2LAhni+TiIiIUoxBDSIiIuoRF154IW688UZ88cUXePXVV7HPPvtg//33N9y/qakJANCnTx/d+0tLSxX7tf2/pKREd3+956mrqwMAbNmyBffdd1+cXwkRERH1FJafEBERUY8488wzkZWVhZtvvhk7d+7ERRddFHX/3NxcAEBVVZXu/ZWVlYr92v5fXV2tu7/e87Q95rjjjkNDQ0PU/4iIiKjnMahBREREPSI3Nxennnoqdu3aBYfDgTPPPDPq/hMmTAAALFiwQPf++fPnAwiXtgBATk4Ohg4disrKSmzcuFGz//fff6/ZNnLkSOTl5eGXX37h6FYiIqIMwKAGERER9Zi//OUvePXVV/Hee+8hLy8v6r4HHXQQRo0ahV9++UXTqHP+/PmYPXs2ioqKcMIJJ7Rv/93vfgdZlvG3v/0NkiS1b9++fTuefvppzWuYzWZceeWVqK6uxk033YSWlhbNPrW1tVixYkWiXyoRERGlAHtqEBERUY/p378/+vfvH9e+giDgySefxCmnnIIrr7wSs2bNwrhx47BlyxZ89NFHsFqteOqpp9rHuQLAtddei08++QSffvopDj30UMyYMQNNTU2YNWsWpkyZgs8++0zzOjfffDNWr16Nl19+GV9++SWmT5+O/v37o6amBlu2bMFPP/2ESy+9FOPHj0/a94GIiIg6h0ENIiIiyhj7778/5s2bhwceeADz5s3DN998g7y8PMycORM33nijJtBgs9nwwQcf4N5778WsWbPw1FNPYeDAgbjxxhtx0kkn6QY1zGYzXn75Zbz33nt47bXX8NVXX6G5uRmFhYUoLy/HDTfcgLPPPru7vmQiIiKKQmhoaJB7ehFERERERERERIliTw0iIiIiIiIiykgMahARERERERFRRmJQg4iIiIiIiIgyEoMaRERERERERJSRGNQgIiIiIiIioozEoAYRERERERERZSQGNYiIiIiIiIgoIzGoQZQkGzZs6Okl0F6A7zPqDnyfUXfg+4xSje8x6i58r/UsBjWIiIiIiIiIKCMxqEFEREREREREGYlBDSIiIiIiIiLKSAxqEBEREREREVFGYlCDiIiIiIiIiDISgxpERERERERElJEY1CAiIiIiIiKijMSgBhERERERERFlJAY1iIiIiIiIiCgjMahBRERERERERBmJQQ0iIiIiIiIiykgMahARERERERFRRmJQg4iIiIiIiIgyEoMaRERERERERJSRGNQgIiIiIiIioozEoAYRERERERERZSQGNYiIiIh6oQ2NAUz9oBL9X9mNB5e7eno5REREKcGgBhEREVEv9PCKZqyuD8IdlHH3kibsaA729JKIiIiSjkENIiIiol7ojY0t7f+WAbyyocV4ZyIiogzFoAYRERHRXsAblHt6CUREREnHoAYRERHRXsAbYlCDiIh6HwY1iIiIiPYCDGoQEVFvxKAGERER0V6AQQ0iIuqNGNQgIiIi2gv4GNQgIqJeiEENIiIior0AG4USEVFvxKAGERER0V6gmUENIiLqhRjUICIiItoLNAcY1CAiot6HQQ0iIiKiXkaWtQEMl1/qgZUQERGlFoMaRERERL1MQCd+UedjUIOIiHofBjWIiIiIehm/pM3UaPDLCOpsJyIiymQMahARERH1MnqZGgCzNYiIqPdhUIOIiIiol/GF9DMyar0MahARUe/CoAYRERFRL6NXfgIAtczUICKiXoZBDSIiIqJeJhDS385MDSIi6m0Y1CAiIiLqZXxGmRoMahARUS/DoAYRERFRL+M37KlhkMJBRESUoRjUICIiIupljKafsKcGERH1NgxqEBEREWUwX0jGqxvcmLWlBZIcztAwbBTK8hMiIuplzD29ACIiIiLqvPPn1OLLnT4AwDXjArh7cl6U8hMGNYiIqHdhpgYRERFRhtrtDrUHNADgiVXNAAC/QeyimkENIiLqZRjUICIiIspQu9z6jT+Nyk9W1gXQwL4aRETUizCoQURERJShmnQ6gsqybFh+AgALKnyG9xEREWUa9tQgIiIiylB1OuUk+75TCW+UoEZzwPg+IiKiTMOgBhEREVGGqtIJauw0KElpEzAoTSEiIspELD8hIiIiylA1nugBDD0MahARUW/CoAYRERFRhtrUFEz4MTptOIiIiDIWgxpEREREGehvPzfio23ehB/HTA0iIupNGNQgIiIiyjBVnhAe/7W5U49lpgYREfUmDGoQERERZZjd7hA6m2/BTA0iIupNGNQgIiIiyjC+KCNbYwkk3luUiIgobTGoQURERJRh/F0oIWGmBhER9SYMahARERFlGH8XAhMBmUENIiLqPRjUICIiIsowfpafEBERAUijoMZDDz2E/Px83Hzzze3bZFnGPffcg9GjR6Nv376YOXMm1qxZo3icz+fDzTffjKFDh6KsrAxnn302du3apdinoaEBl19+OQYOHIiBAwfi8ssvR0NDQ3d8WURERERJx/ITIiKisLQIavz888946aWXMG7cOMX2xx57DE888QTuu+8+zJkzByUlJTj11FPhcrna97ntttswe/ZsPP/88/j000/hcrnw29/+FqFQx2WISy+9FCtWrMA777yDd999FytWrMAVV1zRbV8fERERUTJ1JVNj/h5fEldCRETUs3o8qNHY2IjLLrsMjz/+OPLz89u3y7KMJ598Etdffz1OPvlkjB07Fk8++SSam5vx7rvvtj/2lVdewV133YUjjjgCEydOxNNPP41Vq1Zh3rx5AIB169bh66+/xqOPPoqDDjoIkydPxiOPPIIvvvgCGzZs6IGvmIiIiKhrfF3IttjiCsETZLYGERH1Dj0e1GgLWhx22GGK7du2bUNlZSWOPPLI9m0OhwNTp07FwoULAQDLli1DIBBQ7DNgwACMGjWqfZ9FixYhOzsbBx10UPs+Bx98MJxOZ/s+RERERJlE3RfjopFZWHhqn7gf//Uub5JXRERE1DPMPfniL730EjZv3oynn35ac19lZSUAoKSkRLG9pKQEe/bsAQBUVVXBZDKhqKhIs09VVVX7PkVFRRAEof1+QRBQXFzcvo8eZnFQZ/B9Q92B7zPqDnyfpbedlWYA1vbbHlcjxOoanFtmweu7LTEfv3nnHmzw93zHUL7PKNX4HqPuwvda6owYMSLq/T0W1NiwYQPuuusufPbZZ7BarYb7RQYjgHBZinqbmnofvf1jPU+sbxyR2oYNG/i+oZTj+4y6A99n6S/P6wI2N7XfLikswIgRedjX3wzsboz5+P79+mLE0KxULjEmvs8o1fgeo+7C91rP6rHyk0WLFqG2thZT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v+quu+6q4542HKb09HSjrjsBNARJSUmKi4ur626ggWOcwR0YZ3AHxhlqG2PMM2VkZCgkJKSuu1Et+fn58vX1detnmlKOypST7XTM3qajW/tQ0873955KDQAAAAAA4JEINQAAAAAAgEci1AAAAAAAAB6JUAMAAAAAAHgkQg0AAAAAAOCRCDUAAAAAAIBHItQAAAAAAAAeiVADAAAAAAB4JEINAAAAAADgkQg1AAAAAADwAB9++KFCQ0Mdr5ev/ljN+w28oGtu2rRJoaGhSk1NvbDO1RFCDQAAAAAALsDUqVMVGhqq0NBQNWvWTN27d9cjjzyinJycWv3cMcOGavfHq6rcvlu3bnr55ZedjvXu3Vt79+5VkyZNarp7bmGt6w4AAAAAAODpBg4cqNdee002m02bN2/WPffco9zcXL3wwgtO7YqKimSxWGQymS74M/18feXn63tB1/D29lZkZOQF96WuUKkBAAAAAMAF8vHxUWRkpKKjozVu3DiNGzdOa9as0Zw5c9S3b18tX75c8fHxioiIUE5OjjIyMnTvvfeqffv2io6O1rXXXqsdO3Y4XfMf//iHunbtqubNm2v8+PFKSUlxOu9q+snnn3+uIUOGKCoqSm3atNH48eOVn5+vESNG6PDhw3r00UcdVSWS6+knq1evVr9+/RQREaEuXbro+eefl2EYjvPdunXTc889p/vuu08xMTHq3LmzXnrpJad+vPXWW+rRo4ciIyPVrl07jRkzRkVFRTXwX9pZo6rUWLx4sV566SUlJyerU6dOmjNnjvr161fX3QIAAAAAVCDn62vc+nkBgz+74Gv4+vrKZrNJkg4dOqTExEQtWbJE3t7e8vHx0ciRIxUcHKyVK1cqLCxMK1as0PXXX6/vv/9eUVFR+ve//60777xTDz/8sEaPHq1NmzZp9uzZFX7m2rVrddNNN2natGlauHChioqKtG7dOtntdi1btkyXX365br75Zt1xxx3lXmPnzp26/fbb9cADD+h3v/udtm/frmnTpikoKEhTpkxxtPvb3/6mWbNm6Z577tGXX36pGTNmqE+fPurVq5d27NihBx54QIsWLVKfPn2UkZGhjRs3XvB/U1caTaixatUqzZw5U/PmzVOfPn20ePFijRs3Tlu2bFFMTExddw8AAAAA0ED85z//UWJioq688kpJUmFhoV577TVFRERIkjZs2KAffvhB+/fvl5+fnyTpkUce0WeffaaVK1fq3nvv1auvvqorr7xSDzzwgCSpffv22r59u5YuXSojOEymnGzH5xlBIZKk5557TqNGjdIjjzziONe1a1dJkr+/v8xms4KCgiqcbrJw4UL1799fDz30kONzf/75Zy1YsMAp1Bg8eLAmT54sSZoyZYpee+01bdiwQb169dLhw4cVEBCg4cOHKygoSNKZ6o7a0GimnyxcuFA33XSTbrvtNnXs2FHPPfecIiMj9eabb9Z11wAAAAAAHm7t2rVq2bKlIiMjddVVV6lfv3569tlnJUktWrRwBBqStGvXLuXm5qp9+/Zq2bKl43979uzRwYMHJUl79+5Vz549nT7D8drHzxFkSJIR0lSStHv3bkeQcr727t2r3r17Ox3r27evjh07pszMTMexLl26OLWJiorSyZMnJUmDBg1SdHS0unfvrj/84Q9asWKFsrKyLqhf5WkUlRqFhYXauXOn7r77bqfjgwcP1tatW+uoVwAAAACAhqJfv35asGCBrFarmjdvLi8vL8e5gIAAp7Z2u10RERH69NNPy1znbGVDyTUsyjCZZDSLkr1ZlGQ2SyU+60IZhlHuIqYlj3uV+kyTyeToc1BQkDZu3Khvv/1W69ev1/z58/Xkk0/q66+/VvPmzWusr1IjCTVSU1NVXFys8PBwp+Ph4eFlFlo5KykpyR1dQwPDuIE7MM7gDowzuAPjDLWNMeZ5fH195ePjU+a4pd+/3NqP/Pz8arUvLi6Wj4+PWrRo4XhdXFws6cxuJ3a73emaF110kVJSUmSz2RQbG+vy8+Pi4rRt2zan9539Uv7sMZvNJsMwHK+7du2qr7/+WuPHj3fZTy8vL+Xn5ztds7Cw0HHNs5/73XffObXZtGmTWrRo4Xi/YRiy2WxObex2u4qKipyO9e7dW71799a0adPUtWtXffzxx5o4caLLvmVmZrp8Po+Li3PZ/qxGEWqcVTptqiiBquw/HFBaUlIS4wa1jnEGd2CcwR0YZ6htjDHPlJGRId8L3KLU3fLz82WxWGSxWFz23Wq1ymw2O50bNmyY+vTpo4SEBD3xxBOKi4tTSkqK1q5dq4EDB6pfv3668847NWzYMP3tb3/TqFGj9M033zgqO85ey8vLSyaTyfF6+vTpmjBhguLi4jR27FgZhqGvv/5aCQkJ8vf3V2xsrP7973/r9OnT8vHxUdOmTeXt7e24pq+vr+655x4NHjxY8+fP17hx47R9+3a99tprevTRRx2fYzKZ5OXl5XRPZrNZVqtVvr6++uyzz3Tw4EH169dPYWFh2rRpk7Kzs9WlS5dyf3+Dg4PPa73LRrGmRtOmTWWxWMqkPqdOnSpTvQEAAAAAQG0ymUx67733dMUVV+jee+9Vz549lZCQoP379zumZ/Ts2VMvv/yy3nzzTfXv318fffSRZs6cWeF1hw0bpmXLlunLL7/UgAEDNGLECG3atElm85lH/4ceekhHjhzRJZdconbt2rm8Rnx8vJYsWaKPPvpIffv21RNPPKH77rvPsShoVYSEhGjNmjUaPXq0evXqpVdeeUUvvfRSrew+akpPT69gok7DMWTIEHXt2lULFixwHOvRo4euv/56/eUvf6nDnqGh4NsAuAPjDO7AOIM7MM5Q2xhjnikjI0MhISGVN6xH8vPzPa66pD4639/7RjP95K677tKUKVPUo0cP9e7dW2+++aZOnDihhISEuu4aAAAAAAA4D40m1BgzZoxOnz6t5557TsnJybrooov03nvvqVWrVnXdNQAAAAAAcB4aTaghSZMmTdKkSZPquhsAAAAAAKAGNIqFQgEAAAAAQMNDqAEAAAAAADwSoQYAAAAAAPBIhBoAAAAAgHrBarUqJydHhmHUdVfgRoWFhTKbzy+eaFQLhQIAAAAA6q+AgAAVFBQoMzOzrrtSZZmZmQoODq7rbng0s9mswMDA83ovoQYAAAAAoN7w8fGRj49PXXejylJSUhQTE1PX3Wi0mH4CAAAAAAA8EqEGAAAAAADwSIQaAAAAAADAIxFqAAAAAAAAj2RKT09nrxwAAAAAAOBxqNQAAAAAAAAeiVADAAAAAAB4JEINAAAAAADgkQg1AAAAAACARyLUAAAAAAAAHolQA5D0wgsvaNCgQYqJiVG7du00fvx4/e9//3NqYxiG5syZo06dOikqKkojRozQnj17nNosWbJE1113nVq1aqXQ0FAdOnTI5ed99dVXuuqqq9S8eXO1atVK119/fa3dG+oPd42zTZs2KTQ01OX//vWvf9X2baKOufPvs/379+umm25S27ZtFR0draFDh2rt2rW1en+oH9w5znbu3KnRo0erVatWatOmje69915lZ2fX6v2hfqiJcZaWlqbp06erZ8+eioqKUpcuXfTnP/9Zp0+fdrpOenq6Jk+erFatWqlVq1aaPHmy0tPT3XGbqGPuHGfPP/+8rr76arVo0UKhoaHuuL1GgVADkPTNN9/ojjvu0Oeff67Vq1fLarVq9OjRSktLc7RZsGCBFi5cqGeeeUZff/21wsPDdcMNNygrK8vRJjc3V4MHD9bMmTPL/ayPP/5Yv//97zV+/Hht3LhRX375pW655ZZavT/UD+4aZ71799bevXud/vfnP/9ZgYGBGjp0aK3fJ+qWO/8+Gz9+vAoKCvThhx9q48aN6tOnj2666SYdPHiwVu8Rdc9d4+z48eMaPXq0Wrdura+++koffPCBfvrpJ9155521fo+oezUxzo4fP67jx4/riSee0HfffafXXntN3333ne644w6nz5o0aZJ2796t999/X4mJidq9e7emTJni1vtF3XDnOCsoKNB1112nqVOnuvUeGzpTenq6UdedAOqb7OxstWrVSsuXL9fw4cNlGIY6deqkP/zhD3rggQckSXl5eYqLi9OTTz6phIQEp/fv2LFDgwYN0q5duxQbG+s4XlxcrO7du2v69Om67bbb3HpPqH9qa5y5ctlll6l///5asGBBrd0P6qfaGmepqalq166dVq9erQEDBkiSioqKFBERobfeekujRo1y302iztXWOFuyZIlmz56tpKQkWSwWSdKPP/6o/v37a/v27Wrbtq37bhJ17kLH2VlffPGFxo8fr0OHDik4OFh79+5V79699dlnn6lPnz6SpM2bN2v48OH6/vvvFRcX57Z7RN2rrXFW0ocffqjbbruNaqAaQqUG4EJ2drbsdrujLOzQoUNKTk7W4MGDHW38/PzUr18/bd26tcrX3blzp44cOSJvb28NGDBAHTp00A033KBdu3bV9C3AA9TWOCtt06ZN2r9/v26//fYL7DE8UW2NsyZNmqhjx45auXKlsrOzVVxcrCVLligwMFC9e/eu6dtAPVdb46ygoEBeXl6OQOPsdaQzD51oXGpqnGVlZcnHx0f+/v6SpG3btpX5u6tPnz4KCAi4oH9/4Zlqa5yh9hBqAC7MnDlT3bp1U69evSRJycnJkqTw8HCnduHh4UpJSanydX/55RdJ0lNPPaX7779f7733nlq0aKHrrrtOx48fr5nOw2PU1jgr7e2331bXrl11ySWXnH9n4bFqa5yZTCb985//1J49exQTE6OI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\n",
      "text/plain": [
       "<Figure size 1152x576 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Plot the data\n",
    "train = data[:training_data_len]\n",
    "valid = data[training_data_len:]\n",
    "valid['Predictions'] = predictions\n",
    "#Visualise the model/data\n",
    "plt.figure(figsize=(16,8))\n",
    "plt.title('Model')\n",
    "plt.xlabel('Date', fontsize=18)\n",
    "plt.ylabel('Close Price USD ($)', fontsize=18)\n",
    "plt.plot(train['Close'])\n",
    "plt.plot(valid[['Close', 'Predictions']])\n",
    "plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Close</th>\n",
       "      <th>Predictions</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2020-02-04</th>\n",
       "      <td>2515.0</td>\n",
       "      <td>2448.708496</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-02-05</th>\n",
       "      <td>2578.0</td>\n",
       "      <td>2426.384521</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-02-06</th>\n",
       "      <td>2644.0</td>\n",
       "      <td>2409.757568</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-02-07</th>\n",
       "      <td>2625.0</td>\n",
       "      <td>2402.222168</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-02-10</th>\n",
       "      <td>2539.0</td>\n",
       "      <td>2399.455078</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-04-12</th>\n",
       "      <td>3185.0</td>\n",
       "      <td>2906.112305</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-04-13</th>\n",
       "      <td>3177.0</td>\n",
       "      <td>2920.500977</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-04-14</th>\n",
       "      <td>3197.0</td>\n",
       "      <td>2928.891357</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-04-15</th>\n",
       "      <td>3252.0</td>\n",
       "      <td>2934.384766</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021-04-16</th>\n",
       "      <td>3200.0</td>\n",
       "      <td>2941.469727</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>301 rows ?? 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "             Close  Predictions\n",
       "Date                           \n",
       "2020-02-04  2515.0  2448.708496\n",
       "2020-02-05  2578.0  2426.384521\n",
       "2020-02-06  2644.0  2409.757568\n",
       "2020-02-07  2625.0  2402.222168\n",
       "2020-02-10  2539.0  2399.455078\n",
       "...            ...          ...\n",
       "2021-04-12  3185.0  2906.112305\n",
       "2021-04-13  3177.0  2920.500977\n",
       "2021-04-14  3197.0  2928.891357\n",
       "2021-04-15  3252.0  2934.384766\n",
       "2021-04-16  3200.0  2941.469727\n",
       "\n",
       "[301 rows x 2 columns]"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Show the valid and the predicted prices\n",
    "valid"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[2945.2239]]\n"
     ]
    }
   ],
   "source": [
    "#Get the quote (predict via date)\n",
    "apple_quote = web.DataReader('S32.JO', data_source='yahoo', start='2012-01-01', end='2021-04-19')\n",
    "#Create a dataframe \n",
    "new_df = apple_quote.filter(['Close'])\n",
    "#Get the last 60 days closing price values and convert the dataframe to an array\n",
    "last_60_days = new_df[-60:].values\n",
    "#Scale the data to be values between 0 and 1\n",
    "last_60_days_scaled = scaler.transform(last_60_days)\n",
    "#Create an empty list \n",
    "x_test = []\n",
    "#Append the past 60 days\n",
    "x_test.append(last_60_days_scaled)\n",
    "#Convert the x_test data set to a numpy array\n",
    "x_test = np.array(x_test)\n",
    "#Reshape the data\n",
    "x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape [1], 1))\n",
    "#Get the predicted scaled price\n",
    "pred_price = model.predict(x_test)\n",
    "#undo the scaling\n",
    "pred_price = scaler.inverse_transform(pred_price)\n",
    "print(pred_price)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Date\n",
      "2015-05-15    1920.0\n",
      "2015-05-18    2024.0\n",
      "2015-05-19    2170.0\n",
      "2015-05-20    2149.0\n",
      "2015-05-21    2175.0\n",
      "               ...  \n",
      "2021-04-12    3185.0\n",
      "2021-04-13    3177.0\n",
      "2021-04-14    3197.0\n",
      "2021-04-15    3252.0\n",
      "2021-04-16    3200.0\n",
      "Name: Close, Length: 1505, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "#Get the quote (actual compare)\n",
    "apple_quote2 = web.DataReader('S32.JO', data_source='yahoo', start='2012-04-08', end='2021-04-19')\n",
    "print(apple_quote2['Close'])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
