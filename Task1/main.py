from managers.expense_manager import ExpenseManager
from gui.main_window import MainWindow
from utils.data_handler import load_transactions, save_transactions

if __name__ == "__main__":
    manager = ExpenseManager()
    
    loaded = load_transactions()
    if loaded:
        manager.transactions = loaded
        manager.next_id = max(t.id for t in loaded) + 1 if loaded else 1

    window = MainWindow(manager)

    # Save on close
    def on_close():
        save_transactions(manager.transactions)
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()