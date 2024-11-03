{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5cd70a77-5c40-4684-87e5-5ba6a4996e67",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'streamlit'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[1], line 3\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;66;03m#streamlit webapp layout with comments\u001b[39;00m\n\u001b[0;32m----> 3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mstreamlit\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mst\u001b[39;00m\n\u001b[1;32m      5\u001b[0m \u001b[38;5;66;03m# --- Title and Introduction ---\u001b[39;00m\n\u001b[1;32m      6\u001b[0m st\u001b[38;5;241m.\u001b[39mtitle(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPlotly and Streamlit Interactive Visualizations\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'streamlit'"
     ]
    }
   ],
   "source": [
    "#streamlit webapp layout with comments\n",
    "\n",
    "import streamlit as st\n",
    "\n",
    "# --- Title and Introduction ---\n",
    "st.title(\"Plotly and Streamlit Interactive Visualizations\")\n",
    "st.markdown(\n",
    "    \"\"\"\n",
    "    Welcome! This app demonstrates how to use Plotly Express and Streamlit\n",
    "    to create interactive visualizations with a clean layout.\n",
    "    \"\"\"\n",
    ")\n",
    "\n",
    "# --- Load Dataset ---\n",
    "tips = sns.load_dataset('tips')\n",
    "\n",
    "\n",
    "# ---  Scatter Plot and Bar Chart ---\n",
    "\n",
    "#Visualizations using Plotly\n",
    "fig1 = px.bar(tips, x=\"day\", y=\"tip\")\n",
    "st.plotly_chart(fig1)\n",
    "\n",
    "# --- Bar Plot ---\n",
    "fig2 = px.bar(\n",
    "    tips, x='day', y='tip', color='day',\n",
    "    title='Average Tip by Day',\n",
    "    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},\n",
    "    template='plotly_white',  # Clean white background\n",
    ")\n",
    "st.plotly_chart(fig2)\n",
    "\n",
    "# --- Violin Plot ---\n",
    "fig3 = px.violin(tips, x='sex', y='tip', color='time', title='Violin Plot: Total Bill by Day and Time', box=True, points=\"all\")\n",
    "st.plotly_chart(fig3)\n",
    "\n",
    "# --- Scatter Plot ---\n",
    "fig4 = px.box(\n",
    "    tips, x='day', y='total_bill', color='time',\n",
    "    title='Total Bill Distribution by Day and Time',\n",
    "    labels={'total_bill': 'Total Bill ($)', 'day': 'Day'},\n",
    "    template='ggplot2',  # Classic theme for a beautiful look\n",
    ")\n",
    "st.plotly_chart(fig4)\n",
    "\n",
    "\n",
    "# --- Histogram Plot ---\n",
    "fig5 = px.histogram(\n",
    "    tips, x='tip', color='sex',\n",
    "    title='Distribution of Tips (Colored by Gender)',\n",
    "    labels={'tip': 'Tip ($)', 'sex': 'Gender'},\n",
    "    template='plotly_white',  # Clean and bright look\n",
    ")\n",
    "st.plotly_chart(fig5)\n",
    "\n",
    "# --- Footer ---\n",
    "st.markdown(\"---\")\n",
    "st.markdown(\"Created with Streamlit and Plotly by [edit] Full name.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3df05808-a25e-4838-ad0f-5ddcb945f553",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
