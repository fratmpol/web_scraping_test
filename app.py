from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import webbrowser

def main(inp):

    page = urlopen(inp)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    ans = soup.get_text()


    return ans

app = Flask(__name__)

# Home page and post request
@app.route('/', methods=['GET', 'POST'])
def refresh_results():
    if request.method == 'POST':
        if request.form["text"] != "":
            if request.form["text"] == "/Help":
                return webbrowser.open_new_tab("https://github.com/fratmpol/Texty/blob/fratmpol-patch-2/README.md")
            inp = request.form["text"]
            return render_template('home.html', main=str(main(inp)), inp="")
    inp = ""
    return render_template('home.html', main="insert an url", inp=inp)

if __name__ == '__main__':
    app.run()
