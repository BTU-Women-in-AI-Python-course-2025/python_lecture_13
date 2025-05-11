# `get_object_or_404` in Django 🔍

`get_object_or_404` is a shortcut function that retrieves an object from the database or returns a **404 Not Found** error if the object doesn’t exist.

---

## ✅ Syntax

```python
from django.shortcuts import get_object_or_404

get_object_or_404(ModelClass, **lookup)
```

* **`ModelClass`** – The Django model to query.
* **`lookup`** – Field lookups like `id=1`, `slug='post-title'`, etc.

---

## 📦 Example

```python
from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog_detail.html', {'post': post})
```

If the `BlogPost` with `id=post_id` doesn’t exist, Django will automatically return a **404 page**.

---

## 📛 Why Use It?

* Prevents `DoesNotExist` exceptions.
* Automatically returns a standard 404 error.
* Makes views cleaner and more readable.
