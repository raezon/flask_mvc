#!/bin/bash

# Define the target directory
TARGET_DIR="app/views"

# Check if the views directory exists, if not, create it
if [ ! -d "$TARGET_DIR" ]; then
    mkdir -p "$TARGET_DIR"
    echo "Created directory: $TARGET_DIR"
fi

# Create the index.html view
cat <<EOL > "$TARGET_DIR/index.html"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Products</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <h1 class="my-4">Product List</h1>
        <a href="{{ url_for('create_product_view') }}" class="btn btn-primary mb-3">Add New Product</a>

        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <div class="alert alert-success">
                    {% for category, message in messages %}
                        <p>{{ message }}</p>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}

        <table class="table table-bordered">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Description</th>
                    <th>Price</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {% for product in products %}
                <tr>
                    <td>{{ product.name }}</td>
                    <td>{{ product.description }}</td>
                    <td>{{ product.price }}</td>
                    <td>
                        <a href="{{ url_for('view_product', product_id=product.id) }}" class="btn btn-info btn-sm">View</a>
                        <a href="{{ url_for('edit_product_view', product_id=product.id) }}" class="btn btn-warning btn-sm">Edit</a>
                        <a href="{{ url_for('delete_product_view', product_id=product.id) }}" class="btn btn-danger btn-sm">Delete</a>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
EOL
echo "Created index.html"

# Create the create.html view
cat <<EOL > "$TARGET_DIR/create.html"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Product</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <h1 class="my-4">Create New Product</h1>
        
        <form method="POST">
            <div class="form-group">
                <label for="name">Product Name</label>
                <input type="text" class="form-control" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="description">Product Description</label>
                <textarea class="form-control" id="description" name="description" required></textarea>
            </div>
            <div class="form-group">
                <label for="price">Price</label>
                <input type="number" class="form-control" id="price" name="price" required>
            </div>
            <button type="submit" class="btn btn-primary">Create Product</button>
        </form>
    </div>
</body>
</html>
EOL
echo "Created create.html"

# Create the edit.html view
cat <<EOL > "$TARGET_DIR/edit.html"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Product</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <h1 class="my-4">Edit Product</h1>
        
        <form method="POST">
            <div class="form-group">
                <label for="name">Product Name</label>
                <input type="text" class="form-control" id="name" name="name" value="{{ product.name }}" required>
            </div>
            <div class="form-group">
                <label for="description">Product Description</label>
                <textarea class="form-control" id="description" name="description" required>{{ product.description }}</textarea>
            </div>
            <div class="form-group">
                <label for="price">Price</label>
                <input type="number" class="form-control" id="price" name="price" value="{{ product.price }}" required>
            </div>
            <button type="submit" class="btn btn-primary">Update Product</button>
        </form>
    </div>
</body>
</html>
EOL
echo "Created edit.html"

# Create the view.html view
cat <<EOL > "$TARGET_DIR/view.html"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>View Product</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <h1 class="my-4">{{ product.name }}</h1>
        <p><strong>Description:</strong> {{ product.description }}</p>
        <p><strong>Price:</strong> ${{ product.price }}</p>
        <a href="{{ url_for('edit_product_view', product_id=product.id) }}" class="btn btn-warning">Edit</a>
        <a href="{{ url_for('delete_product_view', product_id=product.id) }}" class="btn btn-danger">Delete</a>
        <a href="{{ url_for('products') }}" class="btn btn-secondary">Back to Products</a>
    </div>
</body>
</html>
EOL
echo "Created view.html"

echo "All views created successfully in $TARGET_DIR"
