# git send-telegram

your git send-email for 2023!

## Setup

- Obtain API credentials from <https://core.telegram.org/api/obtaining_api_id>
- Set credentials:
  ```
  git config sendtelegram.apiid <api_id>
  git config sendtelegram.apihash <api_hash>
  ```
- Set session string:
  ```
  TELEGRAM_API_ID=<api_id> TELEGRAM_API_HASH=<api_hash> ./export-session-string.py
  git config sendtelegram.sessionstring <session_string>
  ```

You're good to go, let's get those patches a-sending!

`git send-telegram --to torvalds HEAD^!`
