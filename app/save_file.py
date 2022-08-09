import sqlite3
import cgi, os
import cgitb; cgitb.enable()
from datetime import datetime

def log_msg(msg):
    # get datetime
    dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    f = open("log.txt", "a")
    f.write(dt + "   " + msg)
    f.close()

log_msg("Top of save_file.py...")

form = cgi.FieldStorage()

# get filename
fileitem = form['filename']

if fileitem.filename:
    # strip leading path from file name to avoid
    # directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    print("fn: " + fn)
    open('./uploads/' + fn, 'wb').write(fileitem.file.read())
    message = 'The file "' + fn + '" was uploaded successfully'
else:
    message = "No file was uploaded"

print("Content-Type: text/html\n")
print("<html>")
print("<body>")
print("<p>" + message + "</p>")
print("</body>")
print("</html>")

#con = sqlite3.connect('example.db')

#cur = con.cursor()

# create table
#cur.execute('''
#       CREATE TABLE stocks
#       (date test, trans text, symbol text, qty real, price real)
#       ''')

# insert row into table
#cur.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)")

#con.commit()

#con.close()
log_msg("Exiting save_file.py...")
