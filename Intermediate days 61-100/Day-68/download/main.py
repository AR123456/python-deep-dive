@app.route('/download')
def download():
    return send_from_directory('static', filename="files/cheat_sheet.pdf")