---

# Network

**Project Title:** Network

**Description:**

Network is a user-friendly social media platform built using Django and JavaScript. Users can create posts, follow others, build their profiles, and engage in real-time interactions.

## Key Features

- **Posts:** Create text-based posts with the ability to tag users and add relevant links.
- **User Profiles:** Personalize your profile with a bio, profile picture, and see your posting history.
- **Follow System:** Follow other users to see their posts on your feed.
- **Real-Time Updates:** See new posts, likes, and edits appear without manual refreshes.
- **Intuitive Interface:** Enjoy a clean and easy-to-navigate layout.

## Technologies Used

- **Backend:** Django (Python), MySQL (or your chosen database)
- **Frontend:** HTML, CSS, JavaScript (AJAX, DOM manipulation), Tailwind CSS (for streamlined styling)

## Getting Started

### Prerequisites:

- Python 3.x
- Django
- MySQL (or your preferred database)
- Node.js (to install required packages)

### Installation:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/luyandamagava/Network
   ```
2. **Navigate into the project directory:**
   ```bash
   cd Network
   ```
3. **Create a virtual environment:**
   ```bash
   python -m venv env
   ```
4. **Activate the virtual environment:**
   - **Linux/macOS:**
     ```bash
     source env/bin/activate
     ```
   - **Windows:**
     ```bash
     env\Scripts\activate
     ```
5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Set up your database:** (instructions may vary depending on your database setup)
7. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
8. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
9. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
10. **Access the project:** Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.

## Usage

1. **Create a new account** using the signup form.
2. **Log in** to access the main feed.
3. **Start posting!** Use `@` to mention other users.
4. **Visit your profile** to make edits and view post history.
5. **Follow other users** to see their content in your feed.

## Contributing

We welcome contributions to this project! Here's how:

1. **Fork the repository.**
2. **Create a new branch** for your feature:
   ```bash
   git checkout -b my-awesome-feature
   ```
3. **Make your changes** and commit them:
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. **Push your branch** to your fork:
   ```bash
   git push origin my-awesome-feature
   ```
5. **Create a new pull request.**

## Future Development

- **Enhanced Search:** Implement search functionality for posts, users, and hashtags.
- **Direct Messaging:** Allow users to send private messages.
- **Image and Video Uploads:** Support multimedia sharing.

## Contact

If you have questions, suggestions, or bug reports, please feel free to open an issue on the repository or contact me at [luyandamagava@gmail.com](mailto:luyandamagava@gmail.com).

## Show Your Support

If you find this project useful, please consider starring the repository!
