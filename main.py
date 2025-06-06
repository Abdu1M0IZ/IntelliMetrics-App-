from tkinter import filedialog, END
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay

from gui import create_gui
from data_preprocessing import load_data, handle_missing_values, select_features_and_target
from ml_model import get_model, evaluate_classification, evaluate_regression


class IntelliMetricsApp:
    def __init__(self):
        # Create the GUI and store references to window and widgets
        self.window, self.ui = create_gui()

        # Keeping track of DataFrame and column lists
        self.df = None
        self.features_list = []

        # Callbacks
        self.ui["upload_button"].config(command=self.upload_file)
        self.ui["train_button"].config(command=self.train_and_evaluate)

        self.fig = plt.Figure(figsize=(3.9, 1.3), facecolor="#A864A8")
        self.ax = self.fig.add_subplot()

        # Styling
        self.ax.tick_params(labelsize=5, colors="white")
        self.ax.set_facecolor('#A864A8')
        self.ax.grid(visible=True, color='white', linestyle='--', alpha=0.2)
        self.ax.plot(color="deepskyblue")
        self.fig.autofmt_xdate()

        # Embed the figure in Tkinter at a given position/size
        self.canvas_fig = FigureCanvasTkAgg(self.fig, master=self.window)
        self.canvas_fig.get_tk_widget().place(x=465, y=522, width=390, height=140)

    def upload_file(self):
        file_path = filedialog.askopenfilename(
            title="Select a CSV or XLSX file",
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")]
        )
        if not file_path:
            return  # User canceled

        try:
            self.df = load_data(file_path)
            self.update_ui_with_data_columns()

            self.ui["results_text"].delete("1.0", END)
            self.ui["results_text"].insert(END, f"Loaded data with shape {self.df.shape}\n")
        except Exception as e:
            self.ui["results_text"].delete("1.0", END)
            self.ui["results_text"].insert(END, f"Error loading file:\n{e}")

    def update_ui_with_data_columns(self):
        feature_listbox = self.ui["feature_listbox"]
        target_dropdown = self.ui["target_dropdown"]
        selected_target_var = self.ui["selected_target_var"]

        feature_listbox.delete(0, END)
        if self.df is not None:
            columns = list(self.df.columns)
            self.features_list = columns

            # Populate feature listbox
            for col in columns:
                feature_listbox.insert(END, col)

            # Populate target dropdown
            menu = target_dropdown["menu"]
            menu.delete(0, "end")
            for col in columns:
                menu.add_command(
                    label=col,
                    command=lambda value=col: selected_target_var.set(value)
                )
            selected_target_var.set("Select Target")

    def train_and_evaluate(self):
        # Check if we have data
        if self.df is None:
            self.ui["results_text"].delete("1.0", END)
            self.ui["results_text"].insert(END, "Please upload a dataset first.\n")
            return

        # Missing values
        strategy = self.ui["selected_missing_values"].get()  # e.g., "mean", "drop", etc.
        data_prep = handle_missing_values(self.df, strategy)

        # Features & Target
        feature_listbox = self.ui["feature_listbox"]
        sel_indices = feature_listbox.curselection()
        if not sel_indices:
            self.ui["results_text"].delete("1.0", END)
            self.ui["results_text"].insert(END, "Please select at least one feature.\n")
            return

        chosen_features = [self.features_list[i] for i in sel_indices]
        target_col = self.ui["selected_target_var"].get()
        if target_col not in data_prep.columns:
            self.ui["results_text"].delete("1.0", END)
            self.ui["results_text"].insert(END, "Please select a valid target variable.\n")
            return

        # Split out features (X) and target (y)
        X, y = select_features_and_target(data_prep, chosen_features, target_col)

        #  Hyperparameters
        entry_1 = self.ui["entry_1"]  # n_estimators
        entry_2 = self.ui["entry_2"]  # max_depth

        try:
            n_estimators = int(entry_1.get())
        except:
            n_estimators = 100

        max_depth_str = entry_2.get().strip()
        if max_depth_str.lower() == "none":
            max_depth = None
        else:
            try:
                max_depth = int(max_depth_str)
            except:
                max_depth = None

        # Model selection
        task_type = self.ui["selected_task"].get()  # e.g., "Classification" or "Regression"
        model_name = self.ui["selected_model"].get()  # e.g., "RandomForest", "LogisticRegression", etc.
        model = get_model(task_type, model_name, n_estimators=n_estimators, max_depth=max_depth)
        if model is None:
            self.ui["results_text"].delete("1.0", END)
            self.ui["results_text"].insert(END, "Invalid model selection.\n")
            return

        # Train/Test Split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train
        try:
            model.fit(X_train, y_train)
        except Exception as e:
            self.ui["results_text"].delete("1.0", END)
            self.ui["results_text"].insert(END, f"Error training model:\n{e}")
            return

        # Predict
        y_pred = model.predict(X_test)

        #  Evaluate
        if task_type.lower() == "classification":
            metrics_dict = evaluate_classification(y_test, y_pred)
        else:
            metrics_dict = evaluate_regression(y_test, y_pred)

        # Clear text and figure for fresh output
        self.ui["results_text"].delete("1.0", END)
        self.fig.clear()  # remove old plots

        # Display metrics in text box
        for k, v in metrics_dict.items():
            if isinstance(v, float):
                self.ui["results_text"].insert(END, f"{k}: {v:.4f}\n")
            else:
                self.ui["results_text"].insert(END, f"{k}: {v}\n")

        # Plot
        ax = self.fig.add_subplot(111)  # new axes
        ax.patch.set_alpha(0)  # transparent background
        ax.grid(True, linestyle="--", alpha=0.5)

        if task_type.lower() == "classification":
            # Expect that metrics_dict contains 'confusion_matrix'
            if 'confusion_matrix' in metrics_dict:
                cm = metrics_dict['confusion_matrix']
                # Display confusion matrix
                cmd = ConfusionMatrixDisplay(cm)
                cmd.plot(ax=ax, cmap=plt.cm.Blues, colorbar=False)
                ax.set_title("Confusion Matrix", fontsize=8)
                # Force small text
                ax.tick_params(labelsize=6)
            else:
                ax.text(0.5, 0.5, "No confusion matrix found", ha='center', va='center')
        else:
            # Regression scatter: Actual vs. Predicted
            ax.scatter(y_test, y_pred, c="#CEA8BC", edgecolors="blue", alpha=0.7)
            ax.set_xlabel("Actual", fontsize=7)
            ax.set_ylabel("Predicted", fontsize=7)
            ax.set_title("Actual vs. Predicted", fontsize=8)
            ax.tick_params(labelsize=6)

        self.fig.tight_layout()
        self.canvas_fig.draw()

    def run(self):
        self.window.mainloop()


# Entrypoint
if __name__ == "__main__":
    app = IntelliMetricsApp()
    app.run()
