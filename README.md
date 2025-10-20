# Task Manager ✨

A beautiful and elegant task management web application built with Flask.

![Task Manager](https://github.com/user-attachments/assets/0f3c1021-ca8a-4d40-bead-9d694c79e478)

## Features

- ✅ Add new tasks with title and description
- ✅ Mark tasks as complete/incomplete
- ✅ Edit existing tasks
- ✅ Delete tasks
- ✅ Persistent storage using JSON
- ✅ Beautiful responsive UI with gradient design
- ✅ Flash messages for user feedback
- ✅ Smooth animations and transitions

## Screenshots

### Empty State
![Empty State](https://github.com/user-attachments/assets/0f3c1021-ca8a-4d40-bead-9d694c79e478)

### Adding Tasks
![Task Added](https://github.com/user-attachments/assets/3bdcb36b-b767-4082-8530-85ecb03ca92a)

### Completed Tasks
![Task Completed](https://github.com/user-attachments/assets/746a6661-7aff-47ce-a298-ad82ba8be965)

### Editing Tasks
![Edit Task](https://github.com/user-attachments/assets/fc4350f8-7319-4aa9-a57b-9278e0d2b00a)

### Updated Tasks
![Updated Task](https://github.com/user-attachments/assets/f1fc5f02-c2d4-4e21-951d-7da8a8c7f2d7)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/seandorsett/pythonstarter.git
cd pythonstarter
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

3. Start managing your tasks!

## Project Structure

```
pythonstarter/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── tasks.json         # Task data storage (auto-generated)
└── templates/
    ├── base.html      # Base template with styling
    ├── index.html     # Main task list page
    └── edit.html      # Task editing page
```

## Technologies Used

- **Backend**: Flask 3.0.0
- **Frontend**: HTML5, CSS3 (embedded)
- **Storage**: JSON file-based persistence
- **Design**: Responsive CSS with gradient backgrounds and smooth animations

## Features in Detail

### Add Tasks
- Simple form with title (required) and description (optional)
- Instant feedback with success messages

### Mark Complete/Incomplete
- Toggle task completion status with a single click
- Visual indication with strikethrough text and different styling
- Green border for completed tasks

### Edit Tasks
- Modify task title and description
- Dedicated edit page with pre-filled data
- Cancel option to return without saving

### Delete Tasks
- Remove tasks with confirmation dialog
- Instant deletion with success message

### Persistent Storage
- All tasks saved to `tasks.json`
- Data persists between application restarts
- Each task has unique ID and timestamp

## UI Features

- 🎨 Beautiful gradient purple background
- 📱 Fully responsive design for mobile and desktop
- ✨ Smooth animations and hover effects
- 💬 Color-coded flash messages (green for success, red for errors)
- 🎯 Clean, modern card-based layout
- 📋 Empty state with helpful icon and message

## License

MIT License - feel free to use this project for your own purposes!