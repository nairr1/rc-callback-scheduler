# Callback Scheduler

A simple Python application that allows users to schedule callbacks using the NICE inContact API. This application features a graphical user interface (GUI) built with Tkinter, making it user-friendly and easy to operate.

## Features

- User-friendly interface for entering mobile numbers.
- Numeric keypad for easy input.
- Schedules callbacks via the NICE inContact API.
- Handles authentication and token management.

## Requirements

- Python 3.x
- `requests` library
- `python-dotenv` library
- `Tkinter` (usually included with Python)

## Installation

1. Clone the repository:

  ```bash
  git clone https://github.com/nairr1/rc-callback-scheduler.git
  cd rc-callback-scheduler
  ```

2. Install required packages:
  ```bash
  pip install requests python-dotenv
  ```

3. Create a `.env` file in the `rc-callback-scheduler/` directory with the following content:
  ```bash
  NICE_AUTH_BASE_URL=https://your_auth_base_url
  NICE_API_BASE_URL=https://your_api_base_url
  NICE_ACCESS_KEY_ID=your_access_key_id
  NICE_ACCESS_KEY_SECRET=your_access_key_secret
  ```

## Usage

1. Run the application:
  ```bash
  python main.py
  ```

2. Enter a mobile number in the input field. You can use the numeric keypad for convenience.

3. Click the "Schedule Callback" button to schedule the callback.

4. A success message and "Contact ID" will be displayed if the callback is scheduled successfully; otherwise, an error message will be shown.