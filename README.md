# Support Bot — Hands-on Lab

This workspace contains a minimal Python support bot that can:

- Search `products.json` for product information (file-search tool)
- Return mock order status via `getOrderStatus(order_id)` (function tool)

Files added:

- `support_bot.py` — implements `file_search_products()`, `getOrderStatus()`, `handle_user_query()` and `create_thread_and_ask()`.
- `main.py` — simple interactive loop (already in workspace).
- `demo.py` — runs the example thread: "What's the price of the 'Pro' model, and what's the status of order #12345?" and prints debug details.

Setup

1. Ensure you have Python 3.8+ and `pip` installed.
2. (Optional) Create and activate a virtual environment:

```bash
python -m venv .venv

# macOS / Linux / Git Bash
source .venv/bin/activate

# Windows (PowerShell) - dot-source the activation script in the current shell
. .venv\Scripts\Activate.ps1

# Windows (cmd.exe)
.venv\Scripts\activate.bat
```

If PowerShell prevents running the activation script, enable local script execution (current user) with:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. (Optional) Create a `.env` file with an `OPENAI_API_KEY` if you later enable OpenAI features.

Run the demo

```bash
python demo.py
```

Interactive mode

```bash
python main.py
```

Lab guidance

- Step 1: Open `support_bot.py` and inspect the assistant instructions and tool implementations.
- Step 2: Run `demo.py` to see how the assistant decides which tools to call.
- Step 3: Modify `getOrderStatus()` to return richer mock data if you want to teach the class how to extend tools.
