from Helpers import *
import Tkinter as tk


class MainView(tk.Toplevel):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)

        # Close app on exit click
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)

        # Window properies
        tk.Toplevel.geometry(self, GuiContent.WINDOW_SIZE)
        tk.Toplevel.title(self, GuiContent.WINDOW_TITLE)

        # Window content
        self.main_container = tk.Frame(self)
        self.main_container.pack()

        self.content_frame = tk.Frame(self.main_container)
        self.content_frame.grid()

        self.top_frame = tk.Frame(self.content_frame)
        self.top_frame.grid(row=0)

        # JSON
        self.input_path = tk.StringVar()
        self.input_path_text_box = tk.Entry(self.top_frame, textvariable=self.input_path, state='disabled', width=40)
        self.input_path_text_box.grid(row=0, column=0)

        self.upload_button = tk.Button(self.top_frame, text=GuiContent.BUTTON_TEXT_OPEN_JSON)
        self.upload_button.grid(row=0, column=1)

        # Template
        self.input_path_template = tk.StringVar()
        self.input_path_template_text_box = tk.Entry(self.top_frame, textvariable=self.input_path_template, state='disabled', width=40)
        self.input_path_template_text_box.grid(row=1, column=0)

        self.upload_button_template = tk.Button(self.top_frame, text=GuiContent.BUTTON_TEXT_OPEN_WORD_TEMPLATE)
        self.upload_button_template.grid(row=1, column=1)

        # Target group
        self.options = [GuiContent.DROP_DOWN_VALUE_NO_SELECTED_TARGET_GROUP]
        self.selected_target_group = tk.StringVar()
        self.selected_target_group.set(self.options[0])  # default value

        self.target_groups_drop_down = tk.OptionMenu(self.content_frame, self.selected_target_group, *self.options)
        self.target_groups_drop_down.grid(row=2)

        # Download
        self.download_button = tk.Button(self.content_frame, text=GuiContent.BUTTON_TEXT_SAVE, state='disabled')
        self.download_button.grid(row=4)

        # Messages
        # -- Error
        self.error_message = tk.StringVar()
        self.error_message_label = tk.Label(self.content_frame, textvariable=self.error_message, fg='red')
        self.error_message_label.grid(row=5)
        # -- Success
        self.success_message = tk.StringVar()
        self.success_message_label = tk.Label(self.content_frame, textvariable=self.success_message)
        self.success_message_label.grid(row=6)

    def set_input_path(self, input_path):
        self.input_path.set(input_path)

    def set_input_path_template(self, input_path):
        self.input_path_template.set(input_path)

    def set_error_message(self, error_message):
        self.error_message.set(error_message)

    def set_success_message(self, success_message):
        self.success_message.set(success_message)

    def disable_download_button(self, disabled):
        if disabled:
            self.download_button.config(state='disabled')
        else:
            self.download_button.config(state='normal')
