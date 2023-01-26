from flask import Flask, render_template, request
import pandas as pd
import os
from tkinter import filedialog
import tkinter as tk

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('App.html')


@app.route('/data', methods=['GET', 'POST'])
def data():
    # if request.method == 'POST':
    #     file = request.form['layout']
    #     data = pd.read_excel(file, index_col=None)
    #     print(data)
    # return render_template('data.html', data=data)
    root = tk.Tk()
    root.withdraw()
    root.overrideredirect(True)
    root.geometry("0x0+0+0")
    root.deiconify()
    root.lift()
    root.focus_force()
    filepath = filedialog.askopenfilename(parent=root, initialdir='C:/Users/', filetypes=(("excel", "*.xlsx"), ("csv", "*.csv"), ("all files", "*.*")))
    data = pd.read_excel(filepath, index_col=None)
    root.destroy()
    return render_template('data.html', data=data)


if __name__=="__main__":
    app.run(debug=True)