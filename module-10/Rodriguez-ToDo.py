# Jose Rodriguez
# 7/26/2026
# Module 10.2 Assignment


# This program creates a scrolling To-Do list using Tkinter.

import tkinter as tk
import tkinter.messagebox as msg


class Todo(tk.Tk):

    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.title("Rodriguez-ToDo")
        self.geometry("350x450")

        # File menu
        menu_bar = tk.Menu(self)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu_bar)

        # Frames and scrolling area
        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(
            self.tasks_canvas,
            orient="vertical",
            command=self.tasks_canvas.yview
        )

        self.tasks_canvas.configure(
            yscrollcommand=self.scrollbar.set
        )

        self.tasks_canvas.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )

        self.scrollbar.pack(
            side=tk.RIGHT,
            fill=tk.Y
        )

        self.canvas_frame = self.tasks_canvas.create_window(
            (0, 0),
            window=self.tasks_frame,
            anchor="n"
        )

        # Instructions
        self.instructions = tk.Label(
            self.text_frame,
            text="Type a task and press Enter.\nRight-click a task to delete it.",
            bg="lightgray",
            fg="black",
            pady=8
        )

        self.instructions.pack(
            side=tk.TOP,
            fill=tk.X
        )

        # Text box for entering tasks
        self.task_create = tk.Text(
            self.text_frame,
            height=3,
            bg="white",
            fg="black"
        )

        self.task_create.pack(
            side=tk.BOTTOM,
            fill=tk.X
        )

        self.text_frame.pack(
            side=tk.BOTTOM,
            fill=tk.X
        )

        self.task_create.focus_set()

        # Complementary task colors
        self.colour_schemes = [
            {"bg": "lightblue", "fg": "black"},
            {"bg": "orange", "fg": "black"}
        ]

        # Starting task
        starting_task = tk.Label(
            self.tasks_frame,
            text="Add your tasks below",
            pady=10
        )

        self.set_task_colour(0, starting_task)
        self.bind_delete(starting_task)

        self.tasks.append(starting_task)

        for task in self.tasks:
            task.pack(
                side=tk.TOP,
                fill=tk.X
            )

        # Keyboard and mouse events
        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

    def bind_delete(self, task):
        # Button-2 and Button-3 support right-click on different Macs.
        task.bind("<Button-2>", self.remove_task)
        task.bind("<Button-3>", self.remove_task)

    def add_task(self, event=None):
        task_text = self.task_create.get(
            1.0,
            tk.END
        ).strip()

        if len(task_text) > 0:
            new_task = tk.Label(
                self.tasks_frame,
                text=task_text,
                pady=10
            )

            self.set_task_colour(
                len(self.tasks),
                new_task
            )

            self.bind_delete(new_task)

            new_task.pack(
                side=tk.TOP,
                fill=tk.X
            )

            self.tasks.append(new_task)

        self.task_create.delete(
            1.0,
            tk.END
        )

    def remove_task(self, event):
        task = event.widget

        answer = msg.askyesno(
            "Delete Task",
            "Delete " + task.cget("text") + "?"
        )

        if answer:
            self.tasks.remove(task)
            task.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)

        selected_scheme = self.colour_schemes[
            task_style_choice
        ]

        task.configure(
            bg=selected_scheme["bg"],
            fg=selected_scheme["fg"]
        )

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(
            scrollregion=self.tasks_canvas.bbox("all")
        )

    def task_width(self, event):
        canvas_width = event.width

        self.tasks_canvas.itemconfig(
            self.canvas_frame,
            width=canvas_width
        )

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(
                int(-1 * (event.delta / 120)),
                "units"
            )
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1

            self.tasks_canvas.yview_scroll(
                move,
                "units"
            )


if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()