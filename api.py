from flask import Flask, jsonify, request
from flask_sqlalchemy  import SQLAlchemy

app = Flask(__name__)

app.config['SQLAlchemy_DATABAASE_URI'] = 'sqlite:///livros.db'
           
db = SQLAlchemy(app)
                
class Livro (db.Model):
    id = db.colum(db.integer, primary_key=True)
    titulo = db.colum(db.String(100),  nullable=False)
    autor = db.colum(db.String(100), nullable=False)  

with app.app_context():
    db.create_all()

livros = [
    {'id': 2, 'titulo': 'O Senhor dos Anéis', 'autor': 'J. R. R. Tolkien'},
    {'id': 3, 'titulo': 'O prisioneiro de Azkhaban', 'autor': 'J. K. Rowling'},
]

@app.route('/api/livros', methods= ['GET'])
def get_livros():
    return jsonify(livros)

@app.route('/api/livros/<int:id>', methods=['GET'])
def get_livro(id):
    livro = next(
        (livro for livro in livros if livro['id'] == id),
        None
    )
    return jsonify(livro) if livro else ('', 404)

@app.route('/api/livros', methods=['POST'])
def add_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

if __name__ == '__main__':
    app.run(port=5000, debug=True)