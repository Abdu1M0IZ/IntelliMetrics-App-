from pathlib import Path
from tkinter import (
    Tk, Canvas, Entry, Text, Button, PhotoImage,
    StringVar, OptionMenu, Listbox, MULTIPLE
)

BASE_DIR = Path(__file__).resolve().parent
ASSETS_PATH = BASE_DIR / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def create_gui():

    window = Tk()
    window.title("IntelliMetrics")
    window.geometry("900x700")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=700,
        width=900,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Background image

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    canvas.create_image(0, 0, anchor="nw", image=image_image_1)

    canvas.create_text(
        81.0, 24.0,
        anchor="nw",
        text="IntelliMetrics",
        fill="#FFFFFF",
        font=("Montserrat Bold", 48 * -1)
    )

    # Additional images placeholders

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    canvas.create_image(210.0, 150.0, image=image_image_2)

    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    canvas.create_image(50, 52, image=image_image_3)

    image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
    canvas.create_image(238.0, 309.0, image=image_image_4)

    image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
    canvas.create_image(599.0, 288.0, image=image_image_5)

    image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
    canvas.create_image(145.0, 458.0, image=image_image_6)

    image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
    canvas.create_image(402.0, 458.0, image=image_image_7)

    image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
    canvas.create_image(599.0, 348.0, image=image_image_8)

    image_image_na = PhotoImage(file=relative_to_assets("image_na.png"))
    canvas.create_image(788.0, 149.0, image=image_image_na)

    image_image_9 = PhotoImage(file=relative_to_assets("image_9.png"))
    canvas.create_image(234.0, 594.0, image=image_image_9)

    image_image_10 = PhotoImage(file=relative_to_assets("image_10.png"))
    canvas.create_image(662.0, 594.0, image=image_image_10)


    # Rectangles (dividers)

    canvas.create_rectangle(215.0, 500.0, 889.0, 501.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(536.0, 480.0, 889.0, 481.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(19.0, 500.0, 39.0, 501.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(19.0, 404.0, 39.0, 405.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(536.0, 403.0, 556.0, 404.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(707.0, 403.0, 889.0, 404.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(260.0, 403.0, 529.0, 404.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(19.0, 480.0, 529.0, 481.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(20.0, 682.0, 889.0, 683.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(19.0, 387.0, 889.0, 388.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(293.0, 204.0, 888.0, 205.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(888.0, 500.0, 889.0, 682.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(888.0, 403.0, 889.0, 481.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(535.0, 403.0, 536.0, 481.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(528.0, 403.0, 529.0, 481.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(711.0, 424.0, 712.0, 472.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(18.0, 205.0, 38.0, 206.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(273.0, 423.0, 274.0, 471.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(887.0, 205.0, 888.0, 387.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(19.0, 501.0, 20.0, 683.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(18.0, 206.0, 19.0, 388.0, fill="#D9D9D9", outline="")
    canvas.create_rectangle(18.0, 404.0, 19.0, 481.0, fill="#D9D9D9", outline="")

    # Text labels
    canvas.create_text(
        264.0, 140.0,
        anchor="nw",
        text=".csv or .xlsx files only",
        fill="#0D0D0D",
        font=("Montserrat Bold", 12 * -1)
    )
    canvas.create_text(
        490.0, 310.0,
        anchor="nw",
        text="Missing Values Handling ",
        fill="#FFFFFF",
        font=("Montserrat Bold", 12 * -1)
    )
    canvas.create_text(
        40.0, 195.0,
        anchor="nw",
        text="Features and Target Selection",
        fill="#FFFFFF",
        font=("Montserrat Bold", 16 * -1)
    )
    canvas.create_text(
        41.0, 393.0,
        anchor="nw",
        text="Task and Model Selection",
        fill="#FFFFFF",
        font=("Montserrat Bold", 16 * -1)
    )
    canvas.create_text(
        557.0, 393.0,
        anchor="nw",
        text="Hyperparameters",
        fill="#FFFFFF",
        font=("Montserrat Bold", 16 * -1)
    )
    canvas.create_text(
        490.0, 250.0,
        anchor="nw",
        text="Target Variable",
        fill="#FFFFFF",
        font=("Montserrat Bold", 12 * -1)
    )
    canvas.create_text(
        27.0, 219.0,
        anchor="nw",
        text="Select Features:",
        fill="#FFFFFF",
        font=("Montserrat Bold", 12 * -1)
    )
    canvas.create_text(
        40.0, 418.0,
        anchor="nw",
        text="Task Type",
        fill="#FFFFFF",
        font=("Montserrat Bold", 12 * -1)
    )
    canvas.create_text(
        297.0, 418.0,
        anchor="nw",
        text="Choose Model",
        fill="#FFFFFF",
        font=("Montserrat Bold", 12 * -1)
    )
    canvas.create_text(
        551.0, 418.0,
        anchor="nw",
        text="n_estimators:",
        fill="#FFFFFF",
        font=("Montserrat Bold", 12 * -1)
    )
    canvas.create_text(
        732.0, 418.0,
        anchor="nw",
        text="max_depth",
        fill="#FFFFFF",
        font=("Montserrat Bold", 12 * -1)
    )
    canvas.create_text(
        40.0, 487.0,
        anchor="nw",
        text="Results and Insights",
        fill="#FFFFFF",
        font=("Montserrat Bold", 16 * -1)
    )

    # Dropdowns

    selected_task = StringVar(value="Classification")
    selected_model = StringVar(value="Logistic Regression")
    selected_missing_values = StringVar(value="Mean Imputation")
    selected_target_var = StringVar(value="Select after loading")

    dropdown_width = 180
    dropdown_height = 15
    dropdown_font = ("Montserrat Bold", 10)

    # Missing Values Handling
    missing_values_options = ["Mean Imputation", "Drop Rows", "Drop Columns"]
    missing_values_dropdown = OptionMenu(
        window,
        selected_missing_values,
        *missing_values_options
    )
    missing_values_dropdown.config(
        bg="#CEA8BC",
        fg="white",
        font=dropdown_font,
        bd=0,
        highlightthickness=0,
        activebackground="#CEA8BC"
    )
    missing_values_dropdown["menu"].config(
        bg="#CEA8BC",
        fg="white",
        bd=0,
        tearoff=0,
        font=("Montserrat Bold", 10)
    )
    missing_values_dropdown.place(x=520, y=335, width=dropdown_width, height=dropdown_height)

    # Target Variable
    target_dropdown = OptionMenu(
        window,
        selected_target_var,
        "Select after loading"
    )
    target_dropdown.config(
        bg="#CEA8BC",
        fg="white",
        font=dropdown_font,
        bd=0,
        highlightthickness=0,
        activebackground="#CEA8BC"
    )
    target_dropdown["menu"].config(
        bg="#CEA8BC",
        fg="white",
        bd=0,
        tearoff=0,
        font=("Montserrat Bold", 10)
    )
    target_dropdown.place(x=520, y=275, width=dropdown_width, height=dropdown_height)

    # Task Type
    task_options = ["Classification", "Regression"]
    task_dropdown = OptionMenu(
        window,
        selected_task,
        *task_options
    )
    task_dropdown.config(
        bg="#CEA8BC",
        fg="white",
        font=dropdown_font,
        bd=0,
        highlightthickness=0,
        activebackground="#CEA8BC"
    )
    task_dropdown["menu"].config(
        bg="#CEA8BC",
        fg="white",
        bd=0,
        tearoff=0,
        font=("Montserrat Bold", 10)
    )
    task_dropdown.place(x=65, y=445, width=dropdown_width, height=dropdown_height)

    # Model Type
    model_options = [
        "Logistic Regression", "Decision Tree Classifier",
        "Random Forest Classifier", "K-Nearest Neighbors",
        "Linear Regression", "Decision Tree Regressor",
        "Random Forest Regressor", "Gradient Boosting Regressor"
    ]
    model_dropdown = OptionMenu(
        window,
        selected_model,
        *model_options
    )
    model_dropdown.config(
        bg="#CEA8BC",
        fg="white",
        font=dropdown_font,
        bd=0,
        highlightthickness=0,
        activebackground="#CEA8BC"
    )
    model_dropdown["menu"].config(
        bg="#CEA8BC",
        fg="white",
        bd=0,
        tearoff=0,
        font=("Montserrat Bold", 10)
    )
    model_dropdown.place(x=325, y=445, width=dropdown_width, height=dropdown_height)


    # Feature Listbox

    feature_listbox = Listbox(
        window,
        selectmode=MULTIPLE,
        bg="#CEA8BC",
        fg="#000000",
        font=("Montserrat Bold", 10),
        borderwidth=0,  # Remove the border width
        highlightthickness=0,  # Remove the highlight border
        relief='flat',  # Flat relief to avoid 3D borders
        highlightbackground="#CEA8BC",  # Match the highlight background to Listbox bg
        highlightcolor="#CEA8BC"  # Match the highlight color to Listbox bg
    )
    feature_listbox.place(x=33, y=243, width=412, height=120)

    # Entries for hyperparameters

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    canvas.create_image(621.0, 454.0, image=entry_image_1)
    entry_1 = Entry(window, bd=0, bg="#CEA8BC", fg="white", highlightthickness=0, font=("Montserrat", 10))
    entry_1.place(x=558.0, y=438.0, width=126.0, height=30)
    entry_1.insert(0, "100")

    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    canvas.create_image(802.0, 454.0, image=entry_image_2)
    entry_2 = Entry(window, bd=0, bg="#CEA8BC", fg="white", highlightthickness=0, font=("Montserrat", 10))
    entry_2.place(x=739.0, y=438.0, width=126.0, height=30)
    entry_2.insert(0, "None")

    # Text widget for results

    results_text = Text(window, bd=0, bg="#934DC3", fg="#FFFFFF", wrap="word")
    results_text.place(x=40, y=530, width=390, height=120)

    # Button: Upload file

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    upload_button = Button(
        window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        bg="white",
        activebackground="white"
    )
    upload_button.place(
        x=29.293,
        y=118.439,
        width=button_image_1.width() - 3,
        height=button_image_1.height()
    )


    # Button: Train & Evaluate

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat",
        bg="white",
        activebackground="white"
    )
    button_2.place(
        x=704.0,
        y=127.0,
        width=button_image_2.width(),
        height=button_image_2.height()
    )

    window.resizable(False, False)

    # Return references in a dictionary
    ui_widgets = {
        "canvas": canvas,
        "feature_listbox": feature_listbox,
        "missing_values_dropdown": missing_values_dropdown,
        "target_dropdown": target_dropdown,
        "task_dropdown": task_dropdown,
        "model_dropdown": model_dropdown,
        "selected_task": selected_task,
        "selected_model": selected_model,
        "selected_missing_values": selected_missing_values,
        "selected_target_var": selected_target_var,
        "entry_1": entry_1,
        "entry_2": entry_2,
        "results_text": results_text,
        "upload_button": upload_button,
        "train_button": button_2,
        # Keep references to images
        "image_image_1": image_image_1,
        "image_image_2": image_image_2,
        "image_image_3": image_image_3,
        "image_image_4": image_image_4,
        "image_image_5": image_image_5,
        "image_image_6": image_image_6,
        "image_image_7": image_image_7,
        "image_image_8": image_image_8,
        "image_image_9": image_image_9,
        "image_image_10": image_image_10,
        "image_image_na": image_image_na,
        "entry_image_1": entry_image_1,
        "entry_image_2": entry_image_2,
        "button_image_1": button_image_1,
        "button_image_2": button_image_2
    }

    return window, ui_widgets
