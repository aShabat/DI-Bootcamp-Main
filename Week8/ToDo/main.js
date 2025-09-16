let tasks = [];
const tasks_div = document.getElementById("tasks");
let next_task_id = 0;
function add_task(text) {
  const task_div = document.createElement("form");
  const clear_task_button = document.createElement("button");
  const toggle_task_radio = document.createElement("input");
  const task_text = document.createElement("p");
  task_text.innerHTML = text;

  new_task = {
    id: next_task_id,
    text: text,
    element: document.createElement("div"),
  };
  new_task.element.innerHTML = new_task.text;
  new_task.element.className = "task";
  tasks_div.appendChild(new_task.element);

  tasks.push(new_task);
  next_task_id++;
}

const new_task_form = document.getElementById("new_task");
new_task_form.addEventListener("submit", (evt) => {
  evt.preventDefault();

  add_task(new_task_form.elements.task_text.value);
  new_task_form.elements.task_text.value = "";
});

const clear_button = document.getElementById("clear_tasks");
clear_button.addEventListener("click", () => {
  for (const task of tasks) {
    tasks_div.removeChild(task.element);
  }
  tasks = [];
});
