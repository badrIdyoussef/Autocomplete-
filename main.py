
from Trie import Trie
from flask import Flask , render_template ,request

app = Flask(__name__)
tr = Trie() 



@app.route('/trie/autoComplete',methods=['POST'])
def autoComplete():

    data = request.get_json()

    if data['characters']  == '':
        return []
    char_list = tr.autoComplete(data['characters'],[])
    if char_list == None:
        return []
    return [sub.replace('_', ' ') for sub in char_list]


@app.route('/')
def home():
    with open('countries.txt') as file_:
        lines = [line.rstrip() for line in file_]
        for line in lines:
            tr.buildTrie(line ,tr.root)
    return render_template('index.html')


if __name__ == '__main__':
  

   app.run()