
import cgi,os

print('content-type:text/html\r\n\r\n')

form = cgi.FieldStorage()

pn = str(form.getvalue("pname"))
fle=form['filename']

print('<h2>%s</h2>'%pn)