import customtkinter
from PIL import Image
import os

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("YT Spammer Purge")
        self.geometry("1920x1080")
        self.state("zoomed")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((1), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="YT Spammer Purge", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.select_list_label = customtkinter.CTkLabel(self.sidebar_frame, text="Made by ThioJoe\nUI Made by Marije", text_color="gray")
        self.select_list_label.grid(row=2, column=0, padx=20, pady=5, sticky="nw")

        self.sidebar_bottom_buttons = customtkinter.CTkFrame(self.sidebar_frame, width=140, corner_radius=0)
        self.sidebar_bottom_buttons.grid(row=7, column=0, rowspan=4, sticky="sew")

        self.settings_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join("assets", "settings_icon_light.png")),
            dark_image=Image.open(os.path.join("assets", "settings_icon_dark.png")))
        self.settings_button = customtkinter.CTkButton(master=self.sidebar_bottom_buttons, text="",
                                                       image=self.settings_image, command=self.open_settings_event,
                                                       width=20, height=20)
        self.settings_button.grid(row=0, column=0, padx=20, pady=5, sticky="nsew")

        self.scan_options = customtkinter.CTkOptionMenu(self,
                                                        values=["Scan specific videos", "Scan recent videos",
                                                                "Scan recent comments", "Scan specific community post [Experimental]",
                                                                "Scan recent community posts [Experimental]"], command=self.set_details)
        self.scan_options.grid(row=1, column=1, padx=20, pady=20, sticky="nw")

        self.channel_link_title = customtkinter.CTkLabel(self, text="Enter Channel link (leave empty if own channel)")
        self.channel_link_title.grid(row=2, column=1, padx=20, pady=(20, 5), sticky="nw")
        self.channel_link = customtkinter.CTkEntry(self, placeholder_text="https://www.youtube.com/@ThioJoe")
        self.channel_link.grid(row=3, column=1, padx=20, pady=(5, 20), sticky="nw")




    def open_settings_event(self):  # Unfinished
        self.settings_window = customtkinter.CTkToplevel(self)
        self.settings_window.title("Settings")
        self.settings_window.geometry("500x250")
        self.settings_window.grid_columnconfigure(1, weight=1)
        self.settings_window.grid_columnconfigure(1, weight=0)
        self.settings_window.grid_rowconfigure(1, weight=1)
        self.scaling_label = customtkinter.CTkLabel(self.settings_window, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=0, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.settings_window,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=1, column=0, padx=20, pady=(10, 20), sticky="new")
        self.scaling_optionemenu.set("100%")
        self.database_frame = customtkinter.CTkFrame(self.settings_window)

    def set_details(self):
        option = self.scan_options.get()



if __name__ == "__main__":
    app = App()
    app.mainloop()