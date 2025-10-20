from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'

TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from JSON file"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to JSON file"""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

@app.route('/')
def index():
    """Display all tasks"""
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """Add a new task"""
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    
    if not title:
        flash('Task title is required!', 'error')
        return redirect(url_for('index'))
    
    tasks = load_tasks()
    new_task = {
        'id': max([task['id'] for task in tasks], default=0) + 1,
        'title': title,
        'description': description,
        'completed': False,
        'created_at': datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    
    flash('Task added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    """Toggle task completion status"""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            save_tasks(tasks)
            status = 'completed' if task['completed'] else 'marked as incomplete'
            flash(f'Task {status}!', 'success')
            break
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    """Edit an existing task"""
    tasks = load_tasks()
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if not task:
        flash('Task not found!', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        
        if not title:
            flash('Task title is required!', 'error')
            return render_template('edit.html', task=task)
        
        task['title'] = title
        task['description'] = description
        save_tasks(tasks)
        
        flash('Task updated successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('edit.html', task=task)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """Delete a task"""
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=False)
