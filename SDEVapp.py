from flask import Flask, request, jsonify

app = Flask(__name__)

# A dictionary to store books, simulating a database
books = {}
next_id = 1

# Creat a Book
@app.route('/book', methods=['POST'])
def create_book():
    global next_id
    data = request.get_json()
    if not data or 'book_name' not in data or 'author' not in data or 'publisher' not in data:
        return jsonify({'error': 'Missing data'}), 400
    
    book = {
        'id': next_id,
        'book_name': data['book_name'],
        'author': data['author'],
        'publisher': data['publisher']
    }
    books[next_id] = book
    next_id += 1
    return jsonify(book), 201

# Retrieve a Book
@app.route('/book/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = books.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(book)

# Update a Book
@app.route('/book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    if book_id not in books:
        return jsonify({'error': 'Book not found'}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Bad Request'}), 400
    
    book = books[book_id]
    book['book_name'] = data.get('book_name', book['book_name'])
    book['author'] = data.get('author', book['author'])
    book['publisher'] = data.get('publisher', book['publisher'])
    
    return jsonify(book)

# Delete Book
@app.route('/book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if book_id not in books:
        return jsonify({'error': 'Book not found'}), 404
    
    del books[book_id]
    return jsonify({'message': 'Book deleted'})

if __name__ == '__main__':
    app.run(debug=True)
