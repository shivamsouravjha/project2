{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled4.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOQ3SQ/5PYdSRh1loja/r7D",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/shivamsouravjha/project2/blob/master/Untitled4.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XWcI-IB6QRDM",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import streamlit as st\n",
        "st.title(\"Streamlit application\")\n",
        "\n",
        "\n",
        "st.markdown(\"Crashes data from nyc\")\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "\n",
        "def take_data(nrows):\n",
        "    data  =  pd.read_csv(\"../input/nypd-motor-vehicle-collisions\",nrows=nrows,parse_dates=[[\"CRASH_DATE\",\"CRASH_TIME\"]])\n",
        "    data.dropna(subset= ['LATITUDE','LONGITUDE'],inplace =True)\n",
        "    lowercase = lambda x:str(x).lower()\n",
        "    data.rename(lowercase,axis=\"columns\",inplace= True)\n",
        "    data.rename(columns = {'crash_date_crash_time':'data/time'},inplace=True)\n",
        "    return data\n",
        "data  = take_data(100000)\n",
        "st.header(\"Place of accident\")\n",
        "patients = st.slider(\"numfber of patients\",0,19)\n",
        "st.map(data.query(\"injured_persons>= @patients\")[['latitude','longitude']].dropna(how = \"any\"))\n",
        "\n",
        "st.header(\"at what time\")\n",
        "hour = st.selectbox(\"hours\",range(0,24),1)\n",
        "st.markdown(\"between %i:00 %i:00 \"%(hour,hour+1))\n",
        "data = data[data['data/time'].dt.hour==hour]\n",
        "import pydeck as pdk\n",
        "midpoint = (np.average(data['latitude']),np.average(data['longitude']))\n",
        "st.write(pdk.Deck(\n",
        "    map_style= 'mapbox://styles/mapbox/light-v9',\n",
        "    initial_view_state={\n",
        "        'latitude': midpoint[0],\n",
        "        'longitude':midpoint[1],\n",
        "        'zoom': 13,\n",
        "        'pitch ': 80,\n",
        "\n",
        "    },\n",
        "    layers = [pdk.Layer(\n",
        "        \"HexagonLayer\",\n",
        "        data = data[['data/time','latitude','longitude']],\n",
        "        get_position = ['longitude','latitude'],\n",
        "        radius =100,\n",
        "        extruded = True,\n",
        "        pickable = True,\n",
        "        elevation_scale=4,\n",
        "        elevation_range=[0,1000],\n",
        "   ),\n",
        "    ],\n",
        "))\n",
        "import plotly.express as px\n",
        "st.header(\"accident time\")\n",
        "filtered = data[(data['data/time'].dt.hour>=hour)&(data['data/time'].dt.hour<hour+1)]\n",
        "hist = np.histogram(filtered['data/time'].dt.minute,bins =60,range=(0,60))[0]\n",
        "chart_data = pd.DataFrame({'minute':range(60),\"crashes\":hist})\n",
        "fig= px.bar(chart_data,x='minute',y='crashes',hover_data=['minute','crashes'])\n",
        "\n",
        "st.write(fig)\n",
        "if st.checkbox(\"how\",False):\n",
        "    st.subheader(\"show\")\n",
        "    st.write(data)\n",
        "\n"
      ],
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Knpgn8mhGq-_",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Qf_4sKVXGsX9",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "S9mt7r_qDq8A",
        "colab_type": "text"
      },
      "source": [
        "# New Section"
      ]
    }
  ]
}
