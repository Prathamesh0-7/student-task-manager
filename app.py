from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
tasks = []
next_id = 1

PAGE = """
<h1>Student Task Manager</h1>
<form method="post" action="/add">
<input name="title" placeholder="Enter a task" required>
<button>Add Task</button>
</form>
<ul>
{% for t in tasks %}
<li>{{t.title}} - {{t.status}}
<form method="post" action="/toggle/{{t.id}}" style="display:inline"><button>Toggle</button></form>
<form method="post" action="/delete/{{t.id}}" style="display:inline"><button>Delete</button></form>
</li>
{% endfor %}
</ul>
<p>DevOps Mini Project | Flask + Docker + Jenkins</p>
"""

@app.get("/")
def home():
    return render_template_string(PAGE, tasks=tasks)

@app.get("/health")
def health():
    return {"status": "healthy"}, 200

@app.post("/add")
def add():
    global next_id
    title = request.form.get("title", "").strip()
    if title:
        tasks.append({"id": next_id, "title": title, "status": "Pending"})
        next_id += 1
    return redirect("/")

@app.post("/toggle/<int:task_id>")
def toggle(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed" if task["status"] == "Pending" else "Pending"
            break
    return redirect("/")

@app.post("/delete/<int:task_id>")
def delete(task_id):
    tasks[:] = [t for t in tasks if t["id"] != task_id]
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
