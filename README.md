# Django Tweet App

A simple Django web application that allows users to post tweets with image uploads and content filtering.

## Features

- Post tweets with up to 280 characters
- Upload images with tweets
- Word filtering (prohibits: shit, fuck, bobo)
- Real-time form validation
- Responsive Bootstrap UI
- Admin panel for tweet management

## Project Structure

```
tweet_project/
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
├── tweet_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── tweets/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
│   └── templates/
│       └── tweets/
│           └── tweet_list.html
├── media/
│   └── tweet_images/
└── static/
```

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd tweet_project
```

### Step 2: Create Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Create Django Project Structure

If starting from scratch, create the project structure:

```bash
# Create main project
django-admin startproject tweet_project .

# Create tweets app
python manage.py startapp tweets
```

### Step 5: Configure Settings

Replace the content of `tweet_project/settings.py` with the provided settings file.

### Step 6: Copy Files

Copy all the provided files to their respective locations:

- `models.py` → `tweets/models.py`
- `forms.py` → `tweets/forms.py`
- `views.py` → `tweets/views.py`
- `urls.py` → `tweets/urls.py`
- `admin.py` → `tweets/admin.py`
- `tweet_list.html` → `templates/tweet_list.html`
- - `tweet_form.html` → `templates/tweet_form.html`
- Main `urls.py` → `tweet_project/urls.py`

### Step 7: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 8: Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### Step 9: Create Media Directory

```bash
mkdir media
mkdir media/tweet_images
```

### Step 10: Start Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

## How to Use the Tweet App

### Creating a Tweet

1. **Navigate to the Homepage**: Open your browser and go to `http://127.0.0.1:8000/`

2. **Compose Your Tweet**: 
   - In the "Compose Tweet" section, enter your tweet content (max 280 characters)
   - The content cannot contain prohibited words: shit, fuck, bobo

3. **Add an Image (Optional)**:
   - Click "Choose File" under "Upload Image"
   - Select an image file (JPG, PNG, GIF, etc.)

4. **Post the Tweet**:
   - Click the "Tweet" button
   - If successful, you'll see a success message and your tweet will appear in the feed
   - If there are errors (prohibited words, etc.), error messages will be displayed

### Viewing Tweets

- All tweets are displayed in chronological order (newest first)
- Each tweet shows:
  - Content text
  - Image (if uploaded)
  - Timestamp

### Admin Panel (Optional)

1. **Access Admin Panel**: Go to `http://127.0.0.1:8000/admin/`
2. **Login**: Use the superuser credentials you created
3. **Manage Tweets**: View, edit, or delete tweets through the admin interface

## Word Filtering

The app automatically filters out tweets containing these prohibited words:
- "shit"
- "fuck" 
- "bobo"

The filtering is case-insensitive and will prevent the tweet from being posted if any of these words are detected.

## File Upload

- Images are uploaded to the `media/tweet_images/` directory
- Supported formats: JPG, PNG, GIF, and other common image formats
- Images are automatically resized and displayed in the tweet feed

## Troubleshooting

### Common Issues

1. **Images not displaying**: Make sure the `media/` directory exists and has proper permissions

2. **Form validation errors**: Check that prohibited words are not in the tweet content

3. **Static files not loading**: Ensure `DEBUG = True` in settings.py for development

4. **Database errors**: Run `python manage.py migrate` to apply database changes

### Development Tips

- The database file `db.sqlite3` is excluded from Git
- Virtual environment is excluded from Git
- Media files are excluded from Git (add sample images manually)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request