import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import config  # Import the settings we just made

def save_to_google_sheets(new_leads):
    """
    Connects to Google Sheets and appends new leads.
    """
    # 1. Define the Scope (Permissions)
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    try:
        # 2. Authenticate using the file from config.py
        credentials = Credentials.from_service_account_file(
            config.CREDENTIALS_FILE, 
            scopes=scopes
        )
        client = gspread.authorize(credentials)

        # 3. Open the Spreadsheet
        sheet = client.open(config.SHEET_NAME).sheet1

        # 4. Prepare Data
        # We convert the list of dictionaries to a Pandas DataFrame first
        df = pd.DataFrame(new_leads)
        
        # Select and Order columns nicely for the sheet
        # We use .get to avoid errors if a column is missing
        clean_data = []
        for lead in new_leads:
            clean_data.append([
                lead.get('platform', 'Reddit'),
                lead.get('username', 'RSS_User'),
                lead.get('url', ''),
                lead.get('content', ''), # The snippet
                lead.get('lead_status', 'Medium'),
                lead.get('reason', '')
            ])

        # 5. Append to Sheet
        # 'value_input_option="USER_ENTERED"' prevents date formatting issues
        sheet.append_rows(clean_data, value_input_option="USER_ENTERED")
        
        print(f"Successfully added {len(new_leads)} rows to {config.SHEET_NAME}")

    except Exception as e:
        print(f"Error saving to Google Sheets: {e}")
        # Re-raise the error so the UI shows the red box
        raise e